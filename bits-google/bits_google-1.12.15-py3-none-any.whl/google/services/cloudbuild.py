# -*- coding: utf-8 -*-
"""Google Cloud Build API."""

from bits.google.services.base import Base
from googleapiclient.discovery import build


class CloudBuild(Base):
    """CloudBuild class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.cloudbuild = build('cloudbuild', 'v1', credentials=credentials)

    #
    # Triggers
    #
    def create_trigger(self, projectId, body):
        """Create a trigger for a project."""
        params = {
            'projectId': projectId,
            'body': body,
        }
        return self.cloudbuild.projects().triggers().create(**params).execute()

    def delete_trigger(self, projectId, triggerId):
        """Delete a single trigger for a project."""
        params = {
            'projectId': projectId,
            'triggerId': triggerId,
        }
        return self.cloudbuild.projects().triggers().delete(**params).execute()

    def get_trigger(self, projectId, triggerId):
        """Return a single trigger for a project."""
        params = {
            'projectId': projectId,
            'triggerId': triggerId,
        }
        return self.cloudbuild.projects().triggers().get(**params).execute().get('triggers', [])

    def get_triggers(self, projectId):
        """Return a list of triggers for a project."""
        params = {'projectId': projectId}
        triggers = self.cloudbuild.projects().triggers()
        request = triggers.list(**params)
        return self.get_list_items(triggers, request, 'triggers')

    def update_trigger(self, projectId, triggerId, body):
        """Update a trigger for a project."""
        params = {
            'projectId': projectId,
            'triggerId': triggerId,
            'body': body,
        }
        return self.cloudbuild.projects().triggers().patch(**params).execute()
