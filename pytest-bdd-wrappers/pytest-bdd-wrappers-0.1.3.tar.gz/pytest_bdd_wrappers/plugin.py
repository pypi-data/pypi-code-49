"""Pytest plugin configuration
"""

from pytest_bdd import exceptions

from .steps import Step, StepMarkName

__metaclass__ = type  # pylint: disable=invalid-name,unused-argument


def parents_stack(parent):
    """
    :type parent: _pytest.python.Instance
    :rtype: list[_pytest.python.Instance]
    """
    if not hasattr(parent, "obj"):
        return []
    return [parent] + parents_stack(parent.parent)


class BDDListener:
    """
    pytest-bdd-wrappers hook listener
    """
    def __init__(self, config):
        """
        :type config: _pytest.config.Config
        """
        self.config = config
        self.scenarios = {}
        self.steps = []

    def pytest_pycollect_makeitem(self, collector, name, obj):
        """
        :type collector: _pytest.python.PyCollector
        :type name: str
        :type obj: object
        """
        pytestmark = getattr(obj, "pytestmark", [])
        if not isinstance(pytestmark, list):
            return
        markers = [m for m in pytestmark if StepMarkName.is_bdd_marker(m)]
        for mark in markers:
            self.steps.append(
                Step(mark.kwargs["name"], collector.obj, obj, name)
            )

    def pytest_pyfunc_call(self, pyfuncitem):
        """
        :type pyfuncitem: _pytest.python.Function
        """
        request = getattr(pyfuncitem, "_request")
        scenario_markers = [
            marker for marker in pyfuncitem.own_markers
            if marker.name == "scenario"
        ]
        if not scenario_markers:
            return
        tested_scenario = scenario_markers[0].kwargs["scenario"]

        for step in tested_scenario.steps:
            step_func = self._find_step(step.name, request, pyfuncitem.parent)
            if not step_func:
                raise exceptions.StepDefinitionNotFoundError(
                    "{} {}".format(step.type, step.name)
                )
            step_func()

    def _find_step(self, name, request, scenario_parent):
        """
        :param name: step from bdd feature file
        :type name: str
        :type request: _pytest.fixtures.FixtureRequest
        :type scenario_parent: _pytest.python.Instance
        :rtype: Callable | None
        """
        steps = [s for s in self.steps if s.is_matching(name)]
        parents = parents_stack(scenario_parent)
        mapped_distance = {
            parents.index(parent): step.to_callable(name, request, parent)
            for step in steps
            for parent in parents
            if step.same_parent(parent.obj)  # pylint: disable=no-member
        }
        _, func = min(
            list(mapped_distance.items()) + [(9999, None)],
            key=lambda e: e[0]
        )
        return func


def pytest_configure(config):
    """
    :type config: _pytest.config.Config
    """
    config.pluginmanager.register(BDDListener(config))
