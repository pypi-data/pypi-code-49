from itertools import tee
import random
import re

from horno.utiles.Singleton import Singleton


#=============================================================================================
class Textos (metaclass=Singleton):

    #------------------------------------------------------------------------------------------
    def ContieneDigitos(self, texto):
    
        return not re.match(".*[0-9]+.*", texto) is None

#=============================================================================================
class Listas (metaclass=Singleton):

    #------------------------------------------------------------------------------------------
    def GetList(self, lista, indice, default=None):
        
        return lista[indice] if 0 <= indice < len(lista) else default 

    #------------------------------------------------------------------------------------------
    def GetListNoVacio(self, default, lista):
        
        lista_no_vacios = [e for e in lista if len(e)]
        return lista_no_vacios[0] if len(lista_no_vacios) else default

    #------------------------------------------------------------------------------------------
    def Unique(self, lista):
        
        return [e for n, e in enumerate(lista) if e not in lista[n + 1:]]

    #------------------------------------------------------------------------------------------
    def GetDict(self, key, default, dic):
        
        return dic.get(key, default)

    #------------------------------------------------------------------------------------------
    def RandomEn(self, valor):
        
        return random.choice(valor)

#=============================================================================================
class Iterables (metaclass=Singleton):
    
    #------------------------------------------------------------------------------------------
    def Pairwise(self, iterable):
        
        "s -> (s0,s1), (s1,s2), (s2, s3), ..."
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
