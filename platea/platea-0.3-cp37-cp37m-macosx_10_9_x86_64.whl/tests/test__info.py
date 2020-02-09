"""
Should run as first test module. Provides useful system information.
"""

import sys
import platform
import numpy as np
import scipy as sp

def test_info():
    print("\n")
    print("#######################################################################")

    uname = platform.uname()

    print("System Information")

    if sys.version_info >= (3, 0):
        print("System: {}".format(uname.system))
        print("Node Name: {}".format(uname.node))
        print("Release: {}".format(uname.release))
        print("Version: {}".format(uname.version))
        print("Machine: {}".format(uname.machine))
        print("Processor: {}".format(uname.processor))
    else:
        print("System: {}".format(uname[0]))
        print("Node Name: {}".format(uname[1]))
        print("Release: {}".format(uname[2]))
        print("Version: {}".format(uname[3]))
        print("Machine: {}".format(uname[4]))
        print("Processor: {}".format(uname[5]))

    print("#######################################################################")

    print("Python Version")
    print(sys.version)
    print("Version Info")
    print(sys.version_info)

    print("#######################################################################")

    print("Numpy Version: {}".format(np.version.version)) # np.__version__
    print("Scipy Version: {}".format(sp.version.full_version)) # sp.__version__

    print("Numpy Backend Config")
    np.__config__.show()

    print("#######################################################################")

    try:
        import pypolyagamma as pypg
        print("Pypolyagamma installed and imported.")
    except Exception as e:
        print("Pypolyagamma is not installed or cannot be imported.")
        print(e)

    print("#######################################################################")
