import requests

class Client():
    def __init__(self, url, headers=None, verify=True, **kwargs):
        self.url = url
        self.headers = headers
        self.verify=verify
        self.kwargs = kwargs

    def execute(self, query):
        """execute query
        """
        if not self.verify:
            requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)
        response = requests.post(self.url, headers=self.headers, verify=self.verify, json=query, **self.kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error when connecting to graphql service")
