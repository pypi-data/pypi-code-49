from os              import remove
from random          import randint
from subprocess      import Popen
from subprocess      import PIPE
from hackpy.info     import *
from hackpy.settings import *
from hackpy.modules  import *

class command:
	##|
	##| Execute system command     : hackpy.command.system('command')
	##| Execute system command     : hackpy.command.hiddenSystem('command')
	##| Execute nircmdc command    : hackpy.command.nircmdc('command')
	##| Execute powershell command : hackpy.command.powershell('command')
	##|
	def system(recived_command, return_code = False):
		process = Popen(
			recived_command,
			shell    = True,
			stdout   = PIPE,
			stderr   = PIPE
			)

		
		output = process.communicate()
		code   = process.returncode

		if output[0]:
			output = output[0].decode('866')
			if output.endswith('\n'):
				output = output[:-1]
		else:
			output = output[1].decode('866')
			print(output)
			if output.endswith('\n'):
				output = output[:-1]

		if return_code:
			return output, code
		else:
			return output


	def hiddenSystem(recived_command):
		vbs_path = temp_path + r'systemCommand-' + str(randint(1, 99999)) + '.vbs'
		with open(vbs_path, 'w') as file:
			file.write('''
set ws = wscript.createobject(\"WScript.shell\")
ws.run(\"''' + recived_command + '''\"), 0, true''')
		command.system(vbs_path)
		remove(vbs_path)

	def nircmdc(recived_command):
		require_module('nircmd.exe')
		return command.system(modules_path + r'nircmd.exe ' + recived_command)

	def powershell(recived_command):
		output = command.system('@powershell.exe ' + recived_command)
		return output