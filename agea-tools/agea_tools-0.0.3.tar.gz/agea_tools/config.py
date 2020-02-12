class Configuration(object):
    def __init__(self):
        # Columnas que soporta el reporte
        self.COLUMNS = ['genero', 'a_edad', 'flag_suscriptor', 'fecha_registracion']
        # Query para extraer los datos de la tabla de pases
        self.PASES_QUERY = '''SELECT * FROM hd_p_vw.vw_pase_usuario_bp WHERE p_id_usuario IN {}'''
        # Num de pases a filtrar en la IN CLAUSE en impala con el objetivo que no explote la consulta
        self.CHUNK_SIZE = 10000


class DbConfiguration(object):
    def __init__(self):
        self.impala_config = {'host': 'bda1agea04.agea.sa', 'port': 21050}

