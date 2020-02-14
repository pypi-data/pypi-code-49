class PasesConfig(object):
    def __init__(self):
        # Columnas que soporta el reporte
        self.COLUMNS = ['genero', 'a_edad', 'flag_suscriptor', 'fecha_registracion']
        # Query para extraer los datos de la tabla de pases
        self.PASES_QUERY = '''SELECT * FROM hd_p_vw.vw_pase_usuario_bp WHERE p_id_usuario IN {}'''
        # Num de pases a filtrar en la IN CLAUSE en impala con el objetivo que no explote la consulta
        self.CHUNK_SIZE = 10000



class NavegacionConfig():
    def __init__(self):
        self.COLUMNS = ['day_partition', 'f_date', 'f_day', 'f_hour', 'f_minute', 'page_visit_header', 
        'page_visit_session_desc', 'page_view_sequence_num', 'sourcesite', 'pase_id', 'page_url', 'platform', 
        'browser_web', 'sist_oper_web', 'country', 'region', 'city', 'entry_type', 'content_id', 'origen', 
        'page_type', 'ns_lista_tags']

        self.MAIN_BROWSERS = ['chrome', 'firefox', 'safari']

        self.MAIN_OS = ['windows', 'android', 'ios', 'macintosh', 'otros']

        self.MAIN_ENTRY_TYPE = ['organic_search', 'social', 'referral', 'direct', 'agea mkt campañas mkt']
        
        self.MAIN_SECTIONS = ['deportes', 'fama', 'politica', 'mundo', 'ciudades', 'viste', 'espectaculos', 'sociedad',
                             'viajes', 'economia', 'fotografia', 'tecnologia', 'policiales', 'autos', 'zonales', 'opinion',
                             'buena-vida', 'entremujeres', 'cultura', 'brandstudio', 'new-york-times-international-weekly',
                             'rural']
        self.SESION = ['HOME', 'SUBHOME', 'TAGS']
        self.CONTENT = ['NOTA', 'MULTIMEDIA', 'GALERIA']
        self.DIARIO = ['GAMING', 'SERVICIOS']
        self.PAYWALL = ['OTROS']

        self.SUSCRIPTORES_QUERY = '''select p_id_usuario as pase_id, campania from hd_p_vw.vw_pase_usuario_bp 
                                     where to_date(fecha_alta_suscripcion) = '{}'
                                  '''

        self.NAVEGACION_QUERY = ''' select day_partition, f_date, f_day, f_hour, f_minute, page_visit_header, page_visit_session_desc, 
                                    page_view_sequence_num, sourcesite, pase_id, page_url, platform, browser_web, 
                                    sist_oper_web, country, region, city, entry_type, content_id, origen, page_type, ns_lista_tags 
                                    from hd_p_vw.vw_navegacion_analytics 
                                    where day_partition = '{}' 
                                    and dataset = 'Clarín' 
                                    and pase_id > 0 
                                    '''


class DbConfiguration(object):
    def __init__(self):
        self.impala_config = {'host': 'bda1agea04.agea.sa', 'port': 21050}

