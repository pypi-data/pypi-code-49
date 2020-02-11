# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Utilities that could be used from AutoML after training for explaining AutoML models."""
from typing import List, Optional, Any, Tuple, Union, cast, Dict

import json
import logging
import time

import pandas as pd
import numpy as np
import scipy
from azureml._restclient.constants import RunStatus
from nimbusml import DprepDataStream, Pipeline as NimbusMLPipeline
from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline, Pipeline

from azureml.automl.runtime.onnx_convert import OnnxConverter
from azureml.automl.runtime.onnx_convert import OnnxInferenceHelper
from azureml.automl.runtime.onnx_convert import OnnxFeaturizerHelper
from azureml.automl.runtime.onnx_convert import OnnxInferenceFromFeaturesHelper
from azureml.automl.core import dataprep_utilities, package_utilities
from azureml.automl.runtime.featurization.streaming import StreamingFeaturizationTransformer
from azureml.automl.runtime.training_utilities import LargeDatasetLimit
from azureml.data import TabularDataset
from azureml.core import Run
from automl.client.core.common import constants, logging_utilities
from automl.client.core.common.exceptions import ArgumentException
from azureml.automl.core.console_interface import ConsoleInterface
from automl.client.core.runtime.types import DataInputType, DataSingleColumnInputType
from automl.client.core.runtime.datasets import DatasetBase
from azureml.automl.core._experiment_observer import ExperimentStatus
from azureml.automl.runtime.cpu_utilities import _get_num_physical_cpu_cores_model_explanations
from azureml.automl.runtime.streaming_pipeline_wrapper import StreamingPipelineWrapper
from azureml.automl.runtime.training_utilities import _upgrade_sparse_matrix_type, _is_sparse_matrix_int_type
from azureml.automl.core._vendor.automl.client.core.common.constants import Transformers
from automl.client.core.common.constants import MODEL_PATH
from azureml.train.automl.exceptions import ConfigException
from azureml.train.automl._azure_experiment_observer import AzureExperimentObserver
from azureml.automl.core.automl_base_settings import AutoMLBaseSettings
from .run import AutoMLRun


ModelExpDebugPkgList = ['azureml-train-automl-runtime',
                        'azureml-interpret',
                        'azureml-explain-model',
                        'interpret-community',
                        'interpret-core']
DefaultWeightRawFeatureToEngineeredFeatureMap = 1.0
ModelExplanationRunId = 'model_explain_run_id'
ModelExplanationBestRunChildId = 'model_explain_best_run_child_id'
EngineeredExpFolderName = 'engineered_exp_folder_name'
RawExpFolderName = 'raw_exp_folder_name'
NumberofBestRunRetries = 12


class StreamingPipelineExplainabilityWrapper:
    """Wrapper for streaming pipelines that implements APIs expected by Azure model explainability library."""

    def __init__(self, pipeline: Any, task: str):
        """
        Initialize the StreamingPipelineExplainabilityWrapper object.

        :param pipeline: Streaming pipeline
        :type pipeline: Any
        :param task: The machine learning task
        :type task: str
        """
        self._pipeline = pipeline

        if task == constants.Tasks.CLASSIFICATION:
            # All NimbusML pipelines (including regression) have a 'predict_proba' method, (even though
            # the 'predict_proba' raises an error for regression pipelines).
            # Azure model explainability library expects 'predict_proba' method only on classification pipelines,
            # and can error if a regression pipeline object has a predict_proba attribute.
            self.predict_proba = self._pipeline.predict_proba

            self._projection_column_name_in_predict_df = 'PredictedLabel'
        else:
            self._projection_column_name_in_predict_df = 'Score'

    def predict(self, *args, **kwargs):
        """Make predictions for target values."""
        result = self._pipeline.predict(*args, **kwargs)
        if isinstance(result, pd.DataFrame):
            # The 'predict' method on Nimbus pipelines returns a pandas DataFrame with predictions,
            # but Azure model explainability library expects a numpy array (like the sklearn predict API).
            result = result[self._projection_column_name_in_predict_df].values
        return result


class ONNXEstimatorInferceHelperExplainabilityWrapper:
    """A wrapper base class for AutoML ONNX pipelines that standard predict() and predict_proba() functions."""

    def __init__(self, onnx_estimator_helper: OnnxInferenceFromFeaturesHelper):
        """
        Initialize the ONNXEstimatorInferceHelperExplainabilityWrapper object.

        :param onnx_estimator_helper: An AutoML ONNX inference helper object. this is specifically a estimator
            inference helper, which only uses the estimator part of the ONNX model, and can only take the
            transformed features as input (with same schema of the output of the featurizer ONNX model).
        :type pipeline: azureml.automl.runtime.onnx_convert.OnnxInferenceFromFeaturesHelper
        """
        self._onnx_estimator_helper = onnx_estimator_helper

    def predict(self, X: DataInputType) -> DataSingleColumnInputType:
        """Make predictions for target values using AutoML ONNX helper model."""
        predict, _ = self._onnx_estimator_helper.predict(X=X, with_prob=False)
        return predict


class ONNXEstimatorClassificationInferceHelperExplainabilityWrapper(ONNXEstimatorInferceHelperExplainabilityWrapper):
    """
    A wrapper class for AutoML ONNX classification pipelines.

    This class implements standard predict() and predict_proba() functions.
    """

    def __init__(self, onnx_estimator_helper: OnnxInferenceFromFeaturesHelper):
        """
        Initialize the ONNXEstimatorClassificationInferceHelperExplainabilityWrapper object.

        :param onnx_estimator_helper: An AutoML ONNX inference helper object.
        :type pipeline: azureml.automl.runtime.onnx_convert.OnnxInferenceFromFeaturesHelper
        """
        super().__init__(onnx_estimator_helper)

    def predict_proba(self, X: DataInputType) -> DataSingleColumnInputType:
        """Return prediction probabilities for target values using AutoML ONNX helper model."""
        predict, predict_proba = self._onnx_estimator_helper.predict(X=X)
        return predict_proba


class ONNXEstimatorRegressionInferceHelperExplainabilityWrapper(ONNXEstimatorInferceHelperExplainabilityWrapper):
    """A wrapper class for AutoML ONNX regression pipelines that implements standard predict() function."""

    def __init__(self, onnx_estimator_helper: OnnxInferenceFromFeaturesHelper):
        """
        Initialize the ONNXEstimatorRegressionInferceHelperExplainabilityWrapper object.

        :param onnx_estimator_helper: An AutoML ONNX inference helper object.
        :type pipeline: azureml.automl.runtime.onnx_convert.OnnxInferenceFromFeaturesHelper
        """
        super().__init__(onnx_estimator_helper)


class AutoMLExplainerSetupClass:
    """
    Placeholder class for all objects needed for interface with AzureML explain package.

    :param X_transform: The featurized training features used for fitting pipelines during AutoML experiment.
    :type X_transform: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
    :param X_test_raw: The raw test features used evaluating an AutoML trained pipeline.
    :type X_test_raw: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
    :param X_test_transform: The featurized test features for evaluating an AutoML estimator.
    :type X_test_transform: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
    :param pipeline: The entire fitted AutoML model.
    :type pipeline: sklearn.pipeline
    :param estimator: The AutoML estimator including the model specific preprocessor and learner.
    :type estimator: sklearn.pipeline
    :param featurizer: The AutoML featurizer which does transformations from raw features to engineered features.
    :type featurizer: sklearn.pipeline
    :param engineered_feature_names: The list of names for the features generated by the AutoML featurizers.
    :type engineered_feature_names: List[str]
    :param raw_feature_names: The list of names for the raw features to be explained.
    :type raw_feature_names: List[str]
    :type feature_map: The mapping of which raw features generated which engineered features expressed
                        as a numpy array or scipy sparse matrix.
    :type feature_map: numpy.ndarray or scipy.sparse.csr_matrix
    :param classes: The list of classes discovered in the labeled column in case of classification problem.
    :type raw_feature_names: List[Any]
    """

    def __init__(self, X_transform: Optional[DataInputType] = None,
                 X_test_raw: Optional[DataInputType] = None,
                 X_test_transform: Optional[DataInputType] = None,
                 pipeline: Optional[Union[Pipeline, StreamingPipelineExplainabilityWrapper]] = None,
                 estimator: Optional[Union[Pipeline, StreamingPipelineExplainabilityWrapper]] = None,
                 featurizer: Optional[Union[Pipeline, StreamingFeaturizationTransformer]] = None,
                 engineered_feature_names: Optional[List[str]] = None,
                 raw_feature_names: Optional[List[str]] = None,
                 feature_map: Optional[DataInputType] = None,
                 classes: Optional[List[Any]] = None):
        """
        Initialize the AutoML explainer setup class.

        :param X_transform: The featurized training features used for fitting pipelines during AutoML experiment.
        :type X_transform: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
        :param X_test_raw: The raw test features used evaluating an AutoML trained pipeline.
        :type X_test_raw: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
        :param X_test_transform: The featurized test features for evaluating an AutoML estimator.
        :type X_test_transform: pandas.DataFrame or numpy.ndarray or scipy.sparse.csr_matrix
        :param pipeline: The entire fitted AutoML model.
        :type pipeline: Union[Pipeline, StreamingPipelineExplainabilityWrapper]
        :param estimator: The AutoML estimator including the model specific preprocessor and learner.
        :type estimator: Union[Pipeline, StreamingPipelineExplainabilityWrapper]
        :param featurizer: The AutoML featurizer which does transformations from raw features to engineered features.
        :type featurizer: Optional[Union[Pipeline, StreamingFeaturizationTransformer]]
        :param engineered_feature_names: The list of names for the features generated by the AutoML featurizers.
        :type engineered_feature_names: List[str]
        :param raw_feature_names: The list of names for the raw features to be explained.
        :type raw_feature_names: List[str]
        :type feature_map: The mapping of which raw features generated which engineered features expressed
                           as a numpy array or scipy sparse matrix.
        :type feature_map: numpy.ndarray or scipy.sparse.csr_matrix
        :param classes: The list of classes discovered in the labeled column in case of classification problem.
        :type raw_feature_names: List[Any]
        """
        self._X_transform = X_transform
        self._X_test_transform = X_test_transform
        self._X_test_raw = X_test_raw
        self._automl_pipeline = pipeline
        self._automl_estimator = estimator
        self._automl_featurizer = featurizer
        self._engineered_feature_names = engineered_feature_names
        self._raw_feature_names = raw_feature_names
        self._feature_map = feature_map
        self._classes = classes

    @property
    def X_transform(self) -> DataInputType:
        """
        Return the featurized training features used for fitting pipelines during AutoML experiment.

        :return: The featurized training features used for fitting pipelines during AutoML experiment.
        :type: DataInputType
        """
        return self._X_transform

    @property
    def X_test_transform(self) -> DataInputType:
        """
        Return the featurized test features for evaluating an AutoML estimator.

        :return: The featurized test features for evaluating an AutoML estimator.
        :type: DataInputType
        """
        return self._X_test_transform

    @property
    def X_test_raw(self) -> DataInputType:
        """
        Return the raw test features used evaluating an AutoML trained pipeline.

        :return: The raw test features used evaluating an AutoML trained pipeline.
        :type: DataInputType
        """
        return self._X_test_raw

    @property
    def automl_pipeline(self) -> Union[Pipeline, StreamingPipelineWrapper]:
        """
        Return the entire fitted AutoML model.

        :return: The entire fitted AutoML model.
        :type: Union[Pipeline, StreamingPipelineWrapper]
        """
        return self._automl_pipeline

    @property
    def automl_estimator(self) -> Union[Pipeline, StreamingPipelineWrapper]:
        """
        Return the AutoML estimator including the model specific preprocessor and learner.

        :return: The AutoML estimator including the model specific preprocessor and learner.
        :type: Union[Pipeline, StreamingPipelineWrapper]
        """
        return self._automl_estimator

    @property
    def automl_featurizer(self) -> Union[Pipeline, StreamingFeaturizationTransformer]:
        """
        Return the AutoML featurizer which does transformations from raw features to engineered features.

        :return: The AutoML featurizer which does transformations from raw features to engineered features.
        :type: Union[Pipeline, StreamingFeaturizationTransformer]
        """
        return self._automl_featurizer

    @property
    def engineered_feature_names(self) -> Optional[List[str]]:
        """
        Return the list of names for the features generated by the AutoML featurizers.

        :return: The list of names for the features generated by the AutoML featurizers.
        :type: List[str]
        """
        return self._engineered_feature_names

    @property
    def raw_feature_names(self) -> Optional[List[str]]:
        """
        Return the list of names for the raw features to be explained.

        :return: The list of names for the raw features to be explained.
        :type: List[str]
        """
        return self._raw_feature_names

    @property
    def feature_map(self) -> DataInputType:
        """
        Return the mapping of which raw features generated which engineered features.

        :return: The mapping of which raw features generated which engineered features.
        :type: DataInputType
        """
        return self._feature_map

    @property
    def classes(self) -> Optional[List[Any]]:
        """
        Return the list of classes discovered in the labeled column in case of classification problem.

        :return: The list of classes discovered in the labeled column in case of classification problem.
        :type: List[Any]
        """
        return self._classes

    def __str__(self) -> str:
        """
        Return the string representation on the AutoML explainer setup class.

        :return: The string representation on the AutoML explainer setup class.
        :type: str
        """
        print_str = "The setup class is: \n"
        if self.X_transform is not None:
            print_str += "\tx_train_transform = {}\n".format(self.X_transform.shape)
        if self.X_test_raw is not None:
            print_str += "\tX_test_raw = {}\n".format(self.X_test_raw.shape)
        if self.X_test_transform is not None:
            print_str += "\tX_test_transform = {}\n".format(self.X_test_transform.shape)
        return print_str


def _get_featurizer(
    fitted_model: Union[Pipeline, StreamingPipelineWrapper]
) -> Union[Pipeline, StreamingFeaturizationTransformer]:
    """Return the featurizer in the AutoML model."""
    pipeline_transformer = None
    for name, transformer in fitted_model.steps[:-1]:
        if (transformer is not None) and \
                (name == Transformers.X_TRANSFORMER or name == Transformers.LAG_TRANSFORMER or
                    name == Transformers.TIMESERIES_TRANSFORMER):
            pipeline_transformer = transformer
    return pipeline_transformer


def _get_pipeline(
    fitted_model: Union[Pipeline, StreamingPipelineWrapper],
    task: str,
    streaming: bool
) -> Union[Pipeline, StreamingPipelineExplainabilityWrapper]:
    """Return pipeline to be used as input to AzureML explainability library."""
    if streaming:
        return StreamingPipelineExplainabilityWrapper(fitted_model, task)
    return fitted_model


def _get_estimator(
        a_pipeline: Union[Pipeline, StreamingPipelineWrapper],
        task: str,
        streaming: bool) -> Union[Pipeline, StreamingPipelineExplainabilityWrapper]:
    """
    Return the estimator in the AutoML model.

    The estimator pipeline includes the model preprocessors and the learner.
    """
    if streaming:
        return _get_estimator_streaming(a_pipeline, task)
    return _get_estimator_non_streaming(a_pipeline)


def _get_estimator_non_streaming(a_pipeline: Pipeline) -> Pipeline:
    """Return the estimator in the AutoML model."""
    excluded_transfomers = set([Transformers.X_TRANSFORMER, Transformers.TIMESERIES_TRANSFORMER,
                                Transformers.LAG_TRANSFORMER])
    modified_steps = [step[1] for step in a_pipeline.steps
                      if step[0] not in excluded_transfomers]
    if len(modified_steps) != len(a_pipeline.steps):
        return make_pipeline(*[s for s in modified_steps])
    else:
        return a_pipeline


def _get_estimator_streaming(
        pipeline: StreamingPipelineWrapper,
        task: str) -> StreamingPipelineExplainabilityWrapper:
    """Return the estimator in the AutoML model."""
    predictor_pipeline = NimbusMLPipeline()
    predictor_pipeline.load_model(pipeline._pipeline.predictor_model)
    return StreamingPipelineExplainabilityWrapper(predictor_pipeline, task)


def _automl_auto_mode_get_explainer_data(
        dataset: DatasetBase,
        logger: logging.Logger,
        streaming: bool) -> Tuple[DataInputType, DataInputType]:
    """Get X and X_valid data to explain from the DatasetBase object."""
    X = dataset.get_X()
    X_valid = dataset.get_X_valid()
    if streaming:
        # Obtain a subsample of the data to pass to Azure explainability library
        # (since the library requires all data to fit in memory).
        # TODO: Right now, for classification datasets, subsampling might leave out some
        # classes. One possible fix is to subsample the data stratified by label column
        X = X.take(LargeDatasetLimit.MAX_ROWS_TO_SUBSAMPLE)
        X_valid = X_valid.take(LargeDatasetLimit.MAX_ROWS_TO_SUBSAMPLE)
        preprocessor = dataset.get_preprocessor()
        if preprocessor is None:
            explainer_data_X = X.to_pandas_dataframe(extended_types=False)
            explainer_data_X_valid = X_valid.to_pandas_dataframe(extended_types=False)
        else:
            logger.debug("Transforming subsampled raw X for streaming explainability")
            explainer_data_X = preprocessor.transform(DprepDataStream(X), as_csr=True)
            logger.debug("Transforming subsampled raw X_valid for streaming explainability")
            explainer_data_X_valid = preprocessor.transform(DprepDataStream(X_valid), as_csr=True)
    else:
        if _is_sparse_matrix_int_type(X):
            logger.info("Integer type detected for X, need to upgrade to float type")
        if _is_sparse_matrix_int_type(X_valid):
            logger.info("Integer type detected for X_valid, need to upgrade to float type")
        # If the training data is in integer format, then the data needs to reformated into float data
        # for LightGBM surrogate model. For different types of workloads, following needs to done:-
        # 1. If this is non-preprocessing/non-timeseries experiment then copy needs to be made via this
        #    conversion.
        # 2. If this is preprocessing/timeseries, then we should read from file cache and update the type
        #    in inplace. Currently we can't. TODO: Once the training data is read from the cache, then update
        #    the code below to change the type inplace.
        explainer_data_X = _upgrade_sparse_matrix_type(X)
        explainer_data_X_valid = _upgrade_sparse_matrix_type(X_valid)
    return explainer_data_X, explainer_data_X_valid


def _get_feature_map(
        fitted_model: Union[Pipeline, StreamingPipelineWrapper], raw_feature_names_list: Optional[List[str]] = None,
        number_of_raw_features: Optional[int] = None) -> DataInputType:
    """Generate a feature map capturing which engineered feature came from which raw feature."""
    if raw_feature_names_list is None and number_of_raw_features is None:
        raise ArgumentException.create_without_pii("At least list of raw feature names or number of raw feature" +
                                                   " are needed to generate feature map")
    if number_of_raw_features is not None:
        feature_map = np.eye(number_of_raw_features, number_of_raw_features)
        return feature_map

    transformer = _get_featurizer(fitted_model)
    if transformer is None:
        feature_map = np.eye(len(cast(List[str], raw_feature_names_list)),
                             len(cast(List[str], raw_feature_names_list)))
        return feature_map

    # Get the JSON representation of the enigneered feature names
    engineered_feature_json_str_list = transformer.get_json_strs_for_engineered_feature_names()

    # Initialize an empty feature map
    feature_map = np.zeros(shape=(len(cast(List[str], raw_feature_names_list)),
                                  len(engineered_feature_json_str_list)))

    # Create a dictionary mapping from raw feature names to indexes
    raw_feature_name_to_index_dict = \
        {cast(List[str], raw_feature_names_list)[index]: index for index in range(
            0, len(cast(List[str], raw_feature_names_list)))}

    # Iterate over all the engineered features
    for engineered_feature_index, engineered_feature_json_str in enumerate(engineered_feature_json_str_list):
        engineered_feature_json = json.loads(engineered_feature_json_str)
        transformer = engineered_feature_json['Transformations']['Transformer1']
        raw_feature_names = [n for n in transformer["Input"]]
        for raw_feature_name in raw_feature_names:
            if raw_feature_name_to_index_dict.get(raw_feature_name) is not None:
                feature_map[raw_feature_name_to_index_dict.get(raw_feature_name), engineered_feature_index] = \
                    DefaultWeightRawFeatureToEngineeredFeatureMap

    return feature_map


def _get_engineered_feature_names(
    fitted_model: Union[Pipeline, StreamingPipelineWrapper]
) -> Optional[List[str]]:
    """Get the engineered feature names from the AutoML pipeline."""
    engineered_feature_names = None
    for name, transformer in fitted_model.steps[:-1]:
        if (transformer is not None) and \
                (name == Transformers.X_TRANSFORMER or name == Transformers.LAG_TRANSFORMER or
                    name == Transformers.TIMESERIES_TRANSFORMER):
            engineered_feature_names = transformer.get_engineered_feature_names()

    return engineered_feature_names


def _convert_to_pandas_or_numpy(
        X: Optional[Union[DataInputType, TabularDataset]] = None,
        y: Optional[Union[DataSingleColumnInputType, TabularDataset]] = None,
        X_test: Optional[Union[DataInputType, TabularDataset]] = None) -> Tuple[Optional[DataInputType],
                                                                                Optional[DataSingleColumnInputType],
                                                                                Optional[DataInputType]]:
    """Convert different azureml data objects to pandas/numpy structures."""
    X_extracted = None
    X_test_extracted = None
    y_numpy = None
    comparer_obj = None
    if X is not None:
        comparer_obj = X
    elif X_test is not None:
        comparer_obj = X_test
    elif y is not None:
        comparer_obj = y
    else:
        raise ArgumentException.create_without_pii("Unable to perform any conversion")

    if isinstance(comparer_obj, pd.DataFrame) or isinstance(comparer_obj, np.ndarray) or \
            scipy.sparse.issparse(comparer_obj):
        X_extracted = X
        X_test_extracted = X_test
        y_numpy = y
    elif isinstance(comparer_obj, TabularDataset):
        if X is not None:
            X_extracted = X._dataflow.to_pandas_dataframe(extended_types=False)
        if X_test is not None:
            X_test_extracted = X_test._dataflow.to_pandas_dataframe(extended_types=False)
        if y is not None:
            y_numpy = y._dataflow.to_pandas_dataframe(extended_types=False).values
    elif dataprep_utilities.is_dataflow(comparer_obj):
        if X is not None:
            X_extracted = dataprep_utilities.retrieve_pandas_dataframe(X)

        if y is not None:
            y_numpy = dataprep_utilities.retrieve_numpy_array(y)

        if X_test is not None:
            X_test_extracted = dataprep_utilities.retrieve_pandas_dataframe(X_test)

    else:
        raise ArgumentException("Unrecognized input data format. Format detected as " + str(type(comparer_obj)))
    return X_extracted, X_test_extracted, y_numpy


def _get_transformed_data(
        fitted_model: Union[Pipeline, StreamingPipelineWrapper],
        X: Optional[Union[DataInputType, TabularDataset]] = None,
        y: Optional[Union[DataSingleColumnInputType, TabularDataset]] = None,
        X_test: Optional[Union[DataInputType, TabularDataset]] = None,
        featurizer: Optional[Union[Pipeline, StreamingFeaturizationTransformer]] = None,
        streaming: Optional[bool] = False) -> Tuple[Optional[DataInputType], Optional[DataInputType]]:
    """
    Transform the train or test data whichever provided.

    Currently this supports only classification/regression/forecasting.
    """
    if streaming:
        return _get_transformed_data_streaming(
            fitted_model, cast(StreamingFeaturizationTransformer, featurizer), X, X_test)
    return _get_transformed_data_non_streaming(fitted_model, featurizer, X, y, X_test)


def _get_transformed_data_non_streaming(
        fitted_model: Optional[Pipeline], featurizer: Optional[Any],
        X: Optional[Union[DataInputType, TabularDataset]] = None,
        y: Optional[Union[DataSingleColumnInputType, TabularDataset]] = None,
        X_test: Optional[Union[DataInputType, TabularDataset]] = None
) -> Tuple[Optional[DataInputType], Optional[DataInputType]]:
    """Transform the train or test data whichever provided."""
    X_transform, X_test_transform, y_numpy = _convert_to_pandas_or_numpy(X=X, y=y, X_test=X_test)
    if X_transform is not None and X_test_transform is not None:
        if X_transform.shape[1] != X_test_transform.shape[1]:
            raise ConfigException("The number of raw features in train and test data are not same. "
                                  "Please inpect your train and test data")

    if fitted_model is not None:
        for name, transformer in fitted_model.steps[:-1]:
            if (transformer is not None) and \
                    (name == Transformers.X_TRANSFORMER or name == Transformers.LAG_TRANSFORMER or
                        name == Transformers.TIMESERIES_TRANSFORMER):
                if name == Transformers.TIMESERIES_TRANSFORMER:
                    if y_numpy is not None:
                        X_transform = transformer.transform(X_transform, y_numpy)
                        X_transform.pop(constants.TimeSeriesInternal.DUMMY_TARGET_COLUMN)
                        if X_test is not None:
                            X_test_transform = transformer.transform(X_test_transform)
                    else:
                        raise ConfigException.create_without_pii(
                            "Explanations for timeseries requires passing of training output column")
                else:
                    if X_transform is not None:
                        X_transform = transformer.transform(X_transform)
                    if X_test is not None:
                        X_test_transform = transformer.transform(X_test_transform)
    elif featurizer is not None:
        X_transform = featurizer.featurize(X_transform)
        X_test_transform = featurizer.featurize(X_test_transform)
    else:
        raise ArgumentException('No construct passed to featurize the data')

    X_transform = _upgrade_sparse_matrix_type(X_transform)
    X_test_transform = _upgrade_sparse_matrix_type(X_test_transform)
    return X_transform, X_test_transform


def _get_transformed_data_streaming(
    fitted_model: StreamingPipelineWrapper,
    featurizer: StreamingFeaturizationTransformer,
    X: Optional[Union[DataInputType, TabularDataset]],
    X_test: Optional[Union[DataInputType, TabularDataset]],
) -> Tuple[DataInputType, DataInputType]:
    """Transform the train or test data whichever provided."""
    X, X_test = _convert_to_pandas([X, X_test])
    if featurizer is None:
        return X, X_test
    if X is None:
        transformed_X = None
    else:
        transformed_X = featurizer.transform(X, as_csr=True)
    if X_test is None:
        transformed_X_test = None
    else:
        transformed_X_test = featurizer.transform(X_test, as_csr=True)
    return transformed_X, transformed_X_test


def _convert_to_pandas(
    data_inputs: List[Optional[Union[DataInputType, TabularDataset]]]
) -> List[Optional[pd.DataFrame]]:
    """Convert data inputs to pandas DataFrames."""
    result = []
    for data_input in data_inputs:
        if data_input is None or isinstance(data_input, pd.DataFrame):
            result.append(data_input)
        elif isinstance(data_input, TabularDataset):
            df = data_input._dataflow.to_pandas_dataframe(extended_types=False)
            result.append(df)
    return result


def _get_unique_classes(y: DataSingleColumnInputType) -> DataSingleColumnInputType:
    """Return the unique classes in y_train."""
    _, _, y_numpy = _convert_to_pandas_or_numpy(y=y)
    return np.unique(y_numpy)


def _get_raw_feature_names(X: DataSingleColumnInputType) -> Optional[List[str]]:
    """Extract the raw feature names from the raw data if available."""
    X_extracted, _, _ = _convert_to_pandas_or_numpy(X=X)
    if isinstance(X_extracted, pd.DataFrame):
        return list(X_extracted.columns)
    else:
        return None


def _convert_to_onnx_models(fitted_model: Pipeline,
                            X: Union[DataInputType, TabularDataset]) -> Tuple[OnnxInferenceHelper,
                                                                              OnnxFeaturizerHelper,
                                                                              OnnxInferenceFromFeaturesHelper]:
    """
    Convert an AutoML python pipeline into ONNX based inference models.

    Return ONNX based inference models for featurizer, estimator and the pipeline.
    """
    onnx_cvt = OnnxConverter(logger=logging.getLogger('OnnxConverterForModelExplanation'),
                             enable_split_onnx_featurizer_estimator_models=True)
    X_raw, _, _ = _convert_to_pandas_or_numpy(X=X)
    onnx_cvt.initialize_input(X_raw)
    # Convert to ONNX models
    onnx_mdl, fea_onnx_mdl, est_onnx_mdl, err = onnx_cvt.convert(
        fitted_model, 'test with transformer', 'test with transformer')

    if err is not None:
        raise Exception("Unable to convert AutoML python models to ONNX models")

    onnx_res = onnx_cvt.get_converted_onnx_model_resource()

    if len(onnx_res) == 0:
        raise Exception("ONNX conversion of AutoML python model failed.")

    # Convert ONNX model to Inference Helper object
    mdl_bytes = onnx_mdl.SerializeToString()
    onnx_mdl_inference = OnnxInferenceHelper(mdl_bytes, onnx_res)

    # Convert featurizer ONNX model to Inference Helper object
    mdl_bytes = fea_onnx_mdl.SerializeToString()
    fea_onnx_mdl_inference = OnnxFeaturizerHelper(mdl_bytes, onnx_res)

    # Convert estimator ONNX model to Inference Helper object
    mdl_bytes = est_onnx_mdl.SerializeToString()
    est_onnx_mdl_inference = OnnxInferenceFromFeaturesHelper(mdl_bytes)

    # Return the converted ONNX model, ONNX featurizer and ONNX estimator
    return onnx_mdl_inference, fea_onnx_mdl_inference, est_onnx_mdl_inference


def automl_setup_model_explanations(fitted_model: Union[Pipeline, StreamingPipelineWrapper], task: str,
                                    X: Optional[Union[DataInputType, TabularDataset]] = None,
                                    X_test: Optional[Union[DataInputType, TabularDataset]] = None,
                                    y: Optional[Union[DataSingleColumnInputType, TabularDataset]] = None,
                                    features: Optional[List[str]] = None,
                                    **kwargs: Any) -> AutoMLExplainerSetupClass:
    """
    Set up the featurized data for explaining an AutoML model.

    :param fitted_model: The fitted AutoML model.
    :type fitted_model: Union[Pipeline, StreamingPipelineWrapper]
    :param task: 'classification', 'regression', or 'forecasting' depending on what kind of ML problem.
    :type task: str or azureml.train.automl.constants.Tasks
    :param X: The training features used when fitting pipelines during AutoML experiment.
    :type X: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or azureml.core.Dataset
        or azureml.data.dataset_definition.DatasetDefinition or azureml.data.TabularDataset
    :param y: Training labels to use when fitting pipelines during AutoML experiment.
    :type y: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or azureml.core.Dataset
        or azureml.data.dataset_definition.DatasetDefinition or azureml.data.TabularDataset
    :param X_test: Test data using which the model will be explained.
    :type X_test: pandas.DataFrame or numpy.ndarray or azureml.dataprep.Dataflow or azureml.core.Dataset
        or azureml.data.dataset_definition.DatasetDefinition or azureml.data.TabularDataset
    :param features: A list of raw feature names.
    :type features: list[str]
    :param kwargs:
    :type kwargs: dict
    :return: The model's explanation setup class
    :type: AutoMLExplainerSetupClass
    """
    should_convert_models_to_onnx = kwargs.get('onnx_compatibility', False)
    if task != constants.Tasks.CLASSIFICATION and task != constants.Tasks.REGRESSION and \
            task != constants.Subtasks.FORECASTING:
        raise ArgumentException.create_without_pii('Invalid task provided')

    # determine whether or not the pipeline is streaming
    if isinstance(fitted_model, StreamingPipelineWrapper):
        streaming = True
    else:
        streaming = False

    if should_convert_models_to_onnx:
        if task == constants.Subtasks.FORECASTING:
            raise ConfigException("ONNX conversion not supported for AutoML forecasting models")
        if streaming:
            raise ConfigException("ONNX conversion not supported for AutoML streaming models")

    print("Current status: Setting up data for AutoML explanations")
    if should_convert_models_to_onnx:
        print("Current status: Setting up the AutoML ONNX featurizer")
        print("Current status: Setting up the AutoML ONNX estimator")
        onnx_pipeline, onnx_featurizer, onnx_estimator = _convert_to_onnx_models(fitted_model, X)
        pipeline = onnx_pipeline
        featurizer = onnx_featurizer
        if task == constants.Tasks.REGRESSION:
            estimator = ONNXEstimatorRegressionInferceHelperExplainabilityWrapper(onnx_estimator)
        else:
            estimator = ONNXEstimatorClassificationInferceHelperExplainabilityWrapper(onnx_estimator)
    else:
        print("Current status: Setting up the AutoML featurizer")
        featurizer = _get_featurizer(fitted_model)
        print("Current status: Setting up the AutoML estimator")
        estimator = _get_estimator(fitted_model, task, streaming)
        pipeline = _get_pipeline(fitted_model, task, streaming)

    if features is None:
        if X is not None:
            raw_feature_names = _get_raw_feature_names(X)
        elif X_test is not None:
            raw_feature_names = _get_raw_feature_names(X_test)
        else:
            raw_feature_names = None
    else:
        raw_feature_names = features
    print("Current status: Setting up the AutoML featurization for explanations")
    if should_convert_models_to_onnx:
        X_transform, X_test_transform = _get_transformed_data(
            None, X=X, y=y, X_test=X_test, featurizer=featurizer, streaming=streaming)
    else:
        X_transform, X_test_transform = _get_transformed_data(
            fitted_model, X=X, y=y, X_test=X_test, featurizer=featurizer, streaming=streaming)

    if X_test is not None:
        _, X_test_raw, _ = _convert_to_pandas_or_numpy(X_test=X_test)
    else:
        X_test_raw = None

    engineered_feature_names = _get_engineered_feature_names(fitted_model)
    engineered_feature_names = features if engineered_feature_names is None else engineered_feature_names

    print("Current status: Generating a feature map for raw feature importance")
    feature_map = _get_feature_map(fitted_model, raw_feature_names)
    if task == constants.Tasks.CLASSIFICATION and y is not None:
        print("Current status: Finding all classes from the dataset")
        classes = _get_unique_classes(y)
    else:
        classes = None

    print("Current status: Data for AutoML explanations successfully setup")
    return AutoMLExplainerSetupClass(X_transform=X_transform, X_test_raw=X_test_raw,
                                     X_test_transform=X_test_transform, pipeline=pipeline,
                                     estimator=estimator, featurizer=featurizer,
                                     engineered_feature_names=engineered_feature_names,
                                     raw_feature_names=raw_feature_names,
                                     feature_map=feature_map, classes=classes)


def automl_check_model_if_explainable(run: Any) -> bool:
    """
    Check to see if an AutoML child run is explainable.

    :param run: The AutoML child run
    :type run: azureml.core.run.Run
    :return: 'True' if model can be explained and 'False' otherwise
    :type: bool
    """
    from azureml.automl.core.model_explanation import ModelExpSupportStr
    automl_run_properties = run.get_properties()
    model_exp_support_property = automl_run_properties.get(ModelExpSupportStr)
    if model_exp_support_property is not None:
        return model_exp_support_property == 'True'
    else:
        return False


def _should_query_for_best_run(parent_run: AutoMLRun, logger: logging.Logger) -> bool:
    """
    Check if we can query the run history to find the best run.

    :param parent_run: The AutoML parent run
    :type parent_run: azureml.train.automl.run.AutoMLRun
    :param logger: logger for info/error messages.
    :return: bool
    """
    number_of_child_runs_in_artifacts = len(parent_run.get_metrics(recursive=True))
    number_of_complete_child_runs = 0
    children = parent_run.get_children(_rehydrate_runs=False)
    for child in children:
        if child._run_dto['status'] == RunStatus.COMPLETED:
            number_of_complete_child_runs += 1

    number_of_retries = 0
    while number_of_retries < NumberofBestRunRetries and \
            number_of_complete_child_runs > number_of_child_runs_in_artifacts:
        logger.info('The number of completed child runs {0} is greater than child runs in artifacts {1}'.format(
                    number_of_complete_child_runs, number_of_child_runs_in_artifacts))
        time.sleep(10)
        number_of_child_runs_in_artifacts = len(parent_run.get_metrics(recursive=True))
        number_of_retries += 1

    if number_of_retries >= NumberofBestRunRetries:
        return False
    return True


def _automl_perform_best_run_explain_model(parent_run: AutoMLRun, dataset: DatasetBase,
                                           automl_settings: AutoMLBaseSettings, logger: logging.Logger,
                                           compute_target: str, current_run: Optional[Run] = None,
                                           experiment_observer: Optional[AzureExperimentObserver] = None,
                                           console_interface: Optional[ConsoleInterface] = None,
                                           model_exp_feature_config: Optional[Dict[
                                               str, Any]] = None) -> None:
    """
    Explain the best model in the training stage and store the explanation in that child run.

    :param parent_run: The AutoML parent run
    :type parent_run: azureml.train.automl.run.AutoMLRun
    :param dataset: Containing X, y and other transformed data info
    :type dataset: DatasetBase
    :param automl_settings: AutoML run settings
    :type automl_settings: AutoMLBaseSettings
    :param logger: logger for info/error messages.
    :param compute_target: Local/ADB/Remote
    :type compute_target: str
    :param current_run: Current run for computing model explanations
    :param current_run: azureml.core.Run
    :param experiment_observer: The experiment observer.
    :type experiment_observer: azureml.train.automl._azure_experiment_observer.AzureExperimentObserver
    :param console_interface: The console interface to write the status of model explanation run.
    :type console_interface: azureml.automl.core.console_interface.ConsoleInterface
    :param model_exp_feature_config: Model explainability configuration
    :type model_exp_feature_config: Dict
    :return: None
    """
    if automl_settings.model_explainability and parent_run.get_tags().get('model_explain_run') is not None:
        if _should_query_for_best_run(parent_run, logger):
            best_run, fitted_model = parent_run.get_output()
            with dataset.open_dataset():
                try:
                    logger.info("Computing model explanations for best run {0} on {1}".format(best_run.id,
                                                                                              compute_target))
                    if current_run is not None:
                        best_run.set_tags({ModelExplanationRunId: str(current_run.id)})

                    if experiment_observer is not None:
                        if console_interface is not None:
                            console_interface.print_section_separator()

                    _automl_auto_mode_explain_model(
                        best_run, dataset, automl_settings,
                        logger, pipeline=fitted_model,
                        experiment_observer=experiment_observer,
                        model_exp_feature_config=model_exp_feature_config)

                    if experiment_observer is not None:
                        if console_interface is not None:
                            console_interface.print_section_separator()

                    parent_run.tag(ModelExplanationBestRunChildId, best_run.id)
                except Exception as e:
                    logging_utilities.log_traceback(e, logger, is_critical=False)
                    logger.warning(
                        "Failed model explanation for best run on {0}.".format(compute_target)
                    )
                    raise e
        else:
            logger.warning("Skipping best run model explanations because some artifacts are missing")


def _automl_auto_mode_explain_model(child_run: Any,
                                    dataset: DatasetBase,
                                    automl_settings: AutoMLBaseSettings,
                                    logger: logging.Logger,
                                    pipeline: Optional[Union[Pipeline, StreamingPipelineWrapper]] = None,
                                    experiment_observer: Optional[AzureExperimentObserver] = None,
                                    model_exp_feature_config: Optional[Dict[str, Any]] = None) -> None:
    """
    Explain the model in the fit stage and store the explanation in child_run.

    :param child_run: the run to store information
    :type child_run: azureml.core.run.Run
    :param dataset: Containing X, y and other transformed data info
    :type dataset: DatasetBase
    :param automl_settings: AutoML run settings
    :type automl_settings: AutoMLBaseSettings
    :param logger: logger for info/error messages.
    :param pipeline: AutoML fitted model
    :type pipeline: Optional[Union[Pipeline, StreamingPipelineWrapper]]
    :param experiment_observer: The experiment observer.
    :type experiment_observer: AzureExperimentObserver
    :return: None
    """
    # Log the versions for relevant packages for model explainability
    all_dependencies_pkg_versions = package_utilities._all_dependencies()
    model_exp_pkg_versions = dict((package, all_dependencies_pkg_versions[package])
                                  for package in ModelExpDebugPkgList if package in all_dependencies_pkg_versions)
    logger.info('The dependent model explainability packages are:- ' + json.dumps(model_exp_pkg_versions))

    from azureml.explain.model.mimic.models.lightgbm_model import LGBMExplainableModel
    from azureml.explain.model.mimic_wrapper import MimicWrapper

    # Check if the child run is explainable. If not throw an exception to the caller
    if not automl_check_model_if_explainable(child_run):
        logger_str = "Model explanations is currently not supported for " + \
                     child_run.get_properties().get('run_algorithm')
        if child_run.get_tags().get('ensembled_algorithms') is not None:
            logger_str += " due to" + child_run.get_tags().get('ensembled_algorithms')

        logger.warning(logger_str)
        raise Exception(logger_str)

    if experiment_observer is not None:
        experiment_observer.report_status(ExperimentStatus.BestRunExplainModel,
                                          "Best run model explanations started")

    logger.info("[RunId:{}]Start model explanation in fit pipeline.".format(child_run.id))

    # Get the model exp run object if available
    model_exp_run_id = child_run.get_tags().get(ModelExplanationRunId)
    if model_exp_run_id is not None:
        model_exp_run = AutoMLRun(experiment=child_run.experiment, run_id=model_exp_run_id)
        user_sdk_dependencies_property = {'dependencies_versions': json.dumps(
            package_utilities.get_sdk_dependencies())}
        model_exp_run.add_properties(user_sdk_dependencies_property)
    else:
        model_exp_run = None

    if pipeline is None:
        # Download the best model from the artifact store
        child_run.download_file(name=MODEL_PATH, output_file_path='model.pkl')
        # Load the AutoML model into memory
        pipeline = joblib.load('model.pkl')

    # Set the engineered/raw features information for model explanation
    columns = dataset.get_engineered_feature_names()
    # Convert columns from type ndarray to list
    if columns is not None and isinstance(columns, np.ndarray):
        columns = columns.tolist()

    # Set the following for MimicExplainer and LightGBM
    # 1. augment data as False
    # 2. The number of cores for LightGBM model
    explainer_kwargs = {
        'explainable_model_args': {
            'n_jobs': _get_num_physical_cpu_cores_model_explanations(
                automl_settings.max_cores_per_iteration)
        },
        'augment_data': False
    }

    logger.info("The number of core being set for explainable model is: " + str(
        _get_num_physical_cpu_cores_model_explanations(automl_settings.max_cores_per_iteration)))

    # Setup the training and test samples for explanations
    explainer_data_X, explainer_data_X_valid = _automl_auto_mode_get_explainer_data(
        dataset, logger, automl_settings.enable_streaming)

    # for classification problems, get the class labels
    class_labels = dataset.get_class_labels()
    y_transformer = dataset.get_y_transformer()
    if y_transformer is not None and class_labels is not None:
        class_labels = y_transformer.inverse_transform(class_labels)

    # Prepare the feature map for raw feature importance
    x_raw_column_names = dataset.get_x_raw_column_names()
    if x_raw_column_names is not None:
        raw_feature_names = x_raw_column_names  # type: Optional[List[str]]
        num_raw_features = None  # type: Optional[int]
    else:
        raw_feature_names = None
        num_raw_features = explainer_data_X.shape[1]
    feature_map = _get_feature_map(pipeline, raw_feature_names_list=raw_feature_names,
                                   number_of_raw_features=num_raw_features)

    # To explain the pipeline which should exclude datatransformer, laggingtransformer and timeseries
    automl_estimator = _get_estimator(pipeline, automl_settings.task_type, automl_settings.enable_streaming)

    if experiment_observer is not None:
        experiment_observer.report_status(ExperimentStatus.ModelExplainationDataSetSetup,
                                          "Model explanations data setup completed")

    logger.info("Data preparation for model explanations completed.")
    explainer = MimicWrapper(child_run.experiment.workspace, automl_estimator, LGBMExplainableModel,
                             init_dataset=explainer_data_X, run=child_run,
                             features=columns, feature_maps=[feature_map],
                             classes=class_labels, explainer_kwargs=explainer_kwargs)

    if explainer_data_X_valid is None:
        explainer_test_data = explainer_data_X
    else:
        explainer_test_data = explainer_data_X_valid

    if experiment_observer is not None:
        experiment_observer.report_status(ExperimentStatus.EngineeredFeaturesExplanations,
                                          "Computation of engineered features started")

    # Compute the engineered explanations
    eng_explanation = explainer.explain(['local', 'global'],
                                        eval_dataset=explainer_test_data)
    if model_exp_run is not None:
        model_exp_run.add_properties({EngineeredExpFolderName: str(eng_explanation.id)})
    logger.info("Computation of engineered feature importance completed.")

    if experiment_observer is not None:
        experiment_observer.report_status(ExperimentStatus.EngineeredFeaturesExplanations,
                                          "Computation of engineered features completed")

    if model_exp_feature_config is not None and \
            model_exp_feature_config.get("RawGlobalAndLocal") is not None and \
            model_exp_feature_config.get("RawGlobalAndLocal") is True:
        if experiment_observer is not None:
            experiment_observer.report_status(ExperimentStatus.RawFeaturesExplanations,
                                              "Computation of raw features started")
        # Compute the raw explanations
        raw_explanation = explainer._automl_aggregate_and_upload(eng_explanation,
                                                                 raw_feature_names=raw_feature_names)
        if model_exp_run is not None:
            model_exp_run.add_properties({RawExpFolderName: str(raw_explanation.id)})

        if experiment_observer is not None:
            experiment_observer.report_status(ExperimentStatus.RawFeaturesExplanations,
                                              "Computation of raw features completed")
        logger.info("Computation of raw feature importance completed.")

    child_run.tag(constants.MODEL_EXPLANATION_TAG, 'True')

    logger.info("[RunId:{}]End model explanation in fit pipeline.".format(child_run.id))

    if experiment_observer is not None:
        experiment_observer.report_status(ExperimentStatus.BestRunExplainModel,
                                          "Best run model explanations completed")
