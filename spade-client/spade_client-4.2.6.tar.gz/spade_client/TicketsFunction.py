#
# Module: TicketsFunction
#
# Description: A class that class binds a set of tickets to a function execution call.
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

class TicketsFunction(ItemsFunction):
    """
    This class binds a set of tickets to a function execution call.
    
    :param array tickets: the collection of tickets over which the function should be executed.
    """
    def __init__(self, tickets, session, xml = False):
        self.tickets = tickets
        ItemsFunction.__init__(self, session, xml)


    def _prepare_document(self):
        """
        Prepares a Tickets document contains the specified ticket identities
        """
        document = ET.Element('tickets')
        if None != self.tickets:
            for ticket in self.tickets:
                ticketElement = ET.Element('ticket')
                ticketElement.text = ticket
                document.append(ticketElement)
        return document
