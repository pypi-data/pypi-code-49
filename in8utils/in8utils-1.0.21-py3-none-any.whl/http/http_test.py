import requests


class HttpClientForTesting:
    def __init__(self):
        self.__session = requests.session()
        self.__verb = None
        self.__url = None
        self.__data = None
        self.__json = None
        self.__headers = {}
        self.__proxies = None
        self.__status_code = -1
        self.__message = None
        self.__timeout = 600

    def get(self, url):
        self.__url = url
        self.__verb = "get"
        return self

    def post(self, url):
        self.__url = url
        self.__verb = "post"
        return self

    def data(self, data):
        self.__data = data
        return self

    def json(self, json):
        self.header("Content-Type", "application/json; charset=UTF-8")
        self.__json = json
        return self

    def header(self, key, value):
        self.__headers[key] = value
        return self

    def headers(self, headers):
        self.__headers = headers
        return self

    def proxies(self, proxies):
        self.__proxies = proxies
        return self

    def ensure(self, status_code, message):
        self.__status_code = status_code
        self.__message = message
        return self

    def timeout(self, timeout):
        self.__timeout = timeout
        return self

    def build(self) -> requests.Response:
        res = Response(self.__headers, self.__data if self.__data else self.__json)
        self.__clean()
        return res

    def __clean(self):
        self.__verb = None
        self.__url = None
        self.__data = None
        self.__json = None
        self.__headers = {}
        self.__proxies = None
        self.__status_code = -1
        self.__message = None
        self.__timeout = 600


class Response(object):
    def __init__(self, headers, data):
        self.headers = headers
        self.content = str(data)
        self.__data = data
    
    def json(self):
        return self.__data
