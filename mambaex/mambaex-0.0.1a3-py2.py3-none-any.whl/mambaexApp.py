from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from .helper.callername import callername

class MambaexApp (BaseHTTPRequestHandler):
    """
    A class for handling server instance
    """

    def __init__(self, name):
        caller = callername(1)
        if caller != 'mambaex.mambaexApps.MambaexApps.getOrCreateApp':
            raise Exception("Can't be create an object directly accessing this class")
        self.name = name
        self.appstack = []

    def get(self, path, callback):
        """
        Add the callback function defination to the stack of the GET method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'GET', 'path': path})
        return self
    def use(self, path, callback):
        """
        Add the callback function defination to the stack of the ALL method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': '*', 'path': path})
        return self
    def post(self, path, callback):
        """
        Add the callback function defination to the stack of the POST method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'POST', 'path': path})
        return self
    def put(self, path, callback):
        """
        Add the callback function defination to the stack of the PUT method of given path
        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'PUT', 'path': path})
        return self
    def patch(self, path, callback):
        """
        Add the callback function defination to the stack of the PATCH method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'PATCH', 'path': path})
        return self
    def delete(self, path, callback):
        """
        Add the callback function defination to the stack of the DELETE method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'DELETE', 'path': path})
        return self
    def do_GET(self):
        pass
    def do_POST(self):
        pass
    def do_DELETE(self):
        pass
    def do_PUT(self):
        pass
    def do_PATCH(self):
        pass
    def listen(self, port):
        """
        Start listening to port

        :param int port: A port at which it starts listening
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        return self
    def stop(self):
        """
        Use to stop listening
        
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        return self
