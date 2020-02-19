
from distutils.core import setup

setup(
    name='auto_abbr',
    version='1.0.0',
    py_modules=['abbr'],
    author='dandanlemuria',
    author_email='18110980003@fudan.edu.cn',
    description='a list of abbreviations for a given string', requires=['requests', 'lxml']
)

