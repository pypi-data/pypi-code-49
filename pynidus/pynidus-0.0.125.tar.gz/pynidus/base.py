import os
from pynidus.clients import ElasticsearchClient, DatabaseClient, GCSClient
from pynidus.errors import ErrorLogger

class MLTBase:
    
    def __init__(self, **kwargs):
        
        es_config = kwargs.get('es_config')
        pg_config = kwargs.get('pg_config')
        gcs_config = kwargs.get('gcs_config')
        bugsnag_config = kwargs.get('bugsnag_config')

        # env = os.getenv('ENV')

        # if env:

        #     if os.getenv('ES_HOST'):
                
        #         es_config = {
        #             'HOST': os.getenv('ES_HOST'),
        #             'USER': os.getenv('ES_USER'),
        #             'PASSWORD': os.getenv('ES_PASSWORD')
        #         }

        #     if os.getenv('PG_HOST'):
                
        #         pg_config = {
        #             'HOST': os.getenv('PG_HOST'),
        #             'USER': os.getenv('PG_USER'),
        #             'PASSWORD': os.getenv('PG_PASSWORD'),
        #             'DATABASE': os.getenv('PG_DATABASE')
        #         }

        #     if os.getenv('BUCKET'):
                
        #         gcs_config = {
        #             'BUCKET': os.getenv('BUCKET')
        #         }

        #     if os.getenv('BUGSNAG_API_KEY'):

        #         bugsnag_config = {
        #             'API_KEY': os.getenv('BUGSNAG_API_KEY'),
        #             'RELEASE_STAGE': os.getenv('BUGSNAG_RELEASE_STAGE')
        #         }

        if es_config:
            self.es_client = ElasticsearchClient(es_config)

        if pg_config:
            self.pg_client = DatabaseClient(pg_config)

        if gcs_config:
            self.gcs_client = GCSClient(gcs_config)

        if bugsnag_config:
            self.error_logger = ErrorLogger(bugsnag_config)

        


