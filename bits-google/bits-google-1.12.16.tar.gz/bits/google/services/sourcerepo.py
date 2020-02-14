# -*- coding: utf-8 -*-
"""Google Source Repo API."""

from bits.google.services.base import Base
from googleapiclient.discovery import build


class SourceRepo(Base):
    """SourceRepo class."""

    def __init__(self, credentials):
        """Initialize a class instance."""
        self.sourcerepo = build('sourcerepo', 'v1', credentials=credentials)

    #
    # Repos
    #
    def create_repo(self, projectId, body):
        """Create a repo for a project."""
        params = {
            'name': 'projects/{}'.format(projectId),
            'body': body,
        }
        return self.sourcerepo.projects().repos().create(**params).execute()

    def delete_repo(self, projectId, repo):
        """Delete a single repo for a project."""
        params = {
            'name': 'projects/{}/repos/{}'.format(projectId, repo),
        }
        return self.sourcerepo.projects().repos().delete(**params).execute()

    def get_repo(self, projectId, repo):
        """Return a single repo for a project."""
        params = {
            'name': 'projects/{}/repos/{}'.format(projectId, repo),
        }
        return self.sourcerepo.projects().repos().get(**params).execute().get('repos', [])

    def get_repos(self, projectId):
        """Return a list of repos for a project."""
        params = {'name': 'projects/{}'.format(projectId)}
        repos = self.sourcerepo.projects().repos()
        request = repos.list(**params)
        return self.get_list_items(repos, request, 'repos')

    def update_repo(self, projectId, repo, body):
        """Update a repo for a project."""
        params = {
            'name': 'projects/{}/repos/{}'.format(projectId, repo),
            'body': body,
        }
        return self.sourcerepo.projects().repos().patch(**params).execute()
