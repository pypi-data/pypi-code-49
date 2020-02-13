# -*- encoding: utf-8 -*-
import os
import re
import subprocess
from subprocess import CalledProcessError
import sys

from halo import Halo
import semver

from suite_py.lib.logger import Logger
from suite_py.lib.config import Config

logger = Logger()
config = Config().load()


def _get_path(repo):
    return os.path.join(config['user']['projects_home'], repo)


def clone(repo):
    subprocess.run(['git', 'clone', 'git@github.com:primait/{}.git'.format(repo)],
                   cwd=config['user']['projects_home'], check=True)


def checkout(repo, branch, new=False):
    try:
        if new:
            subprocess.run(['git', 'checkout', '-b', branch],
                           cwd=_get_path(repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(['git', 'checkout', branch],
                           cwd=_get_path(repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pull(repo, rebase=True)
    except (CalledProcessError) as e:
        if (e.returncode == 128):
            checkout(repo, branch)  # caso checkout -b e branch gia' esistente
        elif (e.returncode == 1):
            # caso checkout normale e branch non esistente
            checkout(repo, branch, new=True)
        else:
            logger.error("Errore eseguendo il comando: {}".format(e))
            sys.exit(-1)


def commit(repo, commit_message='', dummy=False):
    try:
        if dummy:
            subprocess.run(['git', 'commit',  '--allow-empty', '-m',
                            commit_message], cwd=_get_path(repo), check=True)
        else:
            subprocess.run(['git', 'commit',  '-am', commit_message],
                           cwd=_get_path(repo), check=True)
    except (CalledProcessError) as e:
        logger.error("Errore eseguendo il comando: {}".format(e))
        sys.exit(-1)


def push(repo, branch, remote='origin'):
    try:
        subprocess.run(['git', 'push', remote, branch],
                       cwd=_get_path(repo), check=True)
    except (CalledProcessError) as e:
        logger.error("Errore eseguendo il comando: {}".format(e))
        sys.exit(-1)


def pull(repo, rebase=False):
    with Halo(text='Pulling...', spinner='dots', color='magenta'):
        try:
            if rebase:
                subprocess.run(['git', 'pull', "--rebase"],
                               cwd=_get_path(repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.run(['git', 'pull'],
                               cwd=_get_path(repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (CalledProcessError) as e:
            logger.error("Errore eseguendo il comando: {}".format(e))
            sys.exit(-1)


def fetch(repo, remote='origin'):
    with Halo(text='Fetching...', spinner='dots', color='magenta'):
        try:
            subprocess.run(['git', 'fetch', '--quiet'], cwd=_get_path(
                repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['git', 'fetch', '-p', remote, '--quiet'],
                           cwd=_get_path(repo), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (CalledProcessError) as e:
            logger.error("Errore eseguendo il comando: {}".format(e))
            sys.exit(-1)


def sync(repo):
    fetch(repo)
    checkout(repo, 'master')
    pull(repo)


def check_repo_cloned(repo):
    if repo not in os.listdir(config['user']['projects_home']):
        logger.warning(
            "Il progetto non e' presente nella tua home dei progetti, lo clono adesso..")
        clone(repo)


def delete_remote_branch(repo, branch):
    try:
        push(repo, ":{}".format(branch))
        return True
    except BaseException:
        return False


def get_git_username():
    try:
        output = subprocess.run(['git', 'config', 'user.name'],
                                check=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
        output = re.sub("[^A-Za-z]", "", output)
        return re.sub("\n", "", output)
    except (CalledProcessError):
        return None


def get_last_tag(project):
    sync(project)
    return subprocess.check_output(["git", "describe", "--abbrev=0", "--tags"]).decode('utf-8').strip()


def search_remote_branch(repo, regex):
    try:
        output = subprocess.run(['git', 'branch', '-r', '--list', regex],
                                cwd=_get_path(repo), check=True, stdout=subprocess.PIPE)

        return output.stdout.decode("utf-8").strip('\n').strip().strip('origin/')
    except (CalledProcessError):
        return ""


def remote_branch_exists(repo, branch):
    try:
        subprocess.run(['git', 'show-ref', '--quiet', 'refs/remotes/origin/{}'.format(branch)],
                       cwd=_get_path(repo), check=True)
        return True
    except (CalledProcessError):
        return False


def local_branch_exists(repo, branch):
    try:
        subprocess.run(['git', 'show-ref', '--quiet', 'refs/heads/{}'.format(branch)],
                       cwd=_get_path(repo), check=True)
        return True
    except (CalledProcessError):
        return False


def current_branch_name():
    try:
        output = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                                stdout=subprocess.PIPE).stdout.decode('utf-8')
        return re.sub("\n", "", output)
    except (CalledProcessError) as e:
        logger.error("Errore eseguendo il comando: {}".format(e))
        sys.exit(-1)


def is_dirty(repo):
    try:
        subprocess.run(['git', 'diff', '--quiet'], check=True)
        subprocess.run(
            ['git', 'diff', 'HEAD', '--name-only', '--quiet'], check=True)
        return False
    except (CalledProcessError) as e:
        logger.error(
            "Hai modifiche non committate su {} oppure non è un repository!".format(repo))
        sys.exit(-1)


def files_changed_between_commits(from_commit, to_commit):
    p = subprocess.Popen(
        ["git", "diff", from_commit, to_commit, "--name-only"], stdout=subprocess.PIPE)
    result = p.communicate()[0]
    return result.decode('utf-8').splitlines()


def migrations_found(files_changed):
    for file in files_changed:
        if 'migration' in file.lower():
            return True
    return False


def get_last_tag_number(tags):
    for tag in tags:
        if is_semver(tag.name):
            return tag.name
        else:
            continue
    logger.warning("Nessun tag trovato, sto per pubblicare tag 0.1.0")
    return "0.1.0"


def is_semver(tag):
    try:
        return semver.parse(tag)
    except:
        return None
