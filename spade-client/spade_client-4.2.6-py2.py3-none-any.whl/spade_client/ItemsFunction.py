#
# Module: ItemsFunction
#
# Description: A class that class binds a set of items to a function execution call.
#

from __future__ import print_function

DEBUG_SEPARATOR = '--------'
HEADERS = {'Content-Type': 'application/xml',
           'Accept': 'application/xml'}

import sys
sys.path.append('.')

# This code is needed is pyxml if installed
pyxml=None
index = 0
for p in sys.path:
    if -1 != p.find('pyxml'):
         pyxml = p
    index += 1
if None != pyxml:
    sys.path.remove(pyxml)

import xml.dom.minidom
import xml.etree.ElementTree as ET


def _eprint(*args, **kwargs):
    """Prints to standard error"""
    print(*args, file=sys.stderr, **kwargs)


from spade_client import Display, FatalError

def _check_status(url, r, expected):
    """Checks the return status of a request to a URL

    Keyword arguments:
    url      -- the URL to which the request was made
    r        -- the response to the request
    expected -- the expected response code
    """
    if expected == r.status_code:
        return
    elif 400 == r.status_code:
        raise FatalError('Application at "' + url  + '" can not process this request as it is bad', r.status_code, r.text)
    elif 401 == r.status_code:
        raise FatalError('Not authorized to execute commands for Application at "' + url, r.status_code, r.text)
    elif 404 == r.status_code:
        raise FatalError('Application at "' + url  + '" not found', r.status_code, r.text)
    raise FatalError('Unexpected status (' + str(r.status_code) + ') returned from "' + url  + '"', r.status_code, r.text)


class ItemsFunction:
    """
    This class binds a set of items to a function execution call.
    
    :param array items: the collection of items over which the function should be executed.
    """
    def __init__(self, session, xml = False):
        self.debug = xml
        self.session = session


    def debug_separator(self):
        _eprint(DEBUG_SEPARATOR)


    def _pretty_print(self, url, s, response = True):
        """Prints out a formatted version of the supplied XML

        :param str url: the URL to which the request was made.
        :param str s: the XML to print.
        :param bool response: True is the XML is the reponse to a request.
        """
        if self.debug:
            if None != url:
                if response:
                    _eprint('URL : Response : ' + url)
                else:
                    _eprint('URL : Request :  ' + url)
            _eprint(xml.dom.minidom.parseString(s).toprettyxml())
            self.debug_separator()


    def report(self, action):
        document = self._prepare_document()
        action_uri = action.find('uri').text
        self.__pretty_print(action_uri, ET.tostring(document), False)
        r = self.session.get(action_uri, data=ET.tostring(document), headers=HEADERS)
        _check_status(action_uri, r, 200)
        report = ET.fromstring(r.text)
        self.__pretty_print(action_uri, ET.tostring(report))
        Display.items_result(report, 'Results of ' + action.find('name').text)


    def command(self, action):
        if None == self.session:
            return
        document = self._prepare_document()
        action_uri = action.find('uri').text
        self._pretty_print(action_uri, ET.tostring(document), False)
        r = self.session.post(action_uri, data=ET.tostring(document), headers=HEADERS)
        _check_status(action_uri, r, 202)
        report = ET.fromstring(r.text)
        self._pretty_print(action_uri, ET.tostring(report))
        Display.items_result(report, 'Results of ' + action.find('name').text)
