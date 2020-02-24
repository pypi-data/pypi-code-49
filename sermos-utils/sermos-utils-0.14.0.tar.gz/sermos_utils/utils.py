""" Generic utilities
"""
import os
import logging
from sermos_utils.constants import ENV_VAR_DEPLOY_KEY, ENV_VAR_PKG_NAME

logger = logging.getLogger(__name__)


def normalized_pkg_name(pkg_name: str, dashed: bool = False):
    """ We maintain consistency by always specifying the package name as
        the "dashed version".

        Python/setuptools will replace "_" with "-" but resource_filename()
        expects the exact directory name, essentially. In order to keep it
        simple upstream and *always* provide package name as the dashed
        version, we do replacement here to 'normalize' both versions to
        whichever convention you need at the time.

        if `dashed`:
            my-package-name --> my-package-name
            my_package_name --> my-package-name

        else:
            my-package-name --> my_package_name
            my_package_name --> my_package_name
    """
    if dashed:
        return str(pkg_name).replace('_', '-')
    return str(pkg_name).replace('-', '_')


def get_deploy_key(deploy_key: str = None):
    """ Verify deploy key provided, get from environment if None.

        Raise if neither provided nor found.

        Arguments:
            deploy_key (optional): Deployment key, issued by Sermos, that
                dictates the environment into which this request will be
                deployed. Defaults to checking the environment for
                `SERMOS_DEPLOY_KEY`. If not found, will exit.
    """
    deploy_key = deploy_key if deploy_key\
        else os.environ.get(ENV_VAR_DEPLOY_KEY, None)
    if deploy_key is None:
        msg = "Unable to find `deploy-key` in CLI arguments nor in "\
            "environment under `{}`".format(ENV_VAR_DEPLOY_KEY)
        logger.error(msg)
        raise ValueError(msg)
    return deploy_key


def get_client_pkg_name(pkg_name: str = None):
    """ Verify the package name provided and get from environment if None.

        Raise if neither provided nor found.

        Arguments:
          pkg_name (optional): Directory name for your Python
                    package. e.g. my_package_name . If none provided, will check
                    environment for `SERMOS_CLIENT_PKG_NAME`. If not found,
                    will exit.
    """
    pkg_name = pkg_name if pkg_name\
        else os.environ.get(ENV_VAR_PKG_NAME, None)
    if pkg_name is None:
        msg = "Unable to find `pkg-name` in CLI arguments nor in "\
            "environment under `{}`".format(ENV_VAR_PKG_NAME)
        logger.error(msg)
        raise ValueError(msg)
    return pkg_name
