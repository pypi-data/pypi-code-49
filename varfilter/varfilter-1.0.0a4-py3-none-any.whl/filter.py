#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Esteban Barón"
__copyright__ = "Copyright 2020, Esteban Barón ,EBP"
__license__ = "MIT"
__email__ = "esteban@gominet.net"
__status__ = "Alpha"
__version__ = "1.0.0a4"


class IntegerError(Exception):
    #  def __init__(self):
    #        super().__init__('Integer format error')
    pass


class FloatError(Exception):
    pass


class BooleanError(Exception):
    pass


def fint(data=None):
    ret = data
    try:
        if type(ret) is str:
            ret = int(ret, 0)
        else:
            ret = int(ret)
    except (ValueError, TypeError):
        raise IntegerError
    return ret


def fbool(data=None):
    if type(data) is str:
        data = data.strip().lower()
        if data in ('f', 'false', 'n', 'no'):
            data = False
        elif data in ('t', 'true', 'y', 'yes', 's', 'si', 'sí'):
            data = True
    ret = data
    try:
        ret = fint(data)
    except IntegerError:
        pass
    ret = bool(ret)
    return ret


if __name__ == "__main__":
    print("Este fichero pertenece a un módulo, "
          "no es operativo como aplicación independiente.")
