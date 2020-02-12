# coding: utf-8

from __future__ import print_function

def _convert_version(tup):
    """create a PEP 386 pseudo-format conformant string from tuple tup"""
    ret_val = str(tup[0])  # first is always digit
    next_sep = "."  # separator for next extension, can be "" or "."
    for x in tup[1:]:
        if isinstance(x, int):
            ret_val += next_sep + str(x)
            next_sep = '.'
            continue
        first_letter = x[0].lower()
        next_sep = ''
        if first_letter in 'abcr':
            ret_val += 'rc' if first_letter == 'r' else first_letter
        elif first_letter in 'pd':
            ret_val += '.post' if first_letter == 'p' else '.dev'
    return ret_val


version_info = (0, 3)
__version__ = _convert_version(version_info)

del _convert_version


import sys
import os
import shlex
import glob
import subprocess
import argparse

from tox import hookimpl

def expand_interpreter_globs(args):
    # since we run shlex, you can just join the commandline options
    assert args
    if isinstance(args, list):
        args = ' '.join(args)
    # print(args, shlex.split(args))
    return [x for p in shlex.split(args) for x in glob.glob(p)]


def tox_global_config_dir():
    # based on:
    # http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
    # https://wiki.gnome.org/Initiatives/GnomeGoals/XDGConfigFolders
    if os.name == "nt":
        _config_dir = os.environ.get(
            'APPDATA',
            os.path.join(os.path.expanduser("~"), '.tox'))
    else:
        _config_dir = os.environ.get(
            'XDG_CONFIG_HOME',
            os.path.join(os.path.expanduser("~"), '.config'))
        # print(_config_dir)
    cfg_dir = os.path.join(_config_dir, 'tox')
    if not os.path.exists(cfg_dir):
        os.makedirs(cfg_dir)
    return cfg_dir


class InterpreterTarget:
    pass

class InterpreterList(object):
    """read existing list of interpreters, support creation,
    just to be sure the file format is versioned (first line),
    and allows paths with newlines

    This currently uses a simple and extensible format. A YAML file
    would be my preference, but that is a bit overkill for this
    purpose (as would XML).
    I also moved beyond JSON a few years ago, as it is often too simple
    (no comments when you need them), requires quotes where they could
    be inferred (making it easy to break) and disallows comma's where they
    could prevent future edits by humans to go wrong (after the last
    element in a list). I could have used JSON as these files are
    probably only going to be read by this plug-in. But I can
    still change it when needed.
    """
    def __init__(self, file_name):
        self._file_name = file_name
        self._fp = None
        self._b32 = False
        self._version = None
        self._interpreters = []
        self._first_interpreter = True
        self._read()

    # writing the list

    def __enter__(self):
        self._fp = open(self._file_name, 'w')
        self._fp.write('v 1\n')  # interpreter list format
        return self

    def __exit__(self, typ, value, traceback):
        self._fp.write('e \n')
        self._fp.close()

    def pattern(self, pattern):
        self._fp.write('# Original pattern used:\n')
        self._fp.write('g {0}\n'.format(pattern.replace('\n', '\n  ')))

    def write(self, path):
        base_name = os.path.basename(path)
        file_name = os.path.abspath(path)
        if os.name == 'nt' and base_name.endswith('.exe'):
            base_name, _ = os.path.splitext(base_name)
        if base_name == 'python':
            cmd = [
                file_name,
                '-c',
                'import sys; sys.stdout.write("python%d.%d" % '
                'sys.version_info[:2])'
            ]
            try:
                py_ver = subprocess.check_output(cmd)
            except subprocess.CalledProcessError:
                pass
            except OSError:
                pass
            else:
                base_name = py_ver
        if not isinstance(base_name, str):
            base_name = base_name.decode('utf-8')
        assert ' ' not in base_name
        if self._first_interpreter:
            self._first_interpreter = False
            self._fp.write('# Interpreters found:\n')
        # for paths with newlines in them: first write nl count
        self._fp.write('p {0} {1}\n'.format(
            base_name,
            file_name.replace('\n', '\n  ')))

    # reading the list
    def _read(self):
        try:
            fp = open(self._file_name)
        except IOError:
            return
        self._interpreters = []
        self._first_interpreter = True
        line = fp.readline()
        try:
            typ, version_number = line.split()
            self._version = int(version_number)
            assert typ[0] == 'v'
            assert self._version == 1
        except:
            print("wrong version in line", line)
            sys.exit(1)
        keys = set()
        if self._version == 1:
            lines = fp.readlines()
            index = 0
            while lines[index][0] != 'e':
                typ = lines[index][0]
                line = lines[index][2:]
                base = index
                index += 1
                while lines[index][:2] == '  ':
                    line += lines[index][2:]
                    index += 1
                # line = line[:-1]  # strip final newline
                if typ == 'p':
                    it = InterpreterTarget()
                    try:
                        it.key, it.path = line[:-1].split(' ', 1)
                        if it.key in keys and \
                           os.path.dirname(it.path).endswith('-32'):
                            # print('32bit version found', it.key)
                            self._b32 = True
                            it.b32 = True
                        else:
                            keys.add(it.key)
                            it.b32 = False
                    except ValueError:
                        print('line', line)
                        raise
                    self._interpreters.append(it)
        else:
            raise NotImplementedError

    # iterating the list

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):
        try:
            self._index += 1
            return self._interpreters[self._index]
        except IndexError:
            raise StopIteration

    def dump(self):
        if not self._interpreters:
            print('no previously scanned interpreter names')
            print(self._file_name)
            sys.exit(1)
        print('interpreters:')
        for ipr in self._interpreters:
            print(ipr.key, ipr.path)

    def b32(self):
        if self._b32 is None:
            print('hallo')
            print(self._interpreters)
        return self._b32

    if sys.version_info < (3,):
        next = __next__


class GlobInterpreterPlugin:
    def __init__(self, verbose=None):
        self.verbose = verbose if verbose else int(os.environ.get('VERBOSE', 0))
        self._cfg = None
        self._il = InterpreterList(os.path.join(tox_global_config_dir(),
                                                'interpreters.lst'))
        self._bit32 = False

    def tox_configure(self, config):
        # allow global storage of interpreter info, should be in config
        # if not hasattr(config, 'global_config_dir'):
        #     config.global_config_dir = tox_global_config_dir()
        self._cfg = config
        # postprocess config
        if self._cfg.option.help:
            return
        if self._cfg.option.scan:
            if self._cfg.option.args:
                self.scan()
                self._il._read()
            self._il.dump()
            sys.exit(0)
        if self._cfg.option.scan_test:
            self.verbose = 1
            self._tox_get_python_executable(self._cfg.option.scan_test)
            sys.exit(0)

    def scan(self):
        if os.name == "nt":
            args = self._cfg.option.args[:]
            if self.verbose > 0:
                print('args', args)
            exe_args = [x if '.exe' in x.lower() else x + '.exe' for x in args]
            with InterpreterList(self.interpreter_list_file_name()) as il:
                il.pattern(' '.join(exe_args))
                for file_name in expand_interpreter_globs(args):
                    il.write(file_name)
            return
        with InterpreterList(self.interpreter_list_file_name()) as il:
            il.pattern(' '.join(self._cfg.option.args))
            for file_name in expand_interpreter_globs(self._cfg.option.args):
                il.write(file_name)

    def interpreter_list_file_name(self):
        #return os.path.join(self._cfg.global_config_dir, 'interpreters.lst')
        return os.path.join(tox_global_config_dir(), 'interpreters.lst')

    def tox_get_python_executable(self, envconfig):
        assert envconfig.config == self._cfg
        if self.verbose > 0:
            print('path-to-pyhon-executable', envconfig.basepython, end=' ')
        return self._tox_get_python_executable(envconfig.basepython)

    def _tox_get_python_executable(self, basepython):
        #igs = os.environ.get('TOX_INTERPRETER_GLOBS')
        #if igs:
        #    self._il ...... ToDo
        #    for file_name in expand_interpreter_globs(igs):
        #        base_name = os.path.basename(file_name)
        #        file_name = os.path.abspath(file_name)
        #        self._interpreters[base_name] = file_name
        ret_val = None
        for it in self._il:
            if it.key != basepython:
                continue
            if ret_val is None:
                ret_val = it.path
            elif getattr(self._cfg.option, 'b32', False) and it.b32:
                ret_val = it.path
        if self.verbose > 0:
            print (ret_val)
        return ret_val

    def tox_addoption(self, parser):
        if self.verbose > 1:
            print('add command line options')
        parser.add_argument(
            "--scan", action="store_true",
            help="""show scanned executables (needs tox.ini in current dir 
                    even though not used)""")
        if self._il.b32():
            parser.add_argument("--32", action="store_true", dest='b32',
                                help="use 32 bit version if both available")
        # this is for commandline testing of the resolution of
        # tox_get_python_executable
        parser.add_argument("--scan-test", help=argparse.SUPPRESS)



global_interpreter_plugin = GlobInterpreterPlugin()


# adding @hookmpl to GlobInterpreterPlugin would not work
@hookimpl
def tox_configure(config):
    return global_interpreter_plugin.tox_configure(config)


@hookimpl
def tox_get_python_executable(envconfig):
    """envconfig is an instance of the simple class VenConfig
    (in tox/tox/_config). Originally it was not passed in and is
    currently not used although it could be used to drop the need
    to have the config stored by GlobInterpreterPlugin.tox_configure().
    envconfig gets attributes assigned all over the place in the tox code,
    including the attribute basepython (not obvious from the class definition)
    for which we need to return the executable path.
    There might be some other undocumented things hanging of envconfig
    that could be useful, but you cannot just 'dump' the attributes without
    going into infinite recursion :( """
    return global_interpreter_plugin.tox_get_python_executable(envconfig)


@hookimpl
def tox_addoption(parser):
    return global_interpreter_plugin.tox_addoption(parser)
