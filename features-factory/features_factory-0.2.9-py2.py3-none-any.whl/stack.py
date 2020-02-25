from typing import Iterable, List

import pandas as pd

from features_factory.feature_archetype import FeatureArchetype
from features_factory.stack_error import StackError


class Stack:
    """
    A class that makes easy to work with a set of Features, dealing with inter-dependencies.

    A Stack can be though as a set of features.
    Order in which features are inserted does not matter.
    Duplicate features are automatically discarded.

    Once some features are inserted is very easy to:
    * automatically include all the dependencies, using with_dependencies()
    * restrict them only to the input features, using with_input_features_only()

    A Stack makes very easy to verify if all dependencies are satisfied and a pd.DataFrame is usable, using verify().
    Once you inserted all the features in the stack, you will not have bother verifying them one by one.
    Dependencies are handled automatically.

    A Stack makes super-easy to insert the features in a pd.DataFrame, using insert_into().
    Features are inserted starting from the lowest one in the hierarchy, going up.
    For example, if you have a feature D, built on top of C, built on top of A and B, Stack will first
    compute and insert the features A and B, then C, and then finally D.
    """

    lbl_error_type = 'error_type'
    lbl_involved_features = 'involved_features'

    def __init__(self, features: Iterable[FeatureArchetype]=tuple()):
        """
        Create a new Stack.

        E.g.
                stack = Stack([A, B])
            is equivalent to
                stack = FeaturesbuildingBlock()
                stack.add(A)
                stack.add(B)

        :param features:
        """
        self._features = list()

        for feat in features:
            self.add(feat)

    def __len__(self):
        """
        Make possible to know how many features are contained in the FeatureBuildingBlock using the len operator.

        E.g.
            the code:
                stack = Stack([A, B])
                print(len(stack))
            will return:
                2

        :return:
        """
        return len(self._features)

    def __iter__(self):
        """
        Make possible to iterate through the Stack.

        E.g.
            the code:
                stack = Stack([A, B])
                for feat in stack:
                    print(feat.get_name())

            will result in:
                A
                B

        :return:
        """
        return self._features.__iter__()

    def __getitem__(self, item):
        """
        Make possible to access a feature part of the stack as if it were an array.

        E.g.
            stack = Stack([A, B])
            [...]
            feat_A = stack[0]
            feat_B = stack[1]

        :param item:
        :return:
        """
        return self._features[item]

    def __add__(self, other):
        """
        Make possible to add two Stack.

        E.g.
            Stack([A, B, C, D]) + Stack([A, C, E, G])
                = Stack([A, B, C, D, E, G])

        :param other:
        :return:
        """
        result = Stack(self)
        for feat in other:
            result.add(feat)
        return result

    def add(self, feat: FeatureArchetype):
        """
        Add a single feature to the Stack.
        IMPORTANT: If a feature with the same name is already present, then it will not be added.

        :param feat:
        :return:
        """
        if not isinstance(feat, FeatureArchetype):
            raise RuntimeError('ModelFeatures.add() accepts only child objects of the class FeatureArchetype')

        if feat not in self:
            self._features.append(feat)

    def remove(self, feat: FeatureArchetype):
        """
        Remove a single feature from the Stack.
        If the argument is not a child class of FeatureArchetype or is not contained in the building block,
        an exception is raised.

        :param feat:
        :return:
        """
        self._features.remove(feat)

    def clear(self):
        """
        Remove all the features from the Stack.

        :return:
        """
        self._features.clear()

    def names(self) -> List[str]:
        """
        Return a tuple with all the names of the features

        :return:
        """
        return [feat.name() for feat in self._features]

    def with_dependencies(self, **kwargs):
        """
        Return a new stack equal to the current Stack (self), but including the dependencies

        :return: Stack
        """
        result = Stack(self)
        for feat in result:
            for dependency in feat.get_dependencies(**kwargs):
                result.add(dependency)
        return result

    def with_input_features_only(self):
        """
        Return a new stack that contains only the input features contained in the current Stack (self)
        :return:
        """
        return Stack([feat for feat in self if feat.is_input()])

    def verify(self, df: pd.DataFrame, **kwargs) -> StackError:
        """
        Verify that:
        1. the provided DataFrame contains all the required columns
        2. for each feature there are all the dependencies

        :param df:
        :return:
        """
        bbe = StackError()

        for feat in self:
            # verify input data
            if feat.is_input():
                bbe.add_input_data_error(feat.verify_input(df, **kwargs))
            # verify dependencies
            bbe.add_dependency_error(feat.verify_dependencies(self, **kwargs))

        return bbe

    def insert_into(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Insert all the features in the DataFrame, solving the inter-dependencies

        :param df:
        :param kwargs: optional named arguments that might be needed for the single features
        :return: enriched df
        """
        # check that all required dependencies are present
        se = self.verify(df, **kwargs)
        if not se.is_empty():
            raise RuntimeError('during the execution of Stack.insert_into(df), '
                               'an error occurred.\n{}'.format(se.to_string()))

        already_inserted_features = list()

        while len(already_inserted_features) < len(self._features):

            not_inserted_features = list(set(self._features) - set(already_inserted_features))

            features_to_insert_at_this_iteration = [feat for feat in not_inserted_features
                                                    if set(feat.get_dependencies(**kwargs))
                                                        .issubset(already_inserted_features)]

            for feat in features_to_insert_at_this_iteration:
                df = feat.insert_into(df, **kwargs)
                already_inserted_features.append(feat)

        return df

    def filter_out_input_subgroups_smaller_than_n(self, df: pd.DataFrame, min_size: int) -> (pd.DataFrame, list, list):
        """
        Given a DataFrame, break it in subsets according to the features. Then, throw away the subsets with less than
        min_size elements. Finally, reconstruct the DataFrame with the data that "survived" the process.
        The function will then return a 3-tuple with:
        - the filtered DataFrame
        - the valid keys, i.e. the feature combinations that survived the process
        - the dropped keys, i.e. the feature combinations that did not survive the process

        E.g.
            Input:
                features: [A, B]
                df: A: 1, 1, 2, 3, 3, 3
                    B: a, a, b, b, c, d
                    C: y, n, y, n, y, n
                min_size: 2

            Result:
                df: A: 1, 1
                    B: a, a
                    C: y, n
                valid_keys: [(1, a)]
                dropped_keys: [(2, b), (3, b), (3, c), (3, d]

        :param df:
        :param min_size:
        :return: (filtered df, valid keys, dropped keys)
        """
        # verify that all the required columns are present
        missing_columns = [name for name in self.names() if name not in df.columns]
        if len(missing_columns) > 0:
            raise RuntimeError('the execution of Stack.filter_out_input_subgroups_smaller_than_n() '
                               'is not possible because the columns {} are missing'.format(missing_columns))

        # work with a copy of df
        dfc = df.copy()

        valid_keys = list()
        dropped_keys = list()
        for key, dg in dfc.groupby(self.names()):
            if len(dg) >= min_size:
                valid_keys.append(key)
            else:
                dropped_keys.append(key)

        if len(valid_keys) > 0:
            # label for the original index of the df, that should be kept
            lbl_original_index = '__original_index'
            # store the original index in a column
            dfc[lbl_original_index] = dfc.index
            # - make the input features the new index
            # - keep only the data with valid key
            # - make the input features columns again
            # - set as index the column containing the original index
            dfc = dfc.set_index(self.names()).loc[valid_keys, :].reset_index().set_index(lbl_original_index)
            # remove the name of the index
            dfc.index.name = None
        else:
            dfc = dfc.drop(index=dfc.index)

        return dfc, valid_keys, dropped_keys
