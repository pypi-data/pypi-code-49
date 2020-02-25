import datetime
import random
import time

from horno.datos.Fechas import Fecha
from horno.utiles.IO import IOEscritor, IOSistema
from horno.utiles.Singleton import Singleton


#===================================================================================================
class Math (metaclass=Singleton):
    
    #------------------------------------------------------------------------------------------
    def Porcentaje(self, parcial, total):
        return 0 if total == 0 else parcial * 100.0 / total

    #------------------------------------------------------------------------------------------
    def IntervaloNA(self, minimo, maximo, salto=1):
        return range(minimo, maximo, salto)

    #------------------------------------------------------------------------------------------
    def IntervaloNC(self, minimo, maximo, salto=1):
        return self.IntervaloNA(minimo, maximo + 1, salto)

    #------------------------------------------------------------------------------------------
    def Intervalo0A(self, maximo, salto=1):
        return self.IntervaloNA(0, maximo, salto)

    #------------------------------------------------------------------------------------------
    def Intervalo0C(self, maximo, salto=1):
        return self.IntervaloNC(0, maximo, salto)

    #------------------------------------------------------------------------------------------
    def Intervalo1A(self, maximo, salto=1):
        return self.IntervaloNA(1, maximo, salto)

    #------------------------------------------------------------------------------------------
    def Intervalo1C(self, maximo, salto=1):
        return self.IntervaloNC(1, maximo, salto)
    
    #------------------------------------------------------------------------------------------
    def Random(self, valor_ini, valor_fin):
        return random.randint(valor_ini, valor_fin)

#===================================================================================================
class Performance:

    #------------------------------------------------------------------------------------------
    def __init__(self, msg='', gmt_delta_hours=-3):

        self._msg = msg
        self.gmt_delta_hours = gmt_delta_hours
        self.tiempo_ini = None 
        self.tiempo_fin = None 

    #------------------------------------------------------------------------------------------
    def __enter__(self):
        
        self.Iniciar()
        return self

    #------------------------------------------------------------------------------------------
    def __exit__(self, type, value, tb):
        
        self.Finalizar()

    #------------------------------------------------------------------------------------------
    def FechaAString(self, fecha):

        gmt_str = ' GMT%s%s' % ('+' if self.gmt_delta_hours >= 0 else '', self.gmt_delta_hours)
        return fecha.strftime("%d %b %Y %H:%M:%S" + gmt_str)

    #------------------------------------------------------------------------------------------
    def TimespanAString(self, span):

        partes = str(span).split(':')
        return '%s h, %s m, %s s' % (int(partes[0]), int(partes[1]), int(partes[2].split('.')[0]))

    #------------------------------------------------------------------------------------------
    def FechaAGMT(self, fecha):

        sys_delta_hours = -time.timezone / 3600
        return fecha + datetime.timedelta(hours=(self.gmt_delta_hours - sys_delta_hours))

    #------------------------------------------------------------------------------------------
    def Iniciar(self):

        self.tiempo_ini = self.FechaAGMT(Fecha.Ahora().get_val())
        IOSistema().PrintLine('(t) [%s] INI %s' % (self._msg, self.FechaAString(self.tiempo_ini)))
           
    #------------------------------------------------------------------------------------------
    def Finalizar(self):

        self.tiempo_fin = self.FechaAGMT(Fecha.Ahora().get_val())
        
        IOSistema().PrintLine('(t) [%s] FIN %s (%s)' % (self._msg, self.FechaAString(self.tiempo_fin), self.TimespanAString(self.tiempo_fin - self.tiempo_ini)))

    #------------------------------------------------------------------------------------------
    def TiempoAStr(self, obs=''):

        return '%s' % (self.TimespanAString(self.tiempo_fin - self.tiempo_ini))


#===================================================================================================
class Progreso:

    #------------------------------------------------------------------------------------------
    def __init__(self, avance, total, mensaje):
        
        self._finalizado = False
        self._contador = 0
        self._avance = avance
        self._total = total
        self._mensaje = mensaje
        self._porc_ult = -1
        self._porc_nue = -1

    #------------------------------------------------------------------------------------------
    def __enter__(self):
        
        self.Iniciar()
        return self

    #------------------------------------------------------------------------------------------
    def __exit__(self, type, value, tb):
        
        self.Finalizar()

    #------------------------------------------------------------------------------------------
    def Iniciar(self):

        IOSistema().Print('%s (%s).. ' % (self._mensaje, self._total))
        
        if self._porc_ult >= 100 or self._total <= 0:
            self.Finalizar()

    #------------------------------------------------------------------------------------------
    def Incrementar(self):
        
        self._contador = self._contador + 1
        self._porc_nue = int(self._contador * 100 / self._total)
        if self._porc_nue % self._avance == 0 and self._porc_nue != self._porc_ult:
            IOSistema().Print('%s%% ' % (self._porc_nue))
            self._porc_ult = self._porc_nue
        if self._porc_ult >= 100:
            self.Finalizar()

    #------------------------------------------------------------------------------------------
    def Finalizar(self):
        
        if not self._finalizado:
            self._finalizado = True
            IOSistema().PrintLine('[OK]')


#===================================================================================================
class ProgresoThreads:

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre, claves):

        self.io_nul = IOEscritor(IOSistema().DevNull())
        self.nombre = nombre
        self._contadores = dict()
        for clave in claves:
            self._contadores[clave] = {'ini':0, 'fin':0, 'tot':0}

    #------------------------------------------------------------------------------------------
    def SetTotal(self, clave, valor):

        self._contadores[clave]['tot'] = valor

    #------------------------------------------------------------------------------------------
    def IncrementarIniciados(self, clave):
        
        self._contadores[clave]['ini'] = self._contadores[clave]['ini'] + 1
        self.io_nul.EscribirExpress('[%s] %s' % (self.nombre, self._contadores), False, True)

    #------------------------------------------------------------------------------------------
    def IncrementarFinalizados(self, clave):
        
        self._contadores[clave]['fin'] = self._contadores[clave]['fin'] + 1
        self.io_nul.EscribirExpress('[%s] %s' % (self.nombre, self._contadores), False, True)


