# This class serves as an intermediary between the Connection module and every other API module
# Basically just serves a driver for neater API interactions
# This class can further see improvement by providing handling for out of order execution
# Links objects together 
from sfdc_api.utils import Connection
from sfdc_api.tooling import Tooling
from sfdc_api.query import Query
from sfdc_api.metadata import Metadata
from sfdc_api.sobjects import Sobjects
from sfdc_api.wsdl import WSDL


class Session:
    # doesn't store much more than the actual classes, should probably store some more information
    connection = None
    tooling = None
    query = None
    metadata = None
    sobjects = None
    wsdl = None

    # def __init__(self, org_username, org_password, client_id, client_key, org_url):
    def __init__(self, username='', password='', client_key='', client_secret='', org_login_url='https://login.salesforce.com/', version=45.0):
        # initialize connection objects only
        self.connection = Connection(username=username, password=password, client_key=client_key, client_secret=client_secret, org_login_url=org_login_url, version=version)

    def login(self):
        login_response = self.connection.login()
        self.tooling = Tooling(self.connection)
        self.query = Query(self.connection)
        self.metadata = Metadata(self.connection)
        self.sobjects = Sobjects(self.connection)
        self.wsdl = WSDL(self.connection)
        return login_response

    def logout(self):
        self.connection.logout()
