from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .extract_pages import *  # noqa: F401, E402, F403
