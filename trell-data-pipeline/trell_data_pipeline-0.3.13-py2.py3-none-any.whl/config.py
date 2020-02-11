from typing import Dict
from pathlib import Path

import yaml
from yaml.parser import ParserError

from pipeline.types import T


class ConfigLoadError(Exception):
    ''' Custom error to thrown when error occurs while loading the config. '''
    pass


def load_config_file(config_file: Path) -> Dict[str, T]:
    """
    Load a YAML config file from the given path.
    Raises:
        ConfigLoadError if config file could not be loaded.
    Returns:
         The parsed config values.
    """

    try:
        file = open(str(config_file), 'r')
        config = yaml.load(file)
        file.close()

    except IOError as exception:
        raise ConfigLoadError(
            'Failed opening config file: {msg}.'.format(msg=exception)
        ) from exception

    except (ParserError, TypeError) as exception:
        raise ConfigLoadError(
            'Failed parsing config file: {msg}'.format(msg=exception)
        ) from exception

    else:
        return config
