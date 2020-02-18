from hackpy.settings import *
from hackpy.commands import *
from hackpy.modules  import *

class autorun:
    def __init__(self, path):
        self.path = '\"' + path + '\"'
        
    
    # Add file to startup | Method with Registry
    def installRegistry(self):
    	require_module('autorun.exe')
    	status = command.system(modules_path + 'autorun.exe install-registry ' + self.path, return_code = True)[1]
    	print(status)
    	if status == 0:
    		return True
    	else:
    		return False

    # Delete file from startup | Method with Registry
    def uninstallRegistry(self):
    	require_module('autorun.exe')
    	status = command.system(modules_path + 'autorun.exe uninstall-registry ' + self.path, return_code = True)[1]
    	if status == 0:
    		return True
    	else:
    		return False

    # Add file to startup | Method with Taskscheduler
    def installTaskscheduler(self):
        require_module('autorun.exe')
        status = command.system(modules_path + 'autorun.exe install-taskscheduler ' + self.path, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    # Delete file from startup | Method with Taskscheduler
    def uninstallTaskscheduler(self):
        require_module('autorun.exe')
        status = command.system(modules_path + 'autorun.exe uninstall-taskscheduler ' + self.path, return_code = True)[1]
        if status == 0:
            return True
        else:
            return False