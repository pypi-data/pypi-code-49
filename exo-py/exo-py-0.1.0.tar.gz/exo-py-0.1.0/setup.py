import os
import subprocess
import sys

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
  def __init__(self, name):
    Extension.__init__(self, name, sources=[])

class CMakeBuild(build_ext):
  def run(self):
    for ext in self.extensions:
      if isinstance(ext, CMakeExtension):
        install_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_command = os.getenv('CMAKE', 'cmake')
        subprocess.check_call([cmake_command, '--version'])
        cmake_args = [
          '-DCMAKE_BUILD_TYPE=Release',
          f'-DPYTHON_EXECUTABLE={sys.executable}'
        ]
        if not os.path.exists(self.build_temp):
          os.makedirs(self.build_temp)
        if not os.path.exists(install_dir):
          os.makedirs(install_dir)
        env = os.environ.copy()
        command = [cmake_command]
        command.extend(cmake_args)
        command.append(os.getcwd())
        subprocess.check_call(command, cwd=self.build_temp, env=env)
        subprocess.check_call([cmake_command, '--build', '.', '--config', 'Release'], cwd=self.build_temp, env=env)
        subprocess.check_call([cmake_command, '--install', '.', '--prefix', install_dir], cwd=self.build_temp, env=env)
      else:
        build_ext.run()

with open('README.md', 'r') as file:
  long_description = file.read()

setup(
  name='exo-py',
  version='0.1.0',
  author='Jared Duffey',
  author_email='daedalus@daedala.io',
  url='https://github.com/Daedalus451/exopy',
  description='exopy is a Python module for modeling the growth of planetesimals in a disk over time',
  long_description=long_description,
  long_description_content_type='text/markdown',
  classifiers=[
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    'Development Status :: 4 - Beta',
    'Programming Language :: C++',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Scientific/Engineering :: Astronomy',
    'Intended Audience :: Science/Research',
    'Operating System :: OS Independent',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS',
    'Natural Language :: English'
  ],
  python_requires='>=3.6',
  install_requires=[
    'numpy>=1.15.0'
  ],
  ext_modules=[CMakeExtension('exopy')],
  cmdclass={
    'build_ext': CMakeBuild
  },
  zip_safe=False
)
