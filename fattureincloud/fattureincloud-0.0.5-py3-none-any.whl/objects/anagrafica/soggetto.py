# Clienti
from fattureincloud import mixins
from fattureincloud.base import Manager, RESTObject

SOGGETTO_NUOVO_ATTRS = (
    tuple(
        'nome'
    ),
    (
        'referente',
        'indirizzo_via',
        'indirizzo_cap',
        'indirizzo_citta',
        'indirizzo_provincia',
        'indirizzo_extra',
        'paese',
        'paese_iso',
        'mail',
        'tel'
        'fax',
        'piva',
        'cf',
        'termini_pagamento',
        'pagamento_fine_mese',
        'cod_iva_default',
        'extra',
        'PA',
        'PA_codice'
    ),
)

SOGGETTO_MODIFICA_ATTRS = (
    tuple(
        'id'
    ),
    (
        'nome',
        'referente',
        'indirizzo_via',
        'indirizzo_cap',
        'indirizzo_citta',
        'indirizzo_provincia',
        'indirizzo_extra',
        'paese',
        'paese_iso',
        'mail',
        'tel'
        'fax',
        'piva',
        'cf',
        'termini_pagamento',
        'pagamento_fine_mese',
        'cod_iva_default',
        'extra',
        'PA',
        'PA_codice'
    ),
)


class Soggetto(mixins.EliminaMixin, mixins.ModificaMixin, RESTObject):
    """
    Soggetto
    """
    _modifica_attrs = SOGGETTO_MODIFICA_ATTRS


class ClientiManager(mixins.NuovoMixin, mixins.ModificaMixin, mixins.EliminaMixin, Manager):
    _path = 'clienti'
    _obj_cls = Soggetto
    _nuovo_attrs = SOGGETTO_NUOVO_ATTRS
    _modifica_attrs = SOGGETTO_MODIFICA_ATTRS


class FornitoriManager(mixins.NuovoMixin, mixins.ModificaMixin, mixins.EliminaMixin, Manager):
    _path = 'fornitori'
    _obj_cls = Soggetto
    _nuovo_attrs = SOGGETTO_NUOVO_ATTRS
    _modifica_attrs = SOGGETTO_MODIFICA_ATTRS