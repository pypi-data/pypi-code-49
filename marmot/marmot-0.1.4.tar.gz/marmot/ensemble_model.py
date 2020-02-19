import copy
import random
from abc import ABCMeta

import pandas as pd
import numpy as np
from joblib import Parallel, delayed
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from marmot.single_model import (PLSRCV, DartRegCV, ElasticNetCV, GBTRegCV,
                                 KernelRidgeCV, KernelSVRCV, LassoCV,
                                 LinearSVRCV, RidgeCV)
from marmot.util import get_logger


class BaseEnsembleModel(metaclass=ABCMeta):

    single_model_cls = []

    def __init__(self,
                 n_models=30, col_ratio=1.0, row_ratio=0.7,
                 n_trials=100, metric='mse',
                 scale=False, scale_y=False,
                 n_jobs=1, logger='ensemble'):

        self.n_models = n_models

        self.col_size = col_ratio

        self.row_size = row_ratio

        self.n_trials = n_trials

        self.metric = metric

        self.scale = scale

        self.scale_y = scale_y

        self.n_jobs = n_jobs

        self.logger = get_logger(logger)

    def fit(self, X, y):
        self.info()

        X, y = self._input_validation(X, y)

        self.models = {}
        self.masks = {}
        self._rprs_modeling(X, y)

    def info(self):
        self.logger.info(f'\n'
                         f'class: {self.__class__.__name__}\n'
                         f'n_models: {self.n_models}\n'
                         f'scale: {self.scale}\n'
                         f'col_ratio: {self.col_size}\n'
                         f'row_ratio: {self.row_size}\n'
                         f'n_trials for each basemodel: {self.n_trials}\n'
                         f'n_jobs: {self.n_jobs}\n')

    def predict(self, X, uncertainty=False):
        X = self._input_validation(X)

        df_result = pd.DataFrame()
        for i in range(self.n_models):
            model = self.models[i]
            mask = self.masks[i]

            X_ = X[:, mask]
            y_pred = model.predict(X_)
            df_result[i] = list(y_pred)

        pred_mean = df_result.mean(1).values
        pred_std = df_result.std(1).values

        if uncertainty:
            return np.vstack([pred_mean, pred_std])
        else:
            return pred_mean

    def predict_proba(self, X):
        return self.predict(X, uncertainty=True)

    def score(self, X, y):
        X, y = self._input_validation(X, y)

        y_true = y.flatten()
        y_pred = self.predict(X).flatten()

        return r2_score(y_true, y_pred)

    def _rprs_modeling(self, X, y):
        if self.n_jobs > 1:
            results = Parallel(n_jobs=self.n_jobs)(
                [delayed(self._train)(X, y, i) for i in range(self.n_models)])
        else:
            results = [self._train(X, y, i) for i in range(self.n_models)]

        for i, (mask, model) in enumerate(results):
            self.masks[i] = mask
            self.models[i] = model

    def _train(self, X, y, i):
        while True:
            row_mask = np.random.binomial(
                1, self.row_size, X.shape[0]).astype(bool)
            col_mask = np.random.binomial(
                1, self.col_size, X.shape[1]).astype(bool)
            if np.any(row_mask) and np.any(col_mask):
                break

        X_rprs = copy.deepcopy(X[row_mask, :][:, col_mask])
        y_rp = copy.deepcopy(y[row_mask])

        model = self._get_model()
        model.fit(X_rprs, y_rp)

        mask = copy.deepcopy(col_mask)
        model = copy.deepcopy(model)

        return mask, model

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

    def _get_model(self):
        model_cls = random.choice(self.single_model_cls)
        return model_cls(n_trials=self.n_trials, metric=self.metric,
                         scale=self.scale, scale_y=self.scale_y)


class EnsembleRidge(BaseEnsembleModel):

    single_model_cls = [RidgeCV]


class EnsembleLinearSVR(BaseEnsembleModel):

    single_model_cls = [LinearSVRCV]


class EnsembleKernelSVR(BaseEnsembleModel):

    single_model_cls = [KernelSVRCV]


class EnsembleKernelRidge(BaseEnsembleModel):

    single_model_cls = [KernelRidgeCV]


class EnsembleDartReg(BaseEnsembleModel):

    single_model_cls = [DartRegCV]


class EnsembleGBTReg(BaseEnsembleModel):

    single_model_cls = [GBTRegCV]


class EnsemblePLSR(BaseEnsembleModel):

    single_model_cls = [PLSRCV]


class EnsembleLinearReg(BaseEnsembleModel):

    single_model_cls = [RidgeCV, LassoCV, LinearSVRCV, ElasticNetCV, PLSRCV]


class EnsembleKernelReg(BaseEnsembleModel):

    single_model_cls = [KernelRidgeCV, KernelSVRCV]


if __name__ == '__main__':
    from tests.support import get_df_boston
    from sklearn.model_selection import train_test_split

    args = {"n_models": 5,
            "col_ratio": 0.8,
            "row_ratio": 0.8,
            "n_trials": 20,
            "metric": "mse",
            "scale": True,
            "n_jobs": 2}

    X, y = get_df_boston()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3)

    #model = EnsembleRidge(**args)
    model = EnsembleKernelSVR(**args)

    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))
    print(model.predict(X.iloc[1]))
    print(model.predict_proba(X.iloc[1]))
