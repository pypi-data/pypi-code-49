# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Activity-based loggers."""
from typing import Any, Dict, Iterator, Mapping, MutableMapping, Optional, Tuple
from abc import ABC, abstractmethod
import contextlib
import copy
import logging
import platform

from . import constants as constants
from . import logging_utilities as logging_util


def _merge_kwarg_extra(properties: Dict[str, Any],
                       **kwargs: Any) -> Tuple[MutableMapping[str, Any], Any]:
    """Update and return the kwargs['extra'] as extra and the kwargs that pops extra key."""
    if "extra" in kwargs:
        properties = copy.deepcopy(properties)
        extra = kwargs.pop("extra")
        if "properties" in extra:
            properties.update(extra['properties'])
        extra['properties'] = properties
    else:
        # no need to update properties if no extra
        extra = {'properties': properties}
    return extra, kwargs


class ActivityLogger(logging.LoggerAdapter, ABC):
    """Abstract base class for activity loggers."""

    def __init__(self, logger: logging.Logger, extra: Mapping[str, Any]) -> None:
        """
        Create an activity logger.

        :param logger:
        :param extra:
        """
        self.custom_dimensions = {
            'app_name': constants.DEFAULT_LOGGING_APP_NAME,
            'automl_client': None,
            'automl_sdk_version': None,
            'child_run_id': None,
            'common_core_version': None,
            'compute_target': None,
            'experiment_id': None,
            'os_info': platform.platform(),
            'parent_run_id': None,
            'region': None,
            'service_url': None,
            'subscription_id': None,
            'task_type': None
        }
        super().__init__(logger, extra)

    def update_default_property(self,
                                key: str,
                                value: Any) -> None:
        """Update default property in the class.

        Arguments:
            :param key: The custom dimension key needs to be changed.
            :type key: str
            :param value: The value of the corresponding key.
            :type value: Any

        """
        self.update_default_properties({key: value})

    def update_default_properties(self,
                                  properties_dict: Dict[str, Any]) -> None:
        """Update default properties in the class.

        Arguments:
            :param properties_dict: The dict contains all the properties that need to be updated.
            :type properties_dict: dict

        """
        self.custom_dimensions.update(properties_dict)

    def set_custom_dimensions_on_log_config(self, log_config: logging_util.LogConfig) -> None:
        """
        Log activity with duration and status.

        :param log_config: LogConfig class.
        """
        log_config.set_custom_dimensions(self.custom_dimensions)

    @abstractmethod
    def _log_activity(self,
                      logger: Optional[logging.Logger],
                      activity_name: str,
                      activity_type: Optional[str] = None,
                      custom_dimensions: Optional[Dict[str, Any]] = None) -> Iterator[Optional[Any]]:
        """
        Log activity - should be overridden by subclasses with a proper implementation.

        :param logger:
        :param activity_name:
        :param activity_type:
        :param custom_dimensions:
        :return:
        """
        raise NotImplementedError

    @contextlib.contextmanager
    def log_activity(self,
                     logger: Optional[logging.Logger],
                     activity_name: str,
                     activity_type: Optional[str] = None,
                     custom_dimensions: Optional[Dict[str, Any]] = None) -> Iterator[Optional[Any]]:
        """
        Log an activity using the given logger.

        :param logger:
        :param activity_name:
        :param activity_type:
        :param custom_dimensions:
        :return:
        """
        return self._log_activity(logger, activity_name, activity_type, custom_dimensions)

    def process(self, msg: str, kwargs: MutableMapping[str, Any]) -> Tuple[str, MutableMapping[str, Any]]:
        """
        Process a log message and extras before they are turned into a LogRecord.

        :param msg:
        :param kwargs:
        :return:
        """
        extra, kwargs = _merge_kwarg_extra(self.custom_dimensions, **kwargs)
        kwargs['extra'] = extra
        return msg, kwargs


class DummyActivityLogger(ActivityLogger):
    """Dummy activity logger."""

    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Create a DummyActivityLogger.

        :param logger:
        """
        super().__init__(logger or logging.getLogger(), {})

    def _log_activity(self,
                      logger: Optional[logging.Logger],
                      activity_name: str,
                      activity_type: Optional[str] = None,
                      custom_dimensions: Optional[Dict[str, Any]] = None) -> Iterator[None]:
        """
        Do nothing.

        :param logger:
        :param activity_name:
        :param activity_type:
        :param custom_dimensions:
        """
        yield
