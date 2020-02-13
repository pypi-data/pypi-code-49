import abc
from typing import Tuple, Iterable

import pandas as pd

from features_factory.dependencies_error import DependenciesError
from features_factory.input_data_error import InputDataError


class FeatureArchetype(metaclass=abc.ABCMeta):
    """
    Base metaclass for Features.

    Features can be distinguished in:
    - input features
    - features built on top of the input features, that we can name artificial or derived features

    The input features represent a column in the provided df.
    This feature exist only for the sake of checking whether a column with the needed input feature exist and
    that it is in the correct format
    """

    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        """
        Return the feature name
        :return:
        """
        return self._name

    @abc.abstractmethod
    def get_dependencies(self, **kwargs) -> Tuple:
        """
        Return a tuple containing the features necessary to build this feature.
        Notice that if there are no dependencies it means that the feature is an input feature.
        :return: tuple of features (child objects of BaseFeature)
        """

    def is_input(self) -> bool:
        """
        Is it an input feature (meaning that should be present in the starting DataFrame)?
        :return:
        """
        return True if len(self.get_dependencies()) == 0 else False

    @abc.abstractmethod
    def verify_input(self, df: pd.DataFrame, **kwargs) -> InputDataError:
        """
        Return True if input data meet required criteria, False otherwise.
        Criteria:
        - the required columns are present
        - (optional) the format of the columns is correct
        - (optional) NaN are not present in the columns

        Notice that while input features can be fed with the original DataFrame, derived features should be fed
        with a DataFrame after inserting all the required features into the DataFrame.

        Example:

            features: A, B
            feature we want to run verify_input for: sum(dependencies: A, B)

            Given df, we should first run:
                df = A.insert_into(df)
                df = B.insert_into(df)
            and only at this point it makes sense to run:
                sum.verify_input(df)

        To better deal with the artificial feature complexity we recommend using the class Stack,
        which automatically deals with it.

        :param df: pd.DataFrame to check
        :param kwargs: [optional]
        :return:
        """

    def verify_dependencies(self, features: Iterable, **kwargs) -> DependenciesError:
        de = DependenciesError()
        de.add_missing_dependencies(self.name(), [feat.name() for feat in set(self.get_dependencies(**kwargs)) - set(features)])
        return de

    @abc.abstractmethod
    def generate(self, df: pd.DataFrame, **kwargs) -> pd.Series:
        """
        Given a DataFrame guaranteed to have the required columns, return a Series containing the generated feature
        :param df:
        :param kwargs: [optional]
        :return:
        """

    def insert_into(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Given a DataFrame, return a copy of it with the feature.
        IMPORTANT: if a column in the df has the same name as this feature, its values will be overwritten.
        :param df:
        :param kwargs: [optional]
        :return:
        """
        # check that all required dependencies are present
        ie = self.verify_input(df, **kwargs)
        if not ie.is_empty():
            raise RuntimeError('during the execution of {}.insert_into(df), df did not '
                               'fulfill the expected requirements.\n{}'.format(self.name(),
                                                                               ie.to_string()))

        # make a copy of the passed df, so that the original remains unmodified
        df_copy = df.copy()

        # generate the feature df
        feature = self.generate(df_copy, **kwargs)

        # insert the feature in the df. This mean that if there is a name overlap, there will be an overwriting
        df_copy = df_copy.assign(**{self.name(): feature.values})

        return df_copy
