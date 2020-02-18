from hackpy.commands import *
from hackpy.modules  import *

class uac:
    ##|
    ##| hackpy.uac.disable() # Disable UAC // NEED ADMIN!
    ##| hackpy.uac.enable()  # Enable  UAC // NEED ADMIN!
    ##| hackpy.uac.status()  # Status  UAC // NEED ADMIN!
    ##|

    def __init__():
        require_module('uac.exe')
        
    def disable():
        status = command.system(modules_path + 'uac.exe disable', return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def enable():
        status = command.system(modules_path + 'uac.exe enable', return_code = True)[1]
        if status == 0:
            return True
        else:
            return False

    def status():
        status = command.system(modules_path + 'uac.exe status', return_code = True)[1]
        if status == 0:
            return status[0]
        else:
            return False