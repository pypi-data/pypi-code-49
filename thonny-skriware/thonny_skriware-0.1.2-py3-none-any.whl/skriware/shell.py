import tkinter as tk

import thonny


class Shell:
  '''This is just a wrapper for thonny's Shell'''

  def __init__(self):
    self.shell = thonny.get_shell()
    self.text = self.shell.text
  
  def print(self, text, end='\n'):
    self.text.direct_insert(tk.INSERT, '{}{}'.format(text, end))
    self.scroll_down()
  
  def scroll_down(self):
    self.text.see('end')

  def clear(self):
    self.text.set_content('')

  def clear_with_prompt(self):
    self.text.set_content('')
    self.insert_prompt()

  def run_script(self, script):
    self.text._submit_input(script)
  
  def insert_prompt(self):
    self.text._insert_prompt()
  
  def send_keyboard_interrupt(self):
    self.run_script((chr(3)+'\n'))
