# -*- coding: utf-8 -*-
"""Google SQL API."""

from bits.google.services.base import Base
from googleapiclient.discovery import build


class SQL(Base):
    """Google SQL class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.sql = build('sql', 'v1beta4', credentials=credentials, cache_discovery=False)
        self.credentials = credentials

    def get_instances(self, project):
        """Check if group has member."""
        instances = self.sql.instances()
        request = instances.list(project=project)
        return self.get_list_items(instances, request, 'items')
