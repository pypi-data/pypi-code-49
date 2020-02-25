#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from horno.utiles.Singleton import Singleton
import unidecode


class Encoding (metaclass=Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        self.TablaTran = {
            
            # chars = 80 .. 8F
            '\x80':'C', '\x82':'e',

            # chars = A0 .. AF
            '\xa0':'a', '\xa1':'i', '\xa2':'o', '\xa3':'u', '\xa4':'?', '\xa5':'Ñ', '\xa6':'?', '\xa7':'?', '\xa8':'?', '\xa9':'?', '\xaa':'?', '\xab':'?', '\xac':'?', '\xad':'0', '\xae':'?', '\xaf':'?',

            # chars = B0 .. BF
            '\xb0':'?', '\xb1':'?', '\xb2':'?', '\xb3':'?', '\xb4':'?', '\xb5':'?', '\xb6':'?', '\xb7':'?', '\xb8':'?', '\xb9':'?', '\xba':'?', '\xbb':'?', '\xbc':'?', '\xbd':'?', '\xbe':'?', '\xbf':'?',

            # chars = C0 .. CF
            '\xc0':'A', '\xc1':'A', '\xc2':'A', '\xc3':'A', '\xc4':'A', '\xc5':'A', '\xc6':'AE','\xc7':'C', '\xc8':'E', '\xc9':'E', '\xca':'E', '\xcb':'E', '\xcc':'I', '\xcd':'I', '\xce':'I', '\xcf':'I',

            # chars = D0 .. DF
            '\xd0':'D', '\xd1':'Ñ', '\xd2':'O', '\xd3':'O', '\xd4':'O', '\xd5':'O', '\xd6':'O', '\xd7':'?', '\xd8':'O', '\xd9':'U', '\xda':'U', '\xdb':'U', '\xdc':'U', '\xdd':'Y', '\xde':'?', '\xdf':'ss',

            # chars = E0 .. EF
            '\xe0':'a', '\xe1':'a', '\xe2':'a', '\xe3':'a', '\xe4':'a', '\xe5':'a', '\xe6':'ae','\xe7':'c', '\xe8':'e', '\xe9':'e', '\xea':'e', '\xeb':'e', '\xec':'i', '\xed':'i', '\xee':'i', '\xef':'i',
            
            # chars = F0 .. FF
            '\xf0':'d', '\xf1':'ñ', '\xf2':'o', '\xf3':'o', '\xf4':'o', '\xf5':'o', '\xf6':'o', '\xf7':'?', '\xf8':'o', '\xf9':'u', '\xfa':'u', '\xfb':'u', '\xfc':'u', '\xfd':'y', '\xfe':'?', '\xff':'y',
        }

    #------------------------------------------------------------------------------------------
    def Lower(self, texto, extendido=False):
    
        return texto.lower() if not extendido else texto.lower().replace('Ñ', 'ñ')

    #------------------------------------------------------------------------------------------
    def Upper(self, texto, extendido=False):
    
        return texto.upper() if not extendido else texto.upper().replace('ñ', 'Ñ')

    #------------------------------------------------------------------------------------------
    def Capitalizar(self, texto):
    
        def capitalizar_palabra(s):
            return '' if not s else '%s%s' % (self.Upper(s[0], True), self.Lower(s[1:], True))
    
        return ' '.join([ capitalizar_palabra(s) for s in texto.split(' ') ])

    #------------------------------------------------------------------------------------------
    def NormalizarTexto(self, texto):

        return unidecode.unidecode(texto)

    #------------------------------------------------------------------------------------------
    def NormalizarTextoViejo(self, texto):

        if texto is None:
            return texto
        
        texto = self.ToUnicode(texto)
        for (k, v) in self.TablaTran.items():
            texto = texto.replace(self.ToUnicode(k), self.ToUnicode(v))

        return self.ToString(texto)
    
    #------------------------------------------------------------------------------------------
    def NormalizarLista(self, datos):

        return [ Encoding().NormalizarTexto(t) for t in datos ]

    #------------------------------------------------------------------------------------------
    def ToUnicode(self, dato, code='latin1'):

        try:        
            #return dato if isinstance(dato, unicode) else str(dato).decode(code)
            return str(dato)
        except:
            return '<ERROR_ENC_UNI>'
     
    #------------------------------------------------------------------------------------------
    def ToString(self, dato, code='latin1'):

        try:        
            #return dato.encode(code) if isinstance(dato, unicode) else str(dato)
            return str(dato)
        except:
            return '<ERROR_ENC_STR>'

