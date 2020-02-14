import os
from tkinter import *
import tkinter as Tk
import tkinter.ttk as ttk
from pybuildit.gui.graph_tab import GraphTab
from pybuildit.gui.config_tab import ConfigTab
from pybuildit.gui.log_tab import LogTab
from pybuildit.gui.init_tab import InitTab
from pybuildit.gui.control_tab import ControlTab

class MainPanel(Tk.Frame):

    def __init__(self, buildit, master):
        Tk.Frame.__init__(self, master)
        self.buildit = buildit

        self.add_tab()

    def add_tab(self, event=None):
        
        note = ttk.Notebook(self, width=600, height=800)
        isUnsafeMode = int(os.getenv('UNSAFE_BUILDIT', 0)) == 1
        if isUnsafeMode:
            note.add(InitTab(self.buildit, note), text = "Init")
        note.add(ControlTab(self.buildit, note), text = "Control")
        if isUnsafeMode:
            note.add(ConfigTab(self.buildit, 'unsafe-servo.yml', True, note), text = "ServoParam")
        else:
            note.add(ConfigTab(self.buildit, 'servo.yml', True, note), text = "ServoParam")
        note.add(ConfigTab(self.buildit, 'system.yml', False, note), text = "SystemParam")

        note.add(LogTab(self.buildit, isUnsafeMode, note), text = "Log")

        note.add(GraphTab(self.buildit, note), text = "Graph")

        note.pack(fill="both", expand=True)

