from configparser import RawConfigParser

from horno.utiles.IO import IOEscritor


#=============================================================================================
class ConfigManager ():

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        self._parser = RawConfigParser()
        self._archivo = None

    #------------------------------------------------------------------------------------------
    def CargarCFG(self, archivo, append=False):
        
        self._archivo = archivo
        
        if not append:
            self._parser = RawConfigParser()
        
        if archivo.Existe():
            self._parser.read(archivo.Ruta())

    #------------------------------------------------------------------------------------------
    def GuardarCFG(self, archivo=None):
        
        if archivo is None: archivo = self._archivo
        
        archivo.CarpetaPadre().Crear()
        
        with IOEscritor(archivo).Abrir(False, binario=False) as iow:
            self._parser.write(iow.Stream())

    #------------------------------------------------------------------------------------------
    def Obtener(self, seccion, clave, valor_default=None):
        
        valor = self._parser.get(seccion, clave) if self._parser.has_section(seccion) and self._parser.has_option(seccion, clave) else ''
        return valor if valor else valor_default

    #------------------------------------------------------------------------------------------
    def ObtenerTodos(self, seccion):
        
        return self._parser.items(seccion) if self._parser.has_section(seccion) else []

    #------------------------------------------------------------------------------------------
    def AgregarSeccion(self, seccion):
        
        if not self._parser.has_section(seccion):
            self._parser.add_section(seccion)

    #------------------------------------------------------------------------------------------
    def Setear(self, seccion, clave, valor):

        self.AgregarSeccion(seccion)        
        self._parser.set(seccion, clave, valor)
