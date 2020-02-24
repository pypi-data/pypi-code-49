from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from azureml.studio.common.datatable.data_table import DataTable
from azureml.studio.modulehost.constants import ElementTypeName
from azureml.studio.modulehost.module_host_executor import execute

assert_array_almost_equal = np.testing.assert_array_almost_equal
assert_array_equal = np.testing.assert_array_equal


@pytest.fixture
def conftest_data_path():
    return Path(__file__).parent / 'tests/conftest'


@pytest.fixture
def input_dt_german_credit_card_uci(conftest_data_path):
    df = pd.read_csv(conftest_data_path / 'german_credit_card_uci_data.csv')
    return DataTable(df)


@pytest.fixture
def input_dt_adult_census_income(conftest_data_path):
    df = pd.read_csv(conftest_data_path / 'adult_census_income_data.csv')
    return DataTable(df)


@pytest.fixture
def input_train_test_df_check_col_type_compatible(conftest_data_path):
    input_path = conftest_data_path / 'check_col_type_compatible/'
    data_type = {'f0': np.int16, 'f1': np.float64, 'f2': str, 'label': np.int16}
    train_df = pd.read_csv(input_path / 'train.csv', dtype=data_type)
    test_df = pd.read_csv(input_path / 'test_negative.csv')
    return train_df, test_df


@pytest.fixture
def input_df_clientid_unique_values_dataset(conftest_data_path):
    return pd.read_csv(conftest_data_path / 'unique_values_dataset/clientid_data.tsv',
                       sep='\t')


@pytest.fixture
def input_df_text_unique_values_dataset(conftest_data_path):
    return pd.read_csv(conftest_data_path / 'unique_values_dataset/text_data.tsv', sep='\t')


@pytest.fixture
def run_train_cluster_model_e2e():
    def _run_train_cluster_model_e2e(untrained_model_dir, input_data_dir, trained_model_dir, output_data_dir):
        execute([
            '--module-name=azureml.studio.modules.ml.train.train_clustering_model.train_clustering_model',
            '--untrained-model', untrained_model_dir,
            '--dataset', input_data_dir,
            '--trained-model', trained_model_dir,
            '--results-dataset', output_data_dir,
            '--column-set={\"isFilter\":true,\"rules\":[{\"exclude\":false,\"ruleType\":\"AllColumns\"}]}',
            '--check-for-append-or-uncheck-for-result-only=True'
        ])

    return _run_train_cluster_model_e2e


@pytest.fixture
def run_train_generic_model_e2e():
    def _run_train_generic_model_e2e(untrained_model_dir, input_data_dir, trained_model_dir):
        execute([
            '--module-name=azureml.studio.modules.ml.train.train_generic_model.train_generic_model',
            '--untrained-model', untrained_model_dir,
            '--dataset', input_data_dir,
            '--trained-model', trained_model_dir,
            '--label-column={\"isFilter\":true,\"rules\":[{\"exclude\":false,\"ruleType\":\"ColumnNames\",\"columns\":'
            '[\"class\"]}]}'
        ])

    return _run_train_generic_model_e2e


@pytest.fixture
def run_train_anomaly_detection_model_e2e():
    def _run_train_anomaly_detection_model_e2e(untrained_model_dir, input_data_dir, trained_model_dir):
        execute([
            '--module-name=azureml.studio.modules.anomaly_detection.train_anomaly_detection.train_anomaly_detection',
            '--untrained-model', untrained_model_dir,
            '--dataset', input_data_dir,
            '--trained-model', trained_model_dir
        ])

    return _run_train_anomaly_detection_model_e2e


@pytest.fixture
def run_tune_hyper_e2e():
    def _run_tune_hyper_e2e(untrained_model_dir, input_data_dir, trained_model_dir, tune_result_dir):
        execute([
            '--module-name=azureml.studio.modules.ml.train.tune_model_hyperparameters.tune_model_hyperparameters',
            '--untrained-model', untrained_model_dir,
            '--training-dataset', input_data_dir,
            '--sweep-results', tune_result_dir,
            '--trained-best-model', trained_model_dir,
            '--specify-parameter-sweeping-mode', "Random sweep",
            '--maximum-number-of-runs-on-random-sweep=5',
            '--random-seed=0',
            '--name-or-numerical-index-of-the-label-column='
            '{\"isFilter\":true,\"rules\":[{\"exclude\":false,\"ruleType\":'
            '\"ColumnNames\",\"columns\":[\"class\"]}]}',
            '--metric-for-measuring-performance-for-classification=Accuracy',
            '--metric-for-measuring-performance-for-regression', "Mean absolute error"
        ])

    return _run_tune_hyper_e2e


@pytest.fixture
def run_score_generic_e2e():
    def _run_score_generic_e2e(trained_model_dir, input_data_dir, scored_data_dir):
        execute([
            '--module-name=azureml.studio.modules.ml.score.score_generic_module.score_generic_module',
            '--trained-model', trained_model_dir,
            '--dataset', input_data_dir,
            '--scored-dataset', scored_data_dir,
            '--append-score-columns-to-output=True'
        ])

    return _run_score_generic_e2e


@pytest.fixture
def assert_data_table_equals():
    def _assert_data_table_equals(data_table_ref, data_table_now):
        """
        check two data table is equals.
        1. their column names
        2. not float column: strict equals
        3. float column: almost equals up to desired precision.
        :param data_table_ref: reference data table
        :param data_table_now: new output data table
        :return: None
        """
        assert set(data_table_now.column_names) == set(data_table_ref.column_names)
        for column_name in data_table_ref.column_names:
            s1 = data_table_now.get_column(column_name)
            s2 = data_table_ref.get_column(column_name)
            if data_table_now.get_element_type(column_name) == ElementTypeName.FLOAT:
                assert_array_almost_equal(s1, s2)
            else:
                assert_array_equal(s1, s2)

    return _assert_data_table_equals
