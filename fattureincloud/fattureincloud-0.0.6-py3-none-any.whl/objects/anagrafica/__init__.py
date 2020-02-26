from fattureincloud.base import MultipleManager
from .soggetto import *

TYPE_ANAGRAFICA_CLIENTI = 'clienti'
TYPE_ANAGRAFICA_FORNITORI = 'fornitori'

TYPES_ANAGRAFICA = [TYPE_ANAGRAFICA_CLIENTI, TYPE_ANAGRAFICA_FORNITORI]


class AnagraficaManager(MultipleManager):
    """
    Questo set di funzioni agisce su diverse tipologie di soggetti, identificati dalla variabile {soggetto}.
    I valori che possono essere assunti da {soggetto} sono due: clienti e fornitori.
    """
    _resources = {TYPE_ANAGRAFICA_CLIENTI: ClientiManager, TYPE_ANAGRAFICA_FORNITORI: FornitoriManager}
