# -*- coding: utf-8 -*-
#
# Copyright 2015 Spotify AB
# Modifications copyright (C) 2018 databand.ai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
The abstract :py:class:`Target` class.
It is a central concept of databand and represents the state of the workflow.
"""

import abc
import logging
import typing

from typing import Any, Dict, Optional

import six

from dbnd._core.utils.basics.nothing import NOTHING


if typing.TYPE_CHECKING:
    from dbnd._core.task.task import Task
    from targets.metrics.target_value_metrics import ValueMetrics


logger = logging.getLogger(__name__)


class TargetSource(object):
    def __init__(self, task_id, parameter_name=None, name=None):
        self.task_id = task_id
        self.parameter_name = parameter_name
        self.name = name


@six.add_metaclass(abc.ABCMeta)
class Target(object):
    """
    A Target is a resource generated by a :py:class:`~dbnd.tasks.Task`.

    For example, a Target might correspond to a file in HDFS or data in a database. The Target
    interface defines one method that must be overridden: :py:meth:`exists`, which signifies if the
    Target has been created or not.

    Typically, a :py:class:`~dbnd.tasks.Task` will define one or more Targets as output, and the Task
    is considered complete if and only if each of its output Targets exist.
    """

    def __init__(self, properties=None, source=None):
        # type: (Dict[str, Any], TargetSource)->None
        super(Target, self).__init__()
        self.properties = properties or {}
        self.source = source

        # caching and value preview
        self.value_metrics = NOTHING  # type: ValueMetrics
        self._cache = {}

    @abc.abstractmethod
    def exists(self):
        """
        Returns ``True`` if the :py:class:`Target` exists and ``False`` otherwise.
        """
        pass

    def exist_after_write_consistent(self):
        return True

    @property
    def name(self):
        if self.source_parameter:
            return self.source_parameter.name
        return None

    @property
    def source_task(self):
        # type: ()->Optional[Task]
        if self.source:
            from dbnd._core.current import get_task_by_task_id

            return get_task_by_task_id(self.source.task_id)
        return None

    @property
    def task(self):
        # type: ()->Optional[Task]
        return self.source_task

    @property
    def source_parameter(self):
        if self.source:
            return self.source_task._params.get_param(self.source.parameter_name)
        return None

    def clear_cache(self):
        self._cache = {}
