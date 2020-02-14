import sys,os
from tkinter import *
import tkinter as Tk
import tkinter.ttk as ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog
import yaml
from collections import OrderedDict
from pybuildit import *
import logging
from pybuildit.gui.util  import *
import time

logger = logging.getLogger("pybuildit")

class InitTab(Tk.Frame):

    def __init__(self, buildit, master=None):
        Tk.Frame.__init__(self, master)
        self.buildit = buildit

        self.initButton= Tk.Button(self, text='Init', width= "10", command=self.init)
        self.initButton.pack(pady=5)

        self.calibButton = Tk.Button(self, text='Calib', width= "10", command=self.calib)
        self.calibButton .pack(pady=5)

        self.resetButton= Tk.Button(self, text='CheckEnc', width= "10", command=self.checkEnc)
        self.resetButton.pack(pady=5)

        self.zeroButton= Tk.Button(self, text='SetZero', width= "10", command=self.setZero)
        self.zeroButton.pack(pady=5)

        self.resetButton= Tk.Button(self, text='Reset', width= "10", command=self.reset)
        self.resetButton.pack(pady=5)

        self.setFaultButton= Tk.Button(self, text='Fault', width= "10", command=self.fault_open)
        self.setFaultButton.pack(pady=5)

        self.setFaultButton= Tk.Button(self, text='Dump', width= "10", command=self.dump)
        self.setFaultButton.pack(pady=5)

    def fault_open(self):
        
        logger.error("Fault button clicked")
        inputDialog = SelectFaultDialog(self)
        self.wait_window(inputDialog.top)

        if inputDialog.faults is None:
            return
        
        tryBuildit(lambda: self.buildit.fault(builditGuiInfo.targetDevId, inputDialog.faults))
        logger.error("Fault Error1 %s" % str(inputDialog.faults))

    def dump(self):
        params_filetypes = [('yaml files', '.yaml .yml')]
        f = filedialog.asksaveasfile(mode="w",
                                     parent= self, 
                                     initialdir=os.getcwd(),
                                     title="Select file", 
                                     filetypes= params_filetypes, 
                                     defaultextension=".yml")
        if f is None:
            return
        name = f.name
        f.close()

        devId= builditGuiInfo.targetDevId
        self.buildit.save_configuration(devId, name)
        

    def reset(self):
        logger.info("Reset button clicked ")
        tryBuildit(lambda: self.buildit.reset(builditGuiInfo.targetDevId))

    def calib(self):
        logger.info("Calib button clicked ")
        tryBuildit(lambda: calibrate(self.buildit, builditGuiInfo.targetDevId))

    def init(self):
        logger.info("Init button clicked ")

        def f():
            _f = os.path.join(os.path.dirname(__file__), "config/default_params.yml")
            self.buildit.clear_log(builditGuiInfo.targetDevId)
            self.buildit.load_servo_params(builditGuiInfo.targetDevId, _f)
            self.buildit.set_device_id(builditGuiInfo.targetDevId, 1)

        tryBuildit(f)

    def setZero(self):
        logger.info("Zero button clicked ")

        def f():
            p = self.buildit.query_servo_status(builditGuiInfo.targetDevId).position()
            offset0 = self.buildit.get_position_sys_offset(builditGuiInfo.targetDevId)
            offset1 = self.buildit.get_position_offset(builditGuiInfo.targetDevId)
            self.buildit.set_position_sys_offset(builditGuiInfo.targetDevId, (p + offset0 + offset1) % 65536)

        tryBuildit(f)

    def checkEnc(self):
        logger.info("Check Enc button clicked ")

        def f():
            n = 2000
            self.buildit.set_ref_velocity(builditGuiInfo.targetDevId, 200)
            for i in range(n):
                print("debug", i)
                self.buildit.debug(builditGuiInfo.targetDevId, 3)

        tryBuildit(f)



class SelectFaultDialog:
    
    def __init__(self, parent):
        top = self.top = Tk.Toplevel(parent)
        top.grab_set()
        top.focus_set()

        self.faults = None

        self.vars = []
        self.checkButtons = []

        for (faultNo, faultName) in faultDict.items():
            var = Tk.BooleanVar()
            checkButton = Tk.Checkbutton(top, text=faultName, variable=var)
            checkButton.pack(anchor = "w")
            self.vars.append(var)
            self.checkButtons.append(checkButton)

        self.submitButton = Tk.Button(top, text='Submit', command=self.send)
        self.submitButton.pack()

    def send(self):
        self.faults = 0

        for i, var in enumerate(self.vars):
            if var.get() == True:
                self.faults += list(faultDict.keys())[i]

        self.top.destroy()

