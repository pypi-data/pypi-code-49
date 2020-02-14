from .pudo import *
#__all__ = ['run']
VERSION = "1.0.0" # major.minor[.patch[.sub]]

__doc__ = '''
Pudo Python Package

This is an Python Package for running Linux commands with root permission.
We can see this as an alternative to Linux sudo command without password prompt.
This is very handy when you are writing python automation scripts and need to deal with root privileges.
You can use this as an python module or an Linux command.

Below is the code snippit for using in python automation for running cmds under root privilege::

    user$ python3 # or python2
    >>> from . import pudo
    >>> (ret, out) = pudo.run(('ls', '/root')) # or pudo.run('ls /root')
    >>> print(ret)
    >>> 0
    >>> print(out)
    >>> b'Desktop\\nDownloads\\nPictures\\nMusic\\n'

Below is the cmd example for running cmds under root privilege::

    user$ pudo ls /root
    Desktop  Downloads  Pictures  Music
'''


