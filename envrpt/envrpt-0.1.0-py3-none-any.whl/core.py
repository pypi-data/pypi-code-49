
import json
import subprocess  # noqa: B404
import sys

from datetime import datetime
from email import message_from_string

from pip import __version__ as pip_version
from pip._internal.utils.misc import (
    get_installed_distributions,
    dist_is_editable,
    dist_in_usersite,
    dist_is_local,
)
from pip._vendor.packaging.specifiers import SpecifierSet
from pip._vendor.pkg_resources import get_distribution

from .vulnerabilities import identify_vulnerable_packages


def get_environment():
    env = {}

    version = get_distribution('envrpt').version
    env['analyzer'] = 'envrpt/%s' % (version,)
    env['date_analyzed'] = datetime.now()

    ver = sys.version_info
    env['python_version'] = '%s.%s.%s' % (ver.major, ver.minor, ver.micro)
    env['pip_version'] = pip_version

    env['platform'] = sys.platform

    env['runtime'] = sys.implementation.name
    ver = sys.implementation.version
    env['runtime_version'] = '%s.%s.%s' % (ver.major, ver.minor, ver.micro)

    env['base_directory'] = sys.prefix

    return env


def get_pkg_info(pkg_info, key):
    if key in pkg_info and pkg_info[key] != 'UNKNOWN':
        return pkg_info[key]
    return None


def make_package(dist):
    pkg_info = message_from_string(dist.get_metadata(dist.PKG_INFO))

    pkg = {
        'key': dist.key,
        'name': dist.project_name,
        'version': dist.version,
        'description': get_pkg_info(pkg_info, 'Summary'),
        'license': get_pkg_info(pkg_info, 'License'),
        'home_page': get_pkg_info(pkg_info, 'Home-page'),
        'is_editable': dist_is_editable(dist),
        'in_user_site': dist_in_usersite(dist),
        'in_global_site': not dist_is_local(dist),
        'requirements': {
            req.key: str(req.specifier) or None
            for req in dist.requires()
        },
        'issues': [],
    }

    return pkg


def get_packages():
    distributions = get_installed_distributions(
        local_only=False,
        include_editables=True,
        editables_only=False,
        user_only=False,
    )

    packages = {
        pkg['key']: pkg
        for pkg in [
            make_package(dist)
            for dist in distributions
        ]
    }

    return packages


def identify_requirement_conflicts(environment):
    packages = environment['packages']
    for pkg in packages.values():
        for key, version in pkg['requirements'].items():
            if key in packages:
                if version:
                    if packages[key]['version'] not in SpecifierSet(version):
                        pkg['issues'].append({
                            'type': 'REQ_INVALID',
                            'key': key,
                            'requirement': version,
                            'installed': packages[key]['version'],
                        })
            else:
                pkg['issues'].append({
                    'type': 'REQ_MISSING',
                    'key': key,
                    'requirement': version,
                })


def identify_outdated_packages(environment):
    output = subprocess.check_output([  # noqa: B603
        sys.executable,
        '-m', 'pip',
        'list',
        '--outdated',
        '--format=json',
        '--disable-pip-version-check',
    ])

    outdated = {
        pkg['name']: pkg['latest_version']
        for pkg in json.loads(output.decode('utf-8'))
    }

    for pkg in environment['packages'].values():
        if pkg['name'] in outdated:
            pkg['issues'].append({
                'type': 'OUTDATED',
                'latest_version': outdated[pkg['name']],
            })


def analyze_environment(outdated_packages=False, vulnerable_packages=False):
    """
    Analyzes the current Python environment and returns the information in a
    dictionary.

    :param outdated_packages:
        indicates whether or not to check for the existance of newer versions
        of installed packages; if not specified, defaults to False
    :type outdated_packages: bool
    :param vulnerable_packages:
        indicates whether or not to check if the installed packages are known
        to have vulnerabilities; if not specified, defaults to False
    :type vulnerable_packages: bool
    :rtype: dict
    """

    env = get_environment()
    env['packages'] = get_packages()

    identify_requirement_conflicts(env)

    if outdated_packages:
        identify_outdated_packages(env)

    if vulnerable_packages:
        identify_vulnerable_packages(env)

    return env

