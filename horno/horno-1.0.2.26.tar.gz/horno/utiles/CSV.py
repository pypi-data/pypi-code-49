from horno.datos.Encoding import Encoding
from horno.datos.Registro import Registro
from horno.utiles.IO import IOLector
from horno.utiles.Logger import Logger
from horno.utiles.Metricas import Progreso
import csv

#=============================================================================================
class CSVLector:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, nombre, archivo_csv_input, func_reg_id, delim=',', quote='"'):
        
        self._nombre = nombre
        self._archivo = archivo_csv_input
        self._delim = delim
        self._quote = quote
        self._func_reg_id = func_reg_id
        self._header = []
        self._datos = dict()
        self._inicializado = False

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        return self._nombre

    #------------------------------------------------------------------------------------------
    def Archivo(self):
        return self._archivo

    #------------------------------------------------------------------------------------------
    def Header(self):
        return self._header

    #------------------------------------------------------------------------------------------
    def Inicializado(self):
        return self._inicializado

    #------------------------------------------------------------------------------------------
    def Claves(self):
        return self._datos.keys()

    #------------------------------------------------------------------------------------------
    def RegistroNuevo(self):
        reg = Registro()
        for h in self._header:
            reg.setv(h, '')
        return reg

    #------------------------------------------------------------------------------------------
    def ClaveExiste(self, key):
        return key in self._datos
            
    #------------------------------------------------------------------------------------------
    def RegistrosExisten(self, key):
        return self.ClaveExiste(key) and len(self._datos[key]) > 0

    #------------------------------------------------------------------------------------------
    def RegistrosPorId(self, key):
        if not self.ClaveExiste(key):
            return None

        regs = []
        for dato in self._datos[key]:
            reg = self.RegistroUsandoDato(dato)
            regs.append(reg)
            
        return regs

    #------------------------------------------------------------------------------------------
    def RegistrosPorValores(self, dic_prop_valor):

        regs = []
        for key in self._datos.keys():
            for dato in self._datos[key]:
                reg = self.RegistroUsandoDato(dato)
                reg_cumple = True
                for (k, v) in dic_prop_valor.items():
                    if reg.getv(k) != v:
                        reg_cumple = False
                        break
                if reg_cumple:
                    regs.append(reg)
            
        return regs

    #------------------------------------------------------------------------------------------
    def RegistroUsandoDato(self, dato):

        reg = Registro()
        c = 0
        for h in self._header:
            reg.setv(h, dato[c] if c < len(dato) else '')
            c += 1
        return reg

    #------------------------------------------------------------------------------------------
    def ContarRegistros(self):

        r = self._archivo.CantidadLineas()
        return 0 if r == 0 else r - 1 #restar header si hay datos

    #------------------------------------------------------------------------------------------
    def LeerRegistros(self):

        info = {'reg_repetidos':[], 'reg_erroneos':[], 'info_repetidos':[], 'info_erroneos':[], }

        if not self._archivo.Existe():
            Logger().Log('[ %s ] Error: El archivo no existe' % (self._archivo))
            exit()

        self._datos.clear()
        self._archivo.RepararEncoding()

        progreso = Progreso(5, self.ContarRegistros(), '[ %s ] Leyendo' % (self._archivo))

        with IOLector(self._archivo).Abrir(binario=True) as ior:
        
            self._reader = csv.reader(ior.Stream(), delimiter=self._delim, quotechar=self._quote)
    
            for hdr in self._reader:
                self._header = Encoding().NormalizarLista([h.lower() for h in hdr]) 
                break
    
            for dato in self._reader:
                try:
                    progreso.Incrementar()

                    reg = self.RegistroUsandoDato(dato)
                    key = self._func_reg_id(reg)
                    if key not in self._datos:
                        self._datos[key] = []
                    else:
                        info['reg_repetidos'].append(reg)
                        info['info_repetidos'].append(key)
                    self._datos[key].append(Encoding().NormalizarLista(dato))
                    
                except Exception as e:
                    info['reg_erroneos'].append(reg)
                    info['info_erroneos'].append(e)
    
        self._inicializado = True
        
        return info

#=============================================================================================
class CSVEscritor:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, archivo_csv_output='nul', headerstruc=None, escribir_header=True, delim=',', quote='"', quoting=csv.QUOTE_ALL):
        
        self._nombre = archivo_csv_output
        self._archivo = archivo_csv_output
        self._headerstruc = headerstruc
        self._escribir_header = escribir_header
        self._delim = delim
        self._quote = quote
        self._quoting = quoting

        if archivo_csv_output.Existe():
            Logger().Log('[ %s ] Warning: El archivo ya existe' % (archivo_csv_output), False)
        if not archivo_csv_output.CarpetaPadre().Existe():
            Logger().Log('[ %s ] Warning: La carpeta no existe, creando..' % (archivo_csv_output), False)
            archivo_csv_output.CarpetaPadre().Crear()

        self._writer = csv.writer(open(archivo_csv_output.Ruta(), 'wb'), delimiter=self._delim, quotechar=self._quote, quoting=self._quoting)
        
        if self._escribir_header:
            self.EscribirHeader()
        
    #------------------------------------------------------------------------------------------
    def Nombre(self):
        return self._nombre

    #------------------------------------------------------------------------------------------
    def Archivo(self):
        return self._archivo

    #------------------------------------------------------------------------------------------
    def EscribirHeader(self):

        if self._headerstruc is None:
            raise RuntimeError('[ %s ] Error: El _headerstruc no ha sido definido' % (self._archivo))
        
        header = []
        for tdato in self._headerstruc:
            header.append(tdato.Nombre().lower())

        header = Encoding().NormalizarLista(header)
        self._writer.writerow(header)

    #------------------------------------------------------------------------------------------
    def EscribirDatos(self, datos):
        
        progreso = Progreso(5, len(datos), '[ %s ] Escribiendo' % (self._archivo))

        for dato in datos:
            progreso.Incrementar()
            dato = Encoding().NormalizarLista(dato)
            self._writer.writerow(dato)
        
    #------------------------------------------------------------------------------------------
    def EscribirRegistros(self, regs):
        
        progreso = Progreso(5, len(regs), '[ %s ] Escribiendo' % (self._archivo))
        
        for reg in regs:
            progreso.Incrementar()
            self.EscribirRegistro(reg)

    #------------------------------------------------------------------------------------------
    def EscribirRegistro(self, reg):
        
        if self._headerstruc is None:
            raise RuntimeError('[ %s ] Error: El _headerstruc no ha sido definido' % (self._archivo))

        dato = []
        for tdato in self._headerstruc:
            header_nombre = tdato.Nombre()
            dato.append(reg.getv(header_nombre))
            
        self._writer.writerow(dato)
        
    #------------------------------------------------------------------------------------------
    def RedirigirSalida(self, archivo_csv_output):
        
        self.__init__(archivo_csv_output, self._headerstruc, self._escribir_header, self._delim, self._quote, self._quoting)

    #------------------------------------------------------------------------------------------
    def RegistroNuevo(self):
        reg = Registro()
        for tdato in self._headerstruc:
            reg.setv(tdato.Nombre(), '')
        return reg

