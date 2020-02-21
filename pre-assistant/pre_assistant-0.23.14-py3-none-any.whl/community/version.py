from pkg_resources import get_distribution, DistributionNotFound

# default if we can't find something else
__DEFAULT_VERSION = "UNDEFINED - this package is not installed"


def __get_dist_version(dist_name):
    """Read version from distribution if installed as a non editable package."""

    try:
        dist = get_distribution(dist_name)
        if not __dist_is_editable(dist):
            return dist.version
        else:
            # if installed as editable, we don't want to use the installed version,
            # but rather calculate from scm
            return None
    except DistributionNotFound:
        return None


def __get_scm_version():
    """Use git tags to read the package version."""

    try:
        from setuptools_scm import get_version

        return get_version(root="../../../..", relative_to=__file__)
    except (ImportError, LookupError):
        return None


def __dist_is_editable(dist) -> bool:
    """Return True if given Distribution is an editable install."""
    import sys
    import os

    for path_item in sys.path:
        egg_link = os.path.join(path_item, dist.project_name + ".egg-link")
        if os.path.isfile(egg_link):
            return True
    return False


def __get_version(dist_name):
    """Try to find the best version string to describe the current install."""
    return __get_dist_version(dist_name) or __get_scm_version() or __DEFAULT_VERSION


__version__ = __get_version("rasa-x")
