from .sobjects import SObject
from .runtests import RunTests
from urllib.parse import quote


class Tooling:
    _CONNECTION = None
    sobjects = None
    runtests = None

    def __init__(self, conn):
        self._CONNECTION = conn
        self.sobjects = SObject(self._CONNECTION)
        self.runtests = RunTests(self._CONNECTION)

    def completions(self):
        print("Hello from the completions function")

    def execute_anonymous(self):
        print("Hello from the executeAnonymous function")

    def search(self):
        print("Hello from the search function")

    def query(self, query):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/query/?q='+quote(query)
        return self._CONNECTION.send_http_request(endpoint,
                                                  "GET",
                                                  self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])
