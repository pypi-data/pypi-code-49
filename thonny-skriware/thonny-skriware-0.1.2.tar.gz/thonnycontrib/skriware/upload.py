import contextlib
import io
import os
import sys
import threading
import time
import tkinter as tk

import esptool
import thonny
from ampy.files import Files as FileHandler
from ampy.pyboard import Pyboard, PyboardError


class UploadManager(threading.Thread):
  '''Main uploading thread which starts all other upload threads'''

  def __init__(self, plugin, upload_firmware=True, upload_scripts=True):
    threading.Thread.__init__(self)

    self.plugin = plugin
    self.upload_firmware = upload_firmware
    self.upload_scripts = upload_scripts

    self._success = False
    self._success_mutex = threading.Lock()

    self.iostream = io.StringIO()
    self.runner = thonny.get_runner()
    self.progress_thread = ProgressThread(self.iostream)
  
  @property
  def success(self):
    with self._success_mutex:
      return self._success
  
  @success.setter
  def success(self, val):
    with self._success_mutex:
      self._success = val

  def exit_with_msg(self, msg):
    self.iostream.write(msg)
    self.progress_thread._break = True
    self.progress_thread.join()

  def restart_backend(self):
    self.runner.cmd_stop_restart()
    self.iostream.write('Waiting for backend\n')
    while self.runner.get_backend_proxy() is None:
      pass
      
  def run(self):
    self.progress_thread.start()

    backend_proxy = self.runner.get_backend_proxy()
    if hasattr(backend_proxy, '_port'):
      self.port = backend_proxy._port
    else:
      return self.exit_with_msg('No board connected, aborting\n')

    if self.upload_firmware:
      self.success = False
      upload_firmware_thread = UploadFirmwareThread(
        self.iostream,
        self.port,
        self.plugin.firmware_path,
        mgr=self
      )
      upload_firmware_thread.start()
      upload_firmware_thread.join()

      if not self.success:
        return self.exit_with_msg('Uploading firmware failed, aborting\n')
      
    if self.upload_scripts:
      self.success = False
      upload_scripts_thread = UploadScriptsThread(
        self.plugin, self.iostream, self.port, mgr=self)
      upload_scripts_thread.start()
      upload_scripts_thread.join()

      if not self.success:
        return self.exit_with_msg(
          'Uploading Skribot scripts failed, aborting\n')

    self.exit_with_msg('Done, resetting\n')
    self.restart_backend()

    # This is really ugly
    time.sleep(1)
    self.plugin.restart_robot_handler()
    time.sleep(1)
    self.plugin.break_handler()

class ProgressThread(threading.Thread):
  '''This thread prints the common iostream contents into the shell'''

  def __init__(self, iostream):
    threading.Thread.__init__(self)
    self.iostream = iostream
    self._break = False
  
  def run(self):
    shell = thonny.get_shell()
    text = shell.text
    while True:
      text.set_content('')
      text.direct_insert(tk.INSERT, self.iostream.getvalue())
      text.see('end')
      time.sleep(0.5)

      if self._break:
        break

class UploadFirmwareThread(threading.Thread):
  '''Uploads main micropython binary to the board'''

  def __init__(self, iostream, port, fw_path, mgr=None):
    threading.Thread.__init__(self)

    self.iostream = iostream
    self.port = port
    self.mgr = mgr
    self.firmware_path = fw_path

  def run(self):
    self.iostream.write(
      'Uploading micropython firmware to {}\n'.format(self.port))
    self.iostream.write('Disconnecting backend\n')

    thonny.get_runner().disconnect()

    # Apparently Windows needs some time to release the COM port
    if sys.platform == 'win32':
      time.sleep(1)
    
    self.iostream.write('Erasing flash\n')
    with contextlib.redirect_stdout(self.iostream):
      esptool.main((
        '--port', self.port,
        'erase_flash'
      ))

    self.iostream.write('Uploading micropython binary\n')
    with contextlib.redirect_stdout(self.iostream):
      esptool.main((
        '--chip', 'esp32',
        '--port', self.port,
        '--baud', '460800',
        'write_flash', '-z',
        '--flash_mode', 'dio',
        '--flash_freq', '40m',
        '0x1000', self.firmware_path
      ))
    
    self.iostream.write('Done uploading micropython firmware\n')
    if self.mgr is not None:
      self.mgr.success = True

class UploadScriptsThread(threading.Thread):
  '''Uploads the scripts to the board that can be changed by user'''

  def __init__(self, plugin, iostream, port, mgr=None):
    threading.Thread.__init__(self)

    self.plugin = plugin
    self.iostream = iostream
    self.port = port
    self.mgr = mgr

    # ampy handlers
    self.pyboard = Pyboard(port)
    self.file_handler = FileHandler(self.pyboard)

  def run(self):
    self.iostream.write('Uploading Skribot scripts\n')
    scripts = self.plugin.scripts
    pprefix = 'micropython-skribot'

    for script in scripts:
      script_path = self.plugin.relpath(os.path.join(pprefix, script))

      with open(script_path, 'r') as fh:
        data = fh.read()

        self.iostream.write('Uploading {}\n'.format(script))

        retries = 0
        while True:
          try:
            self.file_handler.put(script, data)
            break
          except PyboardError:
            retries += 1
            if retries > 3:
              self.iostream.write('Upload failed, aborting\n')
              return
            else:
              self.iostream.write('Upload failed, retrying\n')
              time.sleep(retries)
          except Exception as e:
            self.iostream.write('Unknown failure\n')
            print(e, file=sys.stderr)
            return

      time.sleep(1)
    
    self.iostream.write('Done uploading Skribot scripts\n')
    if self.mgr is not None:
      self.mgr.success = True
