import re
from pathlib import Path
from typing import Any, Dict, NamedTuple, Optional

import git as _git

from ..config import get_user_config
from ..exceptions import RepoLoaderError
from . import base, local

# Git url regex adapted from https://stackoverflow.com/a/22312124/260303
RX_GIT_URL_PREFIX = r"(?P<prefix>(git|ssh|http(s)?))"
RX_GIT_URL_SEPARATOR = r"(?P<separator>(:|@)(//)?)"
RX_GIT_URL_PATH = r"(?P<path>([\w\.@\:/\-~]+)(\.git)?(/)?)"
RX_GIT_URL = re.compile(RX_GIT_URL_PREFIX + RX_GIT_URL_SEPARATOR + RX_GIT_URL_PATH)


class GitUrl(NamedTuple):
    prefix: str
    separator: str
    raw_path: str

    @property
    def path(self) -> str:
        return self.raw_path.replace(":", "/")


def parse_git_url(url: str) -> Optional[GitUrl]:
    match = RX_GIT_URL.match(url)
    if not match:
        return None
    parts = match.groupdict()
    # Ignore typing: mypy can't detect keys in `groupdict`.
    return GitUrl(
        prefix=parts["prefix"], separator=parts["separator"], raw_path=parts["path"]
    )


class GitRepoLoader(base.BaseRepoLoader):
    """Loader for qwikstart task repos stored in git repos."""

    def __init__(self, git_url: str, path: str = ""):
        git_url = resolve_git_url(git_url)
        local_repo_path = get_local_repo_path(git_url)
        if not local_repo_path.exists():
            download_git_repo(git_url, local_repo_path)
        else:
            update_git_repo(local_repo_path)

        local_path = local_repo_path / path
        self._local_loader = local.LocalRepoLoader(str(local_path))

    @property
    def spec_path(self) -> Path:
        return self._local_loader.spec_path

    def can_load_spec(self) -> bool:
        return self._local_loader.can_load_spec()

    def load_raw_task_spec(self) -> Dict[str, Any]:
        return self._local_loader.load_raw_task_spec()


def resolve_git_url(url: str) -> str:
    prefix, _, repo_path = url.partition(":")
    config = get_user_config()
    if prefix in config.git_abbreviations:
        url = config.git_abbreviations[prefix].format(repo_path)
    return url


def get_local_repo_path(url: str) -> Path:
    git_url = parse_git_url(url)
    if git_url is None:
        raise RepoLoaderError(f"Cannot load from repo with no hostname: {url!r}")

    config = get_user_config()
    return config.qwikstart_cache_path / git_url.path


def download_git_repo(repo_url: str, local_path: Path) -> None:
    try:
        _git.Repo.clone_from(repo_url, str(local_path))
    except (_git.NoSuchPathError, _git.GitCommandError):
        raise RepoLoaderError(f"Could not load git repo: {repo_url}")


def update_git_repo(local_path: Path) -> None:
    _git.Repo(str(local_path)).remote().pull()
