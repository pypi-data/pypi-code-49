'''
This is a universal function library.
'''

import guang.get_version as get_version

__v = get_version.get_version(update=False)

# '0.0.7.2.7'
__version__ = '0.0.' + __v
print('guang.__version__=:', __version__)
__author__ = 'K.y'
__copyright = 'Copyright 2019 K.y'

__all__ = ["ML","Utils","DL", "Voice", "wechat", "ML", "interesting", "app"]

