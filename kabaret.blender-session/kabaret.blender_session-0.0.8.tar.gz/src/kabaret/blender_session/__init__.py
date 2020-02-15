import os

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions


def get_blender_startup_dir():
    from . import user_scripts

    return os.path.dirname(user_scripts.__file__)
