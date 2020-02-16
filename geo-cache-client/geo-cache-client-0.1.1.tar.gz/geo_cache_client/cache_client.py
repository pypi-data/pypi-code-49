import requests

class Cache:
    def __init__(self,
            name,
            api_host="localhost",
            db_host=None,
            port=5000):
        """Cache constructor.
        
        :param name: the name as a string of the cache you want to connect to.
        :param api_host: the IP address of the cache API. Defaults to "localhost".
        :param db_host: the IP address of the actual cache. If not set, it is handled by API.
        :param port: the port of the cache API, defaults to 5000
        """

        self.name = name
        self.api_host = api_host
        self.db_host = db_host
        self.port = port

        self.headers = {
            'content-type': 'application/json'
        }

    def set_closest_server(self, lat, lon):
        url = "http://{host}:{port}/api/closest/{lat}/{lon}".format(
            host=self.api_host,
            port=self.port,
            lat=lat,
            lon=lon)

        response = requests.get(url, headers=self.headers).json()
        if response.get("ip") != None:
            self.api_host = response["ip"]
            self.db_host = None

    def get(self, key):

        url = "http://{host}:{port}/api/{name}/{key}".format(
            host=self.api_host,
            port=self.port,
            name=self.name,
            key=key)
        params = {}

        if self.db_host:
            params["databaseHost"] = self.db_host

        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def set(self, key, value, cas=None):
        data = {
            "value": value
        }
        if cas is not None:
            data["cas"] = cas


        url = "http://{host}:{port}/api/{name}/{key}".format(
            host=self.api_host,
            port=self.port,
            name=self.name,
            key=key)
        params = {}

        if self.db_host:
            params["databaseHost"] = self.db_host
        
        response = requests.post(url, headers=self.headers, params=params, json=data)
        return response.json()