import unittest
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import json
import os
from sklearn.datasets import make_classification

import azureml.automl.core
import azureml.automl.runtime
from automl.client.core.common import constants
from azureml.automl.core.constants import SweepingMode
from azureml.automl.runtime.sweeping.meta_sweeper import Sweepers

from .test_meta_sweeper import MetaSweeperStub


class TestSweepers(unittest.TestCase):
    def test_instantiation(self):
        with self.assertRaises(TypeError):
            Sweepers.get("weight")

    def test_sweeper_config(self):
        X, y = make_classification(n_classes=2, class_sep=2, weights=[0.1, 0.9],
                                   n_informative=30, n_redundant=1, flip_y=0,
                                   n_features=50, n_clusters_per_class=50, n_samples=1000, random_state=40)

        meta_sweeper = MetaSweeperStub(constants.Tasks.CLASSIFICATION, timeout_sec=120)
        sweepers = meta_sweeper._build_sweepers(os.getcwd(), X, y, meta_sweeper._enabled_balancer_configs,
                                                sweeping_mode=SweepingMode.Balancing)
        for sweeper in sweepers:
            self.assertIsNotNone(sweeper.config)
            obj_repr = sweeper.__repr__()
            obj_str = sweeper.__str__()
            self.assertEqual(sweeper.config, obj_repr)
            self.assertEqual(sweeper.config, obj_str)
            config_obj = json.loads(sweeper.config)
            self.assertTrue(config_obj['SweeperType'] in ['weight'])
            self.assertTrue(config_obj['DataProvider'] in ['DiskBasedDataProvider', 'InMemoryDataProvider'])
            self.assertTrue(config_obj['BaselineTransforms'] == [""])
            self.assertTrue(config_obj['ExperimentTransforms'] == [""])
            self.assertTrue(config_obj['Estimator'] in ['LogisticRegression',
                                                        'LinearRegression', 'LGBMClassifier', 'LGBMRegressor'])
            self.assertTrue(config_obj['Scorer'] in ['ClassificationScorer', 'RegressionScorer'])
            self.assertTrue(config_obj['Epsilon'] > 0)
            self.assertTrue(config_obj['IncludeBaselineInExperiment'] in [True, False])
            self.assertTrue(config_obj['Task'] == constants.Tasks.CLASSIFICATION)
            self.assertTrue(config_obj['MetricName']in ['accuracy', 'AUC_micro'])
            self.assertTrue(config_obj['UseCrossValidation'] in [True, False])


if __name__ == '__main__':
    unittest.main()
