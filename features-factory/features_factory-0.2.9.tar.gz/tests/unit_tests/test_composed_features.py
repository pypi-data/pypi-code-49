import unittest

import pandas as pd

from features_factory.composed_features import MeanValueForKeyFeature
from features_factory.input_features import InputFeature


class TestMeanLaneCostPerKmFeature(unittest.TestCase):

    def setUp(self):
        self.lane_id = InputFeature('lane_id')
        self.cost_per_km = InputFeature('cost_per_km')
        self.feat = MeanValueForKeyFeature('mean_lane_cost_per_km', key=self.lane_id, values=self.cost_per_km)

        self.df = pd.DataFrame({self.lane_id.name(): ['id1', 'id1', 'id1', 'id2', 'id1', 'id2', 'id3', 'id1'],
                                self.cost_per_km.name(): [1, -1, 3, 0, 2, 4, 3, 0]})
        self.expected_means = [1, 1, 1, 2, 1, 2, 3, 1]

    def test_means_are_computed_correctly(self):
        # compute means
        means = self.feat.generate(self.df, averaging=True)

        self.assertEqual(means.tolist(), self.expected_means)

    def test_raise_error_if_training_is_not_done(self):
        # compute means raise an exception
        with self.assertRaises(RuntimeError):
            self.feat.generate(self.df, averaging=False)

    def test_if_training_is_done_first_then_is_no_more_needed(self):
        # first generate the feature column with averaging=True
        self.feat.generate(self.df, averaging=True)
        # now it is possible to call it with averaging=False
        means = self.feat.generate(self.df, averaging=False)

        self.assertEqual(means.tolist(), self.expected_means)

    def test_get_dependencies_with_different_averaging_values(self):
        self.assertCountEqual((self.lane_id, self.cost_per_km), self.feat.get_dependencies())
        self.assertCountEqual((self.lane_id, self.cost_per_km), self.feat.get_dependencies(averaging=True))
        self.assertCountEqual((self.lane_id, ), self.feat.get_dependencies(averaging=False))

    def test_verify_input_with_averaging_true(self):
        ie = self.feat.verify_input(self.df, averaging=True)
        self.assertTrue(ie.is_empty())

        df = pd.DataFrame({self.lane_id.name(): ['id1', 'id1', 'id1', 'id2', 'id1', 'id2', 'id3', 'id1']})
        ie = self.feat.verify_input(df, averaging=True)
        self.assertFalse(ie.is_empty())

    def test_verify_input_with_averaging_false(self):
        ie = self.feat.verify_input(self.df, averaging=False)
        self.assertTrue(ie.is_empty())

        df = pd.DataFrame({self.lane_id.name(): ['id1', 'id1', 'id1', 'id2', 'id1', 'id2', 'id3', 'id1']})
        ie = self.feat.verify_input(df, averaging=False)
        self.assertTrue(ie.is_empty())

    def test_verify_dependencies_with_averaging_true(self):
        de = self.feat.verify_dependencies([self.lane_id, self.cost_per_km], averaging=True)
        self.assertTrue(de.is_empty())

        de = self.feat.verify_dependencies([self.lane_id], averaging=True)
        self.assertFalse(de.is_empty())

        de = self.feat.verify_dependencies([], averaging=True)
        self.assertFalse(de.is_empty())

    def test_verify_dependencies_with_averaging_false(self):
        de = self.feat.verify_dependencies([self.lane_id, self.cost_per_km], averaging=False)
        self.assertTrue(de.is_empty())

        de = self.feat.verify_dependencies([self.lane_id], averaging=False)
        self.assertTrue(de.is_empty())

        de = self.feat.verify_dependencies([], averaging=False)
        self.assertFalse(de.is_empty())
