from hackpy.commands import *

class power:
    ##|
    ##| hackpy.power.reboot()
    ##| hackpy.power.shutdown()
    ##| hackpy.power.logoff()
    ##| hackpy.power.hibernate()
    ##|
    def reboot():
        command.system('@shutdown /r /t 0')

    def shutdown():
        command.system('@shutdown /s /t 0')

    def logoff():
        command.system('@shutdown /l')

    def hibernate():
        command.system('@shutdown /h')