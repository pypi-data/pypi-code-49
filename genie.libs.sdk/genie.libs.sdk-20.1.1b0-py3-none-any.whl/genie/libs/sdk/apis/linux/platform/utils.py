
# Python
import re
from os import path
import tempfile

def learn_routem_configs(device, output_config=False):
    """ Gets the current running config on device
        Args:
            output_config ('bool'): Specifies whether the config
            or path of the config is outputted 
        Raise:
            None
        Returns:
            Config ('dict'): {pid: config}
            ex.) Config = {'123': 'config'}
    """
    output = device.parse("ps -ef | grep routem")['pid']
    configs = {}

    for pid, info in output.items():
        config_data = info['cmd'].split()
        
        if len(config_data) == 4:
            config_data = config_data[2]
        else:
            continue

        if output_config:
            with open(config_data, "r") as file:
                config_data = file.read()
        
        configs.setdefault(pid, config_data)

    return configs

def learn_process_pids(device, search):
    """ Finds the PIDs of processes that match the search
        Args:
            search ('str'): The name of the processes to find
        Raise:
            None
        Returns:
            PIDs ('list'): [pid]
            ex.) PIDs = ['123', '456']
    """
    output = device.parse("ps -ef | grep {}".format(search))['pid']

    return list(output.keys())

def kill_processes(device, pids):
    """ Kills the processes with given PIDs 
        Args:
            pids ('list'): List of PIDs
            ex.) pids = [12, 15, 16]
        Raise:
            ValueError: Process with PID does not exist
        Returns:
            None
    """
    for pid in pids:
        output = device.execute("kill {}".format(pid))
        
        if "No such process" in output: 
            raise ValueError("Process with PID {} does not exist.".format(pid))

def start_routem_process(device, config, routem_executable):
    """ Starts the routem executable with the provided config
        Args:
            config ('str'): Path to config file or raw config data
            routem_executable ('str'): Path to routem executable file 
        Raise:
            None
        Returns:
            None
    """
    if not path.exists(config):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
            tmp.write(config)
            config = tmp.name
    
    device.hostname = "bash"
    device.execute("python")
    device.execute("from subprocess import Popen")
    command = "['{}', '-f', '{}', '-i']".format(routem_executable, config)    
    device.execute("Popen({}, shell=False); exit()".format(command))

    