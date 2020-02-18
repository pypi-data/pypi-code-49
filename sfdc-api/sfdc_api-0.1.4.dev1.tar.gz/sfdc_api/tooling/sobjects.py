from json import dumps
"""
#Class: SObject
#   Purpose: This class serves as an abstraction of the SObject model within the Salesforce Tooling API
#       Wraps up all the calls to sobject portion of the tooling api
#TODO: Error handling and presentation
"""
class SObject:
    _CONNECTION = None
   
    """
    #Function: __init__
    #   Purpose: Constructor for SObject, passed in a Connection object reference, for the purpose of sending http requests
    """
    def __init__(self, conn):
        self._CONNECTION = conn
    
    """
    #Function: list_sobjects
    #   Purpose: Lists all available object under the SObject domain in the tooling API
    """
    def list_sobjects(self):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/sobjects/'
        return self._CONNECTION.send_http_request(endpoint, 'GET', self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])
    
    """
    #Function: create
    #   Purpose: Creates an sobject with the given information, receives a dictionary that serves as the body of the http request
    #   Receives: name- name of the sobject type, body - a dictionary of all fields required to create the new object
    """
    def create(self, name, body):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/sobjects/' + name + '/'
        return self._CONNECTION.send_http_request(endpoint, 'POST', self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'], dumps(body).encode('utf8'))

    """
    #Function: describe
    #   Purpose: describes a specific object in the TOOLING API
    #   Receives: name - name of tooling object to study, [detail]- optional flag, used to describe all fields associated with an object
    """
    def describe(self, name, detail=False):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/sobjects/' + name
        if detail:
            endpoint += '/describe/'
        else:
            endpoint += '/'
        return self._CONNECTION.send_http_request(endpoint, 'GET', self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])

    """
    #Function: get_by_id
    #   Purpose: gets a specific instance of an object and describes the associated fields
    """
    def get_by_id(self, name, id):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/sobjects/' + name + '/' + id + '/'
        return self._CONNECTION.send_http_request(endpoint, 'GET', '')
    
    """
    #Function: delete
    #   Purpose: deletes a specific instance of an object
    """
    def delete(self, name, id):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/sobjects/' + name + '/' + id + '/'
        return self._CONNECTION.send_http_request(endpoint, 'DELETE', self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])
    """
    #Function: update
    #   Purpose: used to update the fields associated with a specific object
    """
    def update(self, name, id, body):
        endpoint = self._CONNECTION.CONNECTION_DETAILS["instance_url"]+'/services/data/v43.0/tooling/sobjects/' + name + '/' + id + '/'
        return self._CONNECTION.send_http_request(endpoint, 'PATCH', self._CONNECTION.HTTPS_HEADERS['rest_authorized_headers'])