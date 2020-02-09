"""Decorazione che trasforma una funzione in
uno scrittore e lettore di dati dalla memoria."""

import os
import pickle
import gzip
import logging

from inspect import signature

dir_path = os.path.dirname(os.path.realpath(__file__))

CARTELLA_MEMORIA = os.path.expanduser("~") + '/store/ricorda/'
logger = logging.getLogger(__name__)


class NonRicordabile(Exception):
    pass


def ricorda(funzione):

    def funzione_con_intermediario(*args, **kwargs):

        # print(args)
        # print(kwargs)

        forma_chiamata = signature(funzione)
        chiamata = forma_chiamata.bind(*args, **kwargs)
        chiamata.apply_defaults()
        firma = '_'.join([f'{k}={chiamata.arguments[k]}'
                          for k in chiamata.arguments])
        # print(firma)

        try:

            for arg in args:
                hash(arg)
            for kwarg in kwargs.values():
                hash(kwarg)

        except TypeError as e:

            raise NonRicordabile('Ricorda non può salvare questa chiamata'
                                 f' a causa di: "{e}"')

        nome_modulo = funzione.__module__.split('.')[-1]
        # print(nome_modulo)

        nome_funzione = funzione.__name__
        # assert not '_' in nome_funzione
        # print(nome_funzione)

        logger.info(f'intermedio {nome_modulo}.{nome_funzione} '
                    f'con firma=({firma})')

        memoria_modulo = CARTELLA_MEMORIA + nome_modulo + '/'

        if not os.path.exists(memoria_modulo):
            os.mkdir(memoria_modulo)

        memoria_chiamata = memoria_modulo + \
            f'{nome_funzione}_firma=({firma}).pickle.gz'

        if not os.path.exists(memoria_chiamata):
            logger.info('salvo il valore in memoria')

            risultato = funzione(*args, **kwargs)
            with gzip.open(memoria_chiamata, 'wb') as f:
                pickle.dump(risultato, f)

        else:
            logger.info('carico il valore dalla memoria')
            with gzip.open(memoria_chiamata, 'rb') as f:
                risultato = pickle.load(f)

        return risultato

    return funzione_con_intermediario


if __name__ == '__main__':

    @ricorda
    def test(a):
        return a + 1

    print(test(10))

    @ricorda
    def test1(a, b='ciao'):
        return a + 1

    print(test1(10))
    print(test1(10, 'ciaone'))
