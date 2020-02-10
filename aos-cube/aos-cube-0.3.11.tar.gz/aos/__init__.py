import sys

__version__ = "0.3.11"
__title__ = "aos-cube"
__description__ = (
    "aos commmand line tool for AliOS-Things development.")
__url__ = ""

__author__ = "Alibaba"
__email__ = "aliosthings@service.aliyun.com"

__license__ = "Apache Software License"
__copyright__ = "Copyright 2016-present aos-cube"

if sys.version_info < (2, 7, 0):
    msg = ("aos cube is compatible with Python version >= 2.7\n")
    sys.stderr.write(msg)
    sys.exit(1)
