from datetime import date, datetime, timedelta
from functools import reduce, partial
from operator import is_not
import pandas as pd
import numpy as np
from datetime import datetime
from ..config import NavegacionConfig
from .helpers import PaseUsuarioBp, DataException, ColumnException, PaseSuscriptores, NavegacionPases
from .standardizing import NavegationColumns



# Clase a instanciar para poder generar el reporte
class HabitosNavegacion():
    def __init__(self, data):       

        # Atributos internos
        self._date = []
        self._config = NavegacionConfig()
        self._standardizing = NavegationColumns()
        self._lista_dataframes = []

        # Dataframe generados por la lista recibida o el dataframe original en el caso contrario
        self.data_frame = pd.DataFrame()
        self.data_frame_sesiones = pd.DataFrame()
        self.data_frame_content = pd.DataFrame()
        self.data_frame_diario = pd.DataFrame()
        self.data_frame_paywall = pd.DataFrame()
        self.data_frame_especiales = pd.DataFrame()

        """
        Validamos que la información enviada sea un dataframe con las columnas correspondiente o una lista con 
        los pases_id.
        """
        if isinstance(data, pd.DataFrame):
            self.data_frame = data
            result = all(col in self.data_frame.columns for col in self._config.COLUMNS)
            if not result:
                raise ColumnException(
                    'El dataframe enviado no tiene las columnas necesarias para generar la información '
                    'correspondiente.')
        elif isinstance(data, str):
            self._date = data
            self.data_frame = self._download()
        else:
            raise DataException('El parámetro enviado no es un DataFrame, ni una lista de pases, es un {}.'
                                .format(type(data)))

        
        self._standardizing_columns(self.data_frame)
        self._fill_data_frames()
        self.features_navegacion = pd.DataFrame()
        self._build()

    def _download(self):
        # En el caso de que no se reciba un dataframe pero si una lista, descargamos esa informacion desde impala
        return NavegacionPases().get_data(self._date)

    def _build(self):
        # Generamos el dataframe de habitos en base a la navegacion de cada usuario registrado
        # Generamos una lista de dataframes con los diferentes features
        self._build_sesion_features()
        self._build_hardware_features()
        self._build_location_features()
        self._build_primer_ingreso_features()
        self._build_ultimo_ingreso_features()
        self._build_ingresos_home_features()
        self._build_ingresos_servicios_features()
        self._build_ingresos_content_features()
        self._build_ingresos_especiales_features()
        self._build_ingresos_seccion_features()
        self._build_choques_features()
        self._build_ofertas_features()
        self._build_suscriptores_feature()
        # Iteramos la lista de dataframe, mergeamos por pase_id y devolvemos el dataframe final
        self._lista_dataframes = list(filter(partial(is_not, None), self._lista_dataframes))
        self.features_navegacion = reduce(lambda x, y: pd.merge(x, y, on = 'pase_id', how='outer'), self._lista_dataframes).fillna(0)
        self.features_navegacion['day_partition'] = self._date
        self.features_navegacion['dia_habil'] = self.features_navegacion['day_partition'].astype('datetime64[ns]').apply(self._get_habil)

    def _add_features(self, features):
        # Agregamos un elemento a la lista
        self._lista_dataframes.append(features)

    def _build_sesion_features(self):
        # Generamos los features correspondiente a la cantidad de sesiones y secuencias
        sesiones = self.data_frame.groupby(['pase_id', 'page_visit_session_desc']).size().reset_index(name='cantidad_secuencia')
        sesiones = sesiones.groupby(['pase_id']).agg({'page_visit_session_desc': 'size', 'cantidad_secuencia': sum}) \
                                                          .reset_index().rename(columns={'page_visit_session_desc': 'cantidad_sesiones'})
        self._add_features(sesiones)
    
    def _build_hardware_features(self):
        # Generamos los features que tienen que ver con el hardware, los calculos son por sesiones
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'platform', franja=False))
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'sist_oper_web', franja=False))
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'entry_type', franja=False))
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'f_franja'))
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'platform', franja=True))
        self._add_features(self._build_hardware_data_frame(self.data_frame, 'entry_type', franja=True))

    def _build_location_features(self):
        # Generamos los features de ubicacion del usuario al momento de ingresar
        self._add_features(self._build_location_mode_data_frame(self.data_frame, 'country'))
        self._add_features(self._build_location_mode_data_frame(self.data_frame, 'city'))

    def _build_primer_ingreso_features(self):
        # Generamos un feature que indica la hora del dia del primer ingreso
        primera_visita = self.data_frame.groupby(['pase_id'])['f_hour'].min().reset_index(name='hora_primera_visita')
        self._add_features(primera_visita)

    def _build_ultimo_ingreso_features(self):
        # Generamos un feature que indica la hora del dia del ultimo ingreso
        ultima_visita = self.data_frame.groupby(['pase_id'])['f_hour'].max().reset_index(name='hora_ultima_visita')
        self._add_features(ultima_visita)

    def _build_ingresos_home_features(self):
        # Generamos features contabilizando los ingresos a la home, y tambien lo abrimos por franja y plataforma
        self._add_features(self._build_pivot_table(self._build_home_data_frame(self.data_frame_sesiones), 'page_type'))
        self._add_features(self._build_pivot_table(self._build_home_data_frame(self.data_frame_sesiones, 'f_franja'), 'page_type', extra='f_franja'))
        self._add_features(self._build_pivot_table(self._build_home_data_frame(self.data_frame_sesiones, 'platform'), 'page_type', extra='platform'))

    def _build_ingresos_servicios_features(self):
        # Generamos features contabilizando los ingresos a los servicios y al gaming de clarin
        diario = self.data_frame_diario.groupby(['pase_id', 'page_type']).size().reset_index(name='cantidad')
        diario_franja = self.data_frame_diario.groupby(['pase_id', 'f_franja', 'page_type']).size().reset_index(name='cantidad')
        diario_platform = self.data_frame_diario.groupby(['pase_id', 'platform', 'page_type']).size().reset_index(name='cantidad')
        self._add_features(self._build_pivot_table(diario, 'page_type'))
        self._add_features(self._build_pivot_table(diario_franja, 'page_type', extra='f_franja'))
        self._add_features(self._build_pivot_table(diario_platform, 'page_type', extra='platform')) 

    def _build_ingresos_content_features(self):
        # Generamos features contabilizando los ingresos a la notas, y tambien lo abrimos por franja y plataforma
        self._add_features(self._build_pivot_table(self._build_notas_data_frame(self.data_frame_content), 'page_type'))
        self._add_features(self._build_pivot_table(self._build_notas_data_frame(self.data_frame_content, 'f_franja'), 'page_type', extra='f_franja'))
        self._add_features(self._build_pivot_table(self._build_notas_data_frame(self.data_frame_content, 'platform'), 'page_type', extra='platform'))

    def _build_ingresos_especiales_features(self):
        # Generamos features contabilizando los ingresos a los especiales, y tambien lo abrimos por franja
        self._add_features(self._build_pivot_table(self._build_notas_data_frame(self.data_frame_especiales), 'page_type'))
        self._add_features(self._build_pivot_table(self._build_notas_data_frame(self.data_frame_especiales, 'f_franja'), 'page_type', extra='f_franja'))

    def _build_ingresos_seccion_features(self):
        # Generamos features contabilizando los ingresos a la secciones, y tambien lo abrimos por franja y plataforma
        self._add_features(self._build_pivot_table(self._build_seccion_data_frame(self.data_frame_content), 'sourcesite'))
        self._add_features(self._build_pivot_table(self._build_seccion_data_frame(self.data_frame_content, 'f_franja'), 'sourcesite', extra='f_franja'))

    def _build_choques_features(self):
        # Generamos features contabilizando la cantidad de choques del dia
        landing = self.data_frame_paywall.loc[self.data_frame_paywall['sourcesite'] == 'clarin-paywall']
        chocadores = landing.groupby(['pase_id']).size().reset_index(name='cantidad_choques')
        self._add_features(chocadores)

    def _build_ofertas_features(self):
        # Generamos features contabilizando la cantidad de ingresos a secciones del pago de paywall
        ofertas = self.data_frame_paywall.loc[self.data_frame_paywall['sourcesite'] == 'clarin365']
        ofertas = ofertas.loc[~ofertas['page_url'].str.contains('app|desa|prepro|test|frontend|bienvenid|autogestion|sitio1', regex=True)]
        ofertas = ofertas.loc[ofertas['page_url'].str.contains('datospersonales|formasdepago', regex=True)]
        ofertas.loc[ofertas['page_url'].str.contains('datospersonales'), 'page_url'] = 'pago_datospersonales'
        ofertas.loc[ofertas['page_url'].str.contains('formasdepago'), 'page_url'] = 'pago_formasdepago'
        ofertas = ofertas.groupby(['pase_id', 'page_visit_session_desc', 'page_url']).size().reset_index(name='cantidad')
        ofertas = ofertas.groupby(['pase_id', 'page_url']).size().reset_index(name='cantidad').sort_values('pase_id')
        self._add_features(self._build_pivot_table(ofertas, 'page_url'))

    def _build_suscriptores_feature(self):
        self._date = self.data_frame['day_partition'].max()
        pases_altas =  PaseSuscriptores().get_data(self._date)
        pases_altas['convirtio'] = 1
        self._add_features(pases_altas)

    # Funciones para generar, limpiar y estandarizar los diferentes dataframe
    def _standardizing_columns(self, df):
        # Hacemos el primer procesamiento al dataframe recibido.        
        self.data_frame['f_franja'] = self.data_frame['f_hour'].apply(self._get_franja_horaria)
        self.data_frame = self._standardizing.standardizing_browser(self.data_frame)
        self.data_frame = self._standardizing.standardizing_entry_type(self.data_frame)
        self.data_frame = self._standardizing.standardizing_so(self.data_frame)    

    def _fill_data_frames(self):
        # Separamos el dataframe en difentes tipos que luego seran utilizados para contabilizar
        self.data_frame_sesiones = self.data_frame.loc[self.data_frame['page_type'].isin(self._config.SESION)]
        self.data_frame_content = self.data_frame.loc[self.data_frame['page_type'].isin(self._config.CONTENT)]
        self.data_frame_diario = self.data_frame.loc[self.data_frame['page_type'].isin(self._config.DIARIO)]
        self.data_frame_paywall = self.data_frame.loc[self.data_frame['page_type'].isin(self._config.PAYWALL)]
        self.data_frame_especiales = self.data_frame_content.loc[self.data_frame_content['ns_lista_tags'].str.contains('Especial|especial')]
        self.data_frame = self.data_frame.loc[~self.data_frame['page_type'].isin(self._config.PAYWALL)]
        self.data_frame_especiales['sourcesite'] = 'especiales'
        self.data_frame_especiales['page_type'] = 'ESPECIAL'
        self.data_frame_content['sourcesite'] = self.data_frame_content['page_url'].apply(self._get_seccion)
        self.data_frame_content = self._standardizing.standardizing_sourcesite(self.data_frame_content)

    # Funciones para generar las agrupaciones necesarias que luego se transformaran en features
    def _build_hardware_data_frame(self, df, column=None, franja=False):
        '''
        Esta funcion recibe el dataframe y una columna especifica relacionada con el hardware.
        Agrupamos por cada usuario y por la columna recibida contabilizando la cantidad de sesiones
        realizadas con esta caracteristica.
        En el caso de que franja=True, realizamos otra particion por franja horaria.
        '''
        group_fields = ['pase_id', 'page_visit_session_desc', column]
        if franja:
            group_fields.append('f_franja')
            
        result = df.groupby(group_fields).size().reset_index(name='cantidad')        
        group_fields.remove('page_visit_session_desc')        
        result = result.groupby(group_fields).size().reset_index(name='cantidad')
        
        if franja:
            result[column] = 'sesiones' + '_' + result['f_franja'] + '_' + result[column]
        else:
            result[column] = 'sesiones' + '_' + result[column]
        
        result = result.pivot_table(index='pase_id', columns=column, values='cantidad').fillna(0).reset_index()
        result.columns.name = None
        
        return result

    def _build_location_mode_data_frame(self, df, column):
        # Retornamos el valor mas frecuente de la columna especificada.
        result = df.groupby(['pase_id', 'page_visit_session_desc', column]).size().reset_index(name='cantidad')
        result = result.groupby(['pase_id'])[column].agg(lambda x: pd.Series.mode(x).iat[0]).reset_index(name='moda_{}'.format(column))
        return result

    def _build_home_data_frame(self, df, column=None):
        '''
        Recibe el dataframe y la columna a agrupar. La contabilizacion esta hecha en base a las sesiones.
        No devuelve una linea por usuario, para obtener este resultado utilizar la pivot table.
        '''
        groupby_fields = ['pase_id', 'page_visit_session_desc', 'sourcesite', 'page_type']

        if column is not None:
            groupby_fields.append(column)

        result = df.groupby(groupby_fields).size().reset_index(name='cantidad')
        groupby_fields.remove('page_visit_session_desc')
        result = result.groupby(groupby_fields).size().reset_index(name='cantidad')
        return result

    def _build_notas_data_frame(self, df, column=None):
        '''
        Recibe el dataframe y la columna a agrupar. La contabilizacion esta hecha en base a los distintos content_id.
        No devuelve una linea por usuario, para obtener este resultado utilizar la pivot table.
        '''
        groupby_fields = ['pase_id', 'page_type', 'content_id']

        if column is not None:
            groupby_fields.append(column)

        result = df.groupby(groupby_fields).size().reset_index(name='cantidad')
        groupby_fields.remove('content_id')
        result = result.groupby(groupby_fields).size().reset_index(name='cantidad')
        return result
        
    def _build_seccion_data_frame(self, df, column=None):
        '''
        Recibe el dataframe y la columna a agrupar. La contabilizacion esta hecha en base a los content_id.
        No devuelve una linea por usuario, para obtener este resultado utilizar la pivot table.
        '''
        groupby_fields = ['pase_id', 'sourcesite', 'content_id']

        if column is not None:
            groupby_fields.append(column)

        result = df.groupby(groupby_fields).size().reset_index(name='cantidad')
        groupby_fields.remove('content_id')
        result = result.groupby(groupby_fields).size().reset_index(name='cantidad')
        return result
    
    def _build_pivot_table(self, df, column, extra=None):
        # Genera una linea por cada pase_id
        try:
            if extra is not None:
                df[column] = 'ingresos_' + df[extra] + '_' + df[column].str.lower()
            else:
                df[column] = 'ingresos_' + df[column].str.lower()
            df = df.pivot_table(index='pase_id', columns=column, values='cantidad').reset_index().fillna(0)
            df.columns.name = None
            return df
        except Exception:
            return None

    @staticmethod
    def _get_franja_horaria(hour):
        if 0 < hour <= 6:
            return 'madrugada'
        elif 6 < hour <= 12:
            return 'manana'
        elif 12 < hour <= 18:
            return 'tarde'
        else:
            return 'noche'

    @staticmethod
    def _get_seccion(url):
        import urllib.parse
        path = urllib.parse.urlparse(url).path
        return list(filter(None, path.split('/')))[1]

    @staticmethod
    def _get_habil(day_of_week):
        if day_of_week in (5, 6):
            return 0
        else:
            return 1
