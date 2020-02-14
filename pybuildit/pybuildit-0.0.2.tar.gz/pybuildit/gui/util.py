from tkinter import messagebox
import sys,os
from pybuildit import *
import logging
import errno
from pathlib import Path

logger = logging.getLogger("pybuildit")

faultDict = dict([
            (0x000, "Stable"),
            (0x001, "FOC Duration"),
            (0x002, "Over Voltage"),
            (0x004, "Under Voltage"),
            (0x008, "Over Temperature"),
            (0x010, "Over Position Limit"),
            (0x040, "Break In"),
            (0x100, "Stop Control Error"),
            (0x200, "Stop Timeout"),
            (0x800, "Unknown Error"),
            ])

class BuilditGuiInfo:
    targetDevId = 1

builditGuiInfo = BuilditGuiInfo()
tickListener = []

def tryBuildit(f):
    try:
        return f()
    except MCPError as e:
        messagebox.showerror('communication exception', e.__class__.__name__)

        logger.error('communication exception: %s'%e.__class__.__name__)
    except Exception as e:
        messagebox.showerror('exception',str(e))
        
        logger.error('exception: %s'% str(e))
    return None

def path_of_history():
        if os.name == "posix":
            history_path = os.getenv('HOME')+ "/.pybuildit"  #for linux
        elif os.name == "nt":
            history_path= os.getenv('APPDATA')+ "\\pybuildit"  #for windows
        else:
            print("Path is not found")
        if not os.path.exists(history_path):
            try:
                os.makedirs(history_path)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        return history_path
