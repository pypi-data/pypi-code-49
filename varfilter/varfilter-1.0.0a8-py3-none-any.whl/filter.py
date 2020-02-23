#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Funciones para conversión a tipos de datos básicos.

Definición de Exceptions para integer,Float,Boolean

Funciones de conversión a int,bool,float

"""

__author__ = "Esteban Barón"
__copyright__ = "Copyright 2020, Esteban Barón ,EBP"
__license__ = "MIT"
__email__ = "esteban@gominet.net"
__status__ = "Alpha"
__version__ = "1.0.0a8"


class ConvertionError(Exception):
    pass


class IntegerError(ConvertionError):
    #  def __init__(self):
    #        super().__init__('Integer format error')
    pass


class FloatError(ConvertionError):
    pass


class BooleanError(ConvertionError):
    pass


class StringError(ConvertionError):
    pass


def fint(data=None):
    """Obtiene el valor int

    Convierte a int desde distintos tipos.
    si es str y empieza por 0x lo convierte a hexadecimal
    y si empieza por 0b lo convierte a binario

    Parameters
    ----------
    data : int or str or bool

    Returns
    -------
    int
        Representación int de la entrada

    Raises
    ------
    IntegerError
    """
    try:
        if type(data) is str:
            ret = int(data, 0)
        else:
            ret = int(data)
    except (ValueError, TypeError):
        raise IntegerError
    else:
        return ret


def ffloat(data=None):
    """Obtiene el valor float

    Convierte a float desde distintos tipos.

    Parameters
    ----------
    data : int or float or str or bool

    Returns
    -------
    float
        Representación float de la entrada

    Raises
    ------
    FloatError
    """
    try:
        ret = float(data)
    except (ValueError, TypeError):
        raise FloatError
    else:
        return ret


def fbool(data=None):
    """Obtiene el valor bool

    Convierte a bool desde distintos tipos.
    si es str intenta convertir si es representacion de bool.
    Dato sin valor genera error

    Parameters
    ----------
    data : int or str or bool

    Returns
    -------
    bool
        Representación int de la entrada

    Raises
    ------
    BooleanError
    """
    if type(data) is str:
        data = data.strip().lower()
        if data in ('f', 'false', 'n', 'no'):
            data = False
        elif data in ('t', 'true', 'y', 'yes', 's', 'si', 'sí'):
            data = True
        # Si sólo se admite str e int, esto no es necesario,
        # ya que fint lo tiene en cuenta.
        # Pero si se admiten (que será) más tipos a futuro
        # si lo será.
        elif data == '':
            data = None
    try:
        ret = fint(data)
    except IntegerError:
        raise BooleanError
    else:
        return bool(ret)


def fstr(data=None):
    """Obtiene el valor str

    Convierte a str desde distintos tipos.

    Parameters
    ----------
    data : int or float or str or bool

    Returns
    -------
    str
        Representación str de la entrada

    Raises
    ------
    StringError
    """
    try:
        return str(data)
    except (ValueError, TypeError):
        raise StringError


def fnone(data=None):
    """Devuelve el valor sin filtrar.

    Funcion dummy, devuelve lo  que le entra.

    Parameters
    ----------
    data : any

    Returns
    -------
    any
        Lo mismo que la entrada

    """
    return data


def ffactory(type, data=None):
    """Devuelve el valor filtrado por la función indicada en type

    Metodo factory, llama a la función type de filtrado.

    Parameters
    ----------
    type: str

    data: any

    Returns
    -------
    any
        Depende de la función llamada

    Raises
    ------
    ConvertionError

    """
    dfunc = {
        'int': fint,
        'float': ffloat,
        'bool': fbool,
        'str': fstr,
        'none': fnone,
    }
    if type in dfunc:
        ffunc = dfunc[type]
    else:
        ffunc = dfunc['none']
    return ffunc(data)


if __name__ == "__main__":
    print("Este fichero pertenece a un módulo, "
          "no es operativo como aplicación independiente.")
