from pathlib import Path

from pytest import raises

from {{cookiecutter.project}}.config import find_project_root, PROJECT_ROOT, ROOT_FILE
from {{cookiecutter.project}}.error import ConfigurationError


def test_project_root_exists():
    assert PROJECT_ROOT.is_dir()


def test_project_root_file_exists():
    assert (PROJECT_ROOT / ROOT_FILE).is_file()


def test_project_root_not_found():
    with raises(ConfigurationError):
        find_project_root(Path(Path('.').root), 'nonexisting_filename.xyz')
