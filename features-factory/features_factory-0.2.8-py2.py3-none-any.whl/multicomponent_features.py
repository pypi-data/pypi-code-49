import abc
from typing import Callable, List, Tuple

import pandas as pd

from features_factory.feature_archetype import FeatureArchetype
from features_factory.input_data_error import InputDataError


class MultiComponentFeature(FeatureArchetype, metaclass=abc.ABCMeta):
    """
    Multi-component features are features that map multiple provided features into a new one.
    This means that there is no need of aggregation.
    It is a simple n:1 mapping.

    The simplest example is a feature that results from the sum of multiple features.
    """

    def __init__(self, name: str, dependencies: List[FeatureArchetype], mmap_function: Callable):
        """
        E.g.
            We want to define a feature F that comes from the sum of 5 features: A + B + C + D + E
            Then we write:

            >   F = TwoComponentFeature('F', [A, B, C, D, E], lambda r: r[0] + r[1] + r[2] + r[3] + r[4])

            Notice that the r in the lambda function will contain the two values of A, B, C, D, and E in the order in
            which they are inserted in the MultiComponentFeature initialization.

        :param name:
        :param dependencies:
        :param mmap_function:
        """
        super().__init__(name)
        self._dependencies = dependencies
        self._mmap_function = mmap_function

    def get_dependencies(self, **kwargs) -> Tuple[FeatureArchetype]:
        return tuple(self._dependencies)

    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        ie = InputDataError()
        for dependency in self.get_dependencies():
            name = dependency.name()
            if name not in df.columns:
                ie.add_missing_column(name)
        return ie

    def generate(self, df: pd.DataFrame, **kwargs):
        return df.loc[:, [f.name() for f in self._dependencies]]\
            .apply(self._mmap_function, axis=1)
