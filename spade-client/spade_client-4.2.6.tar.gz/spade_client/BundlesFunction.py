#
# Module: BundlesFunction
#
# Description: A class that class binds a set of bundles to a function execution call.
#

from __future__ import print_function

import sys

# This code is needed is pyxml if installed
pyxml=None
index = 0
for p in sys.path:
    if -1 != p.find('pyxml'):
         pyxml = p
    index += 1
if None != pyxml:
    sys.path.remove(pyxml)

import xml.etree.ElementTree as ET


from spade_client import ItemsFunction

class BundlesFunction(ItemsFunction):
    """
    This class binds a set of bundles to a function execution call.
    
    :param array bundles: the collection of bundles over which the function should be executed.
    """
    def __init__(self, bundles, session, xml = False):
        self.bundles = bundles
        ItemsFunction.__init__(self, session, xml)


    def _prepare_document(self):
        """
        Prepares a Bundles document contains the specified bundle identities
        """
        document = ET.Element('bundles')
        if None != self.bundles:
            for bundle in self.bundles:
                bundleElement = ET.Element('bundle')
                nameElement = ET.Element('name')
                nameElement.text = bundle
                bundleElement.append(nameElement)
                document.append(bundleElement)
        return document
