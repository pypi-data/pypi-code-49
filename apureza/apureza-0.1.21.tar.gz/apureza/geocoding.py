# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""
from collections import OrderedDict

import unidecode
from gistools.geocoding import XParser

__author__ = 'Benjamin Pillot'
__copyright__ = 'Copyright 2019, Benjamin Pillot'
__email__ = 'benjaminpillot@riseup.net'


class SinanParser(XParser):
    """ Class for parsing addresses from SINAN database

    """

    _address_fields = dict(logrado='NM_LOGRADO',
                           numero='NU_NUMERO',
                           complement='NM_COMPLEM',
                           reference='NM_REFEREN')

    def __init__(self):
        super().__init__()
        self._re_parser.update(casa=r"(\b(?:k(?=sa)|c(?=asa|a?s?a?\.*\s*[\W_]*\d{1,3}))a?s?a?\.*\s*[\W_]*)(\d{1,3})?",
                               lote=r"(\bl(?=ote|o?t?e?\.*\s*[\W_]*\d{1,3})o?t?e?\.*\s*[\W_]*)(\d{1,3})?",
                               apartamento=r"(\bap(?=artamento|a?r?t?a?m?e?n?t?o?\.*\s*[\W_]*\d{1,"
                                           r"3})a?r?t?a?m?e?n?t?o?\.*\s*)(\d{1,3})?",

                               rua=r"(\bru?a?\.*\s*)((?:\d{1,3})|(?:.+?(?=condominio|\d)))",
                               avenida=r"(\bave?n?i?d?a?\.*\s*)((?:\d{1,3})|(?:.+?(?=condominio|\d)))",

                               condominio=r"(\bcondo?m?i?n?i?o?\.*\s*)((?:\d{1,3})|(?:.+?(?=\d)))",
                               chacara=r"(\bch(?=acara|a?c?a?r?a?\.*\s*[\W_]*)a?c?a?r?a?\.*\s*)((?:\d{1,3})|(?:.+?("
                                       r"?=\d)))")

    def parse(self, database):
        """ Parse addresses from SINAN database

        :param database: SINAN database
        :return:
        """

        for rough_address in addresses:
            address = unidecode.unidecode(rough_address).lower()


class BrasiliaParser(SinanParser):
    """ Address parser for Brasilia's DF

    """

    def __init__(self):

        self._re_parser.update(super_quadra_norte=r"(\bsqn\.*\s*)(\d{1,3})",
                               super_quadra_sul=r"(\bsqs\.*\s*)(\d{1,3})",
                               quadra=r"(\bq(?:c(?![uadr])|n(?![uadr]))?u?a?d?r?a?\.*\s*[\W_]*)(\d{1,3})",
                               conjunto=r"(\bco?n?j?u?n?t?o?\.*\s*[\W_]*)(\w{1,3})")

        # Build superclass after as we wish quadra and conjunto parsed first
        super().__init__()



