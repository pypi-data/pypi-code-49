import abc
from typing import Tuple, Callable, Union

import pandas as pd

from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError
from features_factory.input_features import InputFeature, StringInputFeature, DateTimeInputFeature, DateInputFeature


class OneComponentFeature(FeatureArchetype, metaclass=abc.ABCMeta):
    """
    One component features are features that map one provided feature into a new one.
    This means that there is no need of aggregation or crossing of multiple features.
    It is a simple 1:1 mapping.

    In the simplest possible scenario, a simple feature could be used to rename a feature.
    """

    def __init__(self, name: str, dependency: InputFeature, map_function: Callable):
        """

        :param name: name of the feature
        :param dependency: feature needed to generate this new feature
        :param map_function: a lambda function that maps the dependency feature into the new feature
        """
        super().__init__(name)
        self._dependency = dependency
        self._map_function = map_function

    def get_dependencies(self, **kwargs) -> Tuple[InputFeature]:
        return self._dependency,

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        if self._dependency.name() not in df.columns:
            ie.add_missing_column(self._dependency.name())
        return ie

    def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
        return df[self.get_dependencies()[0].name()].apply(self._map_function)


class RenamedFeature(OneComponentFeature):
    """
    Create a new column, with values identical to the original one
    """

    def __init__(self, name: str, dependency: InputFeature):
        super().__init__(name, dependency, lambda x: x)


class DateTimeFromStringFeature(OneComponentFeature):
    """
    One component feature that given a datetime expressed as string, convert it into datetime using
    the pandas function to_datetime()
    """

    def __init__(self, name: str, dependency: StringInputFeature):
        super().__init__(name, dependency, lambda x: pd.to_datetime(x))


class DateFromStringFeature(OneComponentFeature):
    """
    One component feature that given a date (or even datetime) expressed as string, convert it into date using
    the pandas function to_datetime() and then extracting the date
    """

    def __init__(self, name: str, dependency: StringInputFeature):
        super().__init__(name, dependency, lambda x: pd.to_datetime(x).date())


class MonthFromDateFeature(OneComponentFeature):
    """
    One component feature that given a dependency representing a date, extract the month (1=January, 12=December)
    """

    def __init__(self, name: str, dependency: Union[DateTimeInputFeature, DateInputFeature]):
        super().__init__(name, dependency, lambda x: x.month)


class WeekdayFromDateFeature(OneComponentFeature):
    """
    One component feature that given a dependency representing a date, extract the weekday.
    Represent the day of the week as an integer, where Monday is 0 and Sunday is 6
    """

    def __init__(self, name: str, dependency: Union[DateTimeInputFeature, DateInputFeature]):
        super().__init__(name, dependency, lambda x: x.weekday())
