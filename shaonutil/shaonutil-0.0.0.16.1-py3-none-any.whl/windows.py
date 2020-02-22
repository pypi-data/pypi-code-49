import ctypes, sys
def is_winapp_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_UAC_permission(func):
	if is_winapp_admin():
	    # Code of your program here
	    func()
	else:
	    # Re-run the program with admin rights
	    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)