#!/usr/bin/python3
"""command module of executor"""
from os import access, environ, X_OK, name as osname
try:
	from os import getuid, getresuid
except ImportError:
	def getuid(): return 1000
	def getresuid(): return 1000

from os.path import abspath, join as pjoin

from sys import stdout as _stdout, stderr as _stderr

from subprocess import run, Popen, PIPE, TimeoutExpired

try:
	from subprocess import DEVNULL
except ImportError:
	DEVNULL = open('/dev/null')

try:
	from tkinter import StringVar, Button, Entry, Frame, Label, Tk, TclError
except ImportError:
	from Tkinter import StringVar, Button, Entry, Frame, Label, Tk, TclError
try:
	import readline
except ImportError:
	pass

_echo_ = _stdout.write
_puke_ = _stderr.write

class XInput(Frame):
	"""password clipping class for tkinter.Frame"""
	inp = None
	def __init__(self, master, message, exchange='', noop=None, noin=None):
		self.noop = noop
		self.noin = noin
		self.exchg = exchange
		self.message = message
		Frame.__init__(self, master)
		self.pack()
		self.inputwindow()
	def _enterexit(self, _=None):
		"""exit by saving challenge-response for input"""
		self.inp = True if not self.input else self.input.get()
		self.quit()
	def _breakexit(self, _=None):
		"""exit by saving challenge-response for input"""
		self.inp = None
		self.quit()
	def _exit(self, _=None):
		"""just exit (for ESC mainly)"""
		self.inp = False
		self.quit()
	def inputwindow(self):
		"""password input window creator"""
		self.lbl = Label(self, text=self.message)
		self.lbl.pack()
		okside = {}
		clside = {}
		self.ok = Button(self)
		self.ok.bind("<Control-c>", self._breakexit)
		self.ok.bind("<Escape>", self._exit)
		self.ok.bind("<Return>", self._enterexit)
		self.ok["text"] = "ok"
		self.ok["command"] =  self._enterexit
		self.ok.bind("<Return>", self._enterexit)
		self.input = False
		okside = {'side': 'bottom'}
		if not self.noin:
			self.input = StringVar()
			self.entry = Entry(self, show=self.exchg)
			self.entry.bind("<Return>", self._enterexit)
			self.entry.bind("<Control-c>", self._breakexit)
			self.entry.bind("<Escape>", self._exit)
			self.entry.focus_set()
			self.entry["textvariable"] = self.input
			self.entry.pack()
			okside = {'side': 'left'}
		if not self.noop:
			self.cl = Button(self)
			self.cl.bind("<Return>", self._enterexit)
			self.cl.bind("<Control-c>", self._breakexit)
			self.cl.bind("<Escape>", self._exit)
			self.cl["text"] = "cancel"
			self.cl["command"] = self._exit
			self.cl.pack({'side': 'right'})
			okside = {'side': 'left'}
		if self.noin:
			self.ok.focus_set()
		self.ok.pack(okside)

def xgetpass(message="input will not be displayed"):
	"""gui representing function"""
	try:
		root = Tk()
		pwc = XInput(root, message, exchange='*')
		_set_focus(root)
		pwc.lift()
		pwc.mainloop()
	except KeyboardInterrupt:
		root.destroy()
		raise KeyboardInterrupt
	try:
		root.destroy()
	except:
		pass
	finally:
		return pwc.inp

def _set_focus(window):
	"""os independent focus setter"""
	if osname == 'nt':
		window.after(1, lambda: window.focus_force())


class Command(object):
	"""Command class"""
	sh_ = True
	su_ = False
	gui = False
	vrb = False
	dbg = False
	_auth = False
	timeout = None
	def __init__(self, *args, **kwargs):
		for arg in args:
			if hasattr(self, str(arg)):
				setattr(self, arg, True)
			elif hasattr(self, '%s_'%arg):
				setattr(self, '%s_'%arg, True)
		if self.dbg:
			cb = '\033[1;30m'
			ce = '\033[0m'
			if osname == 'nt':
				cb = ''
				ce = ''
			_echo_('%s%s\n  %s\n  %s'%(
                cb, str(Command.__mro__),
                '\n  '.join('%s = %s'%(k, v) for \
                    (k, v) in self.__dict__.items()), ce))

	@staticmethod
	def _sttyecho():
		run('stty echo', shell=True)

	@staticmethod
	def __which(prog):
		"""which function like the linux 'which' program"""
		delim = ';' if osname == 'nt' else ':'
		__path = ''
		for path in environ['PATH'].split(delim):
			if access(pjoin(path, prog), X_OK):
				__path = pjoin(abspath(path), prog)
		return __path

	@staticmethod
	def _str(commands):
		"""list/tuple to str converter"""
		#print(commands)
		return ' '.join(str(command) for command in list(commands))

	@staticmethod
	def __sucmd(sudobin, commands):
		if 'sudo' in commands[0]:
			del commands[0]
		if int(getuid()) != 0:
			commands.insert(0, sudobin)
		return commands

	def _list(self, commands):
		"""
		commands string to list converter assuming at least one part
		"""
		#print(commands)
		for cmd in list(commands):
			if cmd and max(len(c) for c in cmd if c) == 1 and len(cmd) >= 1:
				return list(commands)
			return self._list(list(cmd))

	def _sudo(self, commands=None):
		"""privilege checking function"""
		sudo = self.__which('sudo')
		if getuid() == 0:
			self._auth = True
			return commands if commands else True
		if not commands:
			if getuid() == 0: return True
			if int(run([sudo, '-v']).returncode) == 0:
				return True
			sucmds = None
			if self.gui:
				try:
					if int(run(
                          '%s -v'%sudo, timeout=0.5, shell=True).returncode) == 0:
						self._auth = True
				except TimeoutExpired:
					pass
				if not self._auth and int(run('%s -S -v'%sudo, shell=True,
                          input=str('%s\n'%xgetpass(
                          'enter sudo password')).encode()
                          ).returncode) == 0:
					self._auth = True
			elif int(run('%s -v'%sudo, shell=True).returncode) == 0:
				self._auth = True
		if self._auth:
			return self.__sucmd(sudo, commands)
		else:
			if not self._sudo():
				raise PermissionError('cannot execute privileged commands')
			return self.__sucmd(sudo, commands)
		#print(commands)
		#print(self.gui)
		#print(self._auth)
		return self._auth

	def __cmdprep(self, commands, func):
		commands = self._list(commands)
		if self.su_:
			try:
				commands = self._sudo(commands)
			finally:
				self._sttyecho()
		if self.sh_:
			commands = self._str(commands)
		if self.dbg:
			_echo_('\033[01;30m%s\n  `%s`\t{sh: %s, su: %s}\033[0m\n'%(
                func, commands, self.sh_, self.su_))
		return commands

	def run(self, *commands):
		"""just run the command and return the processes PID"""
		commands = self.__cmdprep(commands, self.run)
		return Popen(
            commands,
            stdout=DEVNULL, stderr=DEVNULL, shell=self.sh_).pid

	def call(self, *commands, stdout=True, stderr=True, inputs=None, b2s=None):
		"""
		default command execution
		prints STDERR, STDOUT and returns the exitcode
		"""
		inputs = inputs.encode() if (inputs and b2s) else inputs
		stderr = stderr if stderr else DEVNULL
		stdout = stdout if stdout else DEVNULL
		commands = self.__cmdprep(commands, self.call)
		return int(run(
            commands, shell=self.sh_, stdout=stdout,
            stderr=stderr, timeout=self.timeout, input=inputs).returncode)

	def stdx(self, *commands, inputs=None, b2s=True):
		"""command execution which returns STDERR and/or STDOUT"""
		commands = self.__cmdprep(commands, self.stdx)
		inputs = inputs.encode() if (inputs and b2s) else inputs
		prc = Popen(
		    commands, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=self.sh_)
		out, err = prc.communicate(timeout=self.timeout, input=inputs)
		if b2s and out:
			out = u'%s'%(out).decode()
		if b2s and err:
			err = u'%s'%(err).decode()
		return out, err

	def stdo(self, *commands, inputs=None, b2s=True):
		"""command execution which returns STDOUT only"""
		inputs = inputs.encode() if (inputs and b2s) else inputs
		commands = self.__cmdprep(commands, self.stdo)
		prc = Popen(
            commands, stdin=PIPE, stdout=PIPE, stderr=DEVNULL, shell=self.sh_)
		out, _ = prc.communicate(input=inputs, timeout=self.timeout)
		if b2s:
			out = u'%s'%(out).decode()
		return out

	def stde(self, *commands, inputs=None, b2s=True):
		"""command execution which returns STDERR only"""
		inputs = inputs.encode() if (inputs and b2s) else inputs
		commands = self.__cmdprep(commands, self.stde)
		prc = Popen(
		    commands, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=self.sh_)
		_, err = prc.communicate(timeout=self.timeout, input=inputs)
		if b2s and err:
			err = u'%s'%(err).decode()
		return err

	def erno(self, *commands, inputs=None, b2s=True):
		"""command execution which returns the exitcode only"""
		inputs = inputs.encode() if (inputs and b2s) else inputs
		commands = self.__cmdprep(commands, self.erno)
		prc = Popen(commands, stdin=PIPE, stdout=DEVNULL,
            stderr=DEVNULL, shell=self.sh_)
		prc.communicate(timeout=self.timeout, input=inputs)
		return int(prc.returncode)

	def oerc(self, *commands, inputs=None, b2s=True):
		"""command execution which returns STDERR only"""
		inputs = inputs.encode() if (inputs and b2s) else inputs
		commands = self.__cmdprep(commands, self.oerc)
		prc = Popen(
		    commands, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=self.sh_)
		out, err = prc.communicate(timeout=self.timeout, input=inputs)
		if b2s and out :
			out = u'%s'%(out).decode()
		if b2s and err:
			err = u'%s'%(err).decode()
		return out, err, int(prc.returncode)


cmmd = Command('sh')
sudo = Command('sh', 'su')

def sudofork(*args):
	"""sudo command fork wrapper function"""
	if getresuid() == 0:
		return 0
	eno = 0
	try:
		eno = int(sudo.call(args))
	except KeyboardInterrupt:
		_echo_('\033[34maborted by keystroke\033[0m\n')
		eno = 431
	return eno

if __name__ == '__main__':
	exit(1)
