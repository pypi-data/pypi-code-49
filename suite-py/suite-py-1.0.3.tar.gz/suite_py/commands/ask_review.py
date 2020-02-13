# -*- coding: utf-8 -*-
import readline
import functools
import sys

from slack.errors import SlackClientError

from suite_py.lib.config import Config
from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.logger import Logger
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler.captainhook_handler import CaptainHook
from suite_py.lib.handler.slack_handler import SlackHandler

youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
slack = SlackHandler()


def maybe_get_users_list(timeout):
    try:
        captainhook = CaptainHook()
        if timeout:
            captainhook.set_timeout(timeout)
        return captainhook.get_users_list().json()
    except:
        logger.error(
            "Non riesco ad ottenere la lista degli utenti da captainhook.\
            Controlla di avere attiva la VPN. Se il problema persiste aggiungi i reviewer dal sito GitHub")
        sys.exit(-1)
config = Config().load()


def get_pr(project):
    branch_name = git.current_branch_name()
    pull = github.get_pr_from_branch(project, branch_name)

    if pull.totalCount:
        pr = pull[0]
        logger.info('Ho trovato la pull request numero {} per il branch {} sul repo {}'.format(
            pr.number, branch_name, project))
    else:
        logger.error(
            'Nessuna pull request aperta trovata per il branch {}'.format(branch_name))
        sys.exit(-1)

    return pr


def ask_reviewer(users):
    u_completer = functools.partial(completer, users)
    readline.set_completer(u_completer)
    readline.parse_and_bind("tab: complete")

    youtrack_reviewers = []

    youtrack_reviewers = list(
        input("Scegli i reviewers (nome.cognome - separati da spazio - premere TAB per autocomplete) > ").split())

    if len(youtrack_reviewers) < 1:
        logger.warning("Devi inserire almeno un reviewer")
        return ask_reviewer(users)
    else:
        return youtrack_reviewers


def completer(users, text, state):
    options = [x["youtrack"]
               for x in users if text.lower() in x["youtrack"].lower()]
    try:
        return options[state]
    except IndexError:
        return None


def maybe_send_slack_message(slack_reviewers, url):
    revs = ""
    for rev in slack_reviewers:
        revs += "<@{}> ".format(rev)

    try:
        slack.post(config['user']['notify_channel'], '{}{}'.format(
            revs, url))

        logger.info('Cito reviewers su Slack')
    except SlackClientError as e:
        logger.error("Errore di invio messaggio a Slack:\n{}".format(e))
        sys.exit(-1)


def find_github_and_slack_nicks(youtrack_reviewers, users):
    github_reviewers = []
    slack_reviewers = []
    for rev in youtrack_reviewers:
        for user in users:
            if user["youtrack"] == rev:
                github_reviewers.append(user["github"])
                slack_reviewers.append(user["slack"])

    return github_reviewers, slack_reviewers


def maybe_adjust_youtrack_card(title, youtrack_reviewers):
    youtrack_id = youtrack.get_card_from_name(title)

    if youtrack_id:
        logger.info(
            'Sposto la card {} in review su youtrack e aggiungo i tag degli utenti'.format(youtrack_id))
        youtrack.update_state(youtrack_id, 'Review')
        for rev in youtrack_reviewers:
            try:
                youtrack.add_tag(youtrack_id, "review:{}".format(rev))
            except BaseException as e:
                logger.warning(
                    "Non sono riuscito ad aggiungere i tag di review: {}".format(e))
                sys.exit(-1)
    else:
        logger.warning(
            'Reviewers inseriti SOLO su GitHub. Nessuna card collegata o card nel nome del branch inesistente su YouTrack.')


def entrypoint(project, timeout):
    users = maybe_get_users_list(timeout)
    pr = get_pr(project)
    youtrack_reviewers = ask_reviewer(users)
    github_reviewers, slack_reviewers = find_github_and_slack_nicks(
        youtrack_reviewers, users
    )
    pr.create_review_request(github_reviewers)
    logger.info('Aggiungo reviewers su GitHub')
    maybe_send_slack_message(slack_reviewers, pr.html_url)
    maybe_adjust_youtrack_card(pr.title, youtrack_reviewers)
