# import os
#
# un = os.uname()


def read(filename):
    try:
        with open(filename, 'r') as fd:
            info = fd.read()
    except FileNotFoundError:
        info = None
    return info
