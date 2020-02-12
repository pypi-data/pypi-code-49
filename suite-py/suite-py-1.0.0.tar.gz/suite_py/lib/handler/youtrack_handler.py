# -*- encoding: utf-8 -*-
import os
import re

from PyInquirer import prompt
from youtrack.connection import Connection
from youtrack.youtrack import YouTrackException

from suite_py.lib.tokens import Tokens
from suite_py.lib.config import Config
from suite_py.lib.singleton import Singleton

tokens = Tokens()
config = Config().load()


class YoutrackHandler(metaclass=Singleton):
    _client = None

    def __init__(self):
        self._client = Connection(
            url=config['youtrack']['url'], token=tokens.youtrack)

    def get_users(self):
        return self._client.get_users()

    def get_issue(self, issue_id):
        return self._client.get_issue(issue_id)

    def validate_issue(self, issue_id):
        try:
            if self.get_issue(issue_id):
                return True
        except (YouTrackException) as e:
            return False

    def comment(self, issue_id, comment):
        self._client.execute_command(issue_id, 'comment', comment=comment)

    def update_state(self, issue_id, status):
        self._client.execute_command(issue_id, 'State {}'.format(status))

    def add_tag(self, issue_id, label):
        self._client.execute_command(issue_id, 'tag {}'.format(label))

    def assign_to(self, issue_id, user):
        self._client.execute_command(issue_id, "Assignee {}".format(user))

    def get_link(self, issue_id):
        return "https://prima-assicurazioni-spa.myjetbrains.com/youtrack/issue/{}".format(issue_id)

    def update_issue(self, issue_id, summary, description):
        return self._client.update_issue(issue_id, summary, description)

    def get_issue_ids(self, commits):
        issue_ids = []
        for c in commits:
            issue_id = self.get_card_from_name(c.commit.message)
            if issue_id:
                issue_ids.append(issue_id)
        return issue_ids

    def get_card_from_name(self, name):
        regex = '[A-Z]+-[0-9]+'
        if re.search(regex, name):
            id_card = re.findall(regex, name)[0]
            if not self.validate_issue(id_card):
                return None
            return id_card
        else:
            return None
