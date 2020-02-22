import sys

if sys.version_info[0] == 3 and sys.version_info >= (3, 6):
    from .Core36 import WeApp
elif sys.version_info[0] == 2 and sys.version_info >= (2, 7):
    from Core27 import WeApp
else:
    sys.exit("""Python version Incompatible:

    Python 2 can't be lower than 2.7
    Python 3 can't be lower than 3.6
""")