import abc

import pandas as pd
from typing import Tuple, Callable

from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError
from features_factory.input_features import DateTimeInputFeature


class TwoComponentFeature(FeatureArchetype, metaclass=abc.ABCMeta):
    """
    Two component features are features that map two provided features into a new one.
    This means that there is no need of aggregation.
    It is a simple 2:1 mapping.

    The simplest example is a feature that results from the sum of two features.
    """

    def __init__(self, name: str, first_feature: FeatureArchetype, second_feature: FeatureArchetype,
                 bimap_function: Callable):
        """
        E.g.
            We want to define a feature C that comes from the difference between two features: B - A
            Then we write:

            >   C = TwoComponentFeature('C', A, B, lambda r: r[1] - r[0])

            Notice that the r in the lambda function will contain the two values of A and B, in the order in
            which they are inserted in the TwoComponentFeature initialization.

        :param name:
        :param first_feature:
        :param second_feature:
        :param bimap_function:
        """
        super().__init__(name)
        self._first_feature = first_feature
        self._second_feature = second_feature
        self._bimap_function = bimap_function

    def get_dependencies(self, **kwargs) -> Tuple[FeatureArchetype, FeatureArchetype]:
        return self._first_feature, self._second_feature

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        for dependency in self.get_dependencies():
            name = dependency.name()
            if name not in df.columns:
                ie.add_missing_column(name)
        return ie

    def generate(self, df: pd.DataFrame, **kwargs):
        return df.loc[:, [self._first_feature.name(), self._second_feature.name()]]\
            .apply(self._bimap_function, axis=1)


class DurationFeature(TwoComponentFeature):
    """
    Two component feature that compute the duration of an event. It requires a start_time and an end_time feature.
    """

    def __init__(self, name: str,
                 start_time_feat: DateTimeInputFeature, end_time_feat: DateTimeInputFeature,
                 units: str= 'seconds'):

        super().__init__(name, first_feature=start_time_feat, second_feature=end_time_feat,
                         bimap_function=lambda r: (r[1]-r[0]).total_seconds())

        if units == 'seconds':
            self._format = 'seconds'
        elif units == 'minutes':
            self._format = 'minutes'
        elif units == 'hours':
            self._format = 'hours'
        elif units == 'days':
            self._format = 'days'
        else:
            raise ValueError('units can be only seconds, minutes or hours')

    def generate(self, df: pd.DataFrame, **kwargs):
        diff_seconds = super().generate(df)

        if self._format == 'seconds':
            return diff_seconds
        elif self._format == 'minutes':
            return diff_seconds.apply(lambda x: x/60)
        elif self._format == 'hours':
            return diff_seconds.apply(lambda x: x / 3600)
        elif self._format == 'days':
            return diff_seconds.apply(lambda x: x / 86400)
        else:
            raise RuntimeError('format not recognized: {}'.format(self._format))
