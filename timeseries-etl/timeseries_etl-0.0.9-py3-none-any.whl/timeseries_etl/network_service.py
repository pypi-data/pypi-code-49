"""
If this module evolves, it could be moved outside this project as a standalone tool
"""

import logging
from timeseries_etl.timeseries_etl import PostgresSqlDao


class NetworkService:
    """
    An interface that provide services to extract elements and information from a network
    It was originally implemented to concatenate information about the network to Waze events
    """

    def find_link_by_coords(self, long: float, lat: float, distance_lim: float):
        """
        Locate the links that are within a distance of a given point
        :param long:
        :param lat:
        :param distance_lim:
        """
        raise NotImplementedError("Should have implemented this")


class NetworkServicePostGis(NetworkService):
    """
    An implementation of the NetworkService interface that uses a PostGis database to extract the info
    It was originally implemented to concatenate information about the network to Waze events
    """

    def __init__(self, host: str, port: str, user: str, password: str, dbname: str, schema: str, table: str,
                 geom_field: str):
        """
        To create this service we need the info about the postgis connection and a geom_field representing the
        name of the geometric object in that table
        :param host:
        :param port:
        :param user:
        :param password:
        :param dbname:
        :param schema:
        :param table:
        :param geom_field:
        """
        self.conn_info = {
            'host': host,
            'port': str(port),  # convert to string as psycopg2 expects a string
            'user': user,
            'password': password,
            'database': dbname,
        }
        self.dao = PostgresSqlDao(host, port, user, password, dbname)
        self.schema = schema
        self.table = table
        self.geom_field = geom_field
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.INFO)
        logger_handler = logging.StreamHandler()
        self.log.addHandler(logger_handler)
        logger_handler.setFormatter(
            logging.Formatter('%(asctime)s [%(levelname)s] : [%(module)s:%(lineno)d]-%(name)s : %(message)s'))

    def find_link_by_coords(self, long: float, lat: float, distance_lim: float):
        """
        Locate the links that are within a distance of a given point
        :param long:
        :param lat:
        :param distance_lim:
        """
        self.log.debug("Searching closest item in the DB for long: {0} and lat {1}".format(long, lat))
        sql = "select ST_Distance(ST_SetSRID(ST_Makepoint({0}, {1}), 4326), r.{5}) as distance, r.* " \
              "from {3}.{4} as r " \
              "where ST_DWithin(ST_SetSRID(ST_Makepoint({0}, {1}), 4326), r.{5}, {2} ) " \
              "order by distance".format(long, lat, distance_lim, self.schema, self.table, self.geom_field)
        nearest_elements = self.dao.execute_query(sql)
        return nearest_elements


class NetworkServiceGLP(NetworkService):
    """
    To be implemented in case we want to use the network service
    """

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def find_link_by_coords(self):
        print("Searching into the GLP service: {0} and {1}".format(self.url, self.api_key))
