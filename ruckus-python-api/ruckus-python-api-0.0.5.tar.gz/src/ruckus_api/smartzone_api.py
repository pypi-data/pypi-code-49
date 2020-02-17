import requests
from datetime import datetime
from urllib.parse import urljoin


from .base import SmartZoneBase


class SmartZoneClient(SmartZoneBase):
    '''
    Documentation: http://docs.ruckuswireless.com/smartzone/5.1.2/vsze-public-api-reference-guide-512.html#api-information

    Controller: https://n01.ruckus.cloud.mambowifi.com:8443
    '''
    ###### Convert DATETIME to TIMESTAMP mileseconds
    def ts_format(self, d):
        '''
            Convert to UNIX timestamp in ms
        '''
        return int(d.timestamp()*1000)

    def datetemp(self, date_range):
        a = int(date_range[0].timestamp()*1000)
        b = int(date_range[1].timestamp()*1000)
        date_range = (a, b)
        return date_range

########## LOGON SESSION
    def login(self):
        '''
        Use this API command to log on to the controller and acquire a valid logon session.
        '''
        url = self.endpoint('v8_2/session')
        json = {
                'username': self.username,
                'password': self.password
                }
        r = self.session.post(url, json=json)
        return print(r)

    def retrieve(self):
        '''
        Use this API command to retrieve information about the current logon session.
        '''
        url = self.endpoint('v8_2/session')
        r = self.session.get(url)
        # validação
        return r.json()

########## SESSION MANAGEMENT
    def sessionManagement(self):
        '''
        Use this API command to retrieve information about the current logon sessions.
        '''
        url = self.endpoint('v8_2/sessionManagement')
        r = self.session.get(url)
        # validação
        return r.json()

########## AP GROUP
    def apGroup_retrieve(self, ID, zoneId):
        '''
        Required: id and zoneid (Variable 'id' is 'ID' in this function)
        Use this API command to retrieve information about an AP group.
        '''
        url = self.endpoint('v8_2/rkszones/{}/apgroups/{}'.format(zoneId, ID))
        r = self.session.get(url)
        # validação
        return r.json()

    def apGroup_retrieveList(self, zoneId, index=None, listSize=None):
        '''
        Use this API command to retrieve the list of AP groups that belong to a zone.
        -
        Required: zoneid
        index: string (optional) - The index of the first entry to be retrieved. Default: 0
        listSize: string (optional) - The maximum number of entries to be retrieved. Default: 100
        '''
        data = {}
        if index is None:
            data['index'] = '0'
        else:
            data['index'] = index
        if listSize is None:
            data['listSize'] = '100'
        else:
            data['listSize'] = listSize
        url = self.endpoint('v8_2/rkszones/{}/apgroups'.format(zoneId))
        r = self.session.get(url, data=data)
        # validação
        return r.json()

    def accessPointConfiguration_retrieve(self, apMac):
        '''
        Use this API command to retrieve the configuration of an AP.
        -
        Required: apMac
        '''
        url = self.endpoint('v8_2/aps/{}'.format(apMac))
        r = self.session.get(url)
        # validação
        return r.json()

    def accessPointConfiguration_retrieveList(self, index=None, listSize=None, zoneId=None, domainId=None):
        '''
        Use this API command to retrieve the list of APs that belong to a zone or a domain.
        -
        Required: None
        index: string (optional) - The index of the first entry to be retrieved. Default: 0
        listSize: string (optional) - The maximum number of entries to be retrieved. Default: 100
        zoneId: string (optional) - Filter AP list by zone
        domainId: string (optional) - Filter AP list by domain. Default: current logon domain
        '''
        data = {}
        if index is None:
            data['index'] = '0'
        else:
            data['index'] = index
        if listSize is None:
            data['listSize'] = '100'
        else:
            data['listSize'] = listSize
        if zoneId is not None:
            data['zoneId'] = zoneId
        if domainId is not None:
            data['domainId'] = domainId
        url = self.endpoint('v8_2/aps')
        r = self.session.get(url, data=data)
        # validação
        return r.json()

    def accessPointOperation_retrieveOperationInformation(self, apMac):
        '''
        This API provide detailed AP status and configuration, therefore it was designed for single AP information retrieving. If you need to retrieve large number of ap states, please use “POST://query/ap” (refer to the “Query APs” section of the category “Access Point Operational”).
        -
        Required: apMac
        '''
        url = self.endpoint('v8_2/aps/{}/operational/summary'.format(apMac))
        r = self.session.get(url)
        # validação
        return r.json()

    def accessPointOperational_apPacketCapture(self, apMac):
        '''
        Required: apMac
        Use this API to get AP packet capture status
        '''
        url = self.endpoint('v8_2/aps/{}/apPacketCapture'.format(apMac))
        r = self.session.get(url)
        # validação
        return r.json()

    def accessPointOperational_RetrieveIndoormapList(self, filter_type, filter_value, date_range, search_type=None, search_value=None, attributes=None):
        '''
        Query indoorMap with specified filters. Please click the link for the usage of Query Criteria.
        Link: http://docs.ruckuswireless.com/smartzone/5.1.2/QueryCriteria.html
        -
        Required: filter_type and filter_value.
        Example:
        {
          "filters": [
            {
              "type": "DOMAIN",
              "value": "8b2081d5-9662-40d9-a3db-2a3cf4dde3f7"
            }
          ],
          "fullTextSearch": {
            "type": "AND",
            "value": ""
          },
          "attributes": [
            "*"
          ]
        }
        '''
        date_range = self.datetemp(date_range)
        json = self.filters_json(filter_type, filter_value, date_range[0], date_range[1], search_type, search_value, attributes)
        url = self.endpoint('v8_2/query/indoorMap')
        r = self.session.post(url, json=json)
        # validação
        return r.json()

    def accessPointOperational_queryAps(self, filter_type, filter_value, date_range, search_type=None, search_value=None, attributes=None):
        '''
        Query APs with specified filters Please click the link for the usage of Query Criteria.
        Link: http://docs.ruckuswireless.com/smartzone/5.1.2/QueryCriteria.html
        -
        Required: filter_type and filter_value.
        Example:
        {
          "filters": [
            {
              "type": "DOMAIN",
              "value": "8b2081d5-9662-40d9-a3db-2a3cf4dde3f7"
            }
          ],
          "fullTextSearch": {
            "type": "AND",
            "value": ""
          },
          "attributes": [
            "*"
          ]
        }
        '''
        date_range = self.datetemp(date_range)
        json = self.filters_json(filter_type, filter_value, date_range[0], date_range[1], search_type, search_value, attributes)
        url = self.endpoint('v8_2/query/ap')
        r = self.session.post(url, json=json)
        # validação
        return r.json()

########## WLAN GROUP
    def wlanGroup_retrieveList(self, zoneId, index=None, listSize=None):
        '''
        Use this API command to retrieve the list of WLAN groups within a zone.
        -
        Required: zoneId
        index: string (optional) - The index of the first entry to be retrieved. Default: 0
        listSize: string (optional) - The maximum number of entries to be retrieved. Default: 100
        '''
        url = self.endpoint('v8_2/rkszones/{}/wlangroups'.format(zoneId))
        data = {}
        if index is None:
            data['index'] = '0'
        else:
            data['index'] = index
        if listSize is None:
            data['listSize'] = '100'
        else:
            data['listSize'] = listSize
        r = self.session.get(url, data = data)
        # validação
        return r.json()

########## WLAN
    def wlan_retrieveList(self, zoneId, index=None, listSize=None):
        '''
        Use this API command to retrieve a list of WLANs within a zone.
        -
        Required: zoneId
        index: string (optional) - The index of the first entry to be retrieved. Default: 0
        listSize: string (optional) - The maximum number of entries to be retrieved. Default: 100
        '''
        url = self.endpoint('v8_2/rkszones/{}/wlans'.format(zoneId))
        data = {}
        if index is None:
            data['index'] = '0'
        else:
            data['index'] = index
        if listSize is None:
            data['listSize'] = '100'
        else:
            data['listSize'] = listSize
        r = self.session.get(url, data = data)
        # validação
        return r.json()

    def wlan_queryWlans(self, filter_type, filter_value, date_range, search_type=None, search_value=None, attributes=None):
        '''
        Query WLANs with specified filters. Please click the link for the usage of Query Criteria.
        Link: http://docs.ruckuswireless.com/smartzone/5.1.2/QueryCriteria.html
        -
        Required: filter_type and filter_value
        Example:
        {
          "filters": [
            {
              "type": "DOMAIN",
              "value": "8b2081d5-9662-40d9-a3db-2a3cf4dde3f7"
            }
          ],
          "fullTextSearch": {
            "type": "AND",
            "value": ""
          },
          "attributes": [
            "*"
          ]
        }
        '''
        date_range = self.datetemp(date_range)
        json = self.filters_json(filter_type, filter_value, date_range[0], date_range[1], search_type, search_value, attributes)
        url = self.endpoint('v8_2/query/wlan')
        r = self.session.post(url, json=json)
        # validação
        return r.json()

########## ACCESS POINT APP - FALTA VALIDAR**************************
    def accessPointAPP_retrieveTotalApCount(self, zoneId=None, domainId=None):
        '''
        Use this API command to retrieve the total AP count within a zone or a domain.
        -
        Required: zoneId or domainId
        zoneId: string (optional) - Filter AP total count by zone. Default: current logon domain
        domainId: string (optional) - Filter AP total count by domain. Default: current logon domain
        '''
        assert zoneId or domainId, "ERRO: zoneId or domainId is required."
        data = {}
        if zoneId is not None:
            data['zoneId'] =  zoneId
        if domainId is not None:
            data['domainId'] = domainId
        url = self.endpoint('v8_2/aps/totalCount')
        r = self.session.get(url, data=data)
        # validação
        return r.json()


########## WIRELESS CLIENT
    def wirelessClient_retrieveTotalClientCount(self, apMac):
        '''
        Required: apMac
        Use this API command to retrieve the total client count per AP.
        '''
        url = self.endpoint('v8_2/aps/{}/operational/client/totalCount'.format(apMac))
        r = self.session.get(url)
        # validação
        return r.json()

    def wirelessClient_queryClients(self, filter_type, filter_value, date_range, search_type=None, search_value=None, attributes=None):
        '''
        Query clients with specified filters. Please click the link for the usage of Query Criteria.
        Link: http://docs.ruckuswireless.com/smartzone/5.1.2/QueryCriteria.html
        -
        Required: filter_type, filter_value
        Example:
        {
          "filters": [
            {
              "type": "DOMAIN",
              "value": "8b2081d5-9662-40d9-a3db-2a3cf4dde3f7"
            }
          ],
          "fullTextSearch": {
            "type": "AND",
            "value": ""
          },
          "attributes": [
            "*"
          ]
        }
        '''
        date_range = self.datetemp(date_range)
        json = self.filters_json(filter_type, filter_value, date_range[0], date_range[1], search_type, search_value, attributes)
        url = self.endpoint('v8_2/query/client')
        r = self.session.post(url, json=json)
        # validação
        return r.json()

    def wirelessClient_historicalClient_gen(self, filter_type, filter_value, date_range):
        has_more = True
        page = 1
        while has_more:
            d = self.wirelessClient_historicalClient(
                    filter_type,
                    filter_value,
                    date_range,
                    page=page,
                    limit=1000)
            has_more = d.get('hasMore', False)
            page += 1
            for el in d.get('list', []):
                yield el

    def wirelessClient_historicalClient(self, filter_type, filter_value, date_range, page=1, limit=1000):
        '''
        Use this API command to retrive historical client. Please click the link for the usage of Query Criteria.
        Link: http://docs.ruckuswireless.com/smartzone/5.1.2/QueryCriteria.html
        -
        Required: filter_type and filter_value.
        Example:
        {
          "filters": [
            {
              "type": "DOMAIN",
              "value": "d0d495e1-de50-40e3-8d09-e4bbeb4b4722"
            }
          ]
        }
        '''
        json = {
                "filters": [
                    {
                    "type": filter_type,
                    "value": filter_value
                    }
                    ],
                "extraTimeRange": {
                    "start": self.ts_format(date_range[0]),
                    "end": self.ts_format(date_range[1]),
                    "interval": 0
                    },
                "page": page,
                "limit": limit,
                }
        url = self.endpoint('v8_2/query/historicalclient')
        r = self.session.post(url, json=json)
        # validação
        return r.json()

    def wirelessClient_disconnectClient(self, mac, apMac):
        '''
        Use this API command to disconnect client.
        -
        Required: mac and apMac
        Example:
        {
          "mac": "E8:99:C4:AD:7C:38",
          "apMac": "C0:8A:DE:24:FA:00"

        '''
        json = {
                    "mac": mac,
                    "apMac": apMac
                }
        url = self.endpoint('v8_2/clients/disconnect')
        r = self.session.post(url, json=json)
        # validação
        return r.json()
