from horno.datos.Fechas import Fecha

#=============================================================================================
class Dato:
    
    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False):
        
        self._nombre = nombre
        self._nulo = nulo

    #------------------------------------------------------------------------------------------
    def Nombre(self):
        
        return self._nombre
    
    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        return None

    #------------------------------------------------------------------------------------------
    def ParsearSafe(self, texto, default=None):
        
        parseo = self.Parsear(texto)
        return parseo['res'] if parseo['valido'] else default

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return None
        
    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return None

#=============================================================================================
class DatoInt (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon_ent=0):
        
        Dato.__init__(self, nombre, nulo)
        self._lon_ent = lon_ent

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        try:
            if not str(texto).strip():
                return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

            fl = float(texto)
            if fl.is_integer():
                return {'valido':True, 'res':int(fl), 'error':''}
            else:
                return {'valido':False, 'res':texto, 'error':'["%s" != int]' % (texto)}
        
        except Exception as e:
            return {'valido':False, 'res':texto, 'error':'["%s" != int]' % (texto)}

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '%s' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        p = self.Parsear(dato)
        return str(p['res']).zfill(self._lon_ent)

#=============================================================================================
class DatoFlo (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon_ent=0, lon_dec=0, con_coma=False):
        
        Dato.__init__(self, nombre, nulo)
        self._lon_ent = lon_ent
        self._lon_dec = lon_dec
        self._con_coma = con_coma

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        try:
            if not str(texto).strip():
                return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

            fl = float(texto)
            return {'valido':True, 'res':fl, 'error':''}
        except Exception as e:
            return {'valido':False, 'res':texto, 'error':'["%s" != float]' % (texto)}

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '%s' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):

        try:
            fl = round(float(dato), self._lon_dec)
        except:
            fl = dato
        
        fl_txt = str(fl).split('.')
        ent = fl_txt[0]
        dec = fl_txt[1] if len(fl_txt) >= 2 else '0'
        return ent.zfill(self._lon_ent) + ('.' if self._con_coma else '') + dec[0:self._lon_dec].ljust(self._lon_dec, '0')

#=============================================================================================
class DatoStr (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon=0):
        
        Dato.__init__(self, nombre, nulo)
        self._lon = lon

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        texto = str(texto).strip()
        
        if not texto.strip():
            return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

        if self._lon == 0 or len(texto) <= self._lon:
            return {'valido':True, 'res':texto, 'error':''}
        else:
            return {'valido':False, 'res':texto[0:self._lon], 'error':'len("%s") > %s' % (texto, self._lon)}
        
    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '"%s"' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return str(dato).ljust(self._lon)[:self._lon]

#=============================================================================================
class DatoEnum (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, enums=[], lon=0):
        
        Dato.__init__(self, nombre, nulo)
        self._enums = enums
        self._lon = lon
        
    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        if not str(texto).strip():
            return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

        if texto.upper() in [ e.upper() for e in self._enums ]:
            return {'valido':True, 'res':texto, 'error':''}
        else:
            return {'valido':False, 'res':texto, 'error':'"%s" != %s' % (texto, str(self._enums))}

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '"%s"' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        l = self._lon if self._lon > 0 else len(max(self._enums, key=len))
        
        return str(dato).ljust(l)[:l]

#=============================================================================================
class DatoFec (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, es_edad=False, formato_in='%d/%m/%Y', formato_out='%d/%m/%Y'):
        
        Dato.__init__(self, nombre, nulo)
        self._es_edad = es_edad
        self._formato_in = formato_in
        self._formato_out = formato_out

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        if not str(texto).strip():
            return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

        fecha = Fecha.DesdeString(texto, self._formato_in)
        if not fecha.Date() is None:
            #fix para poder migrar si anios<15, se debe arreglar en tablas de input
            if self._es_edad and Fecha.Ahora().Anio() - fecha.Anio() < 15:
                fecha = Fecha.DesdeValores(1900, 1, 1)
                texto = fecha.AStringConFormatoDefault()
                 
            return {'valido':True, 'res':texto, 'error':''}
        else:
            return {'valido':False, 'res':texto, 'error':'"%s" != fecha (%s)' % (texto, self._formato_in)}

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '"%s"' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):

        lon = 8

        if self._nulo and not dato:
            return '0' * lon
        
        fecha_str = Fecha.DesdeString(dato, self._formato_in).AStringConFormato(self._formato_out)
        if self._nulo and not fecha_str: return ''.ljust(lon)
        if not self._nulo and not fecha_str: return ''.zfill(lon)
        return fecha_str

#=============================================================================================
class DatoFecAnio (DatoFec):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, es_edad=False, formato='%d/%m/%Y'):
        
        DatoFec.__init__(self, nombre, nulo, es_edad, formato)

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        struc = DatoFec.Parsear(self, texto)
        
        if struc['valido']:
            fecha = Fecha.DesdeString(struc['res'], self._formato)
            texto_anio = fecha.Anio()
            return {'valido':True, 'res':texto_anio, 'error':''}
        else:
            return struc

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '"%s"' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return str(dato)
    
#=============================================================================================
class DatoBool (DatoEnum):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False):
        
        DatoEnum.__init__(self, nombre, nulo, ['S', 'N'])
        
    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        if isinstance(texto, bool):
            texto = 'S' if texto == True else 'N'
        
        return DatoEnum.Parsear(self, texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return str(dato)

    #------------------------------------------------------------------------------------------
    @staticmethod
    def AString(dato):
        
        return DatoBool('bool', False).Parsear(dato)['res']

#=============================================================================================
class DatoAlfanum (Dato):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon=0):
        
        Dato.__init__(self, nombre, nulo)
        self._lon = lon

    #------------------------------------------------------------------------------------------
    def Parsear(self, texto):
        
        try:
            if not str(texto).strip():
                return {'valido':True, 'res':texto, 'error':''} if self._nulo else {'valido':False, 'res':texto, 'error':'nulo'} 

            fl = float(texto)
            return DatoInt('', self._nulo).Parsear(texto) 

        except Exception as e:
            return DatoStr('', self._nulo, self._lon).Parsear(texto)

    #------------------------------------------------------------------------------------------
    def Quotear(self, texto):
        
        return '%s' % (texto)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return str(dato).ljust(self._lon)
    
#=============================================================================================
class DatoDNI (DatoAlfanum):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon=15):
        
        DatoAlfanum.__init__(self, nombre, nulo, lon)

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
        
        return str(dato).ljust(self._lon)

#=============================================================================================
class DatoCuit (DatoInt):

    #------------------------------------------------------------------------------------------
    def __init__(self, nombre=None, nulo=False, lon=11, con_guion=False):
        
        DatoInt.__init__(self, nombre, nulo, lon)
        self._con_guion = con_guion

    #------------------------------------------------------------------------------------------
    def Serializar(self, dato):
    
        if self._nulo and not dato:
            return '0' * self._lon_ent

        cuit = str(dato).zfill(11)
        if self._con_guion: cuit = cuit[:2] + '-' + cuit[2:10] + '-' + cuit[10:]
        return cuit.zfill(self._lon_ent)
    
    #------------------------------------------------------------------------------------------
    def Validar(self, dato):
        
        serial = self.Serializar(dato)
        coefs = '54327654320'
        prefs_validos = [20, 23, 24, 27, 30, 33, 34, 50, 55]
        
        if len(serial.replace('-', '')) > 11:
            return False
        
        if int(serial[0:2]) not in prefs_validos:
            return False
        
        val1 = 0
        for n in range(len(coefs)): val1 += int(coefs[n]) * int(serial[n])
        val2 = (11 - val1 % 11) % 11
        return int(serial[-1]) == val2 
