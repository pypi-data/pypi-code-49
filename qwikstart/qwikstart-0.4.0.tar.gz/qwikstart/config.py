import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

import yaml

from . import utils
from .exceptions import ConfigurationError

logger = logging.getLogger(__name__)

QWIKSTART_CONFIG_FILE = Path("~/.qwikstart/config.yml").expanduser()

DEFAULT_CONFIG_DICT: Dict[str, Any] = {
    "qwikstart_cache": "~/.qwikstart/cached_repos",
    "git_abbreviations": {
        "gh": "https://github.com/{0}",
        "gl": "https://gitlab.com/{0}",
        "bb": "https://bitbucket.org/{0}",
    },
}


@dataclass(frozen=True)
class Config:
    qwikstart_cache: str
    git_abbreviations: Dict[str, str]

    @property
    def qwikstart_cache_path(self) -> Path:
        return Path(self.qwikstart_cache).expanduser()


def get_user_config() -> Config:
    user_config = load_custom_config_file()
    known_config_keys = set(utils.get_dataclass_keys(Config))

    unknown_config_keys = set(user_config).difference(known_config_keys)
    if unknown_config_keys:
        logger.warning(
            f"User config, {QWIKSTART_CONFIG_FILE}, contains unknown keys: "
            "{unknown_config_keys}. Ignoring extra keys."
        )
        user_config = {k: v for k, v in user_config.items() if k in known_config_keys}

    return Config(**utils.merge_nested_dicts(DEFAULT_CONFIG_DICT, user_config))


def load_custom_config_file() -> Dict[str, Any]:
    if QWIKSTART_CONFIG_FILE.exists():
        with QWIKSTART_CONFIG_FILE.open() as f:
            logger.debug(f"Loading user config from {QWIKSTART_CONFIG_FILE}")
            user_config = yaml.safe_load(f)

            if not user_config:
                return {}

            if not isinstance(user_config, dict):
                msg = f"Expected {QWIKSTART_CONFIG_FILE} to contain a dictionary."
                raise ConfigurationError(msg)

            return user_config

    logger.debug(f"No user config found at {QWIKSTART_CONFIG_FILE}")
    return {}
