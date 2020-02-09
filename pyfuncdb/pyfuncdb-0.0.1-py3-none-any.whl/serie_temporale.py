"""Decorazione che trasforma una funzione che genera
dati indicizzati dal tempo in uno scrittore e lettore
di una serie temporale scritta in memoria fissa.

La decorazione usa tre argomenti della funzione ospite:

- inizio: datetime/timestamp/str. Chiedi dati a tempo >= inizio.
- fine: datetime/timestamp/str oppure None. Chiedi dati
    a tempo < fine.
- limite: quanti punti dati, al massimo, restituire, a partire
    dal tempo di inizio. Se negativo, a partire dal tempo finale.

In memoria fissa teniamo un blocco di dati contiguo, per cui questa
decorazione è inefficiente se non ci interessa un'intera serie
temporale, cioè un continuo di valori nel tempo,
ma solo certi valori a tempi sporadici.

L'utente può specificare i nomi degli argomenti inizio, fine, e limite.
"""

import os
import logging
from inspect import signature
# from datetime import datetime, timedelta

import numpy as np
import pandas as pd

CARTELLA_MEMORIA = os.path.expanduser("~") + '/store/serie_temporale/'

logger = logging.getLogger(__name__)


class ErroreSerieTemporale(Exception):
    pass


def carica_dati_da_magazzino(percorso_magazzino, inizio, fine, limite):
    dove = f'index >= Timestamp("{inizio}") & index < Timestamp("{fine}")'
    with pd.HDFStore(percorso_magazzino) as s:
        result = s.select('serie_temporale',
                          where=dove)
    if limite < np.inf:
        result = result.iloc[:limite]
    return result


def ottieni_memoria_modulo(nome_modulo):
    return CARTELLA_MEMORIA + nome_modulo + '/'


def ottieni_inizio_nome(nome_funzione, firma):
    return f'{nome_funzione}_firma=({firma})_'


def ottieni_nome_magazzino(nome_modulo, nome_funzione, inizio, fine, firma):
    return ottieni_memoria_modulo(nome_modulo) + \
        ottieni_inizio_nome(nome_funzione, firma) + \
        f'inizio={inizio}_' + \
        f'fine={fine}.h5'


def salva_magazzino(nome_modulo, nome_funzione, risultato, firma):
    inizio_dati_risultato = risultato.index[0]
    fine_dati_risultato = risultato.index[-1]
    percorso_magazzino = ottieni_nome_magazzino(nome_modulo,
                                                nome_funzione,
                                                inizio_dati_risultato,
                                                fine_dati_risultato,
                                                firma)
    logger.info(f'Salvo in memoria {percorso_magazzino}')
    # risultato.index = pd.to_datetime(risultato.index)
    risultato.to_hdf(percorso_magazzino,
                     key='serie_temporale',
                     format='table'
                     )
    return percorso_magazzino


def estrai_firma_e_argomenti(funzione, inizio, fine, limite,
                             args, kwargs):
    forma_chiamata = signature(funzione)
    chiamata = forma_chiamata.bind(*args, **kwargs)
    chiamata.apply_defaults()

    inizio_chiamata = chiamata.arguments[inizio]
    fine_chiamata = chiamata.arguments[fine]
    limite_chiamata = chiamata.arguments[limite]

    altri_argomenti = {k: chiamata.arguments[k]
                       for k in chiamata.arguments
                       if k not in [inizio, fine, limite]}

    firma = ','.join([f'{k}={altri_argomenti[k]}'
                      for k in altri_argomenti])
    return inizio_chiamata, fine_chiamata, limite_chiamata, \
        altri_argomenti, firma


def rinomina_magazzino(percorso_magazzino, nuovo_nome):
    logger.info(f'Rinomino il magazzino: {nuovo_nome}')
    os.rename(percorso_magazzino, nuovo_nome)
    return nuovo_nome


def serie_temporale(inizio='inizio', fine='fine', limite='limite'):

    def decoratore(funzione):

        def funzione_con_intermediario(*args, **kwargs):

            inizio_chiamata, fine_chiamata, limite_chiamata, \
                altri_argomenti, firma = \
                estrai_firma_e_argomenti(funzione, inizio,
                                         fine, limite,
                                         args, kwargs)

            if limite_chiamata == 0:
                return None

            def chiama_funzione(inizio_locale, fine_locale, limite_locale):
                logger.info(f'Chiamo la funzione da {inizio_locale}'
                            f' a {fine_locale} con limite '
                            f'{limite_locale}.')
                argomenti = {inizio: inizio_locale,
                             fine: fine_locale,
                             limite: limite_locale}
                argomenti.update(altri_argomenti)
                risultato = funzione(**argomenti)
                if risultato is not None:
                    risultato.index = pd.to_datetime(risultato.index)
                return risultato

            nome_modulo = funzione.__module__.split('.')[-1]
            nome_funzione = funzione.__name__
            # assert not '_' in nome_funzione

            logger.info(f'intermedio {nome_modulo}.{nome_funzione}'
                        f' con inizio={inizio_chiamata}, fine={fine_chiamata},'
                        f' limite={limite_chiamata}, firma={firma}')

            memoria_modulo = ottieni_memoria_modulo(nome_modulo)
            if not os.path.exists(memoria_modulo):
                os.mkdir(memoria_modulo)

            # controlliamo se esiste già un magazzino
            inizio_nome = ottieni_inizio_nome(nome_funzione, firma)
            magazzini = os.listdir(memoria_modulo)
            candidati = [el for el in magazzini
                         if el[:len(inizio_nome)] == inizio_nome]

            if len(candidati) > 1:
                raise ErroreSerieTemporale('Troppi magazzini con nome '
                                           'compatibile.')

            if not len(candidati):
                logger.info('Nessun dato in memoria, chiamo la funzione.')
                risultato = funzione(*args, **kwargs)
                risultato.index = pd.to_datetime(risultato.index)
                salva_magazzino(nome_modulo, nome_funzione, risultato, firma)
                return risultato

            magazzino = candidati[0]
            percorso_magazzino = memoria_modulo + magazzino
            inizio_dati_memoria = pd.Timestamp(magazzino[
                len(inizio_nome):-3].split('_')[-2][7:])
            fine_dati_memoria = pd.Timestamp(magazzino[
                len(inizio_nome):-3].split('_')[-1][5:])
            logger.info(f'In memoria abbiamo dati da {inizio_dati_memoria}'
                        f' a {fine_dati_memoria}.')

            # Procedo con tre passaggi:
            # - se necessario, estendo il magazzino in memoria a sx
            # - se necessario, estendo il magazzino in memoria a dx
            # - restituisco i valori letti dalla memoria

            # estensione sinistra
            if inizio_chiamata < inizio_dati_memoria:

                logger.info('Estendo a sinistra')

                estensione_sinistra = chiama_funzione(inizio_chiamata,
                                                      inizio_dati_memoria,
                                                      np.inf)

                if estensione_sinistra is not None \
                        and len(estensione_sinistra) > 0:
                    with pd.HDFStore(percorso_magazzino) as s:
                        dati_da_memoria = s.select('serie_temporale')

                    risultato_esteso = pd.concat([estensione_sinistra,
                                                  dati_da_memoria])

                    os.remove(percorso_magazzino)
                    percorso_magazzino = salva_magazzino(nome_modulo,
                                                         nome_funzione,
                                                         risultato_esteso,
                                                         firma)
                    inizio_dati_memoria = inizio_chiamata
                else:
                    logger.info('Nessun dato per estendere a sinistra')
                    nuovo_nome = ottieni_nome_magazzino(nome_modulo,
                                                        nome_funzione,
                                                        inizio_chiamata,
                                                        fine_dati_memoria,
                                                        firma)
                    percorso_magazzino = \
                        rinomina_magazzino(percorso_magazzino, nuovo_nome)

            # estensione destra
            if fine_chiamata > fine_dati_memoria:

                # # controlla quanti punti chiedere
                # if limite_chiamata < np.inf:
                #     dati_già_in_memoria = carica_dati_da_magazzino(
                #                            percorso_magazzino,
                #                            inizio_chiamata,
                #                            fine_chiamata,
                #                            limite_chiamata)
                #     limite_estensione = limite_chiamata - \
                #         len(dati_già_in_memoria)
                # else:
                #     limite_estensione = np.inf

                logger.info('Estendo a destra')
                estensione_destra = chiama_funzione(fine_dati_memoria,
                                                    fine_chiamata,
                                                    np.inf)

                if estensione_destra is not None and \
                        len(estensione_destra) > 0:

                    if estensione_destra.index[0] == fine_dati_memoria:
                        estensione_destra = estensione_destra.iloc[1:]

                    if len(estensione_destra):
                        try:
                            with pd.HDFStore(percorso_magazzino) as s:
                                s.append('serie_temporale', estensione_destra)

                            nuovo_nome = ottieni_nome_magazzino(
                                nome_modulo, nome_funzione,
                                inizio_dati_memoria,
                                estensione_destra.index[-1], firma)

                            percorso_magazzino = rinomina_magazzino(
                                percorso_magazzino, nuovo_nome)
                        except ValueError as e:
                            # TODO test case for this
                            with pd.HDFStore(percorso_magazzino) as s:
                                existing_data = s.select('serie_temporale')
                            if estensione_destra.shape == existing_data.shape:
                                raise e

                            logger.info('Trying to append data of shape '
                                        f'{estensione_destra.shape} '
                                        'to existing data of shape '
                                        f'{existing_data.shape}')

                            risultato_esteso = pd.concat(
                                [existing_data, estensione_destra])

                            os.remove(percorso_magazzino)
                            percorso_magazzino = salva_magazzino(
                                nome_modulo, nome_funzione,
                                risultato_esteso, firma)

                else:
                    logger.info('Nessun dato per estendere a destra')

            # restituisco i valori letti dalla memoria
            return carica_dati_da_magazzino(
                percorso_magazzino,
                inizio_chiamata,
                fine_chiamata,
                limite_chiamata)

        return funzione_con_intermediario

    return decoratore
