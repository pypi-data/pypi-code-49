import json
import logging
import os

import yaml

from miniscule.aws import secrets_manager_constructor
from miniscule.exceptions import MinisculeError

log = logging.getLogger(__name__)


class ConfigLoader(yaml.SafeLoader):
    """Loader that resolves all miniscule tags.  Derives from
    :class:`yaml.SafeLoader` in `PyYAML <https://pypi.org/project/PyYAML/>`_.
    """

    # pylint: disable=too-many-ancestors
    def __init__(self, stream):
        super(ConfigLoader, self).__init__(stream)
        yaml.add_constructor("!or", or_constructor, Loader=ConfigLoader)
        yaml.add_constructor("!env", env_constructor, Loader=ConfigLoader)
        yaml.add_constructor("!merge", merge_constructor, Loader=ConfigLoader)
        yaml.add_constructor(
            "!include/json", include_json_constructor, Loader=ConfigLoader
        )
        yaml.add_constructor(
            "!aws/sm", secrets_manager_constructor, Loader=ConfigLoader
        )


def or_constructor(loader, node):
    for expr in loader.construct_sequence(node):
        if expr is not None:
            return expr
    return None


def env_constructor(loader, node):
    name = loader.construct_yaml_str(node)
    if name in os.environ:
        return yaml.load(os.getenv(name), Loader=loader.__class__)
    return None


def merge_constructor(loader, node):
    result = {}
    for m in loader.construct_sequence(node, deep=True):
        if isinstance(m, dict):
            result.update(m)
        else:
            raise MinisculeError("merge", "Arguments should be maps")
    return result


def include_json_constructor(loader, node):
    path = loader.construct_yaml_str(node)
    try:
        with open(path, "r") as h:
            return json.load(h)
    except FileNotFoundError:
        log.warning("No file at %s", path)
    except json.JSONDecodeError:
        log.warning("Invalid JSON in file %s", path)
    return None


def load_config(stream, Loader=ConfigLoader):
    """Read configuration from a stream.

    :param stream: The stream to read from.
    :param Loader: The loader to use.  This allows clients to extend the list of
        tags that can be resolved.

    :returns: The parsed YAML in which the tags known to :code:`Loader` have been
              resolved.
    """
    return yaml.load(stream, Loader)


def read_config(path=None, Loader=ConfigLoader):
    """Read configuration from a file.

    :param path: Path of the file from which to read the configuration.  If
        None, the path is read from the value of the ``CONFIG`` environment
        variable. If no such variable, path defaults to ``config.yaml``.
    :param Loader: See :func:`miniscule.load_config`.

    :returns: See :func:`miniscule.load_config`.
    """
    path = path or os.environ.get("CONFIG", "config.yaml")
    with open(path, "r") as stream:
        return load_config(stream, Loader=Loader)
