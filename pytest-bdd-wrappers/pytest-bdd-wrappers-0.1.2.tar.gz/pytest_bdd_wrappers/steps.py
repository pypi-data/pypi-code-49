"""BDD Steps decorators
"""
import inspect
import textwrap
from enum import Enum
from functools import partial

import pytest
from _pytest.fixtures import getfixturemarker
from _pytest.python import Class
from pytest_bdd.parsers import get_parser, StepParser, parse

from .utils import IS_PYTHON2, get_args_spec

__metaclass__ = type  # pylint: disable=invalid-name,unused-argument


def fixture_name(fixture):
    """
    :param fixture: Callable
    :rtype: str | None
    """
    marker = getfixturemarker(fixture)
    return marker and (marker.name or fixture.__name__)


def _python2_fixtures(fixtures):  # pragma: nocover
    context = {"pytest": pytest}
    context.update(fixtures)

    class_definition = textwrap.dedent(
        """
        class Fixtures:
            pass
        """
    )
    fixture_definitions = [
        textwrap.dedent(
            """
            @pytest.fixture(name="{name}")
            def _get_fixture_{name}(self):
                return {name}
            """
        ).format(name=name).replace("\n", "\n    ")
        for name in fixtures
    ]

    code = class_definition + "\n".join(fixture_definitions)
    exec(code, context)  # pylint: disable=exec-used
    return context["Fixtures"]


def _python3_fixtures(fixtures):  # pragma: nocover
    return type(
        "Fixtures",
        (object,),
        {
            # pylint: disable=cell-var-from-loop
            k: pytest.fixture(name=k)(lambda: v)
            for k, v in fixtures.items()
        }
    )


def add_fixtures(request, **fixtures):
    """
    :type request: _pytest.fixtures.FixtureRequest
    :param fixtures: kwargs with fixtures to add to request fixture manager
    :type fixtures: dict
    """
    fixtures = (
        _python2_fixtures(fixtures)
        if IS_PYTHON2
        else _python3_fixtures(fixtures)
    )
    manager = getattr(request, "_fixturemanager")
    manager.pytest_plugin_registered(fixtures)


class Step:
    """
    Object representing pytest step function.
    """
    def __init__(self, pattern, parent, func, item_name):
        """
        :param pattern: step pattern
        :type pattern: StepParser | str
        :type item_name: str
        :rtype parent: object
        :rtype func: Callable
        """
        self._pattern = (
            pattern
            if isinstance(pattern, StepParser)
            else parse(pattern)
        )
        self._parser = get_parser(self._pattern)
        self._parent = parent
        self._callable = func
        self._item_name = item_name

    def is_matching(self, name):
        """
        :param name: name of step from bdd feature file
        :type name: str
        :rtype: bool
        """
        return self._parser.is_matching(name)

    def same_parent(self, parent):
        """
        Check if same object or StepDef.parent is class for passed parent
        :type parent: object | type
        :rtype: bool
        """
        is_instance_of_step_parent = (
            inspect.isclass(parent)
            and isinstance(self._parent, parent)
        )
        return is_instance_of_step_parent or parent == self._parent

    def to_callable(self, name, request, parent):
        """
        :param name: step from bdd feature file
        :type name: str
        :type request: _pytest.fixtures.FixtureRequest
        :type parent: _pytest.python.Instance
        :return: Callable
        """

        def call():
            add_fixtures(request, **self._parser.parse_arguments(name))

            func = (
                self._fixture_call(name, request)
                or self._method_call(parent, request)
                or self._callable
            )
            args = {
                arg: request.getfixturevalue(arg)
                for arg in get_args_spec(func)
            }
            return func(**args)

        return call

    def _fixture_call(self, name, request):
        """
        :param name: name of step from bdd feature file
        :type name: str
        :type request: _pytest.fixtures.FixtureRequest
        :rtype: Callable | None
        """
        name = fixture_name(self._callable)
        return name and (lambda: request.getfixturevalue(name))

    def _method_call(self, parent, request):
        """
        :type parent: _pytest.python.Instance
        :type request: _pytest.fixtures.FixtureRequest
        :rtype: Callable | None
        """
        if isinstance(parent, Class):
            return partial(self._callable, request.instance)
        return None


class StepMarkName(Enum):
    """Available BDD steps mark names.
    """
    GIVEN = "bdd_given"
    WHEN = "bdd_when"
    THEN = "bdd_then"

    @classmethod
    def is_bdd_marker(cls, marker):
        """
        :type marker: _pytest.mark.Mark
        :rtype: bool
        """
        try:
            return bool(StepMarkName(marker.name))
        except ValueError:
            return False


def mark_step(step_mark, name):
    """
    Decorator for bdd steps.

    :type step_mark: StepMarkName
    :param name: Name of step from feature file
    :type name: str
    :return: Wrapper for step function
    """

    def wrap(func):
        mark = getattr(pytest.mark, step_mark.value)
        return mark(name=name, step=step_mark)(func)

    return wrap


__all__ = ['Step', 'StepMarkName', 'mark_step']
