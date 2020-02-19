import warnings
from abc import ABCMeta, abstractmethod

import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import RepeatedKFold
from sklearn.svm import SVR
from sklearn.cross_decomposition import PLSRegression
from sklearn.kernel_ridge import KernelRidge
import optuna
import xgboost as xgb

from marmot.util import get_logger

warnings.filterwarnings('ignore')


class BaseSingleModelCV(metaclass=ABCMeta):

    model_cls = None

    def __init__(self, n_trials=200, metric='mse', scale=False, scale_y=False,
                 n_splits=3, n_repeats=10, silent=True, logger="basemodel"):

        self.n_trials = n_trials

        self.metric = metric

        self.scale = scale

        self.scaler = None

        self.scale_y = scale_y

        self.n_splits = n_splits

        self.n_repeats = n_repeats

        self.silent = silent

        self.logger = get_logger(logger)

    def fit(self, X, y):

        self.X, self.y = self._input_validation(X, y)

        if self.silent:
            optuna.logging.disable_default_handler()

        if self.scale:
            self.scaler = StandardScaler()
            self.scaler.fit(self.X)
            self.X = self.scaler.transform(self.X)

        if self.scale_y:
            self.y = np.log1p(self.y)

        study = optuna.create_study(direction=self.direction)
        study.optimize(self, n_trials=self.n_trials)
        self.best_trial = study.best_trial

        self.logger.info(f"\n"
                         f"Best {self.metric} score: "
                         f"{round(self.best_trial.value, 2)}\n"
                         f"Best hyperparams: "
                         f"{self.best_trial.params}\n")

        self.best_model = self.model_cls(**self.best_trial.params)
        self.best_model.fit(self.X, self.y)

    def predict(self, X):
        X = self._input_validation(X)
        if self.scale:
            X = self.scaler.transform(X)
        pred = self.best_model.predict(X)

        if self.scale_y:
            pred = np.exp(pred) - 1

        return pred

    def score(self, X, y):
        X, y = self._input_validation(X, y)
        if self.scale:
            X = self.scaler.transform(X)
        if self.scale_y:
            y = np.log1p(y)

        return self.best_model.score(X, y)

    def kfold_cv(self, model):
        observed = []
        predicted = []

        kf = RepeatedKFold(n_splits=self.n_splits, n_repeats=self.n_repeats)
        for train_index, test_index in kf.split(self.X):
            X_train, X_test = self.X[train_index], self.X[test_index]
            y_train, y_test = self.y[train_index], self.y[test_index]
            model.fit(X_train, y_train)

            predicted += list(model.predict(X_test).flatten())
            observed += list(y_test.flatten())

        if self.metric == 'mse':
            score = mean_squared_error(observed, predicted)
        elif self.metric == 'r2':
            score = r2_score(observed, predicted)
        else:
            NotImplementedError('Unknown metric:', self.metric)

        return score

    @property
    def direction(self):
        return ("minimize" if self.metric == "mse"
                else "maximize" if self.metric == "r2"
                else "Invalid metric")

    def _input_validation(self, *args, **kwargs):
        if len(args) >= 1:
            X = args[0]
            if isinstance(X, pd.Series):
                X = pd.DataFrame(X).T
                X = X.values
            elif isinstance(X, pd.DataFrame):
                X = X.values

            if len(args) >= 2:
                y = args[1]
                if isinstance(y, pd.Series):
                    y = y.values.flatten()
                elif isinstance(y, pd.DataFrame):
                    y = y.values.flatten()

                return X, y
            else:
                return X
        else:
            raise TypeError("Unexpected X or y")

    @abstractmethod
    def __call__(self, trial):
        raise NotImplementedError()


class RidgeCV(BaseSingleModelCV):

    model_cls = Ridge

    def __call__(self, trial):
        alpha = trial.suggest_loguniform('alpha', 1e-3, 1e2)
        model = self.model_cls(alpha=alpha)
        score = self.kfold_cv(model)
        return score


class LassoCV(BaseSingleModelCV):

    model_cls = Lasso

    def __call__(self, trial):
        alpha = trial.suggest_loguniform('alpha', 1e-3, 1e2)
        model = self.model_cls(alpha=alpha)
        score = self.kfold_cv(model)
        return score


class ElasticNetCV(BaseSingleModelCV):

    model_cls = ElasticNet

    def __call__(self, trial):
        alpha = trial.suggest_loguniform('alpha', 1e-3, 1e2)
        l1_ratio = trial.suggest_loguniform('l1_ratio', 1e-3, 1e2)
        model = self.model_cls(alpha=alpha, l1_ratio=l1_ratio)
        score = self.kfold_cv(model)
        return score


class PLSRCV(BaseSingleModelCV):

    model_cls = PLSRegression

    def __call__(self, trial):
        n_components = trial.suggest_int('n_components',
                                         1, int(self.X.shape[1]/2))
        model = self.model_cls(n_components=n_components)
        score = self.kfold_cv(model)
        return score


class KernelRidgeCV(BaseSingleModelCV):

    model_cls = KernelRidge

    def __call__(self, trial):
        kernel = trial.suggest_categorical('kernel', ['rbf', 'polynomial'])
        alpha = trial.suggest_loguniform('alpha', 1e-3, 1e2)
        gamma = trial.suggest_loguniform('gamma', 1e-3, 1e3)

        if kernel == 'polynomial':
            degree = trial.suggest_int('degree', 1, 5)
            model = self.model_cls(kernel=kernel, alpha=alpha,
                                   degree=degree, gamma=gamma)
        elif kernel == 'rbf':
            model = self.model_cls(kernel=kernel, alpha=alpha, gamma=gamma)
        else:
            raise Exception("Unexpected Error")

        score = self.kfold_cv(model)
        return score


class LinearSVRCV(BaseSingleModelCV):

    model_cls = SVR

    def __call__(self, trial):
        C = trial.suggest_loguniform('C', 1e-2, 1e2)
        epsilon = trial.suggest_loguniform('epsilon', 1e-3, 1e2)
        model = self.model_cls(kernel='linear', C=C,
                               epsilon=epsilon)

        score = self.kfold_cv(model)
        return score


class KernelSVRCV(BaseSingleModelCV):

    model_cls = SVR

    def __call__(self, trial):
        C = trial.suggest_loguniform('C', 1e-2, 1e2)
        epsilon = trial.suggest_loguniform('epsilon', 1e-3, 1e2)
        gamma = trial.suggest_loguniform('gamma', 1e-3, 1e3)
        model = self.model_cls(kernel='rbf', C=C,
                               epsilon=epsilon, gamma=gamma)

        score = self.kfold_cv(model)
        return score


class GBTRegCV(BaseSingleModelCV):

    model_cls = xgb.XGBRegressor

    def __call__(self, trial):
        booster = trial.suggest_categorical('booster', ['gbtree'])
        alpha = trial.suggest_loguniform('alpha', 1e-8, 1.0)

        max_depth = trial.suggest_int('max_depth', 1, 9)
        eta = trial.suggest_loguniform('eta', 1e-8, 1.0)
        gamma = trial.suggest_loguniform('gamma', 1e-8, 1.0)
        grow_policy = trial.suggest_categorical(
            'grow_policy', ['depthwise', 'lossguide'])

        model = self.model_cls(verbosity=0, booster=booster,
                               alpha=alpha, max_depth=max_depth, eta=eta,
                               gamma=gamma, grow_policy=grow_policy)

        score = self.kfold_cv(model)
        return score


class DartRegCV(BaseSingleModelCV):

    model_cls = xgb.XGBRegressor

    def __call__(self, trial):
        booster = trial.suggest_categorical('booster', ['dart'])
        alpha = trial.suggest_loguniform('alpha', 1e-8, 1.0)

        max_depth = trial.suggest_int('max_depth', 1, 16)
        eta = trial.suggest_loguniform('eta', 1e-8, 1.0)
        gamma = trial.suggest_loguniform('gamma', 1e-8, 1.0)
        grow_policy = trial.suggest_categorical(
            'grow_policy', ['depthwise', 'lossguide'])

        sample_type = trial.suggest_categorical('sample_type',
                                                ['uniform', 'weighted'])
        normalize_type = trial.suggest_categorical('normalize_type',
                                                    ['tree', 'forest'])
        rate_drop = trial.suggest_loguniform('rate_drop', 1e-8, 1.0)
        skip_drop = trial.suggest_loguniform('skip_drop', 1e-8, 1.0)
        model = self.model_cls(verbosity=0, booster=booster,
                               alpha=alpha, max_depth=max_depth, eta=eta,
                               gamma=gamma, grow_policy=grow_policy,
                               sample_type=sample_type,
                               normalize_type=normalize_type,
                               rate_drop=rate_drop, skip_drop=skip_drop)

        score = self.kfold_cv(model)
        return score


if __name__ == '__main__':
    import pandas as pd
    from tests.support import get_df_boston
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler

    X, y = get_df_boston()
    X_sc = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.values, test_size=0.3)

    #model = LinearSVRCV(n_trials=30, scale=True)
    #model = KernelRidgeCV(n_trials=150, metric="r2", scale=True)
    #model = KernelSVRCV(n_trials=150, metric="r2", scale=True)
    model = RidgeCV(n_trials=10, scale_y=True, metric="r2", scale=True)
    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))
    print(model.predict(X.iloc[1]))
    print(y.iloc[1])
    print(model.best_model)

