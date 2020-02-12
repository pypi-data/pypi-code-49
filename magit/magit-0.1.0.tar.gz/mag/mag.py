#!/usr/bin/env python

import os

import json
import argparse
from glob import glob
from time import time
from subprocess import check_output, CalledProcessError, STDOUT
from collections import OrderedDict
from multiprocessing.pool import ThreadPool

CONFIG_FILE_PATH = os.environ.get("FAP_CONFIG_PATH", os.path.expanduser("~/.fap"))
REPO_BASE = os.environ.get("FAP_REPO_BASE", os.path.expanduser("~/dev/"))

DEFAULT_CONFIG = {
    "python_repos": [  # The order of the repos is important! This is the order in which the packages will be installed
        "rugatka",
        "dev-tools",
        "forter-scripts",
        "forter-backoffice",
        "forter-secrets",
    ],
    "other_repos": ["crons", "crons_dsl", "kitchen"],
    "overrides": {
        "dev-tools": {"path": os.path.expanduser("~/bin")},
        "forter": {"master_branch": "develop", "submodules": True},
        "analytics": {"master_branch": "develop"},
        "marketing": {"master_branch": "develop"},
    },
    "organization_name": "forter"
}


if os.path.exists(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH) as f:
        config = json.load(f)
    CONFIG = DEFAULT_CONFIG.copy()
    CONFIG.update(config)
else:
    CONFIG = DEFAULT_CONFIG
    with open(CONFIG_FILE_PATH, "w") as f:
        json.dump(DEFAULT_CONFIG, f)

BASE_SSH_GITHUB_URL = "git@github.com:{}".format(CONFIG["organization_name"]) + "{0}.git"


def run_multi_threaded(target, iterable):
    tp = ThreadPool(processes=20)
    tp.map(target, iterable)


def get_override(repo, config_name, default):
    repo_overrides = CONFIG["overrides"].get(repo, {})
    return repo_overrides.get(config_name, default)


def get_path(repo):
    return get_override(repo, "path", os.path.join(REPO_BASE, repo))


class Color(object):
    RESET = "\033[39m"

    LIGHTBLACK_EX = "\033[90m"
    LIGHTRED_EX = "\033[91m"
    LIGHTGREEN_EX = "\033[92m"
    LIGHTYELLOW_EX = "\033[93m"
    LIGHTBLUE_EX = "\033[94m"
    LIGHTMAGENTA_EX = "\033[95m"
    LIGHTCYAN_EX = "\033[96m"
    LIGHTWHITE_EX = "\033[97m"


class Logger(object):
    @staticmethod
    def red(msg):
        return Color.LIGHTRED_EX + msg + Color.RESET

    @staticmethod
    def yellow(msg):
        return Color.LIGHTYELLOW_EX + msg + Color.RESET

    @staticmethod
    def green(msg):
        return Color.LIGHTGREEN_EX + msg + Color.RESET

    @staticmethod
    def blue(msg):
        return Color.LIGHTBLUE_EX + msg + Color.RESET

    def error(self, msg, should_exit=True):
        print(self.red(msg))
        if should_exit:
            exit(1)

    @staticmethod
    def log(repo, line):
        repo = Color.LIGHTGREEN_EX + repo
        print("{0:<45}| {1}{2}".format(repo, line, Color.RESET))

    def header(self, header):
        header = self.blue(header)
        print("{s:{c}^{n}}".format(s=header, n=40, c="-"))

    def log_multiline(self, repo, output):
        first_line = True
        for line in output.split("\n"):
            if line:
                line = Color.LIGHTYELLOW_EX + line
                self.log(repo if first_line else "", line)
                first_line = False

    def log_status(self, line, repo):
        if not line:
            return

        if len(line.split()) == 2:
            status_out, line = line.split()
            status_out = Color.LIGHTRED_EX + status_out
            line = Color.LIGHTGREEN_EX + line
            line = "{0} {1}".format(status_out, line)
        else:
            line = Color.LIGHTGREEN_EX + line

        self.log(repo, line)

    def log_install(self, line, name, verbose):
        if not line:
            return

        if verbose or line.startswith("Successfully installed"):
            line = Color.LIGHTYELLOW_EX + line
            self.log(name, line)


logger = Logger()


class Git(object):
    def __init__(self, repo=None):
        self._repo = repo
        self._path = get_path(repo) if repo else None
        self._git_args = self._get_git_args()

    @staticmethod
    def _validate_git():
        try:
            check_output(["git", "--version"])
        except OSError:
            logger.error("git is not installed on the computer")

    def validate_repo(self, repo=None):
        repo_path = get_path(repo) if repo else self._path
        if not os.path.exists(repo_path):
            msg = "Folder `{0}` does not exist".format(repo_path)
            return logger.red(msg)

        try:
            self.status()
        except CalledProcessError as e:
            if "Not a git repository" in str(e):
                msg = "`{0}` is not a git repository".format(repo_path)
            else:
                msg = str(e)
            return logger.red(msg)

        return None

    def _git(self, *args, **kwargs):
        return check_output(["git"] + self._git_args + list(args), stderr=STDOUT, **kwargs)

    def status(self):
        return self._git("status", "-s").strip()

    def _get_git_args(self):
        self._validate_git()
        if not self._repo:
            return []

        return ["--no-pager", "--git-dir", os.path.join(self._path, ".git"), "--work-tree", self._path]

    def get_current_branch_or_tag(self, hide_tags=False):
        """
        Get the value of HEAD, if it's not detached, or emit the
        tag name, if it's an exact match. Throw an error otherwise
        """
        branch = self._git("rev-parse", "--abbrev-ref", "HEAD").strip()
        if hide_tags:
            return branch

        tags = self._git("tag", "--points-at", "HEAD").split()
        result = branch if branch != "HEAD" else ""

        if tags:
            tags = ", ".join(tags)
            tags = logger.yellow("[{0}]".format(tags))
            result = "{0} {1}".format(result, tags).strip()
        return result

    def pull(self):
        return self._git("pull")

    def fetch(self):
        return self._git("fetch", "-ap")

    def checkout(self, branch):
        return self._git("checkout", branch)

    def submodule_update(self):
        return self._git("submodule", "update", cwd=self._path)

    def _git_clone(self, repo, branch, shallow):
        full_url = BASE_SSH_GITHUB_URL.format(repo)
        args = [full_url, self._path, "--branch", branch]
        if shallow:
            args += ["--depth", 1]
        self._git("clone", *args)

    def clone_repo(self, repo, repo_branch, shallow):
        if not self.validate_repo(repo):
            return logger.yellow("Folder already exists. " "Repo probably already cloned")
        else:
            self._git_clone(repo, repo_branch, shallow)
            return logger.green("Successfully cloned `{0}`".format(repo))


class Repos(object):
    def __init__(self, branch="master", all=False):
        if all:
            all_dirs = glob("{}/*".format(REPO_BASE))
            repos = [os.path.basename(d) for d in all_dirs if not Git(d).validate_repo()]
            for repo_name, rule in CONFIG["overrides"].iteritems():
                if "path" in rule:
                    repos.append(repo_name)
            self._repos = OrderedDict((repo, branch) for repo in sorted(repos))
        else:
            all_repos = CONFIG["python_repos"] + CONFIG["other_repos"]
            self._repos = OrderedDict((repo, branch) for repo in all_repos)

    @property
    def repos(self):
        return self._repos.iteritems()

    @staticmethod
    def create_repo_base():
        if not os.path.exists(REPO_BASE):
            print(logger.yellow("Creating base repos dir: {0}".format(REPO_BASE)))
            os.makedirs(REPO_BASE)


def status(args):
    logger.header("Status")
    repos = Repos(all=args.all)
    for repo, _ in repos.repos:
        git = Git(repo)
        output = git.validate_repo()
        if output:
            logger.log(repo, output)
            continue

        branch = git.get_current_branch_or_tag(hide_tags=True)
        logger.log(repo, branch)

        for line in git.status().split("\n"):
            logger.log_status(line, repo)
    return


def pull(args):
    def _pull_repo(repo):
        git = Git(repo)
        try:
            output = git.pull()
        except CalledProcessError as ex:
            output = "Pull failed: {}".format(str(ex))
        logger.log_multiline(repo, output)

        if get_override(repo, "submodules", False):
            output = git.submodule_update()
            logger.log_multiline(repo, output)

    repos = Repos(all=args.all)
    logger.header("Pull")
    run_multi_threaded(target=_pull_repo, iterable=[repo for repo, _ in repos.repos])


def fetch(args):
    def _fetch_repo(repo):
        git = Git(repo)
        try:
            git.fetch()
            output = "Fetched all branches and deleted old ones"
        except CalledProcessError as ex:
            output = "Fetch failed: {}".format(str(ex))
        logger.log_multiline(repo, output)

    repos = Repos(all=args.all)
    logger.header("Fetch")
    run_multi_threaded(target=_fetch_repo, iterable=[repo for repo, _ in repos.repos])


def install(args):
    logger.header("Install")

    for repo in CONFIG["python_repos"]:
        repo_path = get_path(repo)
        if not os.path.exists(repo_path):
            msg = logger.red("Folder `{0}` does not exist".format(repo_path))
            logger.log(repo, msg)
            continue

        try:
            output = check_output(["pip", "install", "-e", repo_path])
        except Exception as e:
            error = Color.LIGHTRED_EX + "Could not pip install " "repo: {0}".format(e)
            logger.log(repo, error)
            continue

        for line in output.split("\n"):
            logger.log_install(line, repo, args.verbose)


def checkout(args):
    repos = Repos(args.branch, all=args.all)
    logger.header("Checkout")
    for repo, repo_branch in repos.repos:
        git = Git(repo)
        try:
            if repo_branch == "master":
                repo_branch = get_override(repo, "master_branch", "master")
            git.checkout(repo_branch)
            branch = git.get_current_branch_or_tag(hide_tags=True)
            logger.log(repo, branch)
        except CalledProcessError:
            output = "Could not checkout branch `{0}`".format(repo_branch)
            logger.log_multiline(repo, output)


def clone(args):
    repos = Repos()

    logger.header("Clone")
    repos.create_repo_base()
    git = Git()

    def _clone_repo(repo, repo_branch, shallow):
        try:
            output = git.clone_repo(repo, repo_branch, shallow)
        except CalledProcessError as e:
            error = str(e)

            if "fatal: destination path" in error:
                error = "Repo is probably already cloned (the folder exists)"
            if "fatal: Could not read from remote repository" in error:
                error = "Make sure you have your GitHub SSH key set up"

            output = "Could not clone repo `{0}`: {1}".format(repo, error)
            output = logger.red(output)

        logger.log_multiline(repo, output)

    run_multi_threaded(
        target=_clone_repo, iterable=[(repo, repo_branch, args.shallow) for repo, repo_branch in repos.repos]
    )


def parse_args():
    parser = argparse.ArgumentParser(description="A tool for manipulating multiple repositories simultaneously")
    subparsers = parser.add_subparsers()

    status_subparser = subparsers.add_parser("status", help="List current branch and file changes in all repos")
    status_subparser.add_argument("-a", "--all", action="store_true")
    status_subparser.set_defaults(func=status)

    pull_subparser = subparsers.add_parser("pull", help="Git pull all repos")
    pull_subparser.add_argument("-a", "--all", action="store_true")
    pull_subparser.set_defaults(func=pull)

    fetch_subparser = subparsers.add_parser("fetch", help="Git fetch all repos")
    fetch_subparser.add_argument("-a", "--all", action="store_true")
    fetch_subparser.set_defaults(func=fetch)

    install_subparser = subparsers.add_parser("install", help="Pip install all python repos")
    install_subparser.add_argument("-v", "--verbose", action="store_true", default=False)
    install_subparser.set_defaults(func=install)

    checkout_subparser = subparsers.add_parser("checkout", help="Checkout all repos to chosen branch (if exists)")
    checkout_subparser.add_argument("branch")
    checkout_subparser.add_argument("-a", "--all", action="store_true")
    checkout_subparser.set_defaults(func=checkout)

    clone_subparser = subparsers.add_parser("clone", help="Clone all repos")
    clone_subparser.add_argument("-s", "--shallow", action="store_true")
    clone_subparser.set_defaults(func=clone)

    return parser.parse_args()


def main():
    start_time = time()
    print_time = True
    try:
        fap_args = parse_args()
        fap_args.func(fap_args)
    except (KeyboardInterrupt, KeyError):
        logger.error("Quitting...")
    except BaseException as e:
        logger.error(str(e))
        print_time = False
    finally:
        if print_time:
            end_time = time()
            logger.header("Took {:.2f} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
