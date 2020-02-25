import datetime
import os

from horno.datos.Encoding import Encoding
from horno.datos.TiposDeDatos import DatoStr
from horno.datos.bd import dbfonpy
from horno.utiles.CSV import CSVEscritor
from horno.utiles.IO import IOSistema
from horno.utiles.Metricas import Progreso
import xlrd

import pyodbc


#=============================================================================================
class CxBase (object):

    #------------------------------------------------------------------------------------------
    def __init__(self):
        
        ''

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        return None
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        return None

    #------------------------------------------------------------------------------------------
    def FuentesODBC(self, nombre):

        return pyodbc.dataSources().get(nombre, '')

    #------------------------------------------------------------------------------------------
    def RealizarQueries(self, queries):
        
        try:
            conn = self.Conexion()
            curs = self.Cursor(conn)

            progreso = Progreso(1, len(queries), 'Ejecutando Querys')
            
            for query in queries:
                
                curs.execute(query)
                
                if query.strip().upper().startswith('SELECT'): 
                    datos = curs.fetchall()
                    columnas = Encoding().NormalizarLista([ d[0] for d in curs.description ])
                    conn.commit()
                else:
                    datos = [];
                    columnas = [];
                    conn.commit()
                    
                progreso.Incrementar()
                
            curs.close()
            conn.close()
            
            return [columnas, datos, None]
            
        except Exception as e:
            return [None, None, '[EXCEPTION] ' + str(e)]

    #------------------------------------------------------------------------------------------
    def RealizarQuery(self, query):
        
        return self.RealizarQueries([query])

    #------------------------------------------------------------------------------------------
    def ArmarSelect(self, tabla):
        
        return 'SELECT * FROM [%s]' % (tabla)

    #------------------------------------------------------------------------------------------
    def ExportarCSV(self, archivo_csv_output, tabla='', gen_script=False, archivo_sql_output='', append=False):
        
        query_select = self.ArmarSelect(tabla) 
        [columnas, datos, result] = self.RealizarQuery(query_select)

        if columnas is None or datos is None:
            IOSistema().PrintLine('[ConexionBases] Warning: (%s) El query no arrojo ningun resultado' % (archivo_csv_output))
            IOSistema().PrintLine('[Result]: %s' % (result))
            columnas = []
            datos = []

        headerstruc = [DatoStr(c,True) for c in columnas]
        csvw = CSVEscritor(archivo_csv_output, headerstruc)
        csvw.EscribirDatos(datos)
        
        def format_comillas(nombre):
            if ' ' in nombre or '/' in nombre or nombre[0] in '1234567890-' or nombre.lower() in ['any']:
                return '"%s"' % (nombre)
            else:
                return nombre
        
        if gen_script:
            com_tabla = format_comillas(tabla) 
            if archivo_sql_output=='':
                archivo_sql_output = '%s.sql' % (archivo_csv_output)
            f = open(archivo_sql_output, 'a+' if append else 'w+')
            f.write('\n---------- %s ----------";' % (com_tabla))
            f.write('\nDROP TABLE IF EXISTS %s;' % (com_tabla))
            f.write('\nCREATE TABLE %s ();' % (com_tabla))
            for columna in columnas:
                com_columna = format_comillas(columna)
                f.write('\nALTER TABLE %s ADD COLUMN %s VARCHAR;' % (com_tabla, com_columna))
            f.write('\nSET CLIENT_ENCODING=\'LATIN1\';')
            f.write('\nCOPY %s FROM \'%s\' WITH DELIMITER \',\' CSV HEADER;' % (com_tabla, os.path.abspath(archivo_csv_output).replace('\\','/')))
            f.close()
        

#=============================================================================================
class CxBaseAccess (CxBase):

    #------------------------------------------------------------------------------------------
    def __init__(self, archivo_mdb_input):
        
        self._archivo = archivo_mdb_input

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        cs = 'DRIVER=%s;DBQ=%s;PWD=%s' % (self.FuentesODBC('MS Access Database'), self._archivo, '')
        return pyodbc.connect(cs)
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        return conexion.cursor()

    #------------------------------------------------------------------------------------------
    def RealizarQueries(self, queries):
    
        res = super(CxBaseAccess, self).RealizarQueries(queries)
        
        return res
    

#=============================================================================================
class CxBaseDBF (CxBase):

    #------------------------------------------------------------------------------------------
    def __init__(self, archivo_dbf_input):
        
        self._archivo = archivo_dbf_input

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        return dbfonpy.connect(self._archivo)
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        return conexion.cursor()
    
    #------------------------------------------------------------------------------------------
    def ExportarCSV(self, archivo_csv_output, tabla=''):
        
        CxBase.ExportarCSV(self, archivo_csv_output, 'dbf')
    
#=============================================================================================
class CxBaseExcel (CxBase):

    #------------------------------------------------------------------------------------------
    def __init__(self, archivo_xls_input, con_header=True):
        
        self._archivo = archivo_xls_input
        self._con_header = con_header

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        cs = 'DRIVER=%s;DBQ=%s;PWD=%s' % (self.FuentesODBC('Excel Files'), self._archivo, '')
        return pyodbc.connect(cs, autocommit=True)
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        return conexion.cursor()
    
    #------------------------------------------------------------------------------------------
    def ExportarCSV(self, archivo_csv_output, tabla=''):
        
        self._hoja_actual = tabla

        CxBase.ExportarCSV(self, archivo_csv_output, '"%s$"' % (tabla))
    
    #------------------------------------------------------------------------------------------
    def RealizarQuery(self, query, tabla=''):
    
        try:
            
            if tabla: self._hoja_actual = tabla
            
            # self.FuentesODBC('Excel Files')
            
            def tran(wb, sh, rownum):
                res = []
                for cell in sh.row(rownum):
                    try:
                        if cell.ctype == xlrd.XL_CELL_DATE:
                            val = datetime.datetime( *xlrd.xldate_as_tuple(cell.value, wb.datemode) )
                        elif cell.ctype == xlrd.XL_CELL_NUMBER and cell.value.is_integer():
                            val = int(cell.value)
                        elif cell.ctype == xlrd.XL_CELL_TEXT:
                            val = Encoding().NormalizarTexto(cell.value)
                        else:
                            val = cell.value
                    except Exception as e2:
                        val = '<ERROR_XLS>'
                    finally:
                        res.append(val)
                return res 
                
            wb = xlrd.open_workbook(self._archivo.Ruta())
            sh = wb.sheet_by_name(self._hoja_actual)

            columnas = []
            datos = []
            for rownum in range(sh.nrows):
                if rownum == 0 and self._con_header:
                    columnas = tran(wb, sh, rownum)
                else:
                    datos.append(tran(wb, sh, rownum))
        
            return [columnas, datos, '']
            
        except Exception as e:
            print 
            return [None, None, '[EXCEPTION] ' + str(e)]
