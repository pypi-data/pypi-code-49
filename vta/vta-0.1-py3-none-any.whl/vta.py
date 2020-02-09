# -*- coding: utf-8 -*-
import os
import requests


__author__ = 'WOODONGGYU'
__copyrights__ = 'Copyright 2020 (C) WOODONGGYU. ALL RIGHTS RESERVED'
__credits__ = ['WOODONGGYU']
__license__ = ''
__maintainer__ = 'WOODONGGYU'
__email__ = 'mrwoo92@naver.com'
__status__ = 'developing'
__version__ = '1.0'
__date__ = '2020-02-09'
__updated__ = ''


class VTA:
    def __init__(self, apikey):
        self.__apikey = apikey
        self.base = 'https://www.virustotal.com/vtapi/v2/'

    def f_report(self, resource, allinfo=None):
        """Retrieve file scan reports"""

        # `allinfo` parameter validation
        if isinstance(allinfo, bool):
            if allinfo is True:
                allinfo = 'true'
            else:
                allinfo = None

        url = self.base + 'file/report'
        params = {
            'apikey': self.__apikey,
            'resource': resource,
            'allinfo': allinfo
        }
        return self._api_request('GET', url, params)

    def f_scan(self, file):
        """Upload and scan a file"""

        if not os.path.isfile(file):
            raise FileNotFoundError
        url = self.base + 'file/scan'
        files = {
            'file': (file, open(file, mode='rb'))
        }
        params = {
            'apikey': self.__apikey
        }
        return self._api_request('POST', url, params, files)

    def f_scan_bigfile(self, file):
        """Get a URL for uploading files larger than 32MB"""

        if not os.path.isfile(file):
            raise FileNotFoundError
        upload_url = self.base + 'file/scan/upload_url'
        params = {
            'apikey': self.__apikey
        }
        response = self._api_request('GET', upload_url, params)

        url = response['upload_url']
        files = {
            'file': (file, open(file, mode='rb'))
        }
        response = requests.post(url, files=files)
        if self._status_validation(response.status_code):
            return response.json()

    def f_rescan(self, resource):
        """Re-scan a file"""

        url = self.base + 'file/rescan'
        params = {
            'apikey': self.__apikey,
            'resource': resource
        }
        return self._api_request('POST', url, params)

    def f_download(self, hash, outfile=None):
        """Download a file"""

        url = self.base + 'file/download'
        params = {
            'apikey': self.__apikey,
            'hash': hash
        }
        response = requests.get(url, params=params)
        if self._status_validation(response.status_code):
            downloaded_file = response.content
        return self._download_file(hash, downloaded_file, outfile)

    def f_behavior(self, hash):
        """Retrieve behaviour report"""

        url = self.base + 'file/behaviour'
        params = {
            'apikey': self.__apikey,
            'hash': hash
        }
        return self._api_request('GET', url, params)

    def f_nt(self, hash, outfile=None):
        """Download a network-traffic(.pcap) file"""

        url = self.base + 'file/network-traffic'
        params = {
            'apikey': self.__apikey,
            'hash': hash
        }
        response = requests.get(url, params=params)
        if self._status_validation(response.status_code):
            downloaded_file = response.content
        return self._download_file(hash, downloaded_file, outfile)

    def f_clusters(self, date):
        """Retrieve file clusters"""

        url = self.base + 'file/clusters'
        params = {
            'apikey': self.__apikey,
            'date': date
        }
        return self._api_request('GET', url, params)

    def f_search(self, query, offset=None):
        """Search for files"""

        # `offset` parameter validation
        if offset is not None:
            if isinstance(offset, int):
                offset = offset
            else:
                offset = None

        url = self.base + 'file/search'
        params = {
            'apikey': self.__apikey,
            'query': query,
            'offset': offset
        }
        return self._api_request('GET', url, params)

    def u_report(self, resource, allinfo=None, scan=None):
        """Retrieve URL scan reports"""

        # `allinfo`, `scan` parameters validation
        if isinstance(allinfo, bool):
            if allinfo is True:
                allinfo = 'true'
            else:
                allinfo = None
        if isinstance(scan, bool):
            if scan is True:
                scan = 1
            else:
                scan = None

        url = self.base + 'url/report'
        params = {
            'apikey': self.__apikey,
            'resource': resource,
            'allinfo': allinfo,
            'scan': scan
        }
        return self._api_request('GET', url, params)

    def u_scan(self, scan_url):
        """Scan an URL"""

        url = self.base + 'url/scan'
        params = {
            'apikey': self.__apikey,
            'url': scan_url
        }
        return self._api_request('POST', url, params)

    def d_report(self, domain):
        """Retrieves a domain report"""

        url = self.base + 'domain/report'
        params ={
            'apikey': self.__apikey,
            'domain': domain
        }
        return self._api_request('GET', url, params)

    def d_ip_report(self, ip):
        """Retrieve an IP address report"""

        url = self.base + 'ip-address/report'
        params = {
            'apikey': self.__apikey,
            'ip': ip
        }
        return self._api_request('GET', url, params)

    def c_get(self, resource):
        """Post comment for a file or URL"""

        url = self.base + 'comments/get'
        params = {
            'apikey': self.__apikey,
            'resource': resource
        }
        return self._api_request('GET', url, params)

    def c_put(self, resource, comment):
        """Post comment for a file or URL"""

        url = self.base + 'comments/put'
        params = {
            'apikey': self.__apikey,
            'resource': resource,
            'comment': comment
        }
        return self._api_request('POST', url, params)

    def _api_request(self, method, url, params, *args):
        # check, if exists `files` parameter
        if args:
            files = args[0]
        else:
            files = None
        # GET method request
        if method == 'GET':
            response = requests.get(url, params=params)
            if self._status_validation(response.status_code):
                return response.json()
        # POST method request
        elif method == 'POST':
            response = requests.post(url, params=params, files=files)
            if self._status_validation(response.status_code):
                return response.json()

    @staticmethod
    def _status_validation(status_code):
        """Returns True, if `status_code` is 200."""

        # api request success
        if status_code == 200:
            return True
        # to occur HTTP_STATUS_CODE exception
        elif status_code == 204:
            raise HTTP_STATUS_204
        elif status_code == 400:
            raise HTTP_STATUS_400
        elif status_code == 403:
            raise HTTP_STATUS_403

    @staticmethod
    def _download_file(hash, raw, outfile=None):
        """Returns file data and make file."""

        # `outfile` path validation
        if outfile is None:
            outfile = hash
        else:
            if not os.path.isdir(os.path.dirname(outfile)):
                raise FileNotFoundError
        # make downloaded file
        with open(outfile, mode='wb') as fp:
            fp.write(raw)
        return raw


class HTTP_STATUS_204(Exception):
    def __str__(self):
        return "Request rate limit exceeded. You are making more requests than allowed."


class HTTP_STATUS_400(Exception):
    def __str__(self):
        return "Bad request. Your request was somehow incorrect."


class HTTP_STATUS_403(Exception):
    def __str__(self):
        return "Forbidden. You don't have enough privileges to make the request."

