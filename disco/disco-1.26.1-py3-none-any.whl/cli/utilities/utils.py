import pkg_resources
import requests
import packaging.version

DISCO_PACKAGE = 'disco'


def _installed_version(package):
    """Gets the version of an installed (pip) cli package

    Args:
        package: the package name.

    Returns:
        str: The version of the installed package.
    """
    try:
        dist = pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        return None

    return str(dist.version)


def disco_cli_version():
    """Gets Dis.co's cli version.

    Returns:
        str: The version of the installed package.
    """
    return _installed_version(DISCO_PACKAGE)


def _latest_version(package=None):
    """Gets the version of package on pypi.python.org

    Args:
        package: the package name.

    Returns:
        str: The latest version of the package.
    """
    try:
        package = package or 'disco'
        url = f'https://pypi.python.org/pypi/{package}/json'
        req = requests.get(url)
        if req.status_code == requests.codes.ok:  # pylint: disable=no-member
            data = req.json()
            version = data['info']['version']
            return version
        return None
    except Exception:  # pylint: disable=broad-except
        return None


def is_update_needed():
    """Checks whether there is a newer version available

    Returns
        bool: 'True' if there is a newer version, 'False' otherwise
    """
    current_ver = disco_cli_version()
    latest_ver = _latest_version(DISCO_PACKAGE)

    if current_ver is None or latest_ver is None:
        return False

    return packaging.version.parse(latest_ver) > packaging.version.parse(current_ver)
