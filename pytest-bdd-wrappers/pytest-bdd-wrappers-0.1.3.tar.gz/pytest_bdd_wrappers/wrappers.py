from functools import partial

import pytest
from pytest_bdd import exceptions
from pytest_bdd.feature import Feature
from pytest_bdd.scenario import get_features_base_dir, get_strict_gherkin
from pytest_bdd.steps import get_caller_module

from .utils import _wrap_function_with_additional_arguments
from .steps import StepMarkName, mark_step


def scenario(
        feature_name,
        scenario_name,
        encoding="utf-8",
        features_base_dir=None,
        example_converters=None
):
    """
    Scenario decorator.

    :param str feature_name: Feature file name.
        Absolute or relative to the configured feature base path.
    :param str scenario_name: Scenario name.
    :param str encoding: Feature file encoding.
    :param str | None features_base_dir: path to directory with feature
    :param example_converters: Dict of example value converting functions
    :type example_converters: dict[ValueName, Callable[[Value], Converted]]
    """
    if features_base_dir is None:
        features_base_dir = get_features_base_dir(get_caller_module())
    feature = Feature.get_feature(
        features_base_dir,
        feature_name,
        encoding=encoding,
        strict_gherkin=get_strict_gherkin(),
    )

    if scenario_name not in feature.scenarios:
        msg = (
            u'Scenario "{scenario_name}" in feature "{feature_name}"'
            u" in {feature_filename} is not found."
        ).format(
            scenario_name=scenario_name,
            feature_name=feature.name or "[Empty]",
            feature_filename=feature.filename,
        )
        raise exceptions.ScenarioNotFound(msg)

    tested_scenario = feature.scenarios[scenario_name]
    tested_scenario.example_converters = example_converters
    tested_scenario.validate()

    def wrap(func):
        example_params = tested_scenario.get_example_params()

        if example_params:
            func = _wrap_function_with_additional_arguments(
                func, example_params,
            )

            for params in tested_scenario.get_params():
                if params:
                    pytest.mark.parametrize(*params)(func)

        pytest.mark.scenario(scenario=tested_scenario)(func)
        return func

    return wrap


def given(name, fixture=None):
    """
    :param name: Name of step from feature file
    :type name: str
    :param fixture: alternative name for fixture
    :type fixture: str | None
    :return: Wrapper for given function
    """

    def wrap(func):
        if not hasattr(func, "_pytestfixturefunction"):
            func = pytest.fixture(name=fixture)(func)
        return mark_step(StepMarkName.GIVEN, name)(func)

    return wrap


when = partial(mark_step, StepMarkName.WHEN)  # pylint: disable=invalid-name
then = partial(mark_step, StepMarkName.THEN)  # pylint: disable=invalid-name

__all__ = ['scenario', 'given', 'when', 'then']
