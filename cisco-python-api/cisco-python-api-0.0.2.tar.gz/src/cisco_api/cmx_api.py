import requests
from datetime import datetime
from urllib.parse import urljoin


from .base import CMXBase

class CMXClient(CMXBase):
    def activeClients(self, siteId):
        '''
        This API returns the active clients seen in the last 20 minutes.
        '''
        data = {
                'siteId': siteId
                }
        url = self._endpoint('api/presence/v1/clients')
        r = self.session.get(url, data=data)
        return r.json()

    #Passer By
    def sumPasserBy(self, siteId, date_range):
        '''
        This API returns the sum of passerby counts for each day in the specified date range.

        '''
        url = self._endpoint('api/presence/v1/passerby/total')
        return self._requestRange(self, url, siteId, date_range)

    #Access
    def access(self, siteId, date_range):
        '''
        This API returns the count of connected visitors seen on a given day. 
        '''
        date_range = self._formadate(date_range)
        url = self._endpoint('presence/v1/connected/count')
        return self._requestRange(self, siteId, date_range)

    def kpiSummary(self, url, site_id, date_range, date=''):
        '''
        This API returns the KPI summary for the given site and specified date or date range.
        '''
        url = self._endpoint('api/presence/v1/kpisummary')
        return self._requestRange(self, siteId, date_range)

     #Unique visitors
    def visitor(self, siteId, date_range, date=''):
        '''
        This API returns the count of unique visitors seen on a day or range of dates.
        '''
        url = self._endpoint('api/presence/v1/visitor/count')
        return self._requestRange(self, url, siteId, date_range)

    #Repeat Visitors
    def repeatVisitors(self, siteId, date_range):
        '''
        This API returns the count of repeat visitors seen on a given day or date range.
        '''
        url = self._endpoint('api/presence/v1/repeatvisitors/count')
        return self._requestRange(self, url, siteId, date_range)

    #Average navigation time 2/2
    def countVisitorsByDwell(self, siteId):
        '''
        This API returns the count of visitors categorized by dwell level seen on a given day or date range.
        '''
        url = self._endpoint('api/presence/v1/dwell/count')
        return self._requestRange(self, url, siteId, date_range)

