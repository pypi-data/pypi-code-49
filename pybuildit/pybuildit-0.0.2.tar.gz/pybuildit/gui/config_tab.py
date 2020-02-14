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

logger = logging.getLogger("pybuildit")

class ConfigTab(Tk.Frame):

    def __init__(self, buildit, configfile = 'params.yml', editable = False, master=None):
        Tk.Frame.__init__(self, master)
        self.buildit = buildit

        yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                             lambda loader, node: OrderedDict(loader.construct_pairs(node)))

        f = open(os.path.join(os.path.dirname(__file__), 'config', configfile))
        if os.name == "nt":
            self.commands = yaml.load(f, Loader= yaml.FullLoader)
        else:
            self.commands = yaml.load(f)
        self.editable = editable
        self.show_params()

    def modal_open(self, command):

        def x():

            answer = simpledialog.askstring("Input", command['message'],
                                            parent=self)
            if answer is None:
                return
            if answer.replace('.', '', 1).lstrip("-+").isnumeric() and self.buildit.is_open():
                try:
                    method = "self.buildit.set_" + command['method']+"(" + str(builditGuiInfo.targetDevId) + ", " + answer +")"
                    eval(method)
                    logger.info('parameter value edit to: %s'%answer)
                except MCPError as e:
                    messagebox.showerror('communication exception', str(e))
                    logger.error('communication exception: %s'% str(e))
                except Exception as e:
                    messagebox.showerror('exception',str(e))
                    logger.error('exception: %s'% str(e))
                self.show_params()
            else: 
                print('do nothing')
                logger.info('do nothing')
        return x

    def refresh(self):
        logger.info("Refresh button clicked")
        self.show_params()

    def show_params(self):
        list = self.slaves()
        for l in list:
            l.destroy()

        self.bottomFrame = Frame(self)
        self.bottomFrame.pack() 

        if self.editable:
            self.saveFileButton= Tk.Button(self.bottomFrame, text='SaveFile', command=self.save_servo_params)
            
            self.saveFileButton.grid(row=0, column=0, columnspan=1, padx=5, pady=5)
            
            self.loadFileButton= Tk.Button(self.bottomFrame, text='LoadFile', command=self.load_servo_params)
            
            self.loadFileButton.grid(row=0, column=1, columnspan=1, padx=5, pady=5)

            self.loadDefaultButton= Tk.Button(self.bottomFrame, text='LoadDefault', command=self.load_defaut_params)
            
            self.loadDefaultButton.grid(row=0, column=2, columnspan=1, padx=5, pady=5)

        self.button= Tk.Button(self.bottomFrame, text='Refresh', command=self.refresh)
        
        self.button.grid(row=0, column=3, columnspan=1, padx=5, pady=5)

        commands = self.commands
        errorOccured = False
        
        for a in commands:
            frame = Frame(self)
            frame.pack()
            param = '?'

            if self.buildit.is_open() and not errorOccured:
                try:
                    method = "self.buildit.get_" + commands[a]['method' ]+"(" + str(builditGuiInfo.targetDevId) + ")"
                    print(method)
                    logger.info(method)
                    param = str(eval(method)) + commands[a]['unit']
                    print(param)
                    logger.info(param)
                
                except Exception as e:
                    errorOccured = True

            label =Label(frame, text= commands[a]['name'], font=("Arial Bold", 10), width=30)
            label.pack(side=LEFT)
            label_param =Label(frame, text= param, width=30, font=("Arial Bold", 10))
            label_param.pack(side=LEFT)

            if self.editable:
                modal= Tk.Button(frame,text='Edit', command=self.modal_open(commands[a]))
                modal.pack(side=LEFT)
    
    def load_parameter_file(self, filepath):
        try:
            f = open(filepath)
            params = yaml.load(f)

            commands = self.commands
            errorOccured = False
            send_params = []

            try:
                for a in commands:
                    command = commands[a]
                    if command['id_name'] in params:
                        name = command['id_name']
                        value = params[name]
                        # TODO: check validate
                        send_params.append({'method':command['method'], 'value': value})
                        print(name + ' : ' + str(value))
                        
                        logger.info("Load parameter file: %s" %(name + ' : ' + str(value)))

            except Exception as e:
                errorOccured = True
                messagebox.showerror('exception',str(e))
                logger.error("exception: %s" %str(e) )

            if not errorOccured:             
                try:
                    for send_param in send_params:
                        method = "self.buildit.set_" + send_param['method']+"(" + str(builditGuiInfo.targetDevId) + ", " + str(send_param['value']) +")"
                        eval(method)
                    
                    self.show_params()
                except MCPError as e:
                    messagebox.showerror('communication exception', "{} {}".format(str(type(e)), str(send_param)))
                    logger.error("communication exception: %s" %str(type(e)) )
                except Exception as e:
                    messagebox.showerror('exception',str(e))
                    logger.error("exception: %s" %str(e) )
        except Exception as e:
            messagebox.showerror('exception',str(e))
            logger.error("exception: %s" %str(e) )

    def load_servo_params(self):
        params_filetypes = [('yaml files', '.yaml .yml')]
        answer = filedialog.askopenfilename(parent=self,
                                            initialdir=os.getcwd(),
                                            title="Please select a parameter file:",
                                            filetypes=params_filetypes)

        if not answer:
            return

        logger.info("LoadFile button clicked")
        self.load_parameter_file(answer)
        logger.info("Load parameter: %s" %self.load_parameter_file(answer))
        
    def load_defaut_params(self):
        
        logger.info("LoadDefault button clicked")
        self.load_parameter_file(os.path.join(os.path.dirname(__file__), 'config', 'default_params.yml'))
        
    def save_servo_params(self):
        
        params_filetypes = [('yaml files', '.yaml .yml')]
        file = filedialog.asksaveasfile(mode="w",
                                     parent= self, 
                                     initialdir=os.getcwd(),
                                     title="Select file", 
                                     filetypes= params_filetypes, 
                                     defaultextension=".yml")
        if file is None:
            return
        name = file.name
        file.close()

        devId= builditGuiInfo.targetDevId
        self.buildit.save_servo_params(devId, name)
