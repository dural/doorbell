import { PythonShell } from 'python-shell'

export const InitDoorbellInterface = () => {
  return new PythonShell('~/doorbell/door-monitor.py', {
    mode: 'text',
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: 'python/',  
  });
}