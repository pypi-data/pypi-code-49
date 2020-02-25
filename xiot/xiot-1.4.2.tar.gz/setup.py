from setuptools import setup

from xiot import __version__

setup(
    name='xiot',
    keywords=('xiot'),
    version=__version__,
    py_modules=['xiot', 'xiotshell'],
    url='https://github.com/sintrb/xiot',
    license='Apache License 2.0',
    author='Robin',
    author_email='sintrb@gmail.com',
    description='A lib for xiot.',
    install_requires=['requests', 'paho-mqtt', 'six'],
)
