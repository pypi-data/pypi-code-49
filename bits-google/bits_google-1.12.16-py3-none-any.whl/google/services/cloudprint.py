# -*- coding: utf-8 -*-
"""Google CloudPrint API."""


from bits.google.services.base import Base
from google.auth.transport.requests import AuthorizedSession
# from googleapiclient.discovery import build


class CloudPrint(Base):
    """CloudPrint class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.base_url = 'https://www.google.com/cloudprint'
        self.credentials = credentials
        # self.cloudprint = build('cloudprint', 'v1', credentials=credentials)
        self.requests = AuthorizedSession(self.credentials)

    def delete_jobs(self, jobid):
        """Delete a single print job."""
        params = {
            'jobid': jobid,
        }
        url = '{}/deletejob'.format(self.base_url)
        response = self.requests.get(url, params=params)

        # raise for status
        response.raise_for_status()

        return response.json()

    def list_jobs(
        self,
        printerid=None,
        owner=None,
        status=None,
        q=None,
        offset=None,
        limit=None,
        sortorder=None,
    ):
        """Return stats."""
        params = {
            'printerid': None,
            'owner': None,
            'status': None,
            'q': None,
            'offset': None,
            'limit': None,
            'sortorder': None,
        }
        url = '{}/jobs'.format(self.base_url)
        response = self.requests.get(url, params=params)

        # raise for status
        response.raise_for_status()

        return response.json()  # .get('jobs', [])

    def search_printers(self):
        """Return stats."""
        url = '{}/search'.format(self.base_url)
        response = self.requests.get(url)

        # raise for status
        response.raise_for_status()

        return response.json().get('printers', [])
