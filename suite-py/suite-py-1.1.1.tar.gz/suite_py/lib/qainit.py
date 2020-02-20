# -*- encoding: utf-8 -*-
import json
import subprocess

from suite_py.lib.logger import Logger
from suite_py.lib.config import Config
from suite_py.lib.handler import git_handler as git
from suite_py.lib.handler.github_handler import GithubHandler


config = Config().load()
logger = Logger()
github = GithubHandler()

# development only
# twig_command = '{}/twig-binaries/bin/twig-feature'.format(config['user']['projects_home'])

qainit_dir = f"{config['user']['projects_home']}/qainit"


def get_qa_projects():
    git.check_repo_cloned("qainit")
    git.sync("qainit")
    with open(f"{qainit_dir}/branch_names", "r") as file:
        branches_obj = json.loads(file.read())

    return list(branches_obj.keys())


def qainit_deploy(args):
    return subprocess.run(
        # development only
        # [twig_command, 'suite', 'deploy', args], cwd=qainit_dir, check=True)
        ["twig", "feature", "suite", "deploy", args],
        cwd=qainit_dir,
        check=True,
    )


def qainit_shutdown(youtrack_id):
    git.check_repo_cloned("qainit")
    git.sync("qainit")
    branch = git.search_remote_branch("qainit", f"*{youtrack_id}*")
    if branch:
        git.checkout("qainit", branch)
        git.commit("qainit", "shutdown", dummy=True)
        git.push("qainit", branch)

    else:
        logger.warning(
            "Non sono riuscito a trovare un qa per questa issue, se il qa esiste, per favore spegnilo manualmente\nDevops are watching you! ( •͡˘ _•͡˘)"
        )
