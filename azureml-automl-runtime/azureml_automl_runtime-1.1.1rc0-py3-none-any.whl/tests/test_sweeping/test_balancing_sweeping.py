import logging
import os
import unittest
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups, make_classification

from azureml.automl.runtime.column_purpose_detection import ColumnPurposeDetector
from automl.client.core.common.constants import Tasks
from automl.client.core.common.activity_logger import DummyActivityLogger
from azureml.automl.core import constants

from .test_meta_sweeper import MetaSweeperStub, MetaSweeperTest


def _create_dummy_data():
    X, y = make_classification(n_classes=2, class_sep=2, weights=[0.1, 0.9],
                               n_informative=30, n_redundant=1, flip_y=0,
                               n_features=50, n_clusters_per_class=50, n_samples=1000, random_state=40)
    return X, y


def _create_newsgroup20_sampled():
    removedata = ('headers', 'footers', 'quotes')
    categories = ['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
    data_train = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42,
                                    remove=removedata)
    sampled_X = pd.DataFrame(data_train.data[:300])
    sampled_y = data_train.target[:300]
    return sampled_X, sampled_y


def _test_balancing_sweep_with_feature_sweep(task, config_overrides, result_expected=True, enable_dnn=True,
                                             transformer_name=None, balancing_strategy_name=None,
                                             is_cross_validation=False):
    X, y = _create_newsgroup20_sampled()
    meta_sweeper = MetaSweeperStub(task, config_overrides=config_overrides, enable_dnn=enable_dnn,
                                   is_cross_validation=is_cross_validation)
    # Run feature sweeping
    stats_and_column_purposes = ColumnPurposeDetector.get_raw_stats_and_column_purposes(X)
    ret_feature_sweep = meta_sweeper.sweep(os.getcwd(), X, y, stats_and_column_purposes)
    print("Added sweepers are: " + str(ret_feature_sweep) if ret_feature_sweep is not None else "None")
    # Transform raw data to feature vector
    X_vec = []
    for cols, tfs in ret_feature_sweep:
        for col in cols:
            X_col = pd.DataFrame(X[col])
            X_vec.extend(tfs.transform(X_col))
    # Run balancing sweeping secondly
    ret_balancing_sweep = meta_sweeper.sweep(os.getcwd(), X_vec, y, sweeping_mode=constants.SweepingMode.Balancing)
    print("Added sweepers are: " + str(ret_balancing_sweep) if ret_balancing_sweep is not None else "None")
    if result_expected:
        assert ret_feature_sweep is not None
        assert len(ret_feature_sweep) > 0
        # Check transformer_name occurs in the list of transformers swept over
        if transformer_name is not None:
            assert str(ret_feature_sweep).__contains__(transformer_name)

        assert ret_balancing_sweep is not None
        assert len(ret_balancing_sweep) > 0
        # Check balancing_strategy_name occurs in the list of transformers swept over
        if balancing_strategy_name is not None:
            assert str(ret_balancing_sweep).__contains__(balancing_strategy_name)
    else:
        assert len(ret_feature_sweep) == 1
        assert len(ret_balancing_sweep) == 1


def _test_balancing_sweep(task, config_overrides, result_expected=True, enable_dnn=False, balancing_strategy_name=None,
                          is_cross_validation=False, logger=None):
    X, y = _create_dummy_data()
    meta_sweeper = MetaSweeperStub(task, config_overrides=config_overrides, enable_dnn=enable_dnn,
                                   is_cross_validation=is_cross_validation)
    if logger:
        meta_sweeper._logger = logger
    ret = meta_sweeper.sweep(os.getcwd(), X, y, sweeping_mode=constants.SweepingMode.Balancing)
    print("Added sweepers are: " + str(ret) if ret is not None else "None")
    if result_expected:
        assert ret is not None
        assert len(ret) > 0
        # Check balancing_strategy_name occurs in the list of transformers swept over
        if balancing_strategy_name is not None:
            assert str(ret).__contains__(balancing_strategy_name)
    else:
        assert len(ret) == 1


class BalancingSweeperTest(unittest.TestCase):
    # create a balancing sweeper
    balancing_sweeper = {
        "name": "ClassWeight",
        "type": "weight",
        "enabled": True,
        "sampler": {
            "id": "count",
            "args": [],
            "kwargs": {}
        },
        "estimator": "logistic_regression",
        "scorer": "AUC_micro",
        "epsilon": 0.001,
    }

    def test_balancing_sweeper_isolation(self):
        config = {
            "classification": {
                "sweeping_enabled": False,
                "enable_class_balancing": True,
                "page_sampled_data_to_disk": True,
                "run_sweeping_in_isolation": True,
                "enabled_sweepers": [],
                "enabled_balancers": [BalancingSweeperTest.balancing_sweeper]
            }
        }
        _test_balancing_sweep(Tasks.CLASSIFICATION, config,
                              result_expected=False, is_cross_validation=False)

    def test_balancing_sweeper_in_process(self):
        config = {
            "classification": {
                "sweeping_enabled": False,
                "enable_class_balancing": True,
                "page_sampled_data_to_disk": True,
                "run_sweeping_in_isolation": False,
                "enabled_sweepers": [],
                "enabled_balancers": [BalancingSweeperTest.balancing_sweeper]
            }
        }
        _test_balancing_sweep(Tasks.CLASSIFICATION, config,
                              result_expected=False, is_cross_validation=False)

    def test_balancing_sweep_with_feature_sweep(self):
        config = {
            "classification": {
                "sweeping_enabled": True,
                "enable_class_balancing": True,
                "page_sampled_data_to_disk": False,
                "run_sweeping_in_isolation": False,
                "enabled_sweepers": [MetaSweeperTest.nonconcat_bert_sweeper,
                                     MetaSweeperTest.word_embedding_concat_sweeper],
                "enabled_balancers": [BalancingSweeperTest.balancing_sweeper]
            }
        }
        _test_balancing_sweep_with_feature_sweep(Tasks.CLASSIFICATION,
                                                 config,
                                                 transformer_name="wordembeddingtransformer",
                                                 balancing_strategy_name="ClassWeight",
                                                 result_expected=True,
                                                 is_cross_validation=False)

    def test_balancing_sweep_isolation_with_logger(self):
        config = {
            "classification": {
                "sweeping_enabled": False,
                "enable_class_balancing": True,
                "page_sampled_data_to_disk": False,
                "run_sweeping_in_isolation": True,
                "enabled_sweepers": [],
                "enabled_balancers": [BalancingSweeperTest.balancing_sweeper]
            }
        }
        logger = DummyActivityLogger()
        _test_balancing_sweep(Tasks.CLASSIFICATION, config,
                              result_expected=False, is_cross_validation=False, logger=logger)


if __name__ == '__main__':
    unittest.main()
