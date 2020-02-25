
from horno.datos.bd.ConexionBases import CxBase


#=============================================================================================
class CxBasePostgres (CxBase):

    #------------------------------------------------------------------------------------------
    def __init__(self, params):
        
        self.params = params

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        import psycopg2
        return psycopg2.connect(
                                host=self.params['host'], 
                                port=self.params['port'], 
                                database=self.params['dbname'], 
                                user=self.params['user'], 
                                password=self.params['password'],
                                )
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        esquema = self.params.get('schema', 'public')

        cur = conexion.cursor()
        cur.execute('SET search_path TO %s;' % (esquema))
        return cur


#=============================================================================================
class CxBaseOracle (CxBase):

    #------------------------------------------------------------------------------------------
    def __init__(self, params):
        
        self.params = params

    #------------------------------------------------------------------------------------------
    def Conexion(self):

        cs = '%s/%s@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=%s)(PORT=%s)))(CONNECT_DATA=(SID=%s)))' \
                % (
                   self.params['user'], 
                   self.params['password'],
                   self.params['host'],
                   self.params['port'],
                   self.params['sid'],
                )
        import cx_Oracle
        return cx_Oracle.connect(cs)
        #return None
    
    #------------------------------------------------------------------------------------------
    def Cursor(self, conexion):

        import cx_Oracle
        return cx_Oracle.Cursor(conexion)
        #return None
        
    #------------------------------------------------------------------------------------------
    def ArmarSelect(self, tabla):
        
        return 'SELECT * FROM %s' % (tabla)

