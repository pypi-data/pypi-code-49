import pandas as pd
import numpy as np
from datetime import datetime
from ..config import Configuration
from .helpers import PaseUsuarioBp

__all__ = ['Summary']

# Errores custom para gestionar el ingreso correcto de los datos
class DataException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class ColumnException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


# Clase a instanciar para poder generar el reporte
class Summary(object):
    def __init__(self, data):
        # Dataframe generado por la lista recibida o el dataframe original en el caso contrario
        self.data_frame = None

        # Atributos internos
        self._pases_id_list = []
        self._config = Configuration()

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
        elif isinstance(data, list):
            self._pases_id_list = data
            self.data_frame = self._download()
        else:
            raise DataException('El parámetro enviado no es un DataFrame, ni una lista de pases, es un {}.'
                                .format(type(data)))

        # Atributos de la clase que pueden ser accedidos por el usuario
        # Sexo
        self.count_men = None
        self.count_women = None
        # Paywall
        self.count_paywall = None
        self.count_not_paywall = None
        # Edad
        self.count_millennials = None
        self.count_x_generation = None
        self.count_boomers = None
        self.count_age_out_of_range = None
        # Antiguedad
        self.mean_month_old = None
        self.median_month_old = None
        self.std_month_old = None
        self.report = {}

        self._build()

    def _download(self):
        # En el caso de que no se reciba un dataframe pero si una lista, descargamos esa informaacion desde impala
        return PaseUsuarioBp().get_data(self._pases_id_list)

    def _build(self):
        """
        Genera el reporte de datos demográficos de los pases correspondientes.
        :return: Un data frame con el resumen de datos demográfico de los pases correspondientes.
        """
        self._parse_sex()
        self._parse_suscriptor()
        self._parse_age()
        self._parse_to_data_frame()

    def _parse_sex(self):
        # Generamos el dataframe agrupado por Género y se lo enviamos al inicializador de variables.
        sex_data_frame = self.data_frame.groupby(['genero']).size().reset_index(name='cantidad'). \
            pivot_table(columns='genero', values='cantidad')

        # Inicializamos las variables.
        try:
            self.count_men = sex_data_frame['Masculino']
        except KeyError:
            self.count_men = 0
        try:
            self.count_women = sex_data_frame['Femenino']
        except KeyError:
            self.count_women = 0

        # Construimos el reporte.
        self.report['masculino'] = self.count_men
        self.report['femenino'] = self.count_women

    def _parse_suscriptor(self):
        # Generamos el dataframe agrupapo por Suscriptor y se lo enviamos al inicializador de variables.
        paywall_data_frame = self.data_frame.groupby(['flag_suscriptor']).size().reset_index(name='cantidad'). \
            pivot_table(columns='flag_suscriptor', values='cantidad')

        # Inicializamos las variables.
        try:
            self.count_paywall = paywall_data_frame['Si']
        except KeyError:
            self.count_paywall = 0
        try:
            self.count_not_paywall = paywall_data_frame['No']
        except KeyError:
            self.count_not_paywall = 0

        # Construimos el reporte.
        self.report['suscriptor'] = self.count_paywall
        self.report['no_suscriptor'] = self.count_not_paywall

    def _parse_age(self):
        # Generamos el dataframe agrupapo por Edad y se lo enviamos al inicializador de variables.
        self.data_frame['age_generation'] = self.data_frame['a_edad'].apply(self.get_age_generation)
        age_data_frame = self.data_frame.groupby(['age_generation']).size().reset_index(name='cantidad'). \
            pivot_table(columns='age_generation', values='cantidad')

        # Inicializamos las variables.
        try:
            self.count_millennials = age_data_frame['Millennials']
        except KeyError:
            self.count_millennials = 0
        try:
            self.count_x_generation = age_data_frame['Generacion X']
        except KeyError:
            self.count_x_generation = 0
        try:
            self.count_boomers = age_data_frame['Boomers']
        except KeyError:
            self.count_boomers = 0
        try:
            self.count_age_out_of_range = age_data_frame['Fuera de rango']
        except KeyError:
            self.count_age_out_of_range = 0

        # Construimos el reporte.
        self.report['millennials'] = self.count_millennials
        self.report['generacion_x'] = self.count_x_generation
        self.report['boomers'] = self.count_boomers
        self.report['edad_fuera_rango'] = self.count_age_out_of_range

    def _parse_month_old(self):
        # Generamos una columna donde calculamos la antiguedad en meses de un pase_id.
        self.data_frame['month_old'] = self.data_frame['fecha_registracion'].astype('datetime64[ns]') \
            .apply(self.get_month_old)

        # Inicialiamos las variables
        self.mean_month_old = self.data_frame['month_old'].mean()
        self.median_month_old = self.data_frame['month_old'].median()
        self.std_month_old = self.data_frame['month_old'].std()

        # Construimos el reporte
        self.report['antiguedad_media'] = self.mean_month_old
        self.report['antiguedad_mediana'] = self.median_month_old
        self.report['antiguedad_desvio'] = self.std_month_old

    def _parse_to_data_frame(self):
        # Generamos el dataframe resumen de las variables definida.
        self.report = pd.DataFrame(self.report)

    @staticmethod
    def get_age_generation(age):
        """
        A partir de la edad recibida retornamos la generación a la que pertenece.
        :param age: Edad del pase_id.
        :return: Un string con la etiqueta de la clase a la que pertenece el pase_id.
        """
        if 17 <= age < 35:
            return 'Millennials'
        elif 35 <= age < 54:
            return 'Generacion X'
        elif 54 <= age < 100:
            return 'Boomers'
        else:
            return 'Fuera de rango'

    @staticmethod
    def get_month_old(date_registration):
        """
        A partir de la fecha de registración cuantos meses de antiguedad tiene el pase como registrado.
        :param date_registration: Fecha de registración del pase_id.
        :return: Un entero indicando la cantidad de meses de antiguedad del pase_id.
        """
        return round((datetime.now() - date_registration) / np.timedelta64(1, 'M'), 2)
