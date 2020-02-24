#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""passcrypt module"""

from sys import argv, stdout

from os import path, remove, environ, chmod, stat, makedirs, name as osname

from yaml import load, dump, Loader, Dumper

from colortext import blu, yel, grn, bgre, tabd, error

from system import \
    userfind, filerotate, setfiletime, \
    xgetpass, xmsgok, xinput, xnotify, \
    filerotate, absrelpath, xyesno, random, copy

from secrecy.gpgtools import GPGTool, GPGSMTool, DecryptError, SignatureError

try:
	from atexit import register
except ImportError:
	pass

class PassCrypt(GPGTool):
	"""passcrypt main class"""
	dbg = None
	vrb = None
	aal = None
	fsy = None
	sho = None
	rnd = None
	out = None
	gsm = None
	sig = True
	dtg = True
	gui = None
	chg = None
	syn = None
	try:
		user = userfind()
		home = userfind(user, 'home')
	except FileNotFoundError:
		user = environ['USERNAME']
		home = path.join(environ['HOMEDRIVE'], environ['HOMEPATH'])
	user = user if user else 'root'
	home = home if home else '/root'
	config = path.join(home, '.config', 'pwclip.cfg')
	plain = path.join(home, '.pwd.yaml')
	crypt = path.join(home, '.passcrypt')
	recvs = []
	keys = {}
	gpgkey = ''
	sslcrt = ''
	sslkey = ''
	sigerr = None
	genpwrex = None
	genpwlen = 24
	__weaks = {}
	__oldweaks = {}
	def __init__(self, *args, **kwargs):
		"""passcrypt init function"""
		for arg in args:
			if hasattr(self, arg):
				setattr(self, arg, True)
		for (key, val) in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, val)
		if self.dbg:
			print(bgre(PassCrypt.__mro__))
			print(bgre(tabd(PassCrypt.__dict__, 2)))
			print(' ', bgre(self.__init__))
			print(bgre(tabd(self.__dict__, 4)))
		self.cpasmsg = '%s %s%s '%(
            blu('enter password for'), yel(self.crypt), blu(':'))
		gargs = list(args) + ['sig'] if self.sig else []
		if self.gui:
			gargs = list(args) + ['gui'] + ['sig'] if self.sig else []
			self.cpasmsg = 'enter password for %s: '%self.crypt
		if self.gsm or (
              self.gsm is None and self.recvs and [
                  r for r in self.recvs if r in GPGSMTool().keylist(True)]):
			GPGSMTool.__init__(self, *args, **kwargs)
		else:
			GPGTool.__init__(self, *args, **kwargs)
		self.keys = self.findkey()
		if not self.keys:
			self._mkconfkeys()
		self.__weaks = dict(sorted(dict(self._readcrypt()).items()))
		self.__oldweaks = str(self.__weaks)
		if osname != 'nt':
			register(self._cryptpass)

	def __del__(self):
		self._cryptpass()

	def _cryptpass(self):
		chgs = []
		crecvs = []
		if path.isfile(self.crypt):
			erecvs = list(set(self.recvlist(self.crypt)))
			for r in erecvs:
				crecvs.append('0x%s'%r[-16:])
			for r in self.recvs:
				if r not in crecvs:
					chgs.append('+ %s'%r)
			for r in crecvs:
				if r not in self.recvs:
					chgs.append('- %s'%r)
		if self.__oldweaks != str(dict(sorted(self.__weaks.items()))) or chgs:
			msg = ('recipients have changed:\n',
                    '\n'.join(c for c in chgs),
                    '\nfrom:\n', ' '.join(erecvs),
                    '\nto:\n', ' '.join(self.recvs),
                    '\nencryption enforced...')
			if chgs:
				if not self.gui:
					error(*msg)
				else:
					xmsgok(' '.join(msg))
			if not self.recvs and not self.findkey():
				self.genkeys(**self._gendefs(self.gui))
			if self.__weaks:
				if self._writecrypt(self.__weaks):
					if self.vrb:
						print(blu('file'), yel(self.crypt), blu('encrypted'))

	def _mkconfkeys(self):
		self.gpgkey = '0x%s'%str(self.genkeys())[-16:]
		cfgs = {'gpg': {}}
		override = False
		if path.isfile(self.config):
			override = True
			with open(self.config, 'r') as cfh:
				cfgs = dict(load(cfh.read(), Loader=Loader))
			if 'gpg' not in cfgs.keys():
				cfgs['gpg'] = {}
		cfgs['gpg']['gpgkey'] = self.gpgkey
		if 'recipients' not in cfgs['gpg'].keys():
			cfgs['gpg']['recipients'] = self.gpgkey
			self.recvs = [self.gpgkey]
		with open(self.config, 'w+') as cfh:
			cfh.write(str(dump(cfgs, Dumper=Dumper)))

	def _readcrypt(self):
		"""read crypt file method"""
		if self.dbg:
			print(bgre(self._readcrypt))
		__dct = {}
		try:
			__dct, err = self.decrypt(self.crypt)
		except DecryptError as err:
			error(err)
			exit(1)
		__dct = dict(load(str(__dct), Loader=Loader))
		if err:
			if err == 'SIGERR':
				if self.gui:
					yesno = xyesno('reencrypt, even though ' \
                        'the passcryt signature could not be verified?')
				else:
					print(grn('reencrypt, even though ' \
                        'the passcryt signature could not be verified?'),
                        '[Y/n]')
					yesno = input()
					yesno = True if yesno in ('', 'y') else False
				if yesno and __dct:
					self._writecrypt(__dct)
		return __dct

	def _writecrypt(self, __weaks):
		"""crypt file writing method"""
		if self.dbg:
			print(bgre(self._writecrypt))
		kwargs = {
            'output': self.crypt,
            'gpgkey': self.gpgkey,
            'recvs': self.recvs}
		filerotate(self.crypt, 3)
		if self.sig and self.dtg:
			filerotate('%s.sig'%self.crypt, 3)
		isok = self.encrypt(
            str(dump(__weaks, Dumper=Dumper)), output=self.crypt)
		chmod(self.crypt, 0o600)
		return isok

	def __askpwdcom(self, sysuser, usr, pwd, com, opw, ocom):
		if self.rnd:
			pwd = self.rndgetpass()
		if self.gui:
			if not pwd:
				pwd = xgetpass(
                    'blank input preserves already set comment/password\nas user %s: enter password for entry %s'%(sysuser, usr))
				pwd = pwd if pwd else opw
				if not pwd:
					xmsgok('password is needed if adding password')
					return
			if not com:
				com = xinput(
				    'enter comment (optional, "___" deletes the comment)')
			com = ocom if not com else com
			if com == '___':
				com = None
		else:
			if not pwd:
				print(
                    blu('blank input preserves already set comment/password'),
                    blu('as user '), yel(sysuser), ': ', sep='')
				pwd = pwd if pwd else self.passwd(msg='%s%s%s%s: '%(
						blu('  enter '), yel('password '),
						blu('for entry '), yel('%s'%usr)))
				pwd = pwd if pwd else opw
				if not pwd:
					error('password is needed if adding password')
					return
			if not com:
				print(
                    blu('  enter '), yel('comment '),
                    blu('(optional, '), yel('___'),
                    blu(' deletes the comment)'), ': ', sep='', end='')
				com = input()
			com = ocom if not com else com
			if com == '___':
				com = None
		return [p for p in [pwd, com] if p is not None]

	def rndgetpass(self):
		while True:
			__pwd = random(self.genpwlen, self.genpwrex)
			yesno = False
			if self.gui:
				yesno = xyesno('use the following password: "%s"?'%__pwd)
			else:
				print('%s %s%s [Y/n]'%(
                    grn('use the following password:'),
                    yel(__pwd), grn('?')), sep='')
				yesno = input()
				yesno = True if str(yesno).lower() in ('y', '') else False
			if yesno:
				break
		return __pwd

	def adpw(self, usr, pwd=None, com=None):
		"""password adding method"""
		if self.dbg:
			print(bgre(tabd({
                self.adpw: {'user': self.user, 'entry': usr,
                            'pwd': pwd, 'comment': com}})))
		if self.user not in self.__weaks.keys():
			self.__weaks[self.user] = {}
		if not self.aal:
			if self.user in self.__weaks.keys():
				if usr in self.__weaks[self.user]:
					if self.gui:
						xmsgok('entry %s already exists for user %s'%(
                            usr, self.user))
					else:
						error(
                            'entry', usr, 'already exists for user', self.user)
					return self.__weaks
				elif self.user not in self.__weaks.keys():
					self.__weaks[self.user] = {}
				__opw, __ocom = self.__weaks[self.user][usr]
				pwdcom = self.__askpwdcom(
                    self.user, usr, pwd, com, __opw, __ocom)
				if pwdcom:
					self.__weaks[self.user][usr] = [p for p in pwdcom if p]
		else:
			for u in self.__weaks.keys():
				if usr in self.__weaks[u].keys():
					if self.gui:
						xmsgok('entry %s already exists for user %s'%(usr, u))
					else:
						error('entry', usr, 'already exists for user', u)
					continue
				__opw, __ocom = self.__weaks[u][usr]
				pwdcom = self.__askpwdcom(
                    self.user, usr, pwd, com, __opw, __ocom)
				if pwdcom:
					self.__weaks[u][usr] = [p for p in pwdcom if p]
		return dict(self.__weaks)

	def chpw(self, usr, pwd=None, com=None):
		"""change existing password method"""
		if self.dbg:
			print(bgre(tabd({
                self.chpw: {'user': self.user, 'entry': usr, 'pwd': pwd}})))
		if not self.aal:
			if self.__weaks and self.user in self.__weaks.keys() and \
                    usr in self.__weaks[self.user].keys():
				try:
					__opw = self.__weaks[self.user][usr][0]
				except IndexError:
					return
				try:
					__ocmd = self.__weaks[self.user][usr][1]
				except IndexError:
					__ocmd = None
				self.__weaks[self.user][usr] = self.__askpwdcom(
                    self.user, usr, pwd, com, __opw, __ocmd)
			else:
				if self.gui:
					xmsgok('no entry named %s for user %s'%(usr, self.user))
				else:
					error('no entry named', usr, 'for user', self.user)
		else:
			for u in self.__weaks.keys():
				#	if self.gui:
				#		xmsgok('entry %s does not exist for user %s'%(usr, u))
				#	else:
				#		error('entry', usr, 'does not exist for user', u)
				#	continue
				__opw = ''
				__ocom = None
				if usr not in self.__weaks[u].keys():
					self.__weaks[u][usr] = [__opw, __ocom]
				elif self.__weaks[self.user][usr]:
					__opw, __ocom = self.__weaks[self.user][usr]
				self.__weaks[u][usr] = self.__askpwdcom(
                    self.user, usr, pwd, com, __opw, __ocom)
		return dict(self.__weaks)

	def rmpw(self, usr):
		"""remove password method"""
		if self.dbg:
			print(bgre(tabd({self.rmpw: {'user': self.user, 'entry': usr}})))
		if self.aal:
			__w = dict(self.__weaks)
			for u in __w.keys():
				try:
					del self.__weaks[u][usr]
					setattr(self, 'chg', True)
				except KeyError:
					if self.gui:
						xmsgok('entry %s not found as user %s'%(usr, u))
					else:
						error('entry', usr, 'not found as user', u)
				if not self.__weaks[u].keys():
					del self.__weaks[u]
		else:
			if self.user in self.__weaks.keys() and \
                  usr in self.__weaks[self.user].keys():
				del  self.__weaks[self.user][usr]
			else:
				if self.gui:
					xmsgok('entry %s not found as user %s'%(usr, self.user))
				else:
					error('entry', usr, 'not found as user', self.user)
			if self.user in self.__weaks.keys() \
                  and not self.__weaks[self.user].keys():
				del self.__weaks[self.user]
		return dict(self.__weaks)

	def lspw(self, usr=None, aal=None):
		"""password listing method"""
		if self.dbg and not self.gui:
			print(bgre(tabd({self.lspw: {'user': self.user, 'entry': usr}})))
		aal = True if aal else self.aal
		__ents = {}
		if self.__weaks:
			if aal:
				__ents = self.__weaks
				if usr:
					usrs = [self.user] + \
                        [u for u in self.__weaks.keys() if u != self.user]
					for u in usrs:
						if u in self.__weaks.keys() and \
                              usr in self.__weaks[u].keys():
							__ents = {usr: self.__weaks[u][usr]}
							break
			elif self.user in self.__weaks.keys():
				__ents = self.__weaks[self.user]
				if usr in __ents.keys():
					__ents = {usr: self.__weaks[self.user][usr]}
		return dict(__ents)

def lscrypt(usr, dbg=None):
	"""passlist wrapper function"""
	if dbg:
		print(bgre(lscrypt))
	__ents = {}
	if usr:
		__ents = PassCrypt().lspw(usr)
	return __ents




if __name__ == '__main__':
	exit(1)
