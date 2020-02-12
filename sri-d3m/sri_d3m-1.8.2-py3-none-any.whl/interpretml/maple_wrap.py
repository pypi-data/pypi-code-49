
from d3m import container
from d3m import metadata as md
from d3m import primitive_interfaces as pi

from sklearn.model_selection import train_test_split
import numpy as np

from sri.common import util, config
from sri.interpretml.MAPLE import MAPLE


Inputs = container.DataFrame
Outputs = container.DataFrame


class MapleHyperparams(md.hyperparams.Hyperparams):

    validation_fraction = md.hyperparams.Hyperparameter[float](
        default = 0.25,
        semantic_types = ['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description = "Fraction of training examples to set aside for internal validation"
    )

    forest_estimator = md.hyperparams.Enumeration(
        values=['rf', 'gbrt'],
        default='rf',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="The underlying estimator to use, either rf=RandomForestRegressor or gbrt=GradientBoostingRegressor",
    )

    estimator_count = md.hyperparams.Hyperparameter[int](
        default = 200,
        semantic_types = ['https://metadata.datadrivendiscovery.org/types/TuningParameter'],
        description = "Number of atomic estimators to learn",
    )

    max_features = md.hyperparams.Hyperparameter[float](
        default = 0.5,
        semantic_types = ['https://metadata.datadrivendiscovery.org/types/TuningParameter'],
    )

    min_samples_leaf = md.hyperparams.Hyperparameter[int](
        default = 10,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/TuningParameter'],
        description = "Minimimum number of instances in leaves of atomic estimators",
    )

    regularization = md.hyperparams.Hyperparameter[float](
        default = 0.001,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/TuningParameter'],
    )


class MapleParams(md.params.Params):
    model: MAPLE


class Maple(pi.supervised_learning.SupervisedLearnerPrimitiveBase[Inputs, Outputs, MapleParams, MapleHyperparams]):
    """
This primitive wraps MAPLE, an algorithm for generating explanations and explainable models via local linear modeling
of neighborhoods chosen with random forests.

See http://papers.nips.cc/paper/7518-model-agnostic-supervised-local-explanations.pdf

This primitive can just be treated as another regressor.  The above references provides evidence that it
outperforms random forest regression on a number of reference problems.

Several of the hyperparameters below are passed through directly to an underlying RF learner.

Hyperparameters:

* **validation_fraction**:  MAPLE sets aside this fraction of input examples for use in feature selection.
* **forest_estimator**:  Determines the underlying learning algorithm to use.
* **estimator_count**:  Sets n_estimators parameter to underlying regressor.
* **max_features**:  Sets max_features parameter to underlying regressor.
* **min_samples_leaf**:  Sets min_samples_leaf parameter to underlying regressor.
* **regularization**:  Sets the regularization parameter to the linear learner used to fit local neighborhoods.
    """

    metadata = md.base.PrimitiveMetadata({
        # Required
        "id": "98488637-e1ac-43ce-8bb1-ff3eeb891705",
        "version": config.VERSION,
        "name": "Autoflow MAPLE",
        "description": """
            Wraps Ameet Talwalkar's MAPLE, an algorithm designed for 'model-agnostic 
            supervised local explanations.'  Here we're providing it as a regressor
            that basically regularizes an underlying random forest to produce better
            estimates in the neighborhood of high curvature in decision space.
        """,
        "python_path": "d3m.primitives.regression.maple.Maple",
        "primitive_family": md.base.PrimitiveFamily.REGRESSION,
        "algorithm_types": [
            md.base.PrimitiveAlgorithmType.RANDOM_FOREST
        ],
        'source': config.SOURCE,

        # Optional
        'keywords': [ 'primitive', 'regression', 'interpretable ML' ],
        'installation': [ config.INSTALLATION ],
    })


    def __init__(self, *, hyperparams: MapleHyperparams, random_seed: int = 0) -> None:
        super().__init__(hyperparams = hyperparams, random_seed = random_seed)

        self.X_train = None
        self.y_train = None
        self.X_valid = None
        self.y_valid = None
        self.model = None

        self.hyperparams = hyperparams
        self._logger = util.get_logger(__name__)
        self._training_data = None

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        df_train, df_valid, y_train, y_valid = train_test_split(inputs, outputs, test_size=self.hyperparams['validation_fraction'])

        # delete features for which all entries are equal (or below a given threshold)
        train_stddev = df_train[df_train.columns[:]].std()
        thresh = 0.0000000001
        drop_small = np.where(train_stddev < thresh)
        if train_stddev[df_train.shape[1] - 1] < thresh:
            print("ERROR: Near constant predicted value")
        df_train = df_train.drop(drop_small[0], axis=1)
        df_valid = df_valid.drop(drop_small[0], axis=1)
        y_train = y_train.drop(drop_small[0], axis=1)
        y_valid = y_valid.drop(drop_small[0], axis=1)

        # Calculate std dev and mean
        train_stddev = df_train[df_train.columns[:]].std()
        train_mean = df_train[df_train.columns[:]].mean()

        # Normalize to have mean 0 and variance 1
        self.X_train = (df_train - train_mean) / train_stddev
        self.X_valid = (df_valid - train_mean) / train_stddev
        self.y_train = y_train
        self.y_valid = y_valid


    def fit(self, *, timeout: float = None, iterations: int = None) -> pi.base.CallResult[None]:
        self._logger.debug("Instantiating MAPLE")
        self.model = MAPLE(self.X_train.values, self.y_train.values, self.X_valid.values, self.y_valid.values)
        return pi.base.CallResult(None)

    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> pi.base.CallResult[Outputs]:
        self._logger.debug("Starting produce")
        result = self.model.predict(inputs.values)
        df = container.DataFrame(result, generate_metadata=True)
        return pi.base.CallResult(df)

    def get_params(self) -> MapleParams:
        return MapleParams(dict(model=self.model))

    def set_params(self, *, params: MapleParams) -> None:
        self.model = params['model']



