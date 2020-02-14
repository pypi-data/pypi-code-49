"""
Templated logging utilizes an optionally provided configuration dictionary to
update default log configurations.

Alternatives to updating the default logging templates can be

    .. code-block:: python

        log_level = logging.INFO # logging.DEBUG, etc.
        log_format = '[%(levelname)8s] %(message)s'
        log_dtfmt = ''
        logging.basicConfig(level=log_level, format=log_format, datefmt=log_dtfmt)

Or,

    .. code-block:: python

        logging.config.dictConfig(config)

For a dictionary logging configuration, ``config``, as below.

For more in-depth information on python logging, see
https://docs.python.org/3.6/library/logging.html
"""

import os.path as op
import json
import logging
import logging.config
import collections.abc

log = logging.getLogger(__name__)


def _recursive_update(template_dict, update_dict):
    """
    Update dictionary template_dict with key/values from dictionary update_dict

    _recursive_update takes two dictionary objects as parameters, template_dict
    and update_dict. The keys of update_dict are iterated through. If the value
    of template_dict key is itself template_dict dictionary the function is
    recursively called on those dictionaries at that level for both
    template_dict and update_dict. When template_dict non-dictionary value is
    encountered, the value for template_dict is updated. If the dictionary
    update_dict has keys that are not present in template_dict, they will be
    added to template_dict recursively. Should these not be valid, they
    will cause an exception in the upstream function.

    Args:
        template_dict (dict): The dictionary to be updated.

        update_dict (dict): The dictionary containing update keys. If
            update_dict is template_dict subset of template_dict, it will
            update just those keys. Else, it will add any keys in update_dict
            not found in template_dict.
    """

    for k, v in update_dict.items():
        if isinstance(v, collections.abc.Mapping):
            _recursive_update(template_dict.get(k, {}), v)
        else:
            template_dict[k] = update_dict[k]


def configure_logging(default_config_name='info', update_config=None):
    """
    Configure logging with default settings or a dictionary of log settings

    __configure_logging__ configures the logging for the gear-toolkit using one
    of either two default json templates (`info`, `debug`--see below).
    Whichever one is used can be updated with optional update_config
    dictionary. With the `update_config` potentially stored within a gear's
    manifest, this function becomes a utility function for the gear toolkit
    context object.

    Args:
        default_config_name (str, optional): A string, 'info' or 'debug',
            indicating the default template to use. Defaults to 'info'.

        update_config (dict, optional): A dictionary containing the keys,
            subkeys, and values of the templates to update.
            Defaults to None.

    Example:
        With

        .. code-block:: python

            config = {
                "formatters": {
                    "gear": {
                        "format": "[TEST] %(levelname)4s %(message)s"
                    }
                }
            }

        ``configure_logging(update_config = config)``

        updates the ['formatters']['gear']['format'] value in the `info`
        default configuration below.

    Note:
        Default logging configuration dictionaries are stored in
        ``<prefix>_default.json``.

        `info`:

        .. code-block:: python

            {
                "version": 1,
                "formatters": {
                    "gear": {
                        "format":"[ %(asctime)3s %(levelname)8s %(name)s: ] %(message)s",
                        "datefmt": "%Y-%m-%d %H:%M:%S"
                    }
                },
                "handlers": {
                    "gear": {
                        "level":"INFO",
                        "formatter": "gear",
                        "class":"logging.StreamHandler"
                    }
                },
                "loggers": {
                    "": {
                        "handlers": ["gear"],
                        "level":"INFO"
                    }
                },
                "disable_existing_loggers": false
            }

        `debug`:

        .. code-block:: python

            {
                "version": 1,
                "formatters": {
                    "gear": {
                        "format": "[ %(asctime)3s %(levelname)8s %(name)s: %(lineno)s - %(funcName)8s() ] %(message)s",
                        "datefmt": "%Y-%m-%d %H:%M:%S"
                    }
                },
                "handlers": {
                    "gear": {
                        "level":"DEBUG",
                        "formatter": "gear",
                        "class":"logging.StreamHandler"
                    }
                },
                "loggers": {
                    "": {
                        "handlers": ["gear"],
                        "level":"DEBUG"
                    }
                },
                "disable_existing_loggers": false
            }
    """

    available_names = ['info', 'debug']

    if default_config_name not in available_names:
        log.warning(
            "The value of %s is not in %s. Reverting to 'info'.",
            default_config_name,
            available_names
        )
        default_config_name = 'info'

    json_file = op.join(
        op.dirname(__file__),
        default_config_name + '_default.json'
    )

    with open(json_file, 'r') as f:
        config = json.load(f)

    if update_config:
        _recursive_update(config, update_config)

    logging.config.dictConfig(config)

    log.info(
        'Log level is %s',
        logging.getLevelName(logging.root.level)
    )
