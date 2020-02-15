#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Esteban Barón"
__copyright__ = "Copyright 2020, Esteban Barón ,EBP"
__license__ = "MIT"
__email__ = "esteban@gominet.net"
__status__ = "Alpha"
__version__ = "1.0.0a4"

import logging
from varfilter import filter


class VarFilter:
    """Obtiene las variables del entorno requeridas"""
    def __init__(self, Adata=None, *sources):
        for data in Adata:
            self._values[data.Name] = fVar(data.Name,
                                           data.Default,
                                           data.Type, sources)

    def __getattribute__(self, attribute):
        if attribute in self._values:
            return self._values[attribute]


#
# Funciones
#
def fVar(name, default=None, type=None, *sources):
    """Obtiene variable de diferentes dicts"""
    logging.debug("fVar: El nombre a buscar es %s", name)
    ret = default
    # logging.debug("fVar: El sources es %s", sources)
    for source in sources:
        # logging.debug("fVar: El source es %s", source)
        if name in source:
            ret = source[name]
            break

    # Filtra la salida dependiendo del type
    if type == 'int':
        try:
            ret = filter.fint(ret)
        except filter.IntegerError:
            ret = None
    else:
        try:
            ret = str(ret)
        except ValueError:
            ret = None

    return ret


if __name__ == "__main__":
    print("Este fichero pertenece a un módulo, "
          "no es operativo como aplicación independiente.")
