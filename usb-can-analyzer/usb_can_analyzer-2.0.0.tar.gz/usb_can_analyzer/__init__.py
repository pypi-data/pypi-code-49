#!/usr/bin/env python3
# coding: utf-8


"""
    This package mainly contains a core module with the the defintion of the Converter class.

    The Converter class allows to read/write data from/to a USB connection with
    a usb can analyzer.
"""

#from os import system
#system("python3 -m pip install --user pyserial")
#system("python3 -m pip install --user --upgrade pyserial")

from usb_can_analyzer.core import Converter


__all__ = [
    "Converter"
]

__version__ = "2.0.0"


if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        pass
