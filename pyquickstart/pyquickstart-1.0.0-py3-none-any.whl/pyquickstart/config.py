from pathlib import Path

from pyquickstart.error import ConfigurationError


def find_project_root(start_path, root_file):
    if (start_path / root_file).is_file():
        return start_path

    if start_path == Path(Path('.').root):
        raise ConfigurationError(
            'Could not find the project root, arrived at system root.'
        )

    return find_project_root(start_path.parent, root_file)


ROOT_FILE = 'CHANGELOG.md'
PROJECT_ROOT = Path(find_project_root(Path(__file__).parent, ROOT_FILE))
