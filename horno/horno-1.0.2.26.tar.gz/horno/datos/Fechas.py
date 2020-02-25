from datetime import timedelta
import datetime

import dateutil.parser


#=============================================================================================
class Fecha:

    #------------------------------------------------------------------------------------------
    def __init__(self, fecha):

        if type(fecha) is not datetime.datetime:
            self._fecha = datetime.datetime.max
        else:
            self._fecha = fecha

    #------------------------------------------------------------------------------------------
    def __cmp__(self, fecha):
        
        if self.get_val() < fecha.get_val():
            return -1
        elif self.get_val() > fecha.get_val():
            return 1
        else:
            return 0

    #------------------------------------------------------------------------------------------
    def __repr__(self):
        
        return str(self)

    #------------------------------------------------------------------------------------------
    def __str__(self):
        
        return self.to_human()

    #------------------------------------------------------------------------------------------
    def Anio(self):
        
        return self._fecha.year if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    def AnioCorto(self):
        
        return int(str(self.Anio())[:-2])
    
    #------------------------------------------------------------------------------------------
    def Mes(self):
        
        return self._fecha.month if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    def Dia(self):
        
        return self._fecha.day if not self._fecha is None else ''

    #------------------------------------------------------------------------------------------
    @staticmethod
    def Ahora():
        
        return Fecha(datetime.datetime.now())

    #------------------------------------------------------------------------------------------
    @staticmethod
    def Hoy():

        return Fecha.Ahora().get_date()         

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeIso(fecha_iso, default=None):
        
        try:
            date = dateutil.parser.parse(fecha_iso)
        except Exception as e:
            date = default
        finally:
            return Fecha(date)

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeUnix(fecha_unix, default=None):
        
        try:
            date = datetime.datetime.utcfromtimestamp(int(fecha_unix)/1000)
        except Exception as e:
            date = default
        finally:
            return Fecha(date)

    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeValores(ano, mes, dia):
        
        return Fecha.DesdeString( '%s-%s-%s' % (ano, mes, dia), '%Y-%m-%d' )
    
    #------------------------------------------------------------------------------------------
    @staticmethod
    def DesdeString(fecha_str, formato, date_default=None):
        
        try:
        
            fecha_str_norm = fecha_str.strip().upper().replace('/','-').split(' ')[0]
            formato = formato.replace('/','-').split(' ')[0]
            
            if not fecha_str_norm:
                return Fecha( date_default )

            if formato in [ '%d-%b-%Y', '%d-%m-%Y' ]:
                [dia,mes,ano] = fecha_str_norm.split('-') 
            elif formato in [ '%Y-%m-%d' ]: 
                [ano,mes,dia] = fecha_str_norm.split('-')
            elif formato in [ '%Y%m%d' ]:
                ano = fecha_str_norm[0:4]; mes = fecha_str_norm[4:6]; dia = fecha_str_norm[6:8]
            else:
                raise Exception('Fecha: Formato no reconocido')
            
            if formato in ['%d-%b-%Y']:
                mes_numero = {'ENE':1,'JAN':1,'FEB':2,'MAR':3,'ABR':4,'APR':4,'MAY':5,'JUN':6,'JUL':7,'AGO':8,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DIC':12,'DEC':12}
                mes = str(mes_numero[mes])
    
            if len(ano) < 4:
                ano = str((2000 if int(ano) <= Fecha.Ahora().AnioCorto() else 1900) + int(ano))
                
            if int(ano) < 1900:
                ano = '1900'
            
            return Fecha( datetime.datetime.strptime('%s-%s-%s' % (dia.zfill(2), mes.zfill(2), ano.zfill(4)), '%d-%m-%Y') )
            
        except Exception as e:
            return Fecha( date_default )

    #------------------------------------------------------------------------------------------
    def AStringConFormato(self, formato):
        
        if self._fecha is None:
            return ''
        else:
            return self._fecha.strftime(formato)

    #------------------------------------------------------------------------------------------
    def AStringConFormatoDefault(self):
        
        return self.AStringConFormato('%d/%m/%Y')

    #------------------------------------------------------------------------------------------
    def to_iso(self):
        
        return self._fecha.isoformat()

    #------------------------------------------------------------------------------------------
    def to_unix(self):
        
        return int(self._fecha.timestamp()*1000)

    #------------------------------------------------------------------------------------------
    def to_human(self, formato_out='%a %d %b %Y, %H:%M'):
        
        weekday = {'sun': 'dom', 'mon': 'lun', 'tue': 'mar', 'wed': 'mie', 'thu': 'jue', 'fri': 'vie', 'sat': 'sab'}
        month = {'jan': 'ene', 'feb': 'feb', 'mar': 'mar', 'apr': 'abr', 'may': 'may', 'jun': 'jun',
                 'jul': 'jul', 'aug': 'ago', 'sep': 'sep', 'oct': 'oct', 'nov': 'nov', 'dec': 'dic'}

        fecha_orig = self._fecha.strftime(formato_out)
        try:
            fecha_part = fecha_orig.split(' ')
            fecha_part[0] = weekday.get(fecha_part[0].lower(), fecha_part[0].lower()) 
            fecha_part[2] = month.get(fecha_part[2].lower(), fecha_part[2].lower())
            return ' '.join(fecha_part)
        except:
            return fecha_orig

    #------------------------------------------------------------------------------------------
    def add_delta(self, **kwargs):
        
        return Fecha(self._fecha + timedelta(**kwargs))

    #------------------------------------------------------------------------------------------
    def get_val(self):
        
        return self._fecha

    #------------------------------------------------------------------------------------------
    def get_date(self):

        return Fecha(datetime.datetime(self.get_val().year, self.get_val().month, self.get_val().day))

    #------------------------------------------------------------------------------------------
    def set_date(self, **kwargs):
        
        return Fecha(self._fecha.replace(**kwargs))

    #------------------------------------------------------------------------------------------
    def diff(self, fecha):
        
        return abs(self._fecha - fecha._fecha)

    #------------------------------------------------------------------------------------------
    def is_past_now(self):
        
        return self._fecha.timestamp() < Fecha.Ahora().get_val().timestamp()

    #------------------------------------------------------------------------------------------
    def is_past_today(self):
        
        return self._fecha.date() < Fecha.Hoy().get_val().date()
