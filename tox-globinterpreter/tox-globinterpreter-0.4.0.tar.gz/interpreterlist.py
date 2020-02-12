# coding: utf-8

from __future__ import print_function

import os
import sys
import subprocess

class InterpeterTarget:
    pass

class InterpreterList(object):
    """read existing list of interpreters, support creation,
    just to be sure the file format is versioned (first line),
    and allows paths with newlines"""
    def __init__(self, file_name, verbose=False):
        self._file_name = file_name
        self._fp = None
        self._verbose = verbose
        self._version = None
        self._interpreters = []

    # writing the list

    def __enter__(self):
        self._fp = open(self._file_name, 'w')
        self._fp.write('v 1\n')  # interpreter list format
        return self

    def __exit__(self, typ, value, traceback):
        self._fp.write('e \n')
        self._fp.close()

    def pattern(self, pattern):
        self._fp.write('g {}\n'.format(pattern.replace('\n', '\n  ')))

    def write(self, path):
        base_name = os.path.basename(path)
        file_name = os.path.abspath(path)
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
        assert ' ' not in base_name
        # for paths with newlines in them: first write nl count
        self._fp.write('p {} {}\n'.format(
            base_name,
            file_name.replace('\n', '\n  ')))

    # reading the list

    def __iter__(self):
        self._fp = open(self._file_name)
        line = self._fp.readline()
        try:
            typ, version_number = line.split()
            self._version = int(version_number)
            assert typ[0] == 'v'
            assert self._version == 1
        except:
            print("wrong version in line", line)
            sys.exit(1)
        fp = self._fp
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
                    it = InterpeterTarget()
                    try:
                        it.key, it.path = line[:-1].split(' ', 1)
                    except ValueError:
                        print('line', line)
                        raise
                    self._interpreters.append(it)
        else:
            raise NotImplementedError
        self._index = -1
        if self._verbose:
            print('interpreters:')
            for ipr in self._interpreters:
                print(ipr.key, ipr.path)
        return self

    def __next__(self):
        try:
            self._index += 1
            return self._interpreters[self._index]
        except IndexError:
            raise StopIteration

    if sys.version_info < (3,):
        next = __next__
