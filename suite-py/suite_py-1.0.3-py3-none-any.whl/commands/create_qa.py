# -*- coding: utf-8 -*-
import json
import subprocess
import sys

from halo import Halo

from suite_py.lib.handler.youtrack_handler import YoutrackHandler
from suite_py.lib.handler.github_handler import GithubHandler
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler import drone_handler as drone
from suite_py.lib.handler import prompt_utils
from suite_py.lib.logger import Logger
from suite_py.lib.qainit import get_qa_projects, qainit_deploy
from suite_py.lib.config import Config


youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
config = Config().load()


def entrypoint(project):
    qa_projects = get_qa_projects()
    if project not in qa_projects:
        logger.error("Il progetto {} non fa parte degli ambienti di QA, niente da fare".format(project))
        sys.exit(0)

    with Halo(text='Updating prima-twig...', spinner='dots', color='magenta'):
        try:
            subprocess.run(['gem', 'update', 'prima-twig'],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            logger.error("Errore durante l'aggiornamento di prima-twig, per favore esegui manualmente `gem update prima-twig`")
            sys.exit(-1)

    branch_name = git.current_branch_name()
    youtrack_id = youtrack.get_card_from_name(branch_name)

    if youtrack_id:
        if prompt_utils.ask_confirm("Ci sono altri progetti da aggiungere al QA che fanno riferimento alla card {}?".format(youtrack_id), default=False):
            twig_arg = multi_repo_qa(youtrack_id, qa_projects)
        else:
            twig_arg = mono_repo_qa(project, branch_name)
    else:
        logger.warning("Non sono riuscito a trovare una issue YouTrack collegata al branch, non e' possibile collegare automaticamente altri progetti a questo QA")
        logger.warning("Se vuoi creare il QA con diversi branch su diversi progetti per favore interrompi il comando ed utilizza twig")
        twig_arg = mono_repo_qa(project, branch_name)

    qainit_deploy(twig_arg)

    if youtrack_id:
        logger.info("Aggiorno la card su youtrack...")
        youtrack.update_state(youtrack_id, config["youtrack"]["test_state"])

    drone_url = drone.get_last_build_url('qainit')
    if drone_url:
        logger.info("Puoi seguire la creazione del QA su {}".format(drone_url))

    logger.info("Configurazione del QA effettuata con successo!")


def multi_repo_qa(youtrack_id, qa_projects):
    logger.info("Cerco gli altri branch su github...")
    repos = list(map(lambda project: github.get_repo(project), qa_projects))

    selected_repos = []
    for repo in repos:
        print('.', end='', flush=True)
        for branch in repo.get_branches():
            if youtrack_id in branch.name:
                selected_repos.append((repo.name, branch))

    print('.')
    logger.info("Progetti trovati:")
    for elem in selected_repos:
        logger.info("{} --> {}".format(elem[0], elem[1].name))

    return twigify(selected_repos)

def mono_repo_qa(project, branch_name):
    logger.info("Creo il qa con il progetto {} e branch {}".format(project, branch_name))
    gh_branch = github.get_repo(project).get_branch(branch_name)
    selected_repos = [(project, gh_branch)]

    return twigify(selected_repos)

def twigify(projects_list):
    projects_dict = {}
    for tuple in projects_list:
        projects_dict[tuple[0]] = {"name": tuple[1].name,
                                   "revision": tuple[1].commit.sha[:15],
                                   "committer": tuple[1].commit.committer.email or "",
                                   "default_branch": False}

    return json.dumps(json.dumps(projects_dict)) # necessario per fare l'escape corretto

    # development only
    # return json.dumps(projects_dict) chiamando twig da file non bisogna dumpare due volte
