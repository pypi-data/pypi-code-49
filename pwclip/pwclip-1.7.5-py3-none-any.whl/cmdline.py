#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-
#
# This file is free software by d0n <d0n@janeiskla.de>
#
# You can redistribute it and/or modify it under the terms of the GNU -
# Lesser General Public License as published by the Free Software Foundation
#
# This is distributed in the hope that it will be useful somehow.
# !WITHOUT ANY WARRANTY!
#
# Without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
"""pwclip main program"""
# global & stdlib imports
try:
	from os import fork
except ImportError:
	def fork(): """fork faker function""" ;return 0

try:
	import readline
except ImportError:
	pass

from re import sub

from os import environ, path, remove, getpid, name as osname

from sys import exit, stdout

from argparse import ArgumentParser

import argcomplete
from argcomplete import autocomplete
from argcomplete.completers import FilesCompleter, ChoicesCompleter

from socket import gethostname as hostname

from time import sleep

from yaml import load, Loader

from getpass import getpass

# local relative imports
from colortext import bgre, bred, tabd, error, fatal, abort

from executor.executor import cmmd

from system import \
    absrelpath, copy, paste, xgetpass, \
    xmsgok, xyesno, xnotify, xinput, xkbid, \
    which, whoami, dictreplace, adbout

from pwclip.passcrypt import PassCrypt, lscrypt

from secrecy import ykchalres, yubikeys

from pwclip.__pkginfo__ import version


def showclip(mode='cli', cliptime=None, clear=None):
	text = paste()
	if mode == 'cli':
		print(text, end='')
		stdout.flush()
		if clear:
			if cliptime:
				sleep(cliptime)
			print('\033c', end='')
	elif mode == 'ano':
		adbout(text)
	elif mode == 'gui':
		xnotify(text)

def forkwaitclip(text, poclp, boclp, wait=3, out=None, enter=None):
	"""clipboard forking, after time resetting function"""
	if out:
		xnotify('pwclip: paste')
		if out == 'gui':
			sep = '"'
			if "'" in text and '"' in text:
				text = sub("'", "\'", text)
				text = sub('"', '\"', text)
				sep = '"'
			elif '"' in text:
				sep = "'"
			cmmd.stdo('xvkbd -secure -no-keypad -delay 17 -text %s%s%s'%(sep, text, sep))
		elif out == 'cli':
			stdout.write(r'%s'%text if not enter else r'%s\n'%text)
			stdout.flush()
		elif out == 'ano':
			adbout(text, enter)
			enter = False
	if enter:
		cmmd.call('%s -i %s "key Return"'%(which('xte'), xkbid()))
	copy(text, mode='pb')
	if fork() == 0:
		try:
			sleep(int(wait))
		finally:
			copy(poclp, mode='p')
			copy(boclp, mode='b')
	exit(0)

def __passreplace(pwlist):
	"""returnes a string of asterisk's as long as the password is"""
	__pwcom = ['*'*len(str(pwlist[0]))]
	if len(pwlist) > 1:
		__pwcom.append(pwlist[1])
	return __pwcom

def __dctpwreplace(pwdict):
	"""password => asterisk replacement function"""
	__pwdict = {}
	for (usr, ent) in pwdict.items():
		if isinstance(ent, dict):
			__pwdict[usr] = {}
			for (u, e) in ent.items():
				__pwdict[usr][u] = __passreplace(e)
		elif ent:
			__pwdict[usr] = __passreplace(ent)
	return __pwdict

def _envconf(srcdict):
	newdict = {}
	for (k, v) in srcdict.items():
		if k in environ.keys():
			newdict[v] = environ[k]
	return newdict

def _printpws_(pwdict, insecure=False):
	"""password printer with in/secure option"""
	if not insecure:
		pwdict = __dctpwreplace(pwdict)
	print(tabd(pwdict))
	exit(0)

def optpars(cfgs, mode, name):
	desc = 'pwclip - Multi functional password manager to temporarily ' \
           'save passphrases to your copy/paste buffers for easy and ' \
           'secure accessing your passwords. The following ' \
           'arguments might also be set by the config ' \
           '~/.config/%s.yaml file.'%name
	epic = 'the yubikey mode is compatible with the challenge-response ' \
           'feature of yubikeys only for now.'
	pars = ArgumentParser(description=desc, epilog=epic)
	pars.set_defaults(**cfgs)
	pars.add_argument(
        '--version',
        action='version', version='%(prog)s-v'+version)
	pars.add_argument(
        '-D', '--debug',
        dest='dbg', action='store_true', help='debugging mode')
	pars.add_argument(
        '-A', '--all',
        dest='aal', action='store_true',
        help='switch to all users entrys ("%s" only is default)'%cfgs['user'])
	pars.add_argument(
        '-E', '--enter',
        dest='ent', action='store_true',
        help='also enter newline when printing password (only useful with ' \
             '-o/-O)')
	pars.add_argument(
        '-O', '--android',
        dest='out', action='store_const', const='ano',
        help='print password to stdout of android device if one is connected')
	pars.add_argument(
        '-o', '--stdout',
        dest='out', action='store_const', const=mode,
        help='print password to stdout (insecure and not recommended)')
	pars.add_argument(
        '-e', '--expression',
        dest='rex', default=False, metavar='EXPRESSION:[LEN]',
        nargs='?' if mode == 'gui' else None,
        help='generate password using EXPRESSION to generate password of '
             'lenght LEN, either LEN is set or 24 is used - use with -g' \
             '(default is "[a-zA-Z0-9\!$%%&/\(\)=\?\+#,\.-:]*:24")')
	pars.add_argument(
        '-g', '--genpw',
        dest='gpw', action='store_true', help='randomly generate password' \
             ', only useful with -a (uses EXPRESSION)')
	pars.add_argument(
        '--show-clip',
        dest='scl', action='store_true',
        help='show current clipboard content ' \
             '(WARNING: insecure - if cliptime set ' \
             'to 0 cli mode does not clear the sreen)')
	pars.add_argument(
        '-s', '--show-passwords',
        dest='sho', action='store_true',
        help='show passwords when listing (replaced by "*" is default)')
	pars.add_argument(
        '-t',
        dest='time', default=3, metavar='seconds', type=int,
        help='time to wait before resetting clip (%s is default)'%cfgs['time'])
	gpars = pars.add_argument_group('gpg/ssl arguments')
	gpars.set_defaults(**cfgs)
	gpars.add_argument(
        '-k', '--key',
        dest='gpgkey', metavar='ID', type=str,
        help='gpg-key ID(s) to use for decryption/signing')
	gpars.add_argument(
        '-r', '--recipients',
        dest='recvs', metavar='"ID [ID ...]"',
        help='one ore more gpg-key ID(s) to use for ' \
             'encryption (strings seperated by spaces within "")')
	gpars.add_argument(
        '-u', '--user',
        dest='usr', metavar='USER', nargs='?' if mode == 'gui' else None,
        default=False if mode == 'gui' else cfgs['user'],
        help='query entrys only for USER (-A overrides, ' \
             '"%s" is default)'%cfgs['user'])
	gpars.add_argument(
        '-p', '--password',
        dest='pwd', default=None,
        help='enter password for add/change actions' \
             '(insecure & not recommended)')
	gpars.add_argument(
        '--comment',
        dest='com', default=None,
        help='enter comment for add/change actions')
	gpars.add_argument(
        '-x', '--x509',
        dest='gpv', action='store_const', const='gpgsm',
        help='force ssl compatible gpgsm mode - usually is autodetected ' \
             '(use --cert & --key for imports)')
	gpars.add_argument(
        '-C', '--cert',
        dest='sslcrt', metavar='SSL-Certificate',
        help='one-shot setting of SSL-Certificate')
	gpars.add_argument(
        '-K', '--ssl-key',
        dest='sslkey', metavar='SSL-Private-Key',
        help='one-shot setting of SSL-Private-Key')
	gpars.add_argument(
        '--ca', '--ca-cert',
        dest='sslca', metavar='SSL-CA-Certificate',
        help='one-shot setting of SSL-CA-Certificate')
	gpars.add_argument(
        '-P', '--passcrypt',
        dest='pcr', metavar='CRYPTFILE',
        default=path.expanduser('~/.passcrypt'),
        help='set location of CRYPTFILE to use as ' \
             'password store (~/.passcrypt is default)')
	gpars.add_argument(
        '-Y', '--yaml',
        dest='yml', metavar='YAMLFILE',
        default=path.expanduser('~/.pwd.yaml'),
        help='set location of YAMLFILE to read whole ' \
             'sets of passwords from a yaml file (~/.pwd.yaml is default)')
	ypars = pars.add_argument_group('yubikey arguments')
	ypars.set_defaults(**cfgs)
	ypars.add_argument(
        '-S', '--slot',
        dest='ysl', default=None, type=int, choices=(1, 2),
        help='set one of the two yubikey slots (only useful with -y)'
        ).completer = ChoicesCompleter((1, 2))
	ypars.add_argument(
        '-y', '--ykserial',
        nargs='?', dest='yks', metavar='SERIAL', default=False,
        help='switch to yubikey mode and optionally set ' \
		     'SERIAL of yubikey (autoselect serial and slot is default)')
	apars = pars.add_argument_group('action arguments')
	apars.set_defaults(**cfgs)
	apars.add_argument(
        '-a', '--add',
        dest='add', metavar='ENTRY', nargs='?' if mode == 'gui' else None,
        default=False, help='add ENTRY (password will be asked interactivly)')
	apars.add_argument(
        '-c', '--change',
        dest='chg', metavar='ENTRY', nargs='?' if mode == 'gui' else None,
        default=False, help='change ENTRY (password will be asked interactivly)')
	apars.add_argument(
        '-d', '--delete',
        dest='rms', metavar='ENTRY', nargs='?' if mode == 'gui' else '+',
        default=False, help='delete ENTRY(s) from the passcrypt list')
	apars.add_argument(
        '-l', '--list',
        dest='lst', metavar='PATTERN', nargs='?',
        default=False,
        help='pwclip an entry matching PATTERN if given ' \
             '- otherwise list all entrys')
	autocomplete(pars)
	args = pars.parse_args()
	return pars, args

def confpars(mode):
	"""pwclip command line opt/arg parsing function"""
	_me = path.basename(path.dirname(__file__))
	cfg = path.expanduser('~/.config/%s.cfg'%_me)
	cfgs = {
        'crypt': path.expanduser('~/.passcrypt'),
        'plain': path.expanduser('~/.pwd.yaml'),
        'time': 3,
        'binary': 'gpg' if osname == 'nt' else 'gpg.exe',
        'user': whoami(),
        }
	try:
		with open(cfg, 'r') as cfh:
			confs = dict(load(cfh.read(), Loader=Loader))
	except (TypeError, FileNotFoundError):
		confs = {}
	cfgmap = {
        'gpg': {'recipients': 'recvs', 'key': 'gpgkey', 'delkey': True},
        'yubikey': {'slot': 'ykslot', 'seerial': 'ykser', 'delkey': True}}
	envmap = {
        'GPGKEY': 'gpgkey',
        'RECIPIENTS': 'recvs',
        'PWCLIPTIME': 'time',
        'YKSERIAL': 'ykser',
        'USER': 'usr',
        'USERNAME': 'usr',
        'YKSLOT': 'ykslot'}
	confs = dictreplace(confs, cfgmap)
	for (k, v) in confs.items():
		cfgs[k] = v
	envs = _envconf(envmap)
	for (k, v) in envs.items():
		cfgs[k] = v
	cfgs['binary'] = 'gpg2'
	if osname == 'nt':
		cfgs['binary'] = 'gpg'
	if 'crypt' not in cfgs.keys():
		cfgs['crypt'] = path.expanduser('~/.passcrypt')
	elif 'crypt' in cfgs.keys() and cfgs['crypt'].startswith('~'):
		cfgs['crypt'] = path.expanduser(cfgs['crypt'])
	if 'plain' not in cfgs.keys():
		cfgs['plain'] = path.expanduser('~/.pwd.yaml')
	elif 'plain' in cfgs.keys() and cfgs['plain'].startswith('~'):
		cfgs['plain'] = path.expanduser(cfgs['plain'])
	pars, args = optpars(cfgs, mode, _me)
	pargs = [a for a in [
        'aal' if args.aal else None,
        'dbg' if args.dbg else None,
        'ent' if args.ent else None,
        'gsm' if args.gpv else None,
        'gui' if mode == 'gui' else None,
        'sho' if args.sho else None] if a]
	__bin = 'gpg2'
	if args.gpv:
		__bin = args.gpv
	if osname == 'nt':
		__bin = 'gpgsm.exe' if args.gpv else 'gpg.exe'
	pkwargs = {}
	pkwargs['binary'] = __bin
	pkwargs['sslcrt'] = args.sslcrt
	pkwargs['sslkey'] = args.sslkey
	if args.gpw:
		_genpwrex = '[a-zA-Z0-9\!$%%&/\(\)=\?\+#,\.-:]*:24'
		pargs.append('rnd')
		if args.rex is not False:
			getrex = input
			msg = 'enter regular expression for new password:'
			err = 'aborted due to empty input'
			if mode == 'gui':
				getrex = xinput
				msg = 'enter regular expression for new password'
				err = 'aborted due to empty input'
			_genpwrex = getrex('enter regular expression for new password')
			if not _genpwrex:
				
				xnotify('aborted due to empty input')
				exit(1)
		elif mode == 'gui':
			_genpwrex = '[a-zA-Z0-9\!$%%&/\(\)=\?\+#,\.-:]*:24'
		genpwrex = _genpwrex
		genpwlen = 24
		if ':' in genpwrex:
			genpwrex, genpwlen = \
                ''.join(str(genpwrex).split(':')[:-1]), \
                str(genpwrex).split(':')[-1]
		pkwargs['genpwrex'] = genpwrex
		pkwargs['genpwlen'] = genpwlen
	if args.pcr:
		pkwargs['crypt'] = args.pcr
	if args.recvs:
		pkwargs['recvs'] = str(args.recvs).split(' ')
	if args.gpgkey:
		pkwargs['gpgkey'] = args.gpgkey
	if args.usr :
		pkwargs['user'] = args.usr
	if args.time:
		pkwargs['time'] = args.time
	if args.yml:
		pkwargs['plain'] = args.yml
	if args.dbg:
		print(bgre(pars))
		print(bgre(tabd(args.__dict__, 2)))
		print(bgre('pargs:\n  %s\npkwargs:\n%s'%(pargs, tabd(pkwargs, 2))))
	if mode != 'gui' and (
          args.yks is False and args.lst is False and \
          args.add is False and args.chg is False and \
          args.rms is False and args.sslcrt is None and \
          args.sslkey is None and args.scl is None):
		pars.print_help()
		exit(0)
	if mode == 'gui':
		return args, pargs, pkwargs
	return args, pargs, pkwargs

def cli():
	args, pargs, pkwargs = confpars('cli')
	if not path.isfile(args.yml) and \
          not path.isfile(args.pcr) and args.yks is False:
		with open(args.yml, 'w+') as yfh:
			yfh.write("""---\n%s:  {}"""%args.usr)
	poclp, boclp = paste('pb')
	if args.yks or args.yks is None:
		if 'YKSERIAL' in environ.keys():
			ykser = environ['YKSERIAL']
		ykser = args.yks if args.yks else None
		if ykser and len(ykser) >= 6:
			ykser = ''.join(str(ykser)[-6:])
		res = ykchalres(getpass(), args.ysl, ykser)
		if not res:
			fatal('could not get valid response on slot ', args.ysl)
		forkwaitclip(res, poclp, boclp, args.time, args.out, args.ent)
		exit(0)
	__ents = {}
	err = None
	if args.add:
		__ents = PassCrypt(*pargs, **pkwargs).adpw(
                           args.add, args.pwd, args.com)
		if not __ents:
			error('something went wrong while adding', args.add)
			exit(1)
		__pc = __ents[args.usr][args.add]
		if __pc:
			if len(__pc) == 2 and osname != 'nt':
				xnotify('%s: %s'%(
                        args.lst, ' '.join(__pc[1:])), args.time)
			forkwaitclip(__pc[0], poclp, boclp, args.time, args.out, args.ent)
	elif args.chg:
		if args.pwd:
			pkwargs['password'] = args.pwd
		__ents = PassCrypt(*pargs, **pkwargs).chpw(
            args.chg, args.pwd, args.com)
		if not args.aal:
			__ents[args.usr]
		if not __ents:
			if [u for (u, es) in __ents.items() if args.chg in es.keys()]:
				exit(0)
			err = ('could not change entry', args.chg)
	elif args.rms:
		ers = []
		for r in args.rms:
			__ents = PassCrypt(*pargs, **pkwargs).rmpw(r)
			if not args.aal:
				__ents[args.usr]
			if r in __ents.keys():
				ers.append(r)
		ewrd = 'entry'
		if len(ers) >= 1:
			ewrd = 'entrys'
		err = ('deleting the following %s failed:', bred(', ').join(
               ers)) if ers else None
	elif args.lst is not False and args.lst is not None:
		__ents = PassCrypt(*pargs, **pkwargs).lspw(args.lst)
		if __ents and args.lst not in __ents.keys():
			err = (
                'could not find entry', args.lst,
                'for', args.usr, 'in', pkwargs['crypt'])
		elif args.lst and __ents:
			__pc = __ents[args.lst]
			if __pc:
				notif = 'pwclip:copy'
				if len(__pc) == 2:
					notif = ' '.join(__pc[1:])
				if osname!= 'nt':
					xnotify(notif)
				forkwaitclip(__pc[0], poclp, boclp, args.time, args.out, args.ent)
				exit(0)
	elif args.lst is None:
		__ents = PassCrypt(*pargs, **pkwargs).lspw()
		err = 'no password entrys or decryption failed' if not __ents else None
	elif args.scl:
		t = 0 if 'time' not in pkwargs.keys() else pkwargs['time']
		showclip(args.out if args.out else 'cli', t, True if t else False)
		exit(0)
	if err:
		fatal(err)
	_printpws_(__ents, args.sho)

def __xdialog(msg, sec=None):
	while True:
		rtn = False
		if sec:
			rtn = xgetpass(msg)
		else:
			rtn = xinput(msg)
		if not rtn:
			yesno = xyesno('no input received, try again?')
			if yesno:
				continue
		break
	return rtn

def gui(typ='pw'):
	"""gui wrapper function to not run unnecessary code"""
	poclp, boclp = paste('pb')
	args, pargs, pkwargs = confpars('gui')
	if args.yks or args.yks is None or typ == 'yk':
		res = ykchalres(xgetpass(), args.ysl, args.yks)
		if not res:
			xmsgok('no response from the key (if there is one)'%res)
			exit(1)
		forkwaitclip(res, poclp, boclp, args.time, args.out, args.ent)
	__ents = None
	usr = args.usr
	if args.usr is None:
		usr = __xdialog('enter username for selected action')
	if usr == 'all':
		pargs.append('aal')
	else:
		pkwargs['user'] = usr
	if args.add is not False:
		_add = __xdialog('as %s: enter name for entry to add'%usr)
		if not _add:
			xnotify('aborted')
			exit(1)
		if _add:
			__ents = PassCrypt(*pargs, **pkwargs).adpw(_add, None, None)
			ok = True
			if not __ents:
				if 'aal' in pargs:
					for (susr, entrys) in __ents.items():
						if _add not in entrys.keys():
							ok = False
				elif usr not in __ents or _add not in __ents[usr].keys():
					ok = False
			if not ok:
				xnotify('something went wrong while adding %s'%_add)
			__pc = __ents[usr][_add]
			notif = 'pwclip:copy'
			if len(__pc) == 2:
				notif = ' '.join(__pc[1:])
			if not args.out and osname != 'nt':
				xnotify(notif)
			forkwaitclip(__pc[0], poclp, boclp, args.time, args.out, args.ent)
			umsg = 'all users'
			if 'aal' not in pargs:
				umsg = 'user %s'%usr
			xnotify('added entry %s for %s'%(_add, umsg))
	elif args.chg is not False:
		_chg = __xdialog(
            'as %s: enter name of the entry to change'%usr)
		if not _chg:
			xnotify('changing entry aborted')
			exit(1)
		if _chg:
			__ents = PassCrypt(*pargs, **pkwargs).chpw(_chg, None, None)
			if not __ents or usr not in __ents or \
                  _chg not in __ents[usr].keys():
				xnotify('something went wrong while changing %s'%_chg)
				exit(1)
			__pc = __ents[usr][_chg]
			notif = 'pwclip:copy'
			if len(__pc) == 2:
				notif = ' '.join(__pc[1:])
			if not args.out and osname != 'nt':
				xnotify(notif)
			forkwaitclip(__pc[0], poclp, boclp, args.time, args.out, args.ent)
			xnotify('changed entry %s for %s'%(_chg, usr))
	elif args.rms is not False:
		_rms = __xdialog(
            'as %s: enter name of the entry(s) to delete'%usr)
		if not _rms:
			xnotify('deleting entry aborted')
			exit(1)
		if _rms and ' ' in _rms:
			_rms = [r.strip() for r in _rms.split(' ')]
		else:
			_rms = [_rms]
		for r in _rms:
			pcr = PassCrypt(*pargs, **pkwargs)
			__ents = pcr.rmpw(r)
			pcr.__del__()
			if osname != 'nt':
				if not __ents:
					xnotify('could not delete entry %s'%r)
				else:
					xnotify('deleted entry %s for %s'%(r, usr))
	elif args.lst is not False:
		__in = args.lst
		if not args.lst:
			__in = args.lst
			_umsg = '%s\'s entrys'%usr
			if args.aal:
				_umsg = 'all entrys'
			__in = __xdialog('enter name to search in %s'%_umsg, True)
		__ent = PassCrypt(*pargs, **pkwargs).lspw(__in)
		if not __ent or (__ent and __in not in __ent.keys() or not __ent[__in]):
			xnotify('either %s or %s where not found in passcrypt'%(
                usr, __in))
			exit(1)
		if __ent:
			__pc = __ent[__in]
			if __pc:
				notif = 'pwclip: copy'
				if len(__pc) == 2:
					notif = ' '.join(__pc[1:])
				if not args.out and osname != 'nt':
					xnotify(notif)
				forkwaitclip(
                    __pc[0], poclp, boclp, args.time, args.out, args.ent)
				exit(0)
	elif args.scl:
		t = 0 if 'time' not in pkwargs.keys() else pkwargs['time']
		showclip('gui', t, True if t else False)
		exit(0)
	else:
		__ents = PassCrypt(*pargs, **pkwargs).lspw()
	if __ents:
		if args.aal:
			pargs.append('aal')
		if not args.sho:
			__ents = __dctpwreplace(__ents)
		xnotify(tabd(__ents))
