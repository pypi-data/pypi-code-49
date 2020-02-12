from __future__ import print_function, unicode_literals
from ..lib.handler.github_handler import GithubHandler
from ..lib.handler.database_handler import DatabaseHandler
from ..lib.logger import Logger
from cement import shell

github = GithubHandler()
logger = Logger()
db = DatabaseHandler()


def entrypoint(args):

    gh_users = github.get_all_users()
    db_users = [user.github_login for user in db.get_all_users()]

    missing_users = [user for user in gh_users if user not in db_users]

    for github_login in missing_users:
        logger.info("Adding {}".format(github_login))

        name = ask_additional_info("{} name:".format(github_login))
        surname = ask_additional_info("{} surname:".format(github_login))
        review_label = ask_additional_info(
            "{} review_label:".format(github_login))

        db.insert_user(github_login, name, surname, review_label)

    logger.info("Utenti aggiornati!")


def ask_additional_info(message):
    p = shell.Prompt(message)

    return p.prompt()
