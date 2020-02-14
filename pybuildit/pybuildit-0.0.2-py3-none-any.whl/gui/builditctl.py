from tkinter import *
import tkinter as tk
from pybuildit.gui.top_panel import TopPanel
from pybuildit.gui.side_panel import SidePanel
from pybuildit.gui.main_panel import MainPanel
import sys,os
from pybuildit import *
from pybuildit.gui.util  import *
import time
import logging
import logging.handlers as handlers

logger = logging.getLogger("pybuildit")

class BuilditGUI(tk.Frame):
    def __init__(self, buildit, master=None):
        tk.Frame.__init__(self, master)
        self.buildit = buildit
        self.pack(expand = True, fill = BOTH)
        self.make_root()
        self.text_log_file()

    def make_root(self):
        root = PanedWindow(self, sashwidth = 2, orient=VERTICAL)
        bottom = PanedWindow(root, sashwidth = 2)
        
        root.pack(expand = True, fill = BOTH)

        main = Label(bottom, text = 'panedwindow\nmain', bg = 'yellow')
    
        side = SidePanel(self.buildit, root)
        main = MainPanel(self.buildit, root)

        bottom.add(side, width=200)
        bottom.add(main)
        
        root.add(TopPanel(self.buildit, root), height=50)
        root.add(bottom)

    def text_log_file(self):
        history_path= path_of_history()
        logfile_name = "{}/buildit-gui.log".format(history_path)

        #Create logger
        logger.setLevel(logging.INFO)
        FORMAT =logging.Formatter("[%(asctime)s] %(levelname)s: %(filename)s:%(lineno)s: %(message)s")
        
        #handler = handlers. TimedRotatingFileHandler(logfile_name, when="M",  interval=5, backupCount=20 )
        handler = handlers.RotatingFileHandler(logfile_name, maxBytes=1000000,  backupCount=0 )
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(FORMAT)

        error_log_name = "{}/error.log".format(history_path)
        errorlog = handlers.RotatingFileHandler(error_log_name, maxBytes=1000000, backupCount=0)
        errorlog.setLevel(logging.ERROR)
        errorlog.setFormatter(FORMAT)
        
        logger.addHandler(handler)
        logger.addHandler(errorlog)
        logger.info("Buildit-GUI STARTED")
        msg = "LOG DATA is gathering ..."
        logger.info(msg)

def main():
    buildit = UnsafeBuildit(baud=115200,port=None,timeout_ms=3000)
    global targetDevId
    targetDevId = 1

    root = tk.Tk()
    root.title("Buildit")

    ww = 900
    wh = 720

    sw = min(root.winfo_screenwidth(), ww)
    sh = min(root.winfo_screenheight(), wh)

    canvas = tk.Canvas(root, width=sw, height=sh)

    h = tk.Scrollbar(root, orient=tk.HORIZONTAL)
    h.pack(side=BOTTOM, fill=X)
    h.config(command=canvas.xview)

    v = tk.Scrollbar(root, orient=tk.VERTICAL)
    v.pack(side=RIGHT, fill=Y)
    v.config(command=canvas.yview)

    canvas.config(scrollregion=(0,0,ww,wh))
    canvas.config(yscrollcommand=v.set, xscrollcommand=h.set)
    canvas.pack(side= LEFT, expand= True, fill=tk.BOTH)

    frame = BuilditGUI(buildit, canvas)
    canvas.create_window((0,0), window=frame, anchor=tk.NW)

    root.mainloop()

if __name__ == '__main__':
    main()



