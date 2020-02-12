import json
import os
import sys
import threading
import time

import ipdb
import thonny
from thonny import get_workbench

from .help import HelpWindow
from .shell import Shell
from .theme import SkriwareTheme
from .upload import UploadManager


class SkriwarePlugin:
  instance = None

  @staticmethod
  def relpath(path):
    return os.path.join(os.path.dirname(__file__), path)

  def __init__(self):
    if SkriwarePlugin.instance is None:
      SkriwarePlugin.instance = self 
      self.workbench = get_workbench()
      self.help_window = None

      self.config = self.load_config()
      self.scripts = self.config['scripts']
      self.commands = self.config['commands']
      for cmd in self.commands:
        cmd['icon'] = SkriwarePlugin.relpath(cmd['icon'])
        cmd['handler'] = getattr(self, cmd['handler'])
      self.firmware_path = SkriwarePlugin.relpath(self.config['firmware_path'])
      self.shell = None

    else:
      pass

    self.workbench.set_option('run.backend_name', 'ESP32')

  def load_config(self):
    with open(SkriwarePlugin.relpath('settings.json'), 'r') as f:
      return json.load(f)

  # NOTE: Handlers
  def debug_handler(self):
    shell = thonny.get_shell()
    runner = thonny.get_runner()
    ipdb.set_trace()

  def select_interpreter_handler(self):
    self.workbench.show_options('interpreter')
  
  def upload_micropython_handler(self):
    mgr = UploadManager(self)
    mgr.start()

  def open_boot_py_handler(self):
    self.open_remote_file('boot.py')
  
  def open_scratchpad_py_handler(self):
    self.open_remote_file('scratchpad.py')

  def restart_robot_handler(self):
    self.shell.run_script('\n'.join((
      'from machine import reset',
      'reset()',
      ''
    )))

  def break_handler(self):
    # HACK, hacks all around
    # This basically checks if the robot is in a loop
    # If it is, then clear the shell twice to remove that ugly warning
    clear_twice = True
    if thonny.get_runner().ready_for_remote_file_operations():
      clear_twice = False

    self.shell.send_keyboard_interrupt()
    self.shell.clear()

    if clear_twice:
      self.shell.shell.after(500, self.shell.clear_with_prompt)
  
  def help_handler(self):
    if self.help_window is not None:
      # Only one help window is necessary
      return

    self.help_window = HelpWindow(parent=self)
    self.help_window.mainloop()

  def open_remote_file(self, fname):
    # TODO:
    # maybe it's a good idea to fetch the file with ampy
    # because this stupid thing evaluates things in the shell
    # raising exceptions that are difficult to catch

    runner = thonny.get_runner()

    if runner.ready_for_remote_file_operations():
      notebook = self.workbench.get_editor_notebook()
      try:
        notebook.show_remote_file(fname)
      except Exception as e:
        self.shell.print('No such file: {}'.format(fname))
        if fname in self.scripts:
          self.shell.print('Try reuploading micropython')
        self.shell.insert_prompt()
    else:
      self.shell.print('\n'.join((
        'Not ready for remote operations',
        'Check if the board is connected properly',
        ''
      )))
      self.shell.insert_prompt()
    
  def load_plugin(self):
    # Add Skriware menu
    for cmd in [c for c in self.commands if c['menubar']]:
      self.workbench.add_command(
        command_id=cmd['name'].lower().replace(' ', '_'),
        menu_name='Skriware',
        command_label=cmd['name'],
        handler=cmd['handler'],
        image=cmd['icon']
      )
    
    # Add Skribot examples menu
    for example in [s for s in self.scripts if s.startswith('example_')]:
      label = example.replace('example_', '')
      label = label.replace('_', ' ').replace('.py', '').strip().title()

      self.workbench.add_command(
        command_id=example,
        menu_name='Skribot examples',
        command_label=label,
        handler=lambda example=example: self.open_remote_file(example)
      )

    # Register themes
    self.workbench.add_ui_theme(
      'Skriware Theme',
      'Clean Sepia',
      SkriwareTheme.theme,
      SkriwareTheme.theme_image_map()
    )

    # Try creating toolbar buttons and registering shell wrapper until success
    # The toolbar object is initialized AFTER the load_plugin is called
    tcmds = [c for c in self.commands if c['toolbar']]
    late_initializer = LateInitializer(self)
    late_initializer.start()

class LateInitializer(threading.Thread):
  '''Initializes things that could not be initialized earlier'''

  def __init__(self, plugin):
    threading.Thread.__init__(self, daemon=True)
    self.plugin = plugin
    self.commands = [c for c in self.plugin.commands if c['toolbar']]
  
  def run(self):
    while True:
      try:
        for cmd in self.commands:
          name = cmd['name']
          icon = self.plugin.workbench.get_image(cmd['icon'])
          
          # This is really bad design but I didn't find any
          # better option to add toolbar button than a private method
          # this internal API has already been changed once
          self.plugin.workbench._add_toolbar_button(
            name, icon, icon, name, name, None, None, cmd['handler'], None, 500)

          self.plugin.shell = Shell()
        break

      except Exception as e:
        print(e, file=sys.stderr)
        time.sleep(0.3)
        continue
