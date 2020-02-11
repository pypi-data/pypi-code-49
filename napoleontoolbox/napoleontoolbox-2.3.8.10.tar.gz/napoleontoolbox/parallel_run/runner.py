#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import torch.nn.functional as F

from napoleontoolbox.neural_net import roll_multi_layer_lstm
from napoleontoolbox.file_saver import dropbox_file_saver
from napoleontoolbox.neural_net import roll_multi_layer_perceptron
from napoleontoolbox.boosted_trees import roll_lightgbm
from napoleontoolbox.features import features_type
from napoleontoolbox.utility import weights
from napoleontoolbox.model_state import resuming_state
from napoleontoolbox.utility import utility

import torch
import torch.nn as nn



class AbstractRunner(ABC):
    def __init__(self, starting_date = None, running_date = None, drop_token=None, dropbox_backup = True, save_model=False, supervision_npy_file_suffix='_supervision.npy', macro_supervision_npy_file_suffix='_macro_supervision.npy', features_saving_suffix='_features.npy', features_names_saving_suffix='_features_names.npy', returns_pkl_file_name='returns.pkl', local_root_directory='../data/', user = 'napoleon', n_start = 252, maximum_precision = False):
        super().__init__()
        self.supervision_npy_file_suffix=supervision_npy_file_suffix
        self.macro_supervision_npy_file_suffix=macro_supervision_npy_file_suffix
        self.features_saving_suffix=features_saving_suffix
        self.features_names_saving_suffix=features_names_saving_suffix
        self.returns_pkl_file_name=returns_pkl_file_name
        self.local_root_directory=local_root_directory
        self.user=user
        self.n_start = n_start
        self.dropbox_backup = dropbox_backup
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token=drop_token,dropbox_backup=dropbox_backup)
        self.save_model = save_model
        self.running_date = running_date
        self.starting_date = starting_date
        self.maximum_precision = maximum_precision

    @abstractmethod
    def runTrial(self,saver, seed, sup, layers, epochs, n_past_features, n, s, whole_history, advance_feature, advance_signal,
                 normalize, activation_string, convolution, lr_start, lr_type, low_bound, up_bound):
        pass


class SimpleRunner(AbstractRunner):
    def runTrial(self, saver, seed, sup, layers, epochs, n_past_features, n, s, feature_type, activation_type, convolution, lr_start, lr_type, low_bound, up_bound, normalize):
        if (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED) and n_past_features is None:
            print('n_past_features must not be None for LSTM history features')
            return
        if (feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_ADVANCED) and n_past_features is not None:
            print('n_past_features must be None for LSTM history features')
            return

        meArg = (
            seed, sup, layers, epochs, n_past_features, n, s, feature_type,
            activation_type, convolution, lr_start, lr_type, low_bound, up_bound, normalize)

        meArgList = list(meArg)
        meArgList = [str(it) for it in meArgList]
        savingKey = ''.join(meArgList)
        savingKey = savingKey.replace('[', '')
        savingKey = savingKey.replace(']', '')
        savingKey = savingKey.replace(',', '')
        savingKey = savingKey.replace(' ', '')
        savingKey = savingKey.replace('.', '')
        # savingKey = savingKey.replace('_','')
        savingKey = 'T_' + savingKey

        print('Launching computation with parameters : '+savingKey)

        ## checking if the computation has already been done
        if saver.checkRunExistence(savingKey):
            print('Run already present : we do nothing')
            return

        supervisors = {}
        supervisors['f_minVar'] = 0
        supervisors['f_maxMean'] = 1
        supervisors['f_sharpe'] = 2
        supervisors['f_MeanVar'] = 3
        supervisors['f_calmar'] = 4
        supervisors['f_drawdown'] = 5

        print('running date '+str(self.running_date))

        df = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder='', returns_pkl_file_name=self.returns_pkl_file_name, local_root_directory = self.local_root_directory)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        df = df[df.index>=self.starting_date]
        df = df[df.index<=self.running_date]
        df = df.fillna(method='ffill')
        print('returns size  '+str(df.shape))
        print('min running date '+str(min(df.index)))
        print('max running date '+str(max(df.index)))

        print('loading supervision results')
        result =self.dbx.local_supervision_npy_overwrite_and_load_array(starting_date= self.starting_date, ending_date = self.ending_date, rebal = s , lower_bound= low_bound, upper_bound = up_bound, local_root_directory= self.local_root_directory, user = self.user, supervision_npy_file_suffix= self.supervision_npy_file_suffix)
        print('supervision results shape')
        print(result.shape)

        np.random.seed(seed)
        torch.manual_seed(seed)
        # Set data
        whole_history = (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED)

        features, features_names = self.dbx.local_features_npy_ovverwrite_and_load_array(starting_date= self.starting_date, ending_date = self.running_date,feature_type=feature_type, n_past_features=n_past_features,
                                                    local_root_directory=self.local_root_directory, user=self.user,
                                                    features_saving_suffix=self.features_saving_suffix,
                                                    features_names_saving_suffix=self.features_names_saving_suffix)


        # the save files necessarily match the beginning date
        features = features[:len(df)]
        result = result[:len(df)]

        X = features[self.n_start:]
        y = result[self.n_start:, :, supervisors[sup]]
        df = df.iloc[self.n_start:]

        print('predictors')
        print(X.shape)
        print('utility')
        print(y.shape)
        print('prices')
        print(df.shape)

        assert df.shape[0] >= X.shape[0]
        assert df.shape[0] >= y.shape[0]

        # convolution 0 : perceptron
        # convolution 1 : LSTM
        # convolution 2 : xgboost
        if whole_history:
            if convolution == 2:
                print('no whole time history with ensembling method')
                return
            if convolution == 0:
                print('no whole time history with multi layers perceptron')
                return
                # uncomment if you want multi layers perceptron with full historical backtest
                # print('flattening predictor time series for perceptron')
                # _X = np.empty((X.shape[0], X.shape[1] * X.shape[2]), dtype=np.float32)
                # for l in range(X.shape[0]):
                #     temp = np.transpose(X[l, :, :])
                #     _X[l, :] = temp.flatten()
                # X = _X

        if not whole_history:
            if convolution == 1:
                print('only whole time history with lstm')
                # print('adding one virtual time stamp')
                # X = X[..., np.newaxis, :]
                return

        print('number of nan/infinity features')
        print(np.isnan(X).sum(axis=0).sum())
        print(np.isinf(X).sum(axis=0).sum())
        print('number of nan/infinity output')
        print(np.isnan(y).sum(axis=0).sum())
        print(np.isinf(y).sum(axis=0).sum())

        print(np.count_nonzero(~np.isnan(X)))


        if self.maximum_precision:
            X = np.float64(X)
            y = np.float64(y)
        else :
            X = np.float32(X)
            y = np.float32(y)


        neural_net_precision = None
        if X.dtype == np.float64:
            neural_net_precision = torch.float64
        if X.dtype == np.float32:
            neural_net_precision = torch.float32

        activation_function = utility.convertActivationType(activation_type)

        if convolution == 1:
            # the number of figures
            input_size = X.shape[2]
            hidden_size = int(layers[-1])
            num_layers = int(layers[-2])
            num_classes = y.shape[1]
            tm = roll_multi_layer_lstm.RollMultiLayerLSTM(
                X=X,
                y=y,
                num_classes=num_classes,
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr_type, lr=lr_start, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 0:
            tm = roll_multi_layer_perceptron.RollMultiLayerPerceptron(
                X=X,
                y=y,
                layers=layers,
                activation=activation_function,  # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision,
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr_type, lr=lr_start, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 2:
            tm = roll_lightgbm.RollLightGbm(
                X=X,
                y=y
            )
            tm = tm.set_roll_period(n, s)

        eval_slice, test_slice = tm.unroll()
        dates_eval_slice, dates_test_slice = df.index[eval_slice], df.index[test_slice]

        state = resuming_state.ModelState(
            eval_slice = eval_slice,
            test_slice = test_slice,
            dates_eval_slice = dates_eval_slice,
            dates_test_slice = dates_test_slice,
            df_eval = df.loc[dates_eval_slice],
            df_test = df.loc[dates_test_slice],
            X_eval = X[eval_slice],
            X_test = X[test_slice],
            y_eval = y[eval_slice],
            y_test = y[test_slice],
            pred_test = tm.y_test[test_slice],
            pred_eval = tm.y_eval[eval_slice]
        )

        recordings_df, activations_df = tm.recorder.get_all_recordings()
        print('recordings '+str(list(recordings_df.columns)))
        print('activatiions ' + str(list(activations_df.columns)))

        # tm.y_test[tm.t:] = tm.sub_predict(tm.X[tm.t:])
        df_ret = df.fillna(method='bfill').pct_change().fillna(0).copy()
        # Process weights
        print('processing weights for '+savingKey)
        weight_mat, last_predicted_weights = weights.process_weights(w=tm.y_test, df=df_ret, s=s, n=n, low_bound=low_bound, up_bound=up_bound,normalize=normalize)
        # Compute portfolio perf
        portfolio = np.cumprod(np.prod(df_ret * weight_mat.values + 1, axis=1))
        if self.save_model :
            tm.save_model_and_last_state(state=state,model_path = self.local_root_directory+savingKey)
        if self.dropbox_backup:
            self.dbx.uploadFileToDropbox(filename=savingKey+'_model.torch', dropbox_subfolder = '', fullpath=self.local_root_directory+savingKey+'_model.torch')
            self.dbx.uploadFileToDropbox(filename=savingKey+'_py.obj', dropbox_subfolder = '', fullpath=self.local_root_directory+savingKey+'_py.obj')

        saver.saveResults(savingKey, portfolio, weight_mat, recordings_df, activations_df)
        print('saved '+ savingKey)
        return  last_predicted_weights



class ResumingRunner(AbstractRunner):
    def runTrial(self, saver, seed, sup, layers, epochs, n_past_features, n, s, feature_type, activation_type, convolution, lr_start, lr_type, low_bound, up_bound, normalize):
        if (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED) and n_past_features is None:
            print('n_past_features must not be None for LSTM history features')
            return
        if (feature_type is features_type.FeaturesType.STANDARD or feature_type is features_type.FeaturesType.STANDARD_ADVANCED) and n_past_features is not None:
            print('n_past_features must be None for LSTM history features')
            return

        meArg = (
            seed, sup, layers, epochs, n_past_features, n, s, feature_type,
            activation_type, convolution, lr_start, lr_type, low_bound, up_bound, normalize)

        meArgList = list(meArg)
        meArgList = [str(it) for it in meArgList]
        savingKey = ''.join(meArgList)
        savingKey = savingKey.replace('[', '')
        savingKey = savingKey.replace(']', '')
        savingKey = savingKey.replace(',', '')
        savingKey = savingKey.replace(' ', '')
        savingKey = savingKey.replace('.', '')
        # savingKey = savingKey.replace('_','')
        savingKey = 'T_' + savingKey

        print('Launching computation with parameters : '+savingKey)

        supervisors = {}
        supervisors['f_minVar'] = 0
        supervisors['f_maxMean'] = 1
        supervisors['f_sharpe'] = 2
        supervisors['f_MeanVar'] = 3
        supervisors['f_calmar'] = 4
        supervisors['f_drawdown'] = 5

        df = self.dbx.local_overwrite_and_load_pickle( folder='', subfolder='', returns_pkl_file_name=self.returns_pkl_file_name, local_root_directory = self.local_root_directory)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')
        df = df[df.index<=self.running_date]
        df = df.fillna(method='ffill')
        print('returns size  '+str(df.shape))
        print('min running date '+str(min(df.index)))
        print('max running date '+str(max(df.index)))




        result =self.dbx.local_supervision_npy_overwrite_and_load_array(rebal = s , lower_bound= low_bound, upper_bound = up_bound, local_root_directory= self.local_root_directory, user = self.user, supervision_npy_file_suffix= self.supervision_npy_file_suffix)

        np.random.seed(seed)
        torch.manual_seed(seed)
        # Set data
        whole_history = (feature_type is features_type.FeaturesType.HISTORY or feature_type is features_type.FeaturesType.HISTORY_ADVANCED)

        features, features_names = self.dbx.local_features_npy_ovverwrite_and_load_array(feature_type=feature_type, n_past_features=n_past_features,
                                                    local_root_directory=self.local_root_directory, user=self.user,
                                                    features_saving_suffix=self.features_saving_suffix,
                                                    features_names_saving_suffix=self.features_names_saving_suffix)



        # X = features[s:-s]
        # y = result[s:-s, :, supervisors[sup]]
        X = features[self.n_start:]
        y = result[self.n_start:, :, supervisors[sup]]
        df = df.iloc[self.n_start:]
        print('predictors')
        print(X.shape)
        print('utility')
        print(y.shape)
        print('prices')
        print(df.shape)

        # convolution 0 : perceptron
        # convolution 1 : LSTM
        # convolution 2 : xgboost

        if whole_history:
            if convolution == 2:
                print('no whole time history with ensembling method')
                return
            if convolution == 0:
                print('no whole time history with multi layers perceptron')
                # uncomment if you want multi layers perceptron with full historical backtest
                # print('flattening predictor time series for perceptron')
                # _X = np.empty((X.shape[0], X.shape[1] * X.shape[2]), dtype=np.float32)
                # for l in range(X.shape[0]):
                #     temp = np.transpose(X[l, :, :])
                #     _X[l, :] = temp.flatten()
                # X = _X

        if not whole_history:
            if convolution == 1:
                print('only whole time history with lstm')
                # print('adding one virtual time stamp')
                # X = X[..., np.newaxis, :]
                return

        print('number of nan/infinity features')
        print(np.isnan(X).sum(axis=0).sum())
        print(np.isinf(X).sum(axis=0).sum())
        print('number of nan/infinity output')
        print(np.isnan(y).sum(axis=0).sum())
        print(np.isinf(y).sum(axis=0).sum())

        print(np.count_nonzero(~np.isnan(X)))

        X = np.float32(X)
        y = np.float32(y)

        neural_net_precision = None
        if X.dtype == np.float64:
            neural_net_precision = torch.float64
        if X.dtype == np.float32:
            neural_net_precision = torch.float32

        activation_function = utility.convertActivationType(activation_type)

        if convolution == 1:
            # the number of figures
            input_size = X.shape[2]
            hidden_size = int(layers[-1]/2)
            num_layers = 1
            num_classes = y.shape[1]
            tm = roll_multi_layer_lstm.RollMultiLayerLSTM(
                X=X,
                y=y,
                num_classes=num_classes,
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr_type, lr=lr_start, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 0:
            tm = roll_multi_layer_perceptron.RollMultiLayerPerceptron(
                X=X,
                y=y,
                layers=layers,
                activation=activation_function,  # nn.Softmax/nn.Softmin can be good activations for this problem
                x_type=neural_net_precision,
                y_type=neural_net_precision,
                # activation_kwargs={'dim':1} # Parameter needed for nn.Softmax/nn.Softmin
            )
            tm.set_optimizer(nn.MSELoss, torch.optim.Adam, lr_type, lr=lr_start, betas=(0.9, 0.999), amsgrad=True)
            tm = tm.set_roll_period(n, s, repass_steps=epochs)
        elif convolution == 2:
            tm = roll_lightgbm.RollLightGbm(
                X=X,
                y=y
            )
            tm = tm.set_roll_period(n, s)

        state = tm.resume_state(model_path = self.local_root_directory+savingKey)
        print('recovered state '+str(state))

