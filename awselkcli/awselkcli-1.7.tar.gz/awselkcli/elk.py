from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3


class ELK:
    def __init__(self, host, region):
        self.host = host
        self.region = region
        self.client = self._login()

    def _login(self):
        credentials = boto3.Session().get_credentials()

        awsauth = AWS4Auth(credentials.access_key,
                           credentials.secret_key,
                           self.region,
                           "es",
                           credentials.token)

        es = Elasticsearch(
            hosts=[{'host': self.host, 'port': 443}],
            http_auth=awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        return es

    def logger(self, body, index, type="log"):
        self.client.index(index=index,
                          body=body,
                          doc_type=type)
