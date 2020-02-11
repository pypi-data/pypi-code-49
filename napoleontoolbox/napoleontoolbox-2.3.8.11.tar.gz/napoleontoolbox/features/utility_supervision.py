#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

import pandas as pd

import numpy as np

from napoleontoolbox.utility import metrics
from napoleontoolbox.file_saver import dropbox_file_saver
from scipy.optimize import Bounds, LinearConstraint, minimize

import torch


class AbstractAssembler(ABC):
    def __init__(self, starting_date=None, running_date = None, drop_token=None, dropbox_backup = True, features_pkl_file_name='features.pkl', macro_features_directory='features_macro', returns_pkl_file_name='returns.pkl', local_root_directory='../data/', user='napoleon',
                 supervision_npy_file_suffix='_supervision.npy', macro_supervision_npy_file_suffix='_macro_supervision.npy',):
        super().__init__()
        self.features_pkl_file_name = features_pkl_file_name
        self.returns_pkl_file_name = returns_pkl_file_name
        self.macro_features_directory=macro_features_directory
        self.local_root_directory = local_root_directory
        self.user = user
        self.supervision_npy_file_suffix = supervision_npy_file_suffix
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token=drop_token,dropbox_backup=dropbox_backup)
        self.macro_supervision_npy_file_suffix=macro_supervision_npy_file_suffix
        self.dropbox_backup = dropbox_backup
        self.running_date = running_date
        self.starting_date = starting_date

    @abstractmethod
    def computeUtility(self, s):
        pass


class UtilitySuperviser(AbstractAssembler):

    def computeMacroForecastingUtility(self, rebal=10,low_bound=0.02, up_bound=0.4, cutting_rate_threshold=0.7):
        df = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder=self.macro_features_directory, returns_pkl_file_name=self.returns_pkl_file_name, local_root_directory = self.local_root_directory)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        strats = [col for col in list(df.columns) if col != 'Date']

        advanced_features = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder=self.macro_features_directory, returns_pkl_file_name=self.features_pkl_file_name, local_root_directory = self.local_root_directory)
        features_names = [col for col in list(advanced_features.columns) if col!='Date']
        advanced_features['Date'] = pd.to_datetime(advanced_features['Date'])
        max_date = max(advanced_features['Date'])
        print('Actual max feature date '+str(max_date))
        print('Actual computing date '+str(self.running_date))
        df=df[df.index>=self.starting_date]
        df=df[df.index<=self.running_date]

        df = df.fillna(method='ffill')
        print('size return '+str(df.shape))

        print('size advanced_features '+str(advanced_features.shape))

        np.random.seed(0)
        torch.manual_seed(0)
        ##===================##
        ##  Setting targets  ##
        ##===================##

        df_bis = df.copy()

        print('merging')
        df_bis = pd.merge(df_bis, advanced_features, how='left', on=['Date'])

        print('merging done')
        df_bis.index = df_bis['Date']
        df_bis = df_bis.drop(columns=['Date'])
        print('return')

        df_bis = df_bis.fillna(method='ffill').fillna(method='bfill')
        # df_ret = df_bis.pct_change().fillna(0.)
        df_ret = df_bis.copy()
        prices = df_bis[strats].values

        for col in strats:
            print(col + str(len(df_bis.columns)))
            df_ret[col] = df_bis[col].pct_change().fillna(0.)

        print('return done')
        print('return computed')

        ret_df = df_ret[strats]
        print('macro index/cash proxy return')
        ret_df = ret_df.mean(axis=1)
        ret_df = ret_df.to_frame()
        ret_df.columns =['PROXY_MARKET']
        ret_df['CASH'] = 0.
        strats = ['CASH','PROXY_MARKET']
        ret = ret_df.values

        feat = df_ret[features_names].values

        dates = df_ret.index


        T = ret_df.index.size
        N = ret_df.columns.size
        w0 = np.ones([N]) / N
        w_ = w0
        previous_w_dic = {}
        previous_w_dic['f_minVar']   = w_.copy()
        previous_w_dic['f_maxMean']  = w_.copy()
        previous_w_dic['f_MeanVar']  = w_.copy()
        previous_w_dic['f_sharpe']   = w_.copy()
        previous_w_dic['f_calmar']   = w_.copy()
        previous_w_dic['f_drawdown'] = w_.copy()

        # print('saving df_ret')
        # df_ret.to_pickle('../data/df_ret.pkl')

        print("recomputing supervision weights")
        # Set constraints and minimze

        utility_size = 6
        result = np.zeros([T, N, utility_size], np.float64)

        def process(series):
            # True if less than 50% of obs. are constant
            return series.value_counts(dropna=False).max() < cutting_rate_threshold * rebal

        # for t in range(max(n_past_features, s), T - s):
        for t in range(rebal, T):
            np.random.seed(0)
            torch.manual_seed(0)
            if t % 500 == 0:
                print('{:.2%}'.format(t / T))
            # we compute the utility output to predict only if not in future
            if t + rebal <= T:
                t_s = t+rebal
                X = ret[t: t_s, :]
                mat_cov = np.cov(X, rowvar=False)
                # Avoid constant assets
                sub_X = ret_df.iloc[t: t_s, :].copy()
                assets = sub_X.apply(process).values
                N_ = assets.sum()
                if N_ != 0:
                    def f_minVar(w):
                        w = w.reshape([N_, 1])
                        return np.sqrt(w.T @ mat_cov[assets][:, assets] @ w)
                    def f_maxMean(w):
                        w = w.reshape([N_, 1])
                        return - np.mean(np.cumprod(X[:, assets] @ w + 1, axis=0)[-1, :])
                    def f_MeanVar(w):
                        w = w.reshape([N_, 1])
                        std_dev = np.sqrt(w.T @ mat_cov[assets][:, assets] @ w)
                        mean_ret = np.mean(np.cumprod(X[:, assets] @ w + 1, axis=0)[-1, :])
                        return np.sqrt(252) * std_dev - (np.float_power(mean_ret, rebal / 252) - 1)
                    def f_sharpe(w):
                        w = w.reshape([N_, 1])
                        return - metrics.sharpe(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1)))
                    def f_calmar(w):
                        w = w.reshape([N_, 1])
                        return - metrics.calmar(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1)))
                    def f_drawdown(w):
                        w = w.reshape([N_, 1])
                        return metrics.drawdown(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1))).max()
                    # Set constraints
                    const_sum = LinearConstraint(np.ones([1, N_]), [1], [1])
                    up_bound_ = max(up_bound, 1 / N_)
                    low_bound_ = min(low_bound, 1 / N_)
                    const_ind = Bounds(low_bound_ * np.ones([N_]), up_bound_ * np.ones([N_]))
                    # Search optimal weights => target
                    f_list = [f_minVar, f_maxMean, f_sharpe, f_MeanVar, f_calmar, f_drawdown]
                    i = 0
                    for f in f_list:
                        previous_w_ = previous_w_dic[f.__name__]
                        np.random.seed(0)
                        torch.manual_seed(0)
                        # Optimize f
                        w__ = minimize(
                            f,
                            previous_w_[assets],
                            method='SLSQP',
                            constraints=[const_sum],
                            bounds=const_ind
                        ).x

                        if np.isnan(w__.sum()):
                            print('Trouble converging : investigate')
                            w__ = previous_w_[assets]

                        w_[assets] = w__
                        w_[~assets] = 0.
                        s_w = w_.sum()

                        if s_w == 1.:
                            next_w = w_
                        elif s_w != 0.:
                            next_w = w_ / s_w
                        else:
                            next_w = w0
                        result[t: t + 1, :, i] = next_w
                        previous_w_dic[f.__name__] = next_w
                        i += 1


                else:
                    for ii in range(utility_size):
                        result[t: t + 1, :, ii] = w0


        print('saving localy file')


        print(np.isnan(result).sum(axis=0).sum())
        print(np.isinf(result).sum(axis=0).sum())
        if np.isnan(result).sum(axis=0).sum() > 0:
            raise Exception('trouble : nan in supervised output')
        if np.isinf(result).sum(axis=0).sum() > 0:
            raise Exception('trouble : nan in supervised output')

        self.dbx.local_supervision_npy_save_and_upload(data = result, rebal = rebal , local_root_directory= self.local_root_directory, user = self.user, supervision_npy_file_suffix= self.macro_supervision_npy_file_suffix)
        print('files saved and updated to dropbox')

    def computeUtility(self, rebal=10,low_bound=0.02, up_bound=0.4, cutting_rate_threshold=0.7):
        df = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder='', returns_pkl_file_name=self.returns_pkl_file_name, local_root_directory = self.local_root_directory)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        strats = [col for col in list(df.columns) if col != 'Date']

        print('size return '+str(df.shape))
        advanced_features = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder=self.macro_features_directory, returns_pkl_file_name=self.features_pkl_file_name, local_root_directory = self.local_root_directory)
        features_names = [col for col in list(advanced_features.columns) if col!='Date']
        advanced_features['Date'] = pd.to_datetime(advanced_features['Date'])

        max_date = max(advanced_features['Date'])
        print('Maximum features date '+str(max_date))
        print('size advanced_features '+str(advanced_features.shape))

        df=df[df.index>=self.starting_date]
        df=df[df.index<=self.running_date]
        df = df.fillna(method='ffill')
        print('Maximum running date '+str(max(df.index)))

        np.random.seed(0)
        torch.manual_seed(0)
        ##===================##
        ##  Setting targets  ##
        ##===================##

        df_bis = df.copy()

        print('merging')
        df_bis = pd.merge(df_bis, advanced_features, how='left', on=['Date'])

        print('merging done')
        df_bis.index = df_bis['Date']
        df_bis = df_bis.drop(columns=['Date'])
        print('return')

        df_bis = df_bis.fillna(method='ffill').fillna(method='bfill')
        # df_ret = df_bis.pct_change().fillna(0.)
        df_ret = df_bis.copy()
        prices = df_bis[strats].values

        for col in strats:
            print(col + str(len(df_bis.columns)))
            df_ret[col] = df_bis[col].pct_change().fillna(0.)

        print('return done')
        print('return computed')

        ret_df = df_ret[strats]
        ret = ret_df.values

        feat = df_ret[features_names].values

        dates = df_ret.index


        T = df.index.size
        N = df.columns.size
        w0 = np.ones([N]) / N
        w_ = w0
        previous_w_dic = {}
        previous_w_dic['f_minVar']   = w_.copy()
        previous_w_dic['f_maxMean']  = w_.copy()
        previous_w_dic['f_MeanVar']  = w_.copy()
        previous_w_dic['f_sharpe']   = w_.copy()
        previous_w_dic['f_calmar']   = w_.copy()
        previous_w_dic['f_drawdown'] = w_.copy()

        # print('saving df_ret')
        # df_ret.to_pickle('../data/df_ret.pkl')

        print("recomputing supervision weights")
        # Set constraints and minimze

        utility_size = 6
        result = np.zeros([T, N, utility_size], np.float64)

        def process(series):
            # True if less than 50% of obs. are constant
            return series.value_counts(dropna=False).max() < cutting_rate_threshold * rebal

        # for t in range(max(n_past_features, s), T - s):
        for t in range(rebal, T):
            np.random.seed(0)
            torch.manual_seed(0)
            if t % 500 == 0:
                print('{:.2%}'.format(t / T))
            # we compute the utility output to predict only if not in future
            if t + rebal <= T:
                t_s = min(t + rebal, T)
                X = ret[t: t_s, :]
                mat_cov = np.cov(X, rowvar=False)
                # Avoid constant assets
                sub_X = ret_df.iloc[t: t_s, :].copy()
                assets = sub_X.apply(process).values
                N_ = assets.sum()
                if N_ != 0:
                    def f_minVar(w):
                        w = w.reshape([N_, 1])
                        return np.sqrt(w.T @ mat_cov[assets][:, assets] @ w)
                    def f_maxMean(w):
                        w = w.reshape([N_, 1])
                        return - np.mean(np.cumprod(X[:, assets] @ w + 1, axis=0)[-1, :])
                    def f_MeanVar(w):
                        w = w.reshape([N_, 1])
                        std_dev = np.sqrt(w.T @ mat_cov[assets][:, assets] @ w)
                        mean_ret = np.mean(np.cumprod(X[:, assets] @ w + 1, axis=0)[-1, :])
                        return np.sqrt(252) * std_dev - (np.float_power(mean_ret, rebal / 252) - 1)
                    def f_sharpe(w):
                        w = w.reshape([N_, 1])
                        return - metrics.sharpe(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1)))
                    def f_calmar(w):
                        w = w.reshape([N_, 1])
                        return - metrics.calmar(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1)))
                    def f_drawdown(w):
                        w = w.reshape([N_, 1])
                        return metrics.drawdown(np.cumprod(np.prod(X[:, assets] @ w + 1, axis=1))).max()
                    # Set constraints
                    const_sum = LinearConstraint(np.ones([1, N_]), [1], [1])
                    up_bound_ = max(up_bound, 1 / N_)
                    low_bound_ = min(low_bound, 1 / N_)
                    const_ind = Bounds(low_bound_ * np.ones([N_]), up_bound_ * np.ones([N_]))
                    # Search optimal weights => target
                    f_list = [f_minVar, f_maxMean, f_sharpe, f_MeanVar, f_calmar, f_drawdown]
                    i = 0
                    for f in f_list:
                        previous_w_ = previous_w_dic[f.__name__]
                        np.random.seed(0)
                        torch.manual_seed(0)
                        # Optimize f
                        w__ = minimize(
                            f,
                            previous_w_[assets],
                            method='SLSQP',
                            constraints=[const_sum],
                            bounds=const_ind
                        ).x

                        if np.isnan(w__.sum()):
                            print('Trouble converging : investigate')
                            w__ = previous_w_[assets]

                        w_[assets] = w__
                        w_[~assets] = 0.
                        s_w = w_.sum()

                        if s_w == 1.:
                            next_w = w_
                        elif s_w != 0.:
                            next_w = w_ / s_w
                        else:
                            next_w = w0
                        result[t: t + 1, :, i] = next_w
                        previous_w_dic[f.__name__] = next_w
                        i += 1


                else:
                    for ii in range(utility_size):
                        result[t: t + 1, :, ii] = w0


        print('saving localy file')
        print(np.isnan(result).sum(axis=0).sum())
        print(np.isinf(result).sum(axis=0).sum())
        if np.isnan(result).sum(axis=0).sum() > 0:
            raise Exception('trouble : nan in supervised output')
        if np.isinf(result).sum(axis=0).sum() > 0:
            raise Exception('trouble : nan in supervised output')

        print('final supervision shape '+ str(result.shape))
        self.dbx.local_supervision_npy_save_and_upload(starting_date= self.starting_date, ending_date = self.running_date, data = result, rebal = rebal , lower_bound= low_bound, upper_bound= up_bound,  local_root_directory= self.local_root_directory, user = self.user, supervision_npy_file_suffix= self.supervision_npy_file_suffix)
        print('files saved and updated to dropbox')






