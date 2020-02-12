# -*- coding: utf-8 -*-
import sys

from halo import Halo
import semver

from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler.slack_handler import SlackHandler
from suite_py.lib.handler import prompt_utils
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler import drone_handler as drone
from suite_py.lib.logger import Logger
from suite_py.lib.config import Config


youtrack = YoutrackHandler()
github = GithubHandler()
config = Config().load()
logger = Logger()
slack = SlackHandler()


def entrypoint(project):
    if prompt_utils.ask_confirm("Sono presenti migration?", default=False):
        logger.error(
            "Impossibile continuare con il deploy a causa di migration presenti. Chiedi ai devops di effettuare il deploy.")
        sys.exit(-1)

    git.is_dirty(project)
    git.fetch(project)
    repo = github.get_repo(project)

    latest_release = get_release(repo)

    versions = bump_versions(latest_release.title)

    commits = github.get_commits_since_release(repo, latest_release)

    check_migrations_deploy(commits)

    message = "\n".join(["* " + c.commit.message.splitlines()[0]
                         for c in commits])

    logger.info("\nLista dei commit:\n{}\n".format(message))

    if not prompt_utils.ask_confirm("Vuoi continuare?"):
        sys.exit(-1)

    new_version = prompt_utils.ask_choices(
        "Seleziona versione:",
        [
            {"name": "Patch {}".format(
                versions["patch"]), "value": versions["patch"]},
            {"name": "Minor {}".format(
                versions["minor"]), "value": versions["minor"]},
            {"name": "Major {}".format(
                versions["major"]), "value": versions["major"]},
        ]
    )

    release_state = config["youtrack"]["release_state"]

    deployed_cards_link = []
    issue_ids = youtrack.get_issue_ids(commits)

    if len(issue_ids) > 0:
        logger.info("Imposto le card in {}".format(release_state))

    for issue_id in issue_ids:
        try:
            deployed_cards_link.append(youtrack.get_link(issue_id))
            youtrack.comment(
                issue_id, "Deploy in produzione di {} effettuato con la release {}".format(args.project, new_version))
            youtrack.update_state(
                issue_id, release_state
            )
        except:
            logger.warning(
                "Si è verificato un errore durante lo spostamento della card {} in {}".format(
                issue_id, release_state)
            )

    create_release(repo, new_version, message, project, deployed_cards_link)


def get_release(repo):
    with Halo(text='Loading...', spinner='dots', color='magenta'):
        latest_release = github.get_latest_release_if_exists(repo)
        tags = repo.get_tags()
        tag = git.get_last_tag_number(tags)
    if latest_release and latest_release.title == tag:
        logger.info("La release attuale è {}".format(latest_release.title))
        return latest_release
    else:
        logger.info("L'ultimo tag trovato è {}".format(tag))
        if not prompt_utils.ask_confirm("Sicuro di voler continuare?"):
            sys.exit(-1)
        return repo.create_git_release(tag, tag, "New release from tag {}".format(tag))


def create_release(repo, new_version, message, project, deployed_cards_link):
    new_release = repo.create_git_release(new_version, new_version, message)
    if new_release:
        logger.info("La release è stata creata! Link: {}".format(
            new_release.html_url))
        slack.post(
            "#deploy", "ho effettuato il deploy di {}. Nuova release con versione {} {}\n{}".format(project, new_version, new_release.html_url, deployed_cards_to_string(deployed_cards_link)))
        drone_url = drone.get_last_build_url(project)
        if drone_url:
            logger.info(
                "Puoi seguire il deploy in produzione su {}".format(drone_url))


def bump_versions(current):
    return {
        "patch": semver.bump_patch(current),
        "minor": semver.bump_minor(current),
        "major": semver.bump_major(current)
    }


def deployed_cards_to_string(cards):
    if len(cards) == 0:
        return ""
    else:
        return "\n".join(cards)


def check_migrations_deploy(commits):
    if len(commits) == 0:
        logger.error("ERRORE: nessun commit trovato")
        sys.exit(-1)
    elif len(commits) == 1:
        files_changed = git.files_changed_between_commits(
            "--raw", "{}~".format(commits[0].sha))
    else:
        files_changed = git.files_changed_between_commits(
            "{}~".format(commits[-1].sha), commits[0].sha)
    if git.migrations_found(files_changed):
        logger.warning("ATTENZIONE: migrations rilevate nel codice")
        if not prompt_utils.ask_confirm("Sicuro di voler continuare?"):
            sys.exit(-1)
