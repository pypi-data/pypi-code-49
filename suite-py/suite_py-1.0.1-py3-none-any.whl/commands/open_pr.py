# -*- encoding: utf-8 -*-
import sys

from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler, GithubException
from suite_py.lib.logger import Logger
from suite_py.lib.config import Config
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler import prompt_utils


youtrack = YoutrackHandler()
github = GithubHandler()
config = Config().load()
logger = Logger()


def entrypoint(project):
    branch_name = git.current_branch_name()

    if not git.remote_branch_exists(project, branch_name):
        logger.error(
            "Non ho trovato il branch {} su GitHub, per favore esegui un 'git push' manualmente".format(branch_name))
        sys.exit(-1)

    youtrack_id = youtrack.get_card_from_name(branch_name)
    if youtrack_id:
        pulls = github.get_pr_from_branch(project, branch_name)
        if pulls.totalCount:
            pr = pulls[0]
            logger.info(
                "Esiste una pull request su GitHub per il branch {}".format(branch_name))

            if prompt_utils.ask_confirm("Vuoi modificare la description della pull request?"):
                edit_pr(pr)
                sys.exit(0)

        else:
            create_pr(project, branch_name, youtrack_id)
    else:
        logger.warning(
            "Non sono riuscito a trovare una issue YouTrack nel nome del branch o la issue indicata non esiste")
        if not prompt_utils.ask_confirm("Vuoi collegare la pull request con una issue?"):
            create_pr(project, branch_name)
        else:
            create_pr(project, branch_name, ask_for_id_card())


def edit_pr(pr):
    pr_body = ask_for_description(pr.body)
    pr.edit(body=pr_body)
    logger.info("Pull request modificata")


def create_pr(repo, branch_name, id_card=None):
    if id_card:
        logger.info("Creo una pull request sul progetto {} per il branch {} collegato con la card {}".format(
            repo, branch_name, id_card))
        link = youtrack.get_link(id_card)
        title = "[{}]: {}".format(
            id_card, youtrack.get_issue(id_card)["summary"])
    else:
        logger.warning("Creo una pull request sul progetto {} per il branch {} SENZA collegamenti a YouTrack".format(
            repo, branch_name))
        link = ""
        title = ask_for_title()

    pr_body = ask_for_description()

    body = "{} \n\n {}".format(link, pr_body)

    try:
        pr = github.create_pr(repo, branch_name, title, body)
        logger.info("Pull request numero {} creata!".format(pr.number))
    except GithubException as e:
        logger.error('Errore durante la richiesta a GitHub: ')
        logger.error(e.data["errors"][0])
        sys.exit(-1)

    if id_card:
        update_card(id_card, repo, pr.html_url)
        logger.info(
            "Inserito link della pull request nella card {}".format(id_card))


def ask_for_description(pr_body=""):
    input("Inserisci la description della pull request. Premendo invio si aprira l'editor di default")
    description = prompt_utils.ask_questions_editor(
        'Inserisci la description della PR: ', pr_body)

    if description == "":
        logger.warning(
            "La descrizione della pull request non può essere vuota")
        ask_for_description(pr_body)
    else:
        return description


def ask_for_id_card():
    id_card = prompt_utils.ask_questions_input(
        'Inserisci ID della card (ex: PRIMA-1234): ')
    if youtrack.validate_issue(id_card):
        return id_card
    else:
        logger.error("ID non esistente su YouTrack")
        ask_for_id_card()


def update_card(id_card, repo, link):
    youtrack.comment(id_card, "PR {} -> {}".format(repo, link))


def ask_for_title():
    title = prompt_utils.ask_questions_input(
        'Inserisci il titolo della pull request: ')
    if title == "":
        logger.warning("Il titolo della pull request non può essere vuoto")
        ask_for_title()
    else:
        return title
