#!/usr/bin/env python3
# coding: utf-8


"""
    This package only contains a core module with the the defintion of the Coulomb_counter class.

    The Coulomb_counter class allows to read and manage data from a USB
    connection with a coulomb counter cc75.
"""

#from os import system
#system("python3 -m pip install --user pyserial")
#system("python3 -m pip install --user --upgrade pyserial")

from coulomb_counter_cc75.core import Coulomb_counter


__all__ = [
    "Coulomb_counter"
]

__version__ = "4.0.0"


if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        pass
