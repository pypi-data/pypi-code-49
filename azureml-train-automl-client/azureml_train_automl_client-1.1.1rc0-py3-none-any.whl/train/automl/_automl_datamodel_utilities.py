# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""File contains globally known feature Ids for automl features and static methods to generate input objects."""

from azureml._restclient.models.feature_config_request import FeatureConfigRequest

FEATURE_SWEEPING_ID = "feature_sweeping"
FEATURE_SWEEPING_VERSION = "1.4"
MODEL_EXPLAINABILITY_ID = "model_explainability"
MODEL_EXPLAINABILITY_VERSION = "1.0"


def _get_feature_sweeping_config_request(task_type: str, is_gpu: bool) -> FeatureConfigRequest:
    return FeatureConfigRequest(feature_version=FEATURE_SWEEPING_VERSION,
                                feature_id=FEATURE_SWEEPING_ID,
                                feature_metadata_map={
                                    'task': task_type,
                                    'is_gpu': is_gpu
                                })


def _get_model_explainability_config_request() -> FeatureConfigRequest:
    return FeatureConfigRequest(feature_version=MODEL_EXPLAINABILITY_VERSION,
                                feature_id=MODEL_EXPLAINABILITY_ID)
