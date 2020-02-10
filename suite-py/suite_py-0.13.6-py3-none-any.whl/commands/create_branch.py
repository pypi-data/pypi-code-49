from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler.github_handler import GithubHandler
from ..lib.handler import git_handler as git
from ..lib.config import Config
from ..lib.logger import Logger
from ..lib.handler import prompt_utils

import re
import sys

youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
config = Config().load()


def entrypoint(args):
    git.is_dirty(args.project)

    try:
        if args.card:
            issue = youtrack.get_issue(args.card)
        else:
            issue = youtrack.get_issue(ask_card())
    except:
        logger.error("Si e' verificato un problema recuperando la issue da youtrack. Controlla che il numero della issue e' corretto")
        sys.exit(-1)

    checkout_branch(args.project, issue)

    youtrack.assign_to(issue["id"], "me")

    youtrack.update_state(issue["id"], config["youtrack"]["picked_state"])

def ask_card():
    return prompt_utils.ask_questions_input('Inserisci il numero della issue youtrack: ', "PRIMA-XXX")

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
