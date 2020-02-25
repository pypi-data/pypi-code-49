import abc
from typing import Tuple, Iterable, List

import numpy as np
import pandas as pd

from features_factory.dependencies_error import DependenciesError
from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError
from features_factory.stack import Stack


class ComposedFeature(FeatureArchetype, metaclass=abc.ABCMeta):
    """
    Composed features are features that require aggregation and/or crossing of multiple features.

    This metaclass facilitate the creation of new classes that fall in this framework.
    In fact, to create one, it is sufficient to define the generate() function.
    However, overwriting some functions to extend their functionalities might be necessary.
    """

    def __init__(self, name: str, dependencies: List[FeatureArchetype]):
        super().__init__(name)
        self._dependencies = dependencies
        self._dependencies_names = self._extract_dependencies_names()

    def get_dependencies(self, **kwargs) -> Tuple[FeatureArchetype]:
        return tuple(self._dependencies)

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        for dependency in self.get_dependencies(**kwargs):
            name = dependency.name()
            if name not in df.columns:
                ie.add_missing_column(name)
        return ie

    def _extract_dependencies_names(self) -> List[str]:
        return Stack(features=self.get_dependencies()).names()


class MeanValueForKeyFeature(ComposedFeature):
    """
    Composed feature that compute the mean value for each block based on a key.

    It requires two features:
    - key: the key feature on which data are grouped and means computed
    - values: the feature that contains the values used to compute the means

    E.g.
        Given the DataFrame df

        A    B
        a    1
        a    2
        b    3
        b    7
        b    5
        c    4

        A is used as key
        B is used for the values

        Executing

        >   mean_value_for_key.insert_into(df, averaging=True)

        we obtain

        A    B    mean_value_for_key
        a    1    1.5
        a    2    1.5
        b    3    5
        b    7    5
        b    5    5
        c    4    4

    When inserting this feature, there are tow possibility: compute the average on the current data or not.
    This is specified with the parameter averaging.

    E.g.
        continuing from the previous example, if we now have a new DataFrame

        A    B
        a    1
        b    3
        b    5

        and we call

        >   mean_value_for_key.insert_into(df, averaging=False)

        we will obtain

        A    B    mean_value_for_key
        a    1    1.5
        b    3    5
        b    5    5

        because the mean values have not been computed again. Instead, the previously computed ones have been retained.

        If we call instead

        >   mean_value_for_key.insert_into(df, averaging=True)
        we will obtain

        A    B    mean_value_for_key
        a    1    1
        b    3    4
        b    5    4

    The parameter averaging is useful in most of the methods, for example in get_dependencies().
    In fact, if averaging=False, the values column is not necessary.

    """

    def __init__(self, name: str, key: FeatureArchetype, values: FeatureArchetype):
        """

        :param name:
        :param key: the feature that contains the keys that will be used to aggregate the data and compute the means.
        :param values: the feature that contains the values that will be averaged
        """
        super().__init__(name, [key, values])
        self._key = key
        self._values = values
        self._means = None

    def get_dependencies(self, averaging: bool=True, **kwargs) -> Tuple[FeatureArchetype]:
        if averaging:
            return super().get_dependencies(**kwargs)
        else:
            return tuple([self._key])

    def verify_dependencies(self, features: Iterable[FeatureArchetype],
                            averaging: bool=True, **kwargs) -> DependenciesError:
        return super().verify_dependencies(features, averaging=averaging, **kwargs)

    def verify_input(self, df: pd.DataFrame, averaging: bool=True, **kwargs) -> InputDataError:
        return super().verify_input(df, averaging=averaging, **kwargs)

    def generate(self, df: pd.DataFrame, averaging: bool=True, **kwargs) -> pd.Series:
        """

        :param df:
        :param averaging:
        :return:
        """

        if averaging:
            self._means = df.loc[:, [self._key.name(), self._values.name()]]\
                .groupby(self._key.name()) \
                .agg({self._values.name(): np.mean}) \
                .rename(columns={self._values.name(): self.name()})
        else:
            if self._means is None:
                raise RuntimeError('cannot append mean values if averages have not been computed on '
                                   'a training set before')

        return df.merge(self._means, how='left', on=self._key.name())[self.name()]
