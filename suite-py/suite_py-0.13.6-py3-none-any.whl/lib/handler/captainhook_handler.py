from __future__ import print_function, unicode_literals
from ..singleton import Singleton
from ..handler import git_handler as git
import os
import requests
import sys


class CaptainHook(metaclass=Singleton):
    _baseurl = None

    def __init__(self):
        self._baseurl = "http://captainhook-internal.prima.it"

    def lock_project(self, project):
        data = {'project': project, 'status': "locked", "user": git.get_git_username()}
        return self.send_post_request("/projects/manage-lock", data)

    def unlock_project(self, project):
        data = {'project': project, 'status': "unlocked", "user": git.get_git_username()}
        return self.send_post_request("/projects/manage-lock", data)

    def status(self, project):
        return self.send_get_request("/projects/check?project={}".format(project))

    def get_users_list(self):
        return self.send_get_request("/users/all")

    def send_post_request(self, endpoint, data):
        return requests.post("{}{}".format(self._baseurl, endpoint), data=data)

    def send_get_request(self, endpoint):
        return requests.get("{}{}".format(self._baseurl, endpoint))
