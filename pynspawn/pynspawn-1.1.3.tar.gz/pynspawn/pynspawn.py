#!/usr/bin/python3 -B

import subprocess

def order(machineID, cwd, cmd):
    try:
        command = ['systemd-run', '--machine', machineID, '--working-directory=' + cwd]
        command.extend(cmd.split(' '))
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(e)
        
def daemonize(name):
    try: 
        #subprocess.check_call(['systemctl', 'enable', 'systemd-nspawn@' + name + '.service'])
        subprocess.check_call(['systemctl', 'start', 'systemd-nspawn@' + name + '.service'])
    except subprocess.CalledProcessError as e:
        print(e)
