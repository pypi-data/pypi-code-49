"""
Applicato a una funziona che recupera un valore istantaneo serializzabile,
salva il risultato al tempo attuale, e permette
in un secondo tempo di usare la stessa funzione
per recuperare anche valori passati. Aggiunge due parole chiave,
"inizio" e "fine", prima di eventuali parole chiave della funzione,
 che possono essere usate per delimitare
l'intervallo temporale per cui vogliamo i dati.
"""

import os
import pickle
import gzip
import logging

# from datetime import datetime, timedelta
import pandas as pd

# from inspect import signature

CARTELLA_MEMORIA = os.path.expanduser("~") + '/store/registra/'

logger = logging.getLogger(__name__)


def registra(funzione):

    def funzione_con_intermediario(inizio=None, fine=None, limite=1):

        if inizio is not None:
            inizio = f'{pd.Timestamp(inizio)}'

        if fine is not None:
            fine = f'{pd.Timestamp(fine)}'

        nome_modulo = funzione.__module__.split('.')[-1]
        memoria_modulo = CARTELLA_MEMORIA + nome_modulo + '/'

        if not os.path.exists(memoria_modulo):
            os.mkdir(memoria_modulo)

        nome_funzione = funzione.__name__
        # assert not '_' in nome_funzione

        memoria_chiamata = memoria_modulo + f'{nome_funzione}'

        logger.info(f'intermedio {nome_modulo}.{nome_funzione} '
                    f'con inizio={inizio}, '
                    f'fine={fine}, limite={limite}')

        risultato_caricato = pd.Series()
        contatore = 0

        for pacco in sorted(os.listdir(memoria_modulo)):
            if pacco[-10:] == '.pickle.gz':
                chiamata = pacco.split('/')[-1]
                nome, tempo = chiamata[:-10].split('_')
                if nome == nome_funzione:
                    if (inizio is None or tempo >= inizio) and \
                            (fine is None or tempo < fine):
                        with gzip.open(memoria_modulo + pacco, 'rb') as f:
                            logger.info(f'carico dati da {pacco}')
                            risultato_caricato.loc[tempo] = \
                                pickle.load(f)
                            contatore += 1
                            if contatore == limite:
                                break

        if (contatore < limite) and (fine is None or
                                     pd.Timestamp(fine) >
                                     pd.datetime.utcnow()):
            logger.info(f'eseguo {nome_modulo}.{nome_funzione}')
            risultato = funzione()
            adesso = pd.datetime.utcnow()
            with gzip.open(memoria_chiamata + f'_{adesso}.pickle.gz',
                           'wb') as f:
                pickle.dump(risultato, f)
            risultato_caricato.loc[adesso] = risultato

        risultato_caricato.index = pd.to_datetime(risultato_caricato.index)

        return risultato_caricato

    return funzione_con_intermediario
