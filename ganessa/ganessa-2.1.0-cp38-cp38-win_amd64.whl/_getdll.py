# -*- coding: utf-8 -*-
'''
Created on 7 sept. 2017

@author: Jarrige_Pi

Determines where and which dll to use

17.12.12: added optional _ck suffix, added PICCOLO_DIR envt variable
18.08.27: added Program Files for x64 environment
20.02.04: use add_dll_directory with python 3.8+ instead of path

'''
from __future__ import (unicode_literals, print_function, absolute_import)
from importlib import import_module
from itertools import product
from sys import modules as sys_modules
from sys import version_info

USE_ADD_DLL = version_info[0:2] >= (3, 8)
from os import environ
import os.path as OP
if USE_ADD_DLL:
    from os import add_dll_directory

debuglevel = 0
class AddDllDirectory(object):
    '''Context manager class with a close() method'''
    def __init__(self, ndir):
        ''' inserts ndir into the windows search path
        required even with add_dll_directory because of activation lib
        '''
        self.dir = ndir
        self.path_modified = ndir.lower() not in unistr(environ['path']).lower().split(';')
        self.add_dll_dir = add_dll_directory(ndir) if USE_ADD_DLL else None
        if self.path_modified:
            if debuglevel > 2:
                print(environ['path'])
            environ['path'] += ';' + ws(ndir)
            if debuglevel:
                print(ws('\tFolder "' + ndir + '" added to PATH environment variable'))
    def close(self):
        '''remove last path'''
        if self.add_dll_dir is not None:
            self.add_dll_dir.close()
            self.add_dll_dir = None
        if self.path_modified:
            environ['path'], check = environ['path'].rsplit(';', 1)
            if debuglevel:
                print(ws('\tFolder "' + check + '" removed from PATH environment variable'))
            self.path_modified = False
            assert ws(self.dir) == check
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()
        return True

from ganessa.util import unistr, ws, X64

class EnvSearchError(Exception):
    '''Custom exception'''
    pass

def _getdllinfo(bth):
    ''' Locates the simulation kernel - picwin32.dll or Ganessa_xx.dll
        in an expected folder and ensures that an appropriate .pyd
        interface exists (EnvSearchError)

        Folder are looked up in the following order:
        - GANESSA_DIR environment variable for Ganessa_xx.dll
        - folder list from PATH environment variable for either dll
        - default installation folders for Piccolo and Picalor
        - for FR, esp, eng and optionally _ck
    '''
    dlls = ('Ganessa_TH.dll' if bth else 'Ganessa_SIM.dll', 'Picwin32.dll')

    # first examine GANESSA_DIR and PICCOLO_DIR
    for ganessa_dir, f in zip(('GANESSA_DIR', 'PICCOLO_DIR'), dlls):
        if ganessa_dir in environ:
            gandir = unistr(environ[ganessa_dir])
            if OP.exists(OP.join(gandir, f)):
                print(f, 'found in environment variable', ganessa_dir)
                with AddDllDirectory(gandir):
                    if _import_ganessa(f, bth, dlls):
                        break
            else:
                print(f, ' ** NOT ** found in environment variable', ganessa_dir)
    else:
        # if none succeeds examine PATH variable
        for gandir, f in product(unistr(environ['path']).split(';'), dlls):
            if OP.exists(OP.join(gandir, f)):
                if debuglevel > 0:
                    print(ws(f + ' found in Path: ' + gandir))
                with AddDllDirectory(gandir):
                    if _import_ganessa(f, bth, dlls):
                        break
        # finally check default installation paths
        else:
            if debuglevel:
                print(' * no dll found in PATH environment variable folders')
            # then default installation folders:
            # (drive) (program folder) (editor name) (software_lang) (dll)
            PROG5 = '/Program Files'
            PROG6_x32 = '/Program Files (x86)'
            PROG6_x64 = '/Program Files'
            pesn = ((PROG6_x32, 'Safege', 'Ganessa_', 0), )
            if X64:
                pesn += ((PROG6_x64, 'Safege', 'Ganessa_', 0), )
            else:
                pesn += ((PROG6_x32, 'Gfi Progiciels',
                        'Picalor6_' if bth else 'Piccolo6_', 1),)
                if not bth:
                    pesn += ((PROG5, 'Adelior', 'Piccolo5_', 1),)
            for d, (p, e, s, n), l, k in product(('D:', 'C:'), pesn,
                     ('FR', 'esp', 'eng', 'UK'), ('', '_ck', '_cl')):
                f = dlls[n]
                gandir = OP.join(d, p, e, s + l + k)
                if debuglevel > 1:
                    print(' ... examining ' + gandir + '/' + f)
                if OP.exists(OP.join(gandir, f)):
                    with AddDllDirectory(gandir):
                        if debuglevel > 0:
                            print(' ... testing ' + gandir + '/' + f)
                        if _import_ganessa(f, bth, dlls):
                            if debuglevel > 0:
                                print(f + ' responding from ' + gandir)
                            del d, p, e, s, l
                            break
                        print(ws(f + ' found in ' + gandir + ' but *NOT* responding'))
            else:
            # On n'a pas trouve
                raise ImportError('Unable to find an adequate '+ ' or '.join(dlls))

    # dll found and API OK: finalise the import
    # with AddDllDirectory(gandir):
    #     mod = _import_ganessa(f, bth, dlls, test=False)
    # context will be closed after call to init.
    to_close = AddDllDirectory(gandir)
    mod = _import_ganessa(f, bth, dlls, test=False)
    return gandir, f, mod, to_close

def _import_ganessa(f, bth, dlls, test=True):
    '''Search for the most recent version of compatible pyganessa dll '''
    pkg = 'ganessa'
    try:
        if f == dlls[1]:
            # look for Picwin32 - no specific 2019 API
            TRIALS = ('_pygan_th2020', '_pygan_th2018', '_pygan_th2017',
                      '_pygan_th2016b', '_pygan_th2016', '_pygan_th2015',
                ) if bth else (
                      '_pygansim2020', '_pygansim2018b', '_pygansim2018',
                      '_pygansim2017b', '_pygansim2017',
                      '_pygansim2016b', '_pygansim2016a', '_pygansim2016',
                      '_pygansim2015', '_pygansim2014')
            for pydll in TRIALS:
                try:
                    mod = import_module('.' + pydll, package=pkg)
                    if debuglevel > 2:
                        print(f, 'FIT', pydll)
                    break               # found -> stop iteration
                except ImportError:
                    if debuglevel > 2:
                        print(f, 'do not fit', pydll, '; mode=', 'test' if test else 'activation')
                    continue
            else:
                # sequence exhausted w/o finding a suitable dll
                raise ImportError
        elif f == dlls[0]:
            # look for Ganessa_xxx
            pydll = '_pygan_th' if bth else '_pygansim'
            mod = import_module('.' + pydll, package=pkg)
    except ImportError:
        if debuglevel > 0:
            print('\t', f, 'error; mode=', 'test' if test else 'activation')
        return False
    else:
        if debuglevel > 0:
            print(f, 'is OK for use with', pydll, '; mode=', 'test' if test else 'activation')
        if test:
            del mod
            return True
        print('  --->  using interface <', pydll, '> for ', f, sep='')
        return mod

class _LookupDomainModule(object):
    def __init__(self):
        for item in ('ganessa.sim', 'ganessa.th'):
            if item in sys_modules:
                self.name = item
                self.module = sys_modules[item]
                break
        else:
            self.name = ''
            self.module = None
            print(' ***\n *** CAUTION *** if used, ganessa.sim or .th should be imported',
                  ' before .OpenFileMMI- Please inform piccolo@safege.fr\n ***')

    def is_th(self):
        '''Returns True if called from ganessa.th'''
        return self.name.endswith('th')
