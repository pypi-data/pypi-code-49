#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Esteban Barón"
__copyright__ = "Copyright 2020, Esteban Barón ,EBP"
__license__ = "MIT"
__email__ = "esteban@gominet.net"
__status__ = "Alpha"
__version__ = "1.0.0a8"

import logging
from varfilter import filter


class VarFilter:
    """Obtiene las variables del entorno requeridas"""
    def __init__(self, Adata=None, *sources):
        for data in Adata:
            self._values[data.Name] = fVar(data.Name,
                                           data.Default,
                                           data.Type,
                                           sources)

    def __getattribute__(self, attribute):
        if attribute in self._values:
            return self._values[attribute]


#
# Funciones
#
def fVar(name, default=None, type=None, *sources):
    """Obtiene variable de diferentes dicts

    Convierte a str desde distintos tipos.
    Si no se encuentra, o error en la conversion devuelve el default.
    Si el default no pasa la conversión devuelve error.
    Si el tipo no es reconocido, se utiliza none, es decir, no convertir

    Parameters
    ----------
    name : str

    default

    type : str

    Returns
    -------
    str
        Representación str de la entrada

    """
    logging.debug("fVar: El nombre a buscar es %s", name)
    found = False
    ret = default

    # logging.debug("fVar: El sources es %s", sources)
    for source in sources:
        if name in source:
            try:
                ret = filter.ffactory(type, source[name])
            except filter.ConvertionError:
                pass
            else:
                found = True
                # Sólo sale si lo ha encontrado y es correcto
                # Es decir, continua búscando si hay error
                break

    if not found and default is not None:
        ret = filter.ffactory(type, default)

    return ret


if __name__ == "__main__":
    print("Este fichero pertenece a un módulo, "
          "no es operativo como aplicación independiente.")
