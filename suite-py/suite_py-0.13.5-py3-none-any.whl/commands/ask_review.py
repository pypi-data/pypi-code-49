from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler.github_handler import GithubHandler
from ..lib.logger import Logger
from ..lib.handler import git_handler as git
from ..lib.handler.captainhook_handler import CaptainHook
from ..lib.handler.slack_handler import SlackHandler
import sys
import readline

youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
slack = SlackHandler()

try:
    captainhook = CaptainHook()
    users = captainhook.get_users_list().json()
except:
    logger.error(
        "Non riesco ad ottenere la lista degli utenti da captainhook.\
        Controlla di avere attiva la VPN. Se il problema persiste aggiungi i reviewer dal sito GitHub")
    sys.exit(-1)


def entrypoint(args):
    branch_name = git.current_branch_name()

    github_reviewers = []
    slack_reviewers = []

    pull = github.get_pr_from_branch(args.project, branch_name)

    if pull.totalCount:
        pr = pull[0]
        logger.info('Ho trovato la pull request numero {} per il branch {} sul repo {}'.format(
            pr.number, branch_name, args.project))
    else:
        logger.error(
            'Nessuna pull request aperta trovata per il branch {}'.format(branch_name))
        sys.exit(-1)

    youtrack_reviewers = ask_reviewer()

    for rev in youtrack_reviewers:
        for user in users:
            if user["youtrack"] == rev:
                github_reviewers.append(user["github"])
                slack_reviewers.append(user["slack"])

    pr.create_review_request(github_reviewers)
    logger.info('Aggiungo reviewers su GitHub')

    revs = ""
    for rev in slack_reviewers:
        revs += "<@{}> ".format(rev)

    slack.post('#review', '{}{}'.format(
        revs, pr.html_url))

    logger.info('Cito reviewers su Slack')

    youtrack_id = youtrack.get_card_from_name(pr.title)

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


def ask_reviewer():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    youtrack_reviewers = []

    youtrack_reviewers = list(
        input("Scegli i reviewers (nome.cognome - separati da spazio - premere TAB per autocomplete) > ").split())

    if len(youtrack_reviewers) < 1:
        logger.warning("Devi inserire almeno un reviewer")
        return ask_reviewer()
    else:
        return youtrack_reviewers


def completer(text, state):
    options = [x["youtrack"]
               for x in users if text.lower() in x["youtrack"].lower()]
    try:
        return options[state]
    except IndexError:
        return None
