#!/usr/bin/python3 -B

import subprocess
#def order(machineID, cmd):
#    try:
#        command = ['systemd-run', '--machine', machineID, '--wait', '--quiet', '--pipe']
#        command.extend(cmd.split(' '))
#        output = subprocess.check_call(command)
#        return output
#    except subprocess.CalledProcessError as e:
#        print(e)

class runner:
    def __init__(self, machineID, conf={}):
        """
            Wrapper for systemd-run
            runner object is build with machineID and optionally an conf dictionary with boolean flags as booleans
                conf:
                  machine:   <machine id>
                  command:   <command to run>
                  ...
            conf may include any of the aguments available to systemd-run
            
            if no conf is passed the default is:
                ```-- quiet --pipe --wait```
            which will pass the stdout and stderr back to the calling script.
            
            Example:
                import pynspawn
                runner = pynspawn.runner("$machinename")
                runner.run(<command string as a list>)

            will run the <command string as list> on $machinename
            
            Will throw a Value Error if no machine ID is supplied.
        """
        if not machineID:
            raise ValueError("No machine ID")

        if str(len(conf.keys())) == str("0"):
            conf = { 'quiet': True, 'pipe': True, 'wait': True, 'machine': machineID }
        else:
            conf['machine'] = machineID
        try:
            sysd_run_cmd_check = subprocess.run(['which', 'systemd-run'], stdout=subprocess.PIPE)
            sysd_run_cmd_check.check_returncode()
            self.sysd_run_cmd = sysd_run_cmd_check.stdout.decode('utf8').strip('\n')
        except subprocess.CalledProcessError as e:
            print(e)
       
        self.sysd_run_nonos = [ 'command' ]
        self.sysd_run_args_list = [ ['--' + key, conf[key]] for key in conf.keys() if key not in self.sysd_run_nonos and conf[key] is not None and conf[key] is not True and conf[key] is not False ]
        self.sysd_run_args_flags = [ ['--' + key, conf[key]] for key in conf.keys() if key not in self.sysd_run_nonos and conf[key] is True ]
        self.sysd_run_args = [ arg for args_pair in self.sysd_run_args_list for arg in args_pair ]
        self.sysd_run_flags = [ arg[0] for arg in self.sysd_run_args_flags ]
    
        self.sysd_run = [ self.sysd_run_cmd ]
        self.sysd_run.extend(self.sysd_run_args)
        self.sysd_run.extend(self.sysd_run_flags)
 
    def run(self, *command):
        if not command:
            raise ValueError("No command supplied")
        subprocess.check_call(['systemctl', 'is-system-running', '--wait'])

        self.sysd_run.extend(command)

        try:
            output = subprocess.Popen(self.sysd_run, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            data, err = output.communicate()
        except subprocess.CalledProcessError as e:
            print(e)
        return data, err

def daemonize(name):
    try: 
        #subprocess.check_call(['systemctl', 'enable', 'systemd-nspawn@' + name + '.service'])
        subprocess.check_call(['systemctl', 'start', 'systemd-nspawn@' + name + '.service'])
    except subprocess.CalledProcessError as e:
        print(e)


