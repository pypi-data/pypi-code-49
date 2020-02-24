import numpy as np
import pandas as pd
from azureml.studio.common.parameter_range import ParameterRangeSettings, Sweepable
from azureml.studio.core.logger import TimeProfile
from azureml.studio.modulehost.attributes import ModeParameter, IntParameter, ParameterRangeParameter, \
    BooleanParameter, ModuleMeta
from azureml.studio.modulehost.attributes import ReleaseState
from azureml.studio.modulehost.attributes import UntrainedLearnerOutputPort
from azureml.studio.modulehost.module_reflector import module_entry, BaseModule
from azureml.studio.modules.anomaly_detection.common.base_anomaly_detection import BaseAnomalyDetectionLearner, \
    CreateLearnerMode, RestoreInfo
from azureml.studio.modules.ml.common.base_learner_setting import BaseLearnerSetting
from nimbusml import Pipeline
from nimbusml.decomposition import PcaAnomalyDetector


class PCAAnomalyDetectionModelModuleDefaultParameters:
    MODE = CreateLearnerMode.SingleParameter
    RANK = 2
    RANK_RANGE = "2; 4; 6; 8; 10"
    OVERSAMPLING = 2
    OVERSAMPLING_RANGE = "2; 4; 6; 8; 10"
    CENTER = False
    NormalizeFeatures = True


class PCABasedAnomalyDetectionModule(BaseModule):
    _param_keys = {
        "mode": "Training mode",
        "rank": "Number of components to use in PCA",
        "oversampling": "Oversampling parameter for randomized PCA",
        "center": "Enable input feature mean normalization",
        "rank_range": "Range for number of PCA components",
        "oversampling_range": "Range for the oversampling parameter used in randomized PCA",
    }

    @staticmethod
    @module_entry(ModuleMeta(
        name="PCA-Based Anomaly Detection",
        description="Create a PCA-based anomaly detection model.",
        category="Anomaly Detection",
        version="1.0",
        owner="Microsoft Corporation",
        family_id="C3822FA5-1095-4C72-BD1E-FD43D285153A",
        release_state=ReleaseState.Beta,
        is_deterministic=True,
    ))
    def run(
            mode: ModeParameter(
                CreateLearnerMode,
                name="Training mode",
                friendly_name="Training mode",
                description="Specify learner options. Use 'SingleParameter' to manually specify all values. "
                            "Use 'ParameterRange' to sweep over tunable parameters.",
                default_value=CreateLearnerMode.SingleParameter,
            ),
            rank: IntParameter(
                name="Number of components to use in PCA",
                friendly_name="Number of components to use in PCA",
                description="Specify the number of components to use in PCA.",
                default_value=2,
                parent_parameter="Training mode",
                parent_parameter_val=(CreateLearnerMode.SingleParameter,),
            ),
            oversampling: IntParameter(
                name="Oversampling parameter for randomized PCA",
                friendly_name="Oversampling parameter for randomized PCA",
                description="Specify the accuracy parameter for randomized PCA training.",
                default_value=2,
                parent_parameter="Training mode",
                parent_parameter_val=(CreateLearnerMode.SingleParameter,),
            ),
            center: BooleanParameter(
                name="Enable input feature mean normalization",
                friendly_name="Enable input feature mean normalization",
                description="Specify if the input data is normalized to have zero mean. ",
                default_value=False,
            ),
            rank_range: ParameterRangeParameter(
                name="Range for number of PCA components",
                friendly_name="Range for number of PCA components",
                description="Specify the range for number of components to use in PCA.",
                default_value="2; 4; 6; 8; 10",
                parent_parameter="Training mode",
                parent_parameter_val=(CreateLearnerMode.ParameterRange,),
                min_limit=1,
                max_limit=100,
                is_int=True,
                is_log=False,
                slider_min=1,
                slider_max=100,
            ),
            oversampling_range: ParameterRangeParameter(
                name="Range for the oversampling parameter used in randomized PCA",
                friendly_name="Range for the oversampling parameter used in randomized PCA",
                description="Specify the range for accuracy parameter used in randomized PCA training.",
                default_value="2; 4; 6; 8; 10",
                parent_parameter="Training mode",
                parent_parameter_val=(CreateLearnerMode.ParameterRange,),
                min_limit=1,
                max_limit=100,
                is_int=True,
                is_log=False,
                slider_min=1,
                slider_max=100,
            )
    ) -> (
            UntrainedLearnerOutputPort(
                name="Untrained model",
                friendly_name="Untrained model",
                description="An untrained PCA-based anomaly detection model.",
            ),
    ):
        input_values = locals()
        output_values = PCABasedAnomalyDetectionModule.run_impl(**input_values)
        return output_values

    @classmethod
    def run_impl(
            cls,
            mode: CreateLearnerMode,
            rank: int,
            oversampling: int,
            center: bool,
            rank_range: ParameterRangeSettings = None,
            oversampling_range: ParameterRangeSettings = None,
    ):
        setting = PCAAnomalyDetectionModelSetting()
        if mode == CreateLearnerMode.SingleParameter:
            setting.init_single(
                rank=rank,
                oversampling=oversampling,
                center=center)
        else:
            setting.init_range(
                rank_range=rank_range,
                oversampling_range=oversampling_range,
                center=center
            )
        return PCAAnomalyDetectionModel(setting),


class PCAAnomalyDetectionModelSetting(BaseLearnerSetting):
    def __init__(self):
        super().__init__()
        self.rank = PCAAnomalyDetectionModelModuleDefaultParameters.RANK
        self.oversampling = PCAAnomalyDetectionModelModuleDefaultParameters.OVERSAMPLING
        self.center = PCAAnomalyDetectionModelModuleDefaultParameters.CENTER
        self.normalize_features = PCAAnomalyDetectionModelModuleDefaultParameters.NormalizeFeatures
        self.create_learner_mode = PCAAnomalyDetectionModelModuleDefaultParameters.MODE
        self.parameter_range = {
            'rank': Sweepable.from_prs(
                "rank_range", ParameterRangeSettings.from_literal(
                    PCAAnomalyDetectionModelModuleDefaultParameters.RANK_RANGE)).attribute_value,
            'oversampling': Sweepable.from_prs(
                "oversampling_range", ParameterRangeSettings.from_literal(
                    PCAAnomalyDetectionModelModuleDefaultParameters.OVERSAMPLING_RANGE)).attribute_value
        }

    def init_single(self,
                    rank: int = PCAAnomalyDetectionModelModuleDefaultParameters.RANK,
                    oversampling: int = PCAAnomalyDetectionModelModuleDefaultParameters.OVERSAMPLING,
                    center=PCAAnomalyDetectionModelModuleDefaultParameters.CENTER):
        self.create_learner_mode = CreateLearnerMode.SingleParameter
        self.rank = rank
        self.oversampling = oversampling
        self.center = center

    def init_range(self, rank_range: ParameterRangeSettings = None, oversampling_range: ParameterRangeSettings = None,
                   center=PCAAnomalyDetectionModelModuleDefaultParameters.CENTER):
        self.create_learner_mode = CreateLearnerMode.ParameterRange
        self.add_sweepable(Sweepable.from_prs('rank', rank_range))
        self.add_sweepable(Sweepable.from_prs('oversampling', oversampling_range))


class PCAAnomalyDetectionModel(BaseAnomalyDetectionLearner):
    def __init__(self, setting: PCAAnomalyDetectionModelSetting):
        super().__init__(setting)

    @property
    def parameter_mapping(self):
        return {
            'rank': RestoreInfo(PCABasedAnomalyDetectionModule._args.rank.friendly_name),
            'oversampling': RestoreInfo(PCABasedAnomalyDetectionModule._args.oversampling.friendly_name),
            'center': RestoreInfo(PCABasedAnomalyDetectionModule._args.center.friendly_name)
        }

    def init_model(self):
        self.model = Pipeline([PcaAnomalyDetector(
            rank=self.setting.rank,
            oversampling=self.setting.oversampling,
            center=self.setting.center,
            random_state=42
        )])

    def _predict(self, test_x: pd.DataFrame):
        try:
            with TimeProfile("Predicting probability"):
                # nimbusml.Pipeline test method
                prob = self.model.predict(test_x).values.ravel()  # pylint: disable=no-member
        except Exception as e:
            raise e

        with TimeProfile("calculating argmax(Probability)"):
            # 1 is inlier while 0 outlier as training with only normal data.
            label = np.where(prob >= 0.5, 1, 0)
        return label, prob
