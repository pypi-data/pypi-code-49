from xml.etree import ElementTree as ET
from functools import partial

import requests

OAI = "https://zenodo.org/oai2d"
OAI_NS = "http://www.openarchives.org/OAI/2.0/"
DATACITE_NS = "http://datacite.org/schema/kernel-3"


def qname(ns, lname):
    return '{%s}%s' % (ns, lname)


oai = partial(qname, OAI_NS)
datacite = partial(qname, DATACITE_NS)


class Metadata(object):
    def __init__(self, e):
        self.e = e

    @property
    def text(self):
        return self.e.text

    def __getitem__(self, item):
        return self.e.attrib[item]

    def __getattr__(self, item):
        if item.endswith('s'):
            return self.getall(item[:-1], parent=self.get(item).e)
        return self.get(item)

    @staticmethod
    def _path(lname):
        return './/{0}'.format(datacite(lname))

    def get(self, lname, parent=None):
        return Metadata((parent or self.e).find(self._path(lname)))

    def getall(self, lname, parent=None):
        return [Metadata(e) for e in (parent or self.e).findall(self._path(lname))]


class Record:
    def __init__(self, e):
        self.e = e
        self.identifier = self.e.find('.//{0}'.format(oai('identifier')))
        self.metadata = Metadata(self.e.find('.//{0}'.format(datacite('resource'))))

    @property
    def id(self):
        return self.identifier.text.split(':')[-1]

    @property
    def doi(self):
        return self.metadata.identifier.text

    @property
    def keywords(self):
        return [e.text for e in self.metadata.subjects]


class OAIXML:
    def __init__(self, xml):
        self.xml = ET.fromstring(xml)

    def __call__(self, lname, parent=None, method='find'):
        return getattr(parent or self.xml, method)('.//{0}'.format(oai(lname)))

    @property
    def resumption_token(self):
        return getattr(self('resumptionToken'), 'text', None)


def request(**params):
    return OAIXML(requests.get(OAI, params=params).text)


class Records(list):
    def __init__(self, community):
        self.community = community
        res = request(
            set='user-{0}'.format(community), metadataPrefix='oai_datacite', verb='ListRecords')
        recs = res('record', method='findall')
        while res.resumption_token:
            res = request(verb='ListRecords', resumptionToken=res.resumption_token)
            recs.extend(res('record', method='findall'))
        list.__init__(self, [Record(e) for e in recs])
