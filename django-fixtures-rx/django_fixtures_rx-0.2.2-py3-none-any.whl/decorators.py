from typing import Callable

from .utilities import get_fixture


def exclude_fixtures(*fixtures_classes_or_accessors):
    def decorator(function: Callable):
        def wrapper(*args, **kwargs):
            for fixture_class_or_accessor in fixtures_classes_or_accessors:
                if isinstance(fixture_class_or_accessor, str):
                    fixture = get_fixture(fixture_class_or_accessor)
                else:
                    fixture = fixture_class_or_accessor(fixture_class_or_accessor.__module__)

                for model in fixture.models:
                    model.objects.using(fixture.database).all().delete()

            return function(*args, **kwargs)

        return wrapper

    return decorator
