# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines constants used in automated ML in Azure Machine Learning.

Before you begin an experiment, you specify the kind of machine learning problem you are solving
with the :class:`azureml.train.automl.automlconfig.AutoMLConfig` class.
Azure Machine Learning supports task types of classification, regression, and forecasting.
For more information, see [How to define a machine learning
task](https://docs.microsoft.com/azure/machine-learning/service/how-to-define-task-type).

For the task types classification, regression, and forecasing, the supported algorithms are listed,
respectively, in the :class:`azureml.train.automl.constants.SupportedModels.Classification`,
:class:`azureml.train.automl.constants.SupportedModels.Regression`, and
:class:`azureml.train.automl.constants.SupportedModels.Forecasting` classes. The listed algorithms
for each task type are used during the automation and tuning process. As a user, there is no need
for you to specify the algorithm. For more information, see [Configure automated ML experiments in
Python](https://docs.microsoft.com/azure/machine-learning/service/how-to-configure-auto-train).
"""

from automl.client.core.common.constants import (
    ModelClassNames,
    MODEL_PATH,
    MODEL_PATH_TRAIN,
    MODEL_PATH_ONNX,
    MODEL_RESOURCE_PATH_ONNX,
    EnsembleConstants,
    Defaults,
    RunState,
    API,
    AcquisitionFunction,
    Status,
    PipelineParameterConstraintCheckStatus,
    OptimizerObjectives,
    Optimizer,
    Tasks as CommonTasks,
    ClientErrors,
    ServerStatus,
    TimeConstraintEnforcement,
    PipelineCost,
    Metric,
    MetricObjective,
    TrainingType,
    NumericalDtype,
    TextOrCategoricalDtype,
    TrainingResultsType,
    get_metric_from_type,
    get_status_from_type,
)

from azureml.automl.core.constants import (
    FeatureType, SupportedTransformers, FeaturizationConfigMode
)


AUTOML_SETTINGS_PATH = "automl_settings.pkl"
AUTOML_FIT_PARAMS_PATH = "fit_params.pkl"
LOCAL_SCRIPT_NAME = "_script.py"
LOCAL_PREDICT_NAME = "_predict.py"
PREDICT_INPUT_FILE = "predict.pkl"
PREDICTED_METRIC_NAME = "predicted"
LOCAL_MODEL_PATH = "model.pkl"


class SupportedModels:
    """Defines friendly names for automated ML algorithms supported by Azure Machine Learning."""

    class Classification:
        """Defines classification algorithm names."""

        LogisticRegression = 'LogisticRegression'
        SGDClassifier = 'SGD'
        MultinomialNB = 'MultinomialNaiveBayes'
        BernoulliNB = 'BernoulliNaiveBayes'
        SupportVectorMachine = 'SVM'
        LinearSupportVectorMachine = 'LinearSVM'
        KNearestNeighborsClassifier = 'KNN'
        DecisionTree = 'DecisionTree'
        RandomForest = 'RandomForest'
        ExtraTrees = 'ExtremeRandomTrees'
        LightGBMClassifier = 'LightGBM'
        GradientBoosting = 'GradientBoosting'
        TensorFlowDNNClassifier = 'TensorFlowDNN'
        TensorFlowLinearClassifier = 'TensorFlowLinearClassifier'
        XGBoostClassifier = 'XGBoostClassifier'
        AveragedPerceptronClassifier = 'AveragedPerceptronClassifier'
        LinearSVMClassifier = 'LinearSVMClassifier'

    class Regression:
        """Defines regression algorithm names."""

        ElasticNet = 'ElasticNet'
        GradientBoostingRegressor = 'GradientBoosting'
        DecisionTreeRegressor = 'DecisionTree'
        KNearestNeighborsRegressor = 'KNN'
        LassoLars = 'LassoLars'
        SGDRegressor = 'SGD'
        RandomForestRegressor = 'RandomForest'
        ExtraTreesRegressor = 'ExtremeRandomTrees'
        LightGBMRegressor = 'LightGBM'
        TensorFlowLinearRegressor = 'TensorFlowLinearRegressor'
        TensorFlowDNNRegressor = 'TensorFlowDNN'
        XGBoostRegressor = 'XGBoostRegressor'
        FastLinearRegressor = 'FastLinearRegressor'
        OnlineGradientDescentRegressor = 'OnlineGradientDescentRegressor'

    class Forecasting(Regression):
        """Defines forecasting algorithm names."""

        AutoArima = 'AutoArima'
        Prophet = 'Prophet'
        TCNForecaster = 'TCNForecaster'


MODEL_EXPLANATION_TAG = "model_explanation"

MAX_ITERATIONS = 1000
MAX_SAMPLES_BLACKLIST = 5000
MAX_SAMPLES_BLACKLIST_ALGOS = [SupportedModels.Classification.KNearestNeighborsClassifier,
                               SupportedModels.Regression.KNearestNeighborsRegressor,
                               SupportedModels.Classification.SupportVectorMachine]
EARLY_STOPPING_NUM_LANDMARKS = 20

DATA_SCRIPT_FILE_NAME = "get_data.py"

"""Names of algorithms that do not support sample weights."""
Sample_Weights_Unsupported = {
    ModelClassNames.RegressionModelClassNames.ElasticNet,
    ModelClassNames.ClassificationModelClassNames.KNearestNeighborsClassifier,
    ModelClassNames.RegressionModelClassNames.KNearestNeighborsRegressor,
    ModelClassNames.RegressionModelClassNames.LassoLars
}

"""Algorithm names that we must force to run in single threaded mode."""
SINGLE_THREADED_ALGORITHMS = [
    ModelClassNames.ClassificationModelClassNames.KNearestNeighborsClassifier,
    ModelClassNames.RegressionModelClassNames.KNearestNeighborsRegressor
]

TrainingType.FULL_SET.remove(TrainingType.TrainValidateTest)


class ComputeTargets:
    """Defines names of compute targets supported in automated ML in Azure Machine Learning.

    Specify the compute target of an experiment run using the :class:`azureml.train.automl.automlconfig.AutoMLConfig`
    class.
    """

    DSVM = 'VirtualMachine'
    BATCHAI = 'BatchAI'
    AMLCOMPUTE = 'AmlCompute'
    LOCAL = 'local'
    ADB = 'ADB'


class TimeSeries:
    """Defines parameters used for time-series forecasting.

    The parameters are specified with the :class:`azureml.train.automl.automlconfig.AutoMLConfig` class.
    """

    TIME_COLUMN_NAME = 'time_column_name'
    GRAIN_COLUMN_NAMES = 'grain_column_names'
    DROP_COLUMN_NAMES = 'drop_column_names'
    MAX_HORIZON = 'max_horizon'


class Tasks(CommonTasks):
    """A subclass of Tasks in common.core that can be extended to add more task types for the SDK."""

    CLASSIFICATION = CommonTasks.CLASSIFICATION
    REGRESSION = CommonTasks.REGRESSION
    FORECASTING = 'forecasting'
    IMAGE_CLASSIFICATION = CommonTasks.IMAGE_CLASSIFICATION
    IMAGE_MULTI_LABEL_CLASSIFICATION = CommonTasks.IMAGE_MULTI_LABEL_CLASSIFICATION
    IMAGE_OBJECT_DETECTION = CommonTasks.IMAGE_OBJECT_DETECTION
    ALL_IMAGE = CommonTasks.ALL_IMAGE
    ALL = [CommonTasks.CLASSIFICATION, CommonTasks.REGRESSION, FORECASTING] + ALL_IMAGE


class ExperimentObserver:
    """Constants used by the Experiment Observer to report progress during preprocessing."""

    EXPERIMENT_STATUS_TAG_NAME = "experiment_status"
    EXPERIMENT_STATUS_DESCRIPTION_TAG_NAME = "experiment_status_descr"


class Scenarios:
    """Constants for the various curated environment scenarios."""

    SDK = "SDK"
