from fattureincloud.base import MultipleManager
from .fatture import *

TYPE_DOCUMENTO_FATTURE = 'fatture'
TYPE_DOCUMENTO_PROFORMA = 'proforma'
TYPE_DOCUMENTO_ORDINI = 'ordini'
TYPE_DOCUMENTO_PREVENTIVI = 'preventivi'
TYPE_DOCUMENTO_NDC = 'ndc'
TYPE_DOCUMENTO_RICEVUTE = 'ricevute'
TYPE_DOCUMENTO_DDT = 'ddt'
TYPE_DOCUMENTO_RAPPORTI = 'rapporti'
TYPE_DOCUMENTO_ORDFORN = 'ordforn'

TYPES_DOCUMENTO = [TYPE_DOCUMENTO_FATTURE, TYPE_DOCUMENTO_PROFORMA, TYPE_DOCUMENTO_ORDINI, TYPE_DOCUMENTO_PREVENTIVI, TYPE_DOCUMENTO_NDC, TYPE_DOCUMENTO_RICEVUTE, TYPE_DOCUMENTO_DDT, TYPE_DOCUMENTO_RAPPORTI, TYPE_DOCUMENTO_ORDFORN]


class DocumentoManager(MultipleManager):
    """
    Documenti emessi:
        Questo set di funzioni agisce su diverse tipologie di documenti, identificate dalla variabile {tipo-doc}.
        I valori che possono essere assunti da {tipo-doc} sono i seguenti: fatture, ricevute, preventivi, ordini, ndc, proforma, rapporti, ordforn e ddt.
        Per chiarezza si specifica che "ndc" identifica le note di credito, "ordini" gli ordini a cliente e "ordforn" gli ordini a fornitore.
    """
    _resources = {TYPE_DOCUMENTO_FATTURE: FattureManager}
