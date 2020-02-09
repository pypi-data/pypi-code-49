import importlib.util
import inspect
import os
from types import ModuleType
from typing import List
from typing import TYPE_CHECKING

from django.apps import apps

from . import exceptions
from .exceptions import FixturesNotFound

if TYPE_CHECKING:
    from .fixtures import BaseFixture


def snake_case(camel_name: str, divider: str = '-') -> str:
    snake_case_name = ''

    for index, symbol in enumerate(camel_name):
        if symbol.isupper() and index not in [0, len(camel_name) - 1] and not camel_name[index + 1].isupper():
            snake_case_name += divider

        snake_case_name += symbol.lower()

    return snake_case_name


def get_apps_labels() -> List[str]:
    return [app.label for app in apps.get_app_configs()]


def get_app_path(app_label: str) -> str:
    return apps.get_app_config(app_label).path


def get_fixtures_path(app_label: str):
    return os.path.join(get_app_path(app_label), 'fixtures')


def get_fixture_filepath(app_label: str, name: str) -> str:
    fixtures_path = get_fixtures_path(app_label)

    if not os.path.isdir(fixtures_path):
        os.mkdir(fixtures_path)

    return os.path.join(fixtures_path, f'{name}.json')


def get_fixtures_module(app_label: str) -> ModuleType:
    try:
        fixtures_filepath = os.path.sep.join([get_app_path(app_label), 'fixtures.py'])
        spec = importlib.util.spec_from_file_location(app_label, fixtures_filepath)
        spec.loader.exec_module(module := importlib.util.module_from_spec(spec))
    except FileNotFoundError:
        raise FixturesNotFound(app_label)

    return module


def is_fixture_class(class_: type) -> bool:
    from .fixtures import BaseFixture
    return hasattr(class_, '__mro__') and BaseFixture in inspect.getmro(class_)


def lookup_fixtures(app_label: str = None) -> List['BaseFixture']:
    apps_labels, fixtures = [app_label] if app_label else get_apps_labels(), []

    for app_label in apps_labels:
        try:
            fixtures_module = get_fixtures_module(app_label)
        except (LookupError, exceptions.FixturesNotFound):
            continue

        for name, fixture_class in inspect.getmembers(fixtures_module, is_fixture_class):
            if not inspect.isabstract(fixture_class):
                fixtures.append(fixture_class(app_label))

    return fixtures


def get_fixture(accessor: str) -> 'BaseFixture':
    app_label, fixture_name = accessor.split('.', 1)

    try:
        fixtures_module = get_fixtures_module(app_label)
    except (LookupError, exceptions.FixturesNotFound):
        raise exceptions.FixtureNotFound(accessor)

    if hasattr(fixtures_module, fixture_name):
        return getattr(fixtures_module, fixture_name)(app_label)
    else:
        raise exceptions.FixtureNotFound(accessor)


def get_fixtures(*accessors: str) -> List['BaseFixture']:
    fixtures = [] if accessors else lookup_fixtures()

    for accessor in accessors:
        if '.' not in accessor:
            if not len(fixtures_lookup := lookup_fixtures(accessor)):
                raise exceptions.FixturesNotFound(accessor)

            fixtures += fixtures_lookup
        else:
            fixtures.append(get_fixture(accessor))

    return fixtures
