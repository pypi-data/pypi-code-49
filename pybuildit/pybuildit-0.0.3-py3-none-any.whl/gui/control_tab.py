from tkinter import *
import tkinter as Tk
import tkinter.ttk as ttk
import sys
from pybuildit import *
from pybuildit.gui.util  import *
import logging
from tkinter import messagebox
from tkinter import font

logger = logging.getLogger("pybuildit")

class ControlTab(Tk.Frame):
     
    def __init__(self, buildit, master):
        Tk.Frame.__init__(self, master)
        self.buildit = buildit

        self.parameter_config = Label(self, text="PARAMETER CONTROL", anchor=N, font=("Arial", 10))
        self.parameter_config.grid(row=0, column=1, columnspan=1, padx=15, pady=15)
        self.parameter_config.configure(font=self.config_underline(self.parameter_config))

        self.max_pos_limit = Label(self, text="Max Position Limit", anchor=N, font=("Arial", 9))
        self.max_pos_limit.grid(row=1, column=0, columnspan=1, padx=5, pady=5)

        self.max_pos_limit_button = Tk.Button(self, text="SET", width = "20", command = self.set_position_max_limit)
        self.max_pos_limit_button.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

        self.max_pos_limit_clear_button = Tk.Button(self, text="CLEAR", width = "20", command = self.clear_position_max_limit)
        self.max_pos_limit_clear_button.grid(row=1, column=2, columnspan=1, padx=5, pady=5)

        self.min_pos_limit = Label(self, text="Min Position Limit", anchor=N, font=("Arial", 9) )
        self.min_pos_limit.grid(row=2, column=0, columnspan=1, padx=5, pady=5)

        self.min_pos_limit_button = Tk.Button(self, text="SET", width = "20", command = self.set_position_min_limit)
        self.min_pos_limit_button.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

        self.min_pos_limit_clear_button = Tk.Button(self, text="CLEAR", width = "20", command = self.clear_position_min_limit)
        self.min_pos_limit_clear_button.grid(row=2, column=2, columnspan=1, padx=5, pady=5)

        self.other_config = Label(self, text="OTHER CONTROL", anchor=N, font=("Arial", 10) )
        self.other_config.grid(row=3, column=1, columnspan=1, padx=15, pady=15)
        self.other_config.configure(font=self.config_underline(self.other_config))

        self.reset_rot = Label(self, text="Reset Rotation", anchor=N, font=("Arial", 9) )
        self.reset_rot.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

        self.reset_rot_button= Tk.Button(self, text='RESET', width= "20", command=self.reset_rotation)
        self.reset_rot_button.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

    def config_underline(self, v):
        self.f =font.Font(v, v.cget("font"))
        self.f.configure(underline=True)
        return self.f

    def reset_rotation(self):
        logger.info("ResetRotation reset button clicked")
        tryBuildit(lambda: self.buildit.reset_rotation(builditGuiInfo.targetDevId, 0))

    def get_current_position(self):
        pos = tryBuildit(lambda: self.buildit.query_servo_status(builditGuiInfo.targetDevId).position())
        logger.info("Current Position value is: {}".format(pos))
        return pos

    def set_position_max_limit(self):
        logger.info("Position max limit is set to {}".format(self.get_current_position()))
        tryBuildit(lambda: self.buildit.set_position_max_limit(builditGuiInfo.targetDevId,(self.get_current_position())))

    def set_position_min_limit(self):
        logger.info("Position min limit is set to {}".format(self.get_current_position()))
        tryBuildit(lambda: self.buildit.set_position_min_limit(builditGuiInfo.targetDevId,self.get_current_position()))

    def clear_position_max_limit(self):
        logger.info("Position min limit is set to {}".format(self.default_max_pos_limit()))
        tryBuildit(lambda: self.buildit.set_position_max_limit(builditGuiInfo.targetDevId,self.default_max_pos_limit()))

    def clear_position_min_limit(self):
        logger.info("Position min limit is set to {}".format(self.default_min_pos_limit()))
        tryBuildit(lambda: self.buildit.set_position_min_limit(builditGuiInfo.targetDevId,self.default_min_pos_limit()))

    def load_default_params(self, val):
        with open(os.path.join(os.path.dirname(__file__), 'config', 'default_params.yml'), "r") as file:
            try:
                self.params= (yaml.safe_load(file))
                for key, value in self.params.items():
                    if key =="PARAM_ID_POSITION_MAX_LIMIT":
                        self.PosMaxLimit= value
                    if key =="PARAM_ID_POSITION_MIN_LIMIT":
                        self.PosMinLimit= value
            except yaml.YAMLError as exc:
                print(exc)

        if val == "max":
            logger.info("Default pos_max_limit value is: {}".format(int(self.PosMaxLimit)))
            return int(self.PosMaxLimit)

        if val == "min": 
            logger.info("Default pos_min_limit value is: {}".format(int(self.PosMinLimit)))
            return int(self.PosMinLimit)

    def default_max_pos_limit(self):
        return self.load_default_params("max")

    def default_min_pos_limit(self):
        return self.load_default_params("min")