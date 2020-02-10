from __future__ import print_function, unicode_literals
from .logger import Logger
from .config import Config
from .handler import git_handler as git
from .handler.github_handler import GithubHandler

import subprocess
import json

config = Config().load()
logger = Logger()
github = GithubHandler()

# development only
#twig_command = '{}/twig-binaries/bin/twig-feature'.format(config['user']['projects_home'])

qainit_dir = '{}/qainit'.format(config['user']['projects_home'])


def get_qa_projects():
    git.check_repo_cloned('qainit')
    git.sync('qainit')
    with open('{}/branch_names'.format(qainit_dir), 'r') as file:
        branches_obj = json.loads(file.read())

    return list(branches_obj.keys())


def qainit_deploy(args):
    return subprocess.run(
        # development only
        #[twig_command, 'suite', 'deploy', args], cwd=qainit_dir, check=True)
        ['twig', 'feature', 'suite', 'deploy', args], cwd=qainit_dir, check=True)


def qainit_shutdown(youtrack_id):
    git.check_repo_cloned('qainit')
    git.sync('qainit')
    branch = git.search_remote_branch('qainit', '*{}*'.format(youtrack_id))
    if branch:
        try:
            git.checkout('qainit', branch)
            git.commit('qainit', 'shutdown', dummy=True)
            git.push('qainit', branch)
        except:
            logger.error(
                "Non sono riuscito a spegnere il qa, per favore spegnilo manualmente!\nDevops are watching you! ( •͡˘ _•͡˘)")

    else:
        logger.warning(
            "Non sono riuscito a trovare un qa per questa issue, se il qa esiste, per favore spegnilo manualmente\nDevops are watching you! ( •͡˘ _•͡˘)")
