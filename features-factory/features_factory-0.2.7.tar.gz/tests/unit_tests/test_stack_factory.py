import unittest

import pandas as pd

from features_factory.input_features import IntInputFeature, FloatInputFeature
from features_factory.one_component_features import OneComponentFeature
from features_factory.stack_factory import StackFactory


class TestStackFactory(unittest.TestCase):

    def test_clones(self):
        int1 = IntInputFeature('int1')
        int2 = IntInputFeature('int2')
        float1 = FloatInputFeature('float1')

        names = ['2 x int1', '2 x int2', '2 x float1']
        dependencies = [int1, int2, float1]
        args = [{'name': name, 'dependency': feat, 'map_function': lambda x: 2*x}
                for name, feat in zip(names, dependencies)]
        stack = StackFactory.clones(OneComponentFeature, args)

        df = pd.DataFrame({int1.name(): [3, 5, 7], int2.name(): [15, 20, 50], float1.name(): [2.2, 0.1, 5.5]})
        df = stack.with_dependencies().insert_into(df)

        self.assertCountEqual([int1.name(), int2.name(), float1.name()] + names, df.columns)
        self.assertEqual((2*df[int1.name()]).to_list(), df[names[0]].to_list())
        self.assertEqual((2*df[int2.name()]).to_list(), df[names[1]].to_list())
        self.assertEqual((2*df[float1.name()]).to_list(), df[names[2]].to_list())
