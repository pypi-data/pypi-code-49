# All .ui files and .so files are added through keyword: package_data, because setuptools doesn't include them automatically.
import sys
import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

program_name = "xfntrwin"

def _post_install(dir_):
    from subprocess import run 
    run([sys.executable,'post_install_cmd.py',dir_],
         cwd = os.path.join(dir_,program_name))

class install(_install):
    """Post-install for installation mode"""
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib, ), 
                     msg = "Running post install task")

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = program_name,
    version = "0.2.2",
    author = "Zhu Liang",
    author_email = "zliang8@uic.edu",
    description = "A software that analyzes xfntr data",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/zhul9311/XFNTR-win.git",
    packages = find_packages(),
    package_dir = {'':'.'},
    package_data = {
        '' : ['xr_ref.so','GUI/*']
    },
    exclude_package_data = {
        '' : ['.git/','.setup.py.swp']
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6',
    install_requires = [
        'pyqt5',
        'scipy',
        'matplotlib',
        'lmfit',
        'periodictable'
    ],
    entry_points = { # create scripts and add to sys.PATH
        'console_scripts':[
            'xfntrwin1 = xfntrwin.main:main'
        ],
        'gui_scripts': [
            'xfntrwin = xfntrwin.main:main'
        ]
    },
    cmdclass = { # something to run after install (e.g. deal with xr_ref.f90.
        'install':install
    }
)
