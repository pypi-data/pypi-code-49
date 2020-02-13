# -*- coding: utf-8 -*-
import re
import sys

from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler import git_handler as git
from suite_py.lib.config import Config
from suite_py.lib.logger import Logger
from suite_py.lib.handler import prompt_utils


youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
config = Config().load()


def entrypoint(project, card):
    git.is_dirty(project)

    try:
        if card:
            issue = youtrack.get_issue(card)
        else:
            issue = youtrack.get_issue(ask_card())
    except:
        logger.error("Si e' verificato un problema recuperando la issue da youtrack. Controlla che il numero della issue e' corretto")
        sys.exit(-1)

    checkout_branch(project, issue)

    youtrack.assign_to(issue["id"], "me")

    youtrack.update_state(issue["id"], config["youtrack"]["picked_state"])

def ask_card():
    return prompt_utils.ask_questions_input(
        'Inserisci il numero della issue youtrack:', config['user']['default_slug'])

def checkout_branch(project, issue):
    branch_name = prompt_utils.ask_questions_input("Inserisci nome del branch: ", re.sub(
        r'([\s\\.,~\^:\[\]"\'?]|[^\x00-\x7F])+', "-", issue["summary"]
    ).lower())

    parent_branch_name = prompt_utils.ask_questions_input(
        "Inserisci branch iniziale: ", "master")

    branch_type = issue["Type"].lower().replace(" ", "-")

    branch_name = "{}/{}/{}".format(
        branch_type, branch_name, issue["id"]
    )

    git.checkout(project, parent_branch_name)

    git.checkout(project, branch_name)
