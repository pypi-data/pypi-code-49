# -*- encoding: utf-8 -*-
import re

from youtrack.connection import Connection
from youtrack.youtrack import YouTrackException

from suite_py.lib.tokens import Tokens
from suite_py.lib.config import Config
from suite_py.lib.singleton import Singleton

tokens = Tokens()
config = Config().load()

REGEX = r"([A-Z]+-[0-9]+)"
URL = "https://prima-assicurazioni-spa.myjetbrains.com/youtrack/issue/"


class YoutrackHandler(metaclass=Singleton):
    _client = None

    def __init__(self):
        self._client = Connection(url=config["youtrack"]["url"], token=tokens.youtrack)

    def get_users(self):
        return self._client.get_users()

    def get_issue(self, issue_id):
        return self._client.get_issue(issue_id)

    def validate_issue(self, issue_id):
        try:
            if self.get_issue(issue_id):
                return True
        except YouTrackException:
            pass
        return False

    def comment(self, issue_id, comment):
        self._client.execute_command(issue_id, "comment", comment=comment)

    def update_state(self, issue_id, status):
        self._client.execute_command(issue_id, f"State {status}")

    def add_tag(self, issue_id, label):
        self._client.execute_command(issue_id, f"tag {label}")

    def assign_to(self, issue_id, user):
        self._client.execute_command(issue_id, f"Assignee {user}")

    def get_link(self, issue_id):
        return f"{URL}{issue_id}"

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
        if re.search(REGEX, name):
            id_card = re.findall(REGEX, name)[0]
            if self.validate_issue(id_card):
                return id_card
        return None

    def replace_card_names_with_md_links(self, text):
        return re.sub(REGEX, f"[\\1]({URL}\\1)", text)
