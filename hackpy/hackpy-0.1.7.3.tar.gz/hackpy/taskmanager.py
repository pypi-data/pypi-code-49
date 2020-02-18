from os import remove
from random import randint
from hackpy.info     import *
from hackpy.commands import *


class taskmanager:
    ##|
    ##| hackpy.taskmanager.enable()
    ##| hackpy.taskmanager.disable()
    ##|
    ##| hackpy.taskmanager('process_name.exe').kill()
    ##| hackpy.taskmanager('process_name.exe').start()
    ##| hackpy.taskmanager('process_name.exe').find() # return True or False
    ##| hackpy.taskmanager.list() # return all process list
    ##| hackpy.taskmanager.getpid('process_name.exe') # return process id
    ##|
    def __init__(self, process):
        self.process = process

    def enable():
        status = command.system('@reg.exe ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 0' + devnull, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def disable():
        status = command.system('@reg.exe ADD "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /f /v "DisableTaskMgr" /t REG_DWORD /d 1' + devnull, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def kill(self):
        status = command.system('@taskkill /F /IM ' + self.process + devnull, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def start(self):
        status = command.system('@start ' + self.process + devnull, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def find(process):
        process_list = taskmanager.list()
        if (process in process_list):
            return True
        else:
            return False

    def list():
        random_number = str(randint(1, 99999))
        list_path = temp_path + r'process_list_' + random_number + '.tmp'
        command.system('@tasklist > ' + list_path)
        with open(list_path, 'r', encoding = "utf8", errors = 'ignore') as file:
            process_list = []
            for line in file.readlines():
                line = line.replace('\n', '').split()
                if (line):
                    process = line[0]
                    pid     = line[1]
                    if (process.endswith('.exe')):
                        process_list.append(process)
        remove(list_path)
        return process_list

    def getpid(process):
        random_number = str(randint(1, 99999))
        list_path = temp_path + r'process_pid_' + random_number + '.tmp'
        command.system('@tasklist > ' + list_path)
        with open(list_path, 'r', encoding = "utf8", errors = 'ignore') as file:
            for line in file.readlines():
                line = line.replace('\n', '').split()
                if (line):
                    process_name = line[0]
                    process_id   = line[1]
                    if (process_name.endswith('.exe')):
                        if (process_name.lower() == process.lower()):
                            break
                        else:
                            process_id = False

        remove(list_path)
        return process_id