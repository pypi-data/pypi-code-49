from horno.datos.Fechas import Fecha
import datetime
class Registro:

    #------------------------------------------------------------------------------------------
    def __init__(self, datos=None, valor_default=''):
        
        self.valor_default = valor_default
        self._datos = dict()
        if datos is not None:
            for (k, v) in datos.items():
                self._datos[str(k).lower()] = v

    #------------------------------------------------------------------------------------------
    def __str__(self):
        
        res = '\n'
        for (k, v) in sorted(self._datos.items(), key=lambda p: p[0]):
            res += '[%s] = %s\n' % (k, v)
        return res

    #------------------------------------------------------------------------------------------
    def __repr__(self):
        
        return str(self)

    #------------------------------------------------------------------------------------------
    def __getitem__(self, prop):
        
        return self.getv(prop)

    #------------------------------------------------------------------------------------------
    def __setitem__(self, prop, valor):
        
        return self.setv(prop, valor)

    #------------------------------------------------------------------------------------------
    def claves(self):
        
        return self._datos.keys()

    #------------------------------------------------------------------------------------------
    def copia(self):
        
        reg = Registro()
        for (k, v) in self._datos.items():
            reg.setv(k, v)
        
        return reg

    #------------------------------------------------------------------------------------------
    def existe_clave(self, prop):
        
        prop = prop.lower()
        return prop in self._datos

    #------------------------------------------------------------------------------------------
    def getv(self, prop, valor_default=None):
        
        prop = prop.lower()
        if self.existe_clave(prop):
            return self._datos[prop]
        else:
            return valor_default if valor_default is not None else self.valor_default
    
    #------------------------------------------------------------------------------------------
    def gets(self, prop):
        
        return str(self.getv(prop))
    
    #------------------------------------------------------------------------------------------
    def getn(self, prop, valor_default=None):
        
        try:
            val = self.getv(prop)
            fl = float(val)
        except:
            fl = valor_default if valor_default is not None else self.valor_default
        finally:
            return fl

    #------------------------------------------------------------------------------------------
    def getd(self, prop):
        
        try:
            d = Fecha(None)
            val = self.getv(prop)
            if type(val) == str:
                d = Fecha.DesdeString(val.replace(',', '/'), '%d/%m/%Y')
            elif type(val) == datetime.datetime:
                d = Fecha(val)
        except:
            d = None
        finally:
            return d

    #------------------------------------------------------------------------------------------
    def setv(self, prop, valor):
        
        prop = prop.lower()
        self._datos[prop] = valor
    
    #------------------------------------------------------------------------------------------
    def setv_si_clave_vacia(self, prop, valor):
        
        prop = prop.lower()
        if not self.existe_clave(prop) or self.valor_vacio(prop):
            self._datos[prop] = valor

    #------------------------------------------------------------------------------------------
    def setv_si_valor_no_vacio(self, prop, valor):
        
        prop = prop.lower()
        if valor.strip():
            self._datos[prop] = valor

    #------------------------------------------------------------------------------------------
    def valor_vacio(self, prop):
        
        prop = prop.lower()
        return not str(self.getv(prop)).strip()

    #------------------------------------------------------------------------------------------
    def valor_numerico(self, prop, entero=False):
        
        val = self.getv(prop)
        if entero:
            return int(float(val)) if len(val) else self.valor_default
        else:
            return float(val) if len(val) else self.valor_default

