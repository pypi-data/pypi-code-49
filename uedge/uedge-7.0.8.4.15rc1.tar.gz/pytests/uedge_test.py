import os
import contextlib
import unittest
from uedge.uexec import uexec as execfile

@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
       yield 
    finally:
       os.chdir(previous_dir)


if os.path.exists('pytests/level_1/dotest.py'):
     with pushd('pytests/level_1'):
         execfile('dotest.py')

if os.path.exists('pytests/level_2/dotest.py'):
      with pushd('pytests/level_2'):
         execfile('dotest.py')
