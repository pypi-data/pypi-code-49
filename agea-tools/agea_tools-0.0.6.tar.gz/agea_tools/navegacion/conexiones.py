import ibis
from ..config import DbConfiguration


class Impala(object):
    def __init__(self):
        self._config = DbConfiguration()
        self._db_conn = ibis.impala.connect(self._config.impala_config['host'], self._config.impala_config['port'])

    def execute(self, query=None, limit=None, database=None):
        """
        Ejecuta la query en impala.
        :param query: Query a ejecutar.
        :param limit: Cantidad de registro que queremos recibir, por defecto es None.
        :param database: Base de datos a la cual pertenece la query, por defecto es None.
        :return: Un data frame con los resultados de la query ejecutada.
        """
        self._db_conn.database(database)
        return self._clean(self._db_conn.sql(query).execute(limit=limit))

    @staticmethod
    def _clean(df):
        df.columns = map(str.lower, df.columns)
        return df
