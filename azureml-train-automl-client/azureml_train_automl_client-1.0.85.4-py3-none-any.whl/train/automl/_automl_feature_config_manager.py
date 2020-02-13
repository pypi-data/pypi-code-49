# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Class for getting AutoML features' configuration from JOS"""
from typing import cast, Dict, Any, Optional, List
import logging

from azureml._restclient.jasmine_client import JasmineClient
from azureml._restclient.models.feature_config_request import FeatureConfigRequest
from azureml._restclient.models.feature_config_response import FeatureConfigResponse
from azureml._restclient.models.feature_profile_input_dto import FeatureProfileInputDto
from azureml._restclient.models.feature_profile_output_dto import FeatureProfileOutputDto

from automl.client.core.common import logging_utilities
from azureml.automl.core.configuration.sweeper_config import SweeperConfig
from azureml.train.automl.automl_model_explain import AutoMLModelExplanationConfig
from ._automl_datamodel_utilities import _get_feature_sweeping_config_request, \
    _get_model_explainability_config_request
from .utilities import _is_gpu
from ._automl_datamodel_utilities import MODEL_EXPLAINABILITY_ID


class AutoMLFeatureConfigManager():
    """Config manager for automl features."""

    def __init__(self, jasmine_client: JasmineClient, logger: Optional[logging.Logger] = None):
        """
        Config manager for AutoML features. eg. Feature sweeping

        :param jasmine_client: Jasmine REST client.
        :param logger: Logger.
        """
        self.jasmine_client = jasmine_client
        self._logger = logger or logging.getLogger(AutoMLFeatureConfigManager.__class__.__name__)
        self.feature_profile_input_dto_version = "1.0.0"

    def get_feature_profiles(self,
                             parent_run_id: str,
                             feature_config_requests: List[FeatureConfigRequest]) -> \
            Dict[str, FeatureConfigResponse]:
        """
        Get feature profile information for specified list of features.

        :param run_id: Parent run id.
        :param feature_config_requests: List of FeatureConfigRequest object.
        :rtype: Dict[str, FeatureConfigResponse] where key is feature_id.
        """
        input_map = {}  # type: Dict[str, FeatureConfigRequest]
        for feature in feature_config_requests:
            input_map[feature.feature_id] = feature
        feature_profile_input_dto = FeatureProfileInputDto(version=self.feature_profile_input_dto_version,
                                                           feature_config_input_map=input_map)
        response_dto = self.jasmine_client.get_feature_profiles(
            parent_run_id, feature_profile_input_dto)  # type: FeatureProfileOutputDto
        return cast(Dict[str, FeatureConfigResponse], response_dto.feature_config_output_map)

    def get_feature_sweeping_config(self,
                                    enable_feature_sweeping: bool,
                                    parent_run_id: str,
                                    task_type: str) -> Dict[str, Any]:
        """
        Get feature sweeping config from JOS.

        :param enable_feature_sweeping: Enable feature sweeping.
        :param parent_run_id: AutoML parent run Id.
        :param task_type: Task type- Classification, Regression, Forecasting.
        :rtype: Feature sweeping config for the specified task type, empty if not available/found.
        """
        if enable_feature_sweeping is False:
            return {}

        try:
            is_gpu = _is_gpu()
            feature_config_request = _get_feature_sweeping_config_request(task_type=task_type,
                                                                          is_gpu=is_gpu)
            response = self.get_feature_profiles(parent_run_id,
                                                 [feature_config_request])  # type: FeatureProfileOutputDto

            feature_conf_response = response[feature_config_request.feature_id]  # type: FeatureConfigResponse

            feature_sweeping_config = response[feature_config_request.feature_id].feature_config_map['config'] \
                if feature_conf_response.is_enabled else {}
            return cast(Dict[str, Any], feature_sweeping_config)
        except Exception:
            # Putting below message as info to avoid notebook failure due to warning.
            message = "Unable to fetch feature sweeping config from service, defaulting to blob store config."
            self._logger.info("{message}".format(message=message))
            # Below code can be used to test the feature_sweeping_config changes locally or on remote machine without
            # need of JOS.
            config = self._get_default_feature_sweeping_config()
            return cast(Dict[str, Any], config[task_type])

    def _get_default_feature_sweeping_config(self) -> Dict[str, Any]:
        """Read config and setup the list of enabled sweepers."""
        try:
            return SweeperConfig(logger=self._logger).get_config()
        except (IOError, FileNotFoundError) as e:
            self._logger.warning("Error trying to read configuration file")
            logging_utilities.log_traceback(e, self._logger, is_critical=False)
            return {}

    def get_model_explainability_config(self,
                                        parent_run_id: str,
                                        is_remote: bool = False) -> Dict[str, Any]:
        """
        Get model explainability config from JOS.

        :rtype: model explanation config for the given workspace.
        """
        config = self._get_default_model_explainability_config(is_remote=is_remote)
        return config
        # TODO: Uncomment the code below once the support on JOS is added for handling feature
        #       tower config is added.
        """
        try:
            feature_config_request = _get_model_explainability_config_request()
            response = self.get_feature_profiles(parent_run_id,
                                                 [feature_config_request])  # type: FeatureProfileOutputDto

            feature_config_response = response[feature_config_request.feature_id]  # type: FeatureConfigResponse

            model_exp_config = response[feature_config_request.feature_id].feature_config_map['config'] \
                if feature_config_response.is_enabled else {}
            return cast(Dict[str, Any], model_exp_config)
        except Exception as e:
            message = "Unable to fetch model explanation config from service, defaulting to blob store config."
            self._logger.info("{message}".format(message=message))
            config = self._get_default_model_explainability_config(is_remote=is_remote)
            return config
        """

    def _get_default_model_explainability_config(self, is_remote: bool = False) -> Dict[str, Any]:
        """Return default model explainability config."""
        try:
            return AutoMLModelExplanationConfig(logger=self._logger).get_config(is_remote=is_remote)
        except (IOError, FileNotFoundError) as e:
            self._logger.warning("Error trying to read model explanation configuration file")
            logging_utilities.log_traceback(e, self._logger, is_critical=False)
            return {}

    def get_feature_configurations(self, parent_run_id: str,
                                   model_explainability: bool = False,
                                   is_remote: bool = False) -> Dict[str, Any]:
        feature_config = {}
        if model_explainability is True:
            feature_config[MODEL_EXPLAINABILITY_ID] = self.get_model_explainability_config(parent_run_id,
                                                                                           is_remote=is_remote)
        else:
            feature_config[MODEL_EXPLAINABILITY_ID] = {}

        return feature_config
