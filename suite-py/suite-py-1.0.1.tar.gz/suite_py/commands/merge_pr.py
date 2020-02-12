# -*- coding: utf-8 -*-
import os
import re
import sys

from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler.captainhook_handler import CaptainHook
from suite_py.lib.config import Config
from suite_py.lib.logger import Logger
from suite_py.lib.handler import prompt_utils
from suite_py.lib.qainit import qainit_shutdown
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler import drone_handler as drone


youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
config = Config().load()


def entrypoint(project, timeout):
    lock = CaptainHook()
    if timeout:
        lock.set_timeout(timeout)

    stop_if_master_locked(project, lock)

    pr = select_pr(project)
    branch_name = pr.head.ref
    youtrack_id = youtrack.get_card_from_name(branch_name)


    check_migrations_merge(pr)

    logger.info("Eseguo il merge...")

    merge_status = pr.merge(
        commit_title="{} (#{})".format(pr.title, pr.number), commit_message='', merge_method='squash')

    if not merge_status.merged:
        logger.error("Si è verificato un errore durante il merge.")
        sys.exit(-1)

    drone_build = get_drone_build(project, merge_status.sha)

    if drone_build:
        logger.info(
            "Pull request mergiata su master! Puoi seguire lo stato della build su {}".format(drone_build))
    else:
        logger.info("Pull request mergiata su master!")

    git.fetch(project)
    if git.remote_branch_exists(project, branch_name):
        git.delete_remote_branch(project, branch_name)

    if prompt_utils.ask_confirm("Vuoi bloccare staging? (Necessario se bisogna testare su staging)", default=False):
        lock.lock_project(project)

    if youtrack_id:
        logger.info("Aggiorno lo stato della card su youtrack...")
        youtrack.update_state(youtrack_id, config["youtrack"]["merged_state"])
        logger.info("Card aggiornata")

        logger.info("Spengo il qa, se esiste")
        qainit_shutdown(youtrack_id)
    else:
        logger.warning(
            "Non sono riuscito a trovare una issue YouTrack nel nome del branch o la issue indicata non esiste.")
        logger.warning(
            "Nessuna card aggiornata su YouTrack e nessun QA spento in automatico")

    logger.info("Tutto fatto!")
    sys.exit()


def select_pr(project):
    if github.user_is_admin(project):
        logger.info("Ottengo le pull request da GitHub...")
        logger.warning(
            "Sei admin del repository, puoi fare il merge skippando i check (CI, review, ecc...)\nDa grandi poteri derivano grandi responsabilita'")
        prs = github.get_list_pr(project)
    else:
        logger.info("Ottengo le pull request con check verdi da GitHub...")
        prs = list(filter(lambda pr: pr.mergeable and pr.mergeable_state ==
                          "clean", github.get_list_pr(project)))

    if prs.totalCount > 0:
        choices = [{"name": "{} {}".format(
            i.number, i.title), "value": i} for i in prs]
        return prompt_utils.ask_choices('Seleziona PR: ', choices)
    else:
        logger.warning(
            "Non esistono pull request pronte per il merge, per favore controlla su https://github.com/primait/{}/pulls".format(project))
        sys.exit(-1)


def stop_if_master_locked(project, lock):
    try:
        request = lock.status(project)
    except:
        logger.error("Impossibile contattare CaptainHook, stai usando la VPN?")
        sys.exit(-1)

    if request.status_code != 200:
        logger.error("Impossibile determinare lo stato del lock su master.")
        sys.exit(-1)

    if request.json()["locked"]:
        logger.error(
            "Il progetto è lockato su master. Impossibile continuare.")
        sys.exit(-1)


def get_drone_build(project, sha):
    drone_build = drone.get_pr_build_url(
        project, sha)
    if drone_build != "":
        return drone_build
    return None


def check_migrations_merge(pr):
    files_changed = [x.filename for x in pr.get_files()]
    if git.migrations_found(files_changed):
        logger.warning("ATTENZIONE: migrations rilevate nel codice")
        if not prompt_utils.ask_confirm("Sicuro di voler continuare?"):
            sys.exit(-1)
