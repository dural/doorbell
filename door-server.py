#!/usr/bin/env python3

import time
import automationhat
import sys

import queue
import threading


def main():
  command_queue = queue.LifoQueue()
  read_thread = threading.Thread(target=read_loop, args=[command_queue])
  read_thread.start()
  run_loop(command_queue)


def read_loop(command_queue):
  while True:
    command_queue.put_nowait(sys.stdin.readline().rstrip('\n'))


def run_loop(command_queue):
  thread_local = threading.local()
  thread_local.doorbell_on_state = False

  while True:
    run_command(command_queue)
    read_doorbell(thread_local)


def run_command(command_queue):
  try:
    command = command_queue.get(timeout=0.5)
  except queue.Empty:
    pass
  else:
    automationhat.relay.on() if command == "unlock" else automationhat.relay.off()


def read_doorbell(thread_local):
  doorbell_on_state = automationhat.input.one.read() == 1

  if doorbell_on_state != thread_local.doorbell_on_state:
    thread_local.doorbell_on_state = doorbell_on_state
    print("doorbell_on") if doorbell_on_state else print("doorbell_off")


if __name__ == "__main__":
  main()
