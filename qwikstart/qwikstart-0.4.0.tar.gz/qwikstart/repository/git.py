from pathlib import Path
from typing import Any, Dict
from urllib.parse import urlparse

import git as _git

from ..config import get_user_config
from ..exceptions import RepoLoaderError
from . import base, local


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
    parsed_url = urlparse(url)
    if parsed_url.hostname is None:
        raise RepoLoaderError(f"Cannot load from repo with no hostname: {url!r}")
    local_repo_path = parsed_url.hostname + str(parsed_url.path)

    config = get_user_config()
    return config.qwikstart_cache_path / local_repo_path


def download_git_repo(repo_url: str, local_path: Path) -> None:
    try:
        _git.Repo.clone_from(repo_url, str(local_path))
    except (_git.NoSuchPathError, _git.GitCommandError):
        raise RepoLoaderError(f"Could not load git repo: {repo_url}")


def update_git_repo(local_path: Path) -> None:
    _git.Repo(str(local_path)).remote().pull()
