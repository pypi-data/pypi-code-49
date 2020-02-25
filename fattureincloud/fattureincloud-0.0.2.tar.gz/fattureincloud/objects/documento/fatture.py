# Fatture
from fattureincloud import mixins
from fattureincloud.base import Manager, RESTObject

FATTURA_NUOVO_ATTRS = (
    (
        'nome',
    ),
    (
        "id_cliente",
        "id_fornitore",
        "indirizzo_via",
        "indirizzo_cap",
        "indirizzo_citta",
        "indirizzo_provincia",
        "indirizzo_extra",
        "paese",
        "paese_iso",
        "lingua",
        "piva",
        "cf",
        "autocompila_anagrafica",
        "salva_anagrafica",
        "numero",
        "data",
        "valuta",
        "valuta_cambio",
        "prezzi_ivati",
        "rivalsa", # [Non presente in ddt e ordforn]
        "cassa", # [Non presente in ddt e ordforn]
        "rit_acconto", # [Non presente in ddt e ordforn]
        "imponibile_ritenuta", # [Non presente in ddt e ordforn]
        "rit_altra", # [Non presente in ddt e ordforn]
        'marca_bollo', # [Non presente in ddt e ordforn]
        'oggetto_visibile', # [Non presente in ddt]
        'oggetto_interno', # [Non presente in ddt]
        'centro_ricavo', # [Non presente in ddt e ordforn]
        # 'centro_costo', #  [Solo in ordforn]
        'note', # [Non presente in ddt]
        'nascondi_scadenza', # [Non presente in ddt]
        'ddt', # [Non presente in ndc e ordforn]
        'ftacc', # [Solo in fatture]
        'id_template', # [Solo se tipo!=ddt]
        # 'ddt_id_template', # [Solo se ddt=true]
        # 'ftacc_id_template', # [Solo se ftacc=true]
        'mostra_info_pagamento', # [Non presente in ddt e ndc]
        'metodo_pagamento',
        'metodo_titoloN',
        'metodo_descN',
        # 'mostra_totali', # [Solo per preventivi, rapporti e ordforn]
        'mostra_bottone_paypal', # [Solo per ricevute, fatture, proforma, ordini]
        'mostra_bottone_bonifico', # [Solo per ricevute, fatture, proforma, ordini]
        'mostra_bottone_notifica', # [Solo per ricevute, fatture, proforma, ordini]
        'lista_articoli',
        'lista_pagamenti',
        'ddt_numero', # [Se ddt=true]
        'ddt_data', # [Se ddt=true]
        'ddt_colli', # [Se ddt/ftacc=true]
        'ddt_peso', # [Se ddt/ftacc=true]
        'ddt_causale', # [Se ddt/ftacc=true]
        'ddt_luogo', # [Se ddt/ftacc=true]
        'ddt_trasportatore', # [Se ddt/ftacc=true]
        'ddt_annotazioni', # [Se ddt/ftacc=true]
        'PA', # [Solo per fatture e ndc elettroniche]
        'PA_tipo_cliente',
        'PA_tipo',
        'PA_numero',
        'PA_data',
        'PA_cup',
        'PA_cig',
        'PA_codice',
        'PA_pec',
        'PA_esigibilita',
        'PA_modalita_pagamento',
        'PA_istituto_credito',
        'PA_iban',
        'PA_beneficiario',
        'extra_anagrafica',
        'split_payment', # [Solo per fatture, ndc e proforma NON elettroniche]
    ),
)

FATTURA_MODIFICA_ATTRS = (
    tuple(),
    (
        'id',
        'token',
        "id_cliente",
        "id_fornitore",
        'nome',
        "indirizzo_via",
        "indirizzo_cap",
        "indirizzo_citta",
        "indirizzo_provincia",
        "indirizzo_extra",
        "paese",
        "paese_iso",
        "lingua",
        "piva",
        "cf",
        "autocompila_anagrafica",
        "salva_anagrafica",
        "numero",
        "data",
        "valuta",
        "valuta_cambio",
        "prezzi_ivati",
        "rivalsa",  # [Non presente in ddt e ordforn]
        "cassa",  # [Non presente in ddt e ordforn]
        "rit_acconto",  # [Non presente in ddt e ordforn]
        "imponibile_ritenuta",  # [Non presente in ddt e ordforn]
        "rit_altra",  # [Non presente in ddt e ordforn]
        'marca_bollo',  # [Non presente in ddt e ordforn]
        'oggetto_visibile',  # [Non presente in ddt]
        'oggetto_interno',  # [Non presente in ddt]
        'centro_ricavo',  # [Non presente in ddt e ordforn]
        # 'centro_costo', #  [Solo in ordforn]
        'note',  # [Non presente in ddt]
        'nascondi_scadenza',  # [Non presente in ddt]
        'ddt',  # [Non presente in ndc e ordforn]
        'ftacc',  # [Solo in fatture]
        'id_template',  # [Solo se tipo!=ddt]
        # 'ddt_id_template', # [Solo se ddt=true]
        # 'ftacc_id_template', # [Solo se ftacc=true]
        'mostra_info_pagamento',  # [Non presente in ddt e ndc]
        'metodo_pagamento',
        'metodo_titoloN',
        'metodo_descN',
        # 'mostra_totali', # [Solo per preventivi, rapporti e ordforn]
        'mostra_bottone_paypal',  # [Solo per ricevute, fatture, proforma, ordini]
        'mostra_bottone_bonifico',  # [Solo per ricevute, fatture, proforma, ordini]
        'mostra_bottone_notifica',  # [Solo per ricevute, fatture, proforma, ordini]
        'lista_articoli',
        'lista_pagamenti',
        'ddt_numero',  # [Se ddt=true]
        'ddt_data',  # [Se ddt=true]
        'ddt_colli',  # [Se ddt/ftacc=true]
        'ddt_peso',  # [Se ddt/ftacc=true]
        'ddt_causale',  # [Se ddt/ftacc=true]
        'ddt_luogo',  # [Se ddt/ftacc=true]
        'ddt_trasportatore',  # [Se ddt/ftacc=true]
        'ddt_annotazioni',  # [Se ddt/ftacc=true]
        'PA',  # [Solo per fatture e ndc elettroniche]
        'PA_tipo_cliente',
        'PA_tipo',
        'PA_numero',
        'PA_data',
        'PA_cup',
        'PA_cig',
        'PA_codice',
        'PA_pec',
        'PA_esigibilita',
        'PA_modalita_pagamento',
        'PA_istituto_credito',
        'PA_iban',
        'PA_beneficiario',
        'extra_anagrafica',
        'split_payment',  # [Solo per fatture, ndc e proforma NON elettroniche]
    ),
)

FATTURA_INVIAMAIL_ATTRS = (
    (
        'mail_mittente',
        'mail_destinatario',
        'oggetto',
        'messaggio'
    ),
    (
        'id',
        'token',
        'includi_documento',
        'invia_ddt',
        'invia_fa',
        'includi_allegato',
        'invia_copia',
        'allega_pdf'
    )
)


class Fatture(mixins.DettagliMixin, mixins.EliminaMixin, mixins.ModificaMixin, RESTObject):
    """
    Fatture
    """
    _modifica_attrs = FATTURA_MODIFICA_ATTRS


class FattureManager(mixins.CRUDMixin, mixins.InfoMixin, mixins.InfoMailMixin, mixins.InviaMailMixin, Manager):
    _path = 'fatture'
    _obj_cls = Fatture
    _nuovo_attrs = FATTURA_NUOVO_ATTRS
    _modifica_attrs = FATTURA_MODIFICA_ATTRS
    _dettagli_obj_key = 'dettagli_documento'
    _inviamail_attrs = FATTURA_INVIAMAIL_ATTRS