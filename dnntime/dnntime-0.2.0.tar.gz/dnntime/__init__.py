####################################################################################
####                     Auto Time Series Final  0.0.15                         ####
####                           Python 3 Version                                 ####
####                    Conceived and Developed by Ram Seshadri                 ####
####                        All Rights Reserved                                 ####
####################################################################################

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
sns.set(style="white", color_codes=True)
import copy
import ipdb
from collections import defaultdict
import operator
import time
#######################################
# Models
from .models import build_rnn_model, build_lstm_model, build_gru_model, build_convlstm_model
# Utils
from .utils import colorful, load_ts_data, clean_ts_data, convert_timeseries_dataframe_to_supervised, \
                          time_series_plot, print_static_rmse, print_dynamic_rmse
from .utils.classes import timesteps, interval_to_freq, interval_to_timesteps
from .utils.etl import split_data


def make_ts_magic(data, ts_column, sep=',', target=None, univarate=True,
                  time_interval='', forecast_period='', auto_clean=False,
                  score_type='rmse', conf_int=0.95, model_type='all', verbose=0):
    """
    ####################################################################################
    ####                          Auto Time Series                                  ####
    ####                           Python 3 Version                                 ####
    ####                    Authored and Developed by Kevin Chen                    ####
    ####                    Original Credit to Ram Seshadri                         ####
    ####                        All Rights Reserved                                 ####
    ####################################################################################
    ##################################################################################################
    DEEP_TIMESERIES IS A COMPLEX MODEL BUILDING UTILITY FOR TIME SERIES DATA. SINCE IT AUTOMATES MANY
    TASKS INVOLVED IN A COMPLEX ENDEAVOR, IT ASSUMES MANY INTELLIGENT DEFAULTS. BUT YOU CAN CHANGE THEM.
    Auto_Timeseries will rapidly build predictive models based on Statsmodels ARIMA, Seasonal ARIMA
    and Scikit-Learn ML. It will automatically select the BEST model which gives best score specified.
    It will return the best model and a dataframe containing predictions for forecast_period (default=2).
    #####################################################################################################
    INPUT:
    #####################################################################################################
    trainfile: name of the file along with its data path or a dataframe. It accepts both.
    ts_column: name of the datetime column in your dataset (it could be name or number)
    target: name of the column you are trying to predict. Target could also be the only column in your data
    score_type: 'rmse' is the default. You can choose among "mae", "mse" and "rmse".
    forecast_period: default is 2. How many periods out do you want to forecast? It should be an integer
    time_interval: default is "Month". What is the time period in your data set. Options are: "days",
    model_type: default is "stats". Choice is between "stats", "prophet" and "ml". "All" will build all.
        - stats will build statsmodels based ARIMA< SARIMAX and VAR models
        - ml will build a machine learning model using Random Forests provided explanatory vars are given
        - prophet will build a model using FB Prophet -> this means you must have FB Prophet installed
        - all will build all the above models which may take a long time for large data sets.
    We recommend that you choose a small sample from your data set bedfore attempting to run entire data.
    #####################################################################################################
    and the evaluation metric so it can select the best model. Currently only 2 are supported: RMSE and
    Normalized RMSE (ratio of RMSE to the standard deviation of actuals). Other eval metrics will be soon.
    the target variable you are trying to predict (if there is more than one variable in your data set),
    and the time interval that is in the data. If your data is in a different time interval than given,
    Auto_Timeseries will automatically resample your data to the given time interval and learn to make
    predictions. Notice that except for filename and ts_column which are required, all others are optional.
    Note that optionally you can give a separator for the data in your file. Default is comman (",").
    "time_interval" options are: 'Days', 'Weeks', 'Months', 'Qtr', 'Year', 'Minutes', 'Hours', 'Seconds'.
    Optionally, you can give seasonal_period as any integer that measures the seasonality in the data.
    If not, seasonal_period is assumed automatically as follows: Months = 12, Days = 30, Weeks = 52,
    Qtr = 4, Year = 1, Hours = 24, Minutes = 60 and Seconds = 60.
    If you want to give your own order, please input it as non_seasonal_pdq and seasonal_PDQ in the input
    as tuples. For example, seasonal_PDQ = (2,1,2) and non_seasonal_pdq = (0,0,3). It will accept only tuples.
    The defaul is None and Auto_Timeseries will automatically search for the best p,d,q (for Non Seasonal)
    and P, D, Q (for Seasonal) orders by searching for all parameters from 0 to 12 for each value of
    p,d,q and 0-3 for each P, Q and 0-1 for D.
    #####################################################################################################
    """

    start_time = time.time()

    ##### Best hyper-parameters in statsmodels chosen using the best aic, bic or whatever. Select here.
    stats_scoring = 'aic'
    seed = 99


    ########## This is where we start the loading of the data file ######################
    ts_df = load_ts_data(data, ts_column, sep)
    freq, _ = interval_to_freq(time_interval)

    if auto_clean:
        ts_df = clean_ts_data(ts_df, target, as_freq=freq)
    df_orig = copy.deepcopy(ts_df)

    # Set target if not already done so
    if target is None:
        if ts_df.shape[1] == 1:
            ### If there is only one column, you assume that to be the target column ####
            target = ts_df.columns[0]
        else:
            raise ValueError("No target column name specified.")
            return
    elif target in ['first_col', 'first_column']:
        target = ts_df.columns[0]
        print(f"    Taking the first column '{target}' in dataset as target variable.")
    elif target in ['last_col', 'last_column']:
        target = ts_df.columns[-1]
        print(f"    Taking the last column '{target}' in dataset as target variable.")
    # Create univerate time-series from dataset if specified, else leave as it is
    if univarate:
        ts_df = ts_df[target].to_frame()

    ts_df = ts_df['2018'] # hardcoded data cutoff

    ##################################################################################################
    ### Turn the time series index into a variable and calculate the difference.
    ### If the difference is not in days, then it is a hourly or minute based time series
    ### If the difference a multiple of days, then test it for weekly, monthly, qtrly, annual etc.
    ##################################################################################################
    # if ts_df.index.dtype=='int' or ts_df.index.dtype=='float':
    #     ### You must convert the ts_df index into a date-time series using the ts_column given ####
    #     ts_df = ts_df.set_index(ts_column)
    # ts_index = ts_df.index

    ################    IF TIME INTERVAL IS NOT GIVEN DO THIS   ########################
    #######   This is where the program tries to tease out the time period in the data set ###########
    ##################################################################################################
    # if time_interval == '':
    #     ts_index = pd.to_datetime(ts_df.index)
    #     diff = (ts_index[1] - ts_index[0]).to_pytimedelta()
    #     diffdays = diff.days
    #     diffsecs = diff.seconds
    #     if diffsecs == 0:
    #         diff_in_hours = 0
    #         diff_in_days = abs(diffdays)
    #     else:
    #         diff_in_hours = abs(diffdays*24*3600 + diffsecs)/3600
    #     if diff_in_hours == 0 and diff_in_days >= 1:
    #         print('Time series input in days = %s' % diff_in_days)
    #         if diff_in_days == 7:
    #             print('it is a Weekly time series.')
    #             time_interval = 'weeks'
    #         elif diff_in_days == 1:
    #             print('it is a Daily time series.')
    #             time_interval = 'days'
    #         elif 28 <= diff_in_days < 89:
    #             print('it is a Monthly time series.')
    #             time_interval = 'months'
    #         elif 89 <= diff_in_days < 178:
    #             print('it is a Quarterly time series.')
    #             time_interval = 'qtr'
    #         elif 178 <= diff_in_days < 360:
    #             print('it is a Semi Annual time series.')
    #             time_interval = 'qtr'
    #         elif diff_in_days >= 360:
    #             print('it is an Annual time series.')
    #             time_interval = 'years'
    #         else:
    #             print('Time Series time delta is unknown')
    #             return
    #     if diff_in_days == 0:
    #         if diff_in_hours == 0:
    #             print('Time series input in Minutes or Seconds = %s' % diff_in_hours)
    #             print('it is a Minute time series.')
    #             time_interval = 'minutes'
    #         elif diff_in_hours >= 1:
    #             print('it is an Hourly time series.')
    #             time_interval = 'hours'
    #         else:
    #             print('It is an Unknown Time Series delta')
    #             return
    # else:
    #     print('Time Interval is given as %s' % time_interval)

    ################# This is where you test the data and find the time interval #######
    #create train, test data
    n_input = interval_to_timesteps('biweek', freq)  # let's input the two weeks (24*14 timesteps)
    n_output = interval_to_timesteps(forecast_period, freq)  # let's forecast the next day (24 timesteps)
    n_val = interval_to_timesteps('biweek', freq)  # validation dataset size
    n_test = interval_to_timesteps('month', freq)

    # Hyperparameters
    n_features = 1  # number of feature(s)
    n_units = 128   # number of units per layer
    d_rate = 0.15   # dropout rate

    n_batch = 512  # batch size
    n_epoch = 2    # number of epochs


    ##################################################################################################
    ### Transform dataset into supervised ML problem with walk-forward validation.
    ### Shifting time-steps
    ##################################################################################################
    orig, train, val, test = split_data(ts_df,
                                        n_test=n_test,  # size of test set
                                        n_val=n_val,  # size of validation set
                                        n_input=n_input,   # input timestep seq
                                        n_output=n_output, # output timestep seq
                                        g_min=0,     # min gap ratio
                                        g_max=0.01)  # max gap ratio

    X, y, t = orig  # original data tuple in supervised format
    X_train, y_train, t_train = train
    X_val, y_val, t_val = val
    X_test, y_test, t_test = test

    print(f"data shape = ", ts_df.shape)
    print("X.shape = ", X.shape)
    print("y.shape = ", y.shape)
    print("t.shape = ", t.shape)
    print("X_train.shape = ", X_train.shape)
    print("y_train.shape = ", y_train.shape)
    print("t_train.shape = ", t_train.shape)
    print("X_val.shape = ", X_val.shape)
    print("y_val.shape = ", y_val.shape)
    print("t_val.shape = ", t_val.shape)
    print("X_test.shape = ", X_test.shape)
    print("y_test.shape = ", y_test.shape)
    print("t_test.shape = ", t_test.shape)

    train_prct = round(len(X_train)/len(X)*100, 2)
    val_prct = round(len(X_val)/len(X)*100, 2)
    test_prct = round(len(X_test)/len(X)*100, 2)
    gap_prct = round(100-train_prct-val_prct-test_prct, 2)
    print("\nSplit %:")
    print(f"Train: {train_prct}%, Val: {val_prct}%, Test: {test_prct}%, Gap: {gap_prct}%")


    ########################### This is where we store all models in a nested dictionary ##########
    mldict = lambda: defaultdict(mldict)
    ml_dict = mldict()
    try:
        if model_type.lower() == 'all':
            print('Running all model types. This will take a long time. Be Patient...')
    except:
        print('Check if your model type is a string or one of the available types of models')
    # ######### This is when you need to use FB Prophet ###################################
    # ### When the time interval given does not match the tested_time_interval, then use FB.
    # #### Also when the number of rows in data set is very large, use FB Prophet, It is fast.
    # #########                RNN              ###################################
    if model_type.lower() in ['rnn', 'all']:
        name = 'RNN'
        print(colorful.BOLD + '\nRunning a vanilla RNN Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_rnn_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    RNN may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['lstm', 'all']:
        name = 'LSTM'
        print(colorful.BOLD + '\nRunning a LSTM Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_lstm_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    LSTM may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['gru', 'all']:
        name = 'GRU'
        print(colorful.BOLD + '\nRunning a GRU Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_gru_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    GRU may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['convlstm', 'all']:
        name = 'CONVLSTM'
        print(colorful.BOLD + '\nRunning a ConvLSTM Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_lstm_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    ConvLSTM may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    # elif model_type.lower() in ['stats','all']:
    #     ##### First let's try the following models in sequence #########################################
    #     nsims = 100   ### this is needed only for M-H models in PyFlux
    #     name = 'PyFlux'
    #     print(colorful.BOLD + '\nRunning PyFlux Model...' + colorful.END)
    #     try:
    #         ml_dict[name]['model'], ml_dict[name]['forecast'], rmse, norm_rmse = \
    #             build_pyflux_model(ts_df, target, p_max, q_max, d_max, forecast_period,
    #                                'MLE', nsims, score_type, verbose)
    #         if isinstance(rmse,str):
    #             print('    PyFlux not installed. Install PyFlux and run it again')
    #             score_val = np.inf
    #             rmse = np.inf
    #             norm_rmse = np.inf
    #     except:
    #         print('    PyFlux model error: predictions not available.')
    #         score_val = np.inf
    #         rmse = np.inf
    #         norm_rmse = np.inf
    #     ##### Make sure that RMSE works, if not set it to np.inf  #########
    #     if score_type == 'rmse':
    #         score_val = rmse
    #     else:
    #         score_val = norm_rmse
    #     ml_dict[name][score_type] = score_val
    #     ################### Let's build an ARIMA Model and add results #################
    #     name = 'ARIMA'
    #     print(colorful.BOLD + '\nRunning Non Seasonal ARIMA Model...' + colorful.END)
    #     try:
    #         ml_dict[name]['model'], ml_dict[name]['forecast'], rmse, norm_rmse = build_arima_model(ts_df[target],
    #                                                 stats_scoring,p_max,d_max,q_max,
    #                                 forecast_period=forecast_period,method='mle',verbose=verbose)
    #     except:
    #         print('    ARIMA model error: predictions not available.')
    #         score_val = np.inf
    #     if score_type == 'rmse':
    #         score_val = rmse
    #     else:
    #         score_val = norm_rmse
    #     ml_dict[name][score_type] = score_val
    #     ############# Let's build a SARIMAX Model and get results ########################
    #     name = 'SARIMAX'
    #     print(colorful.BOLD + '\nRunning Seasonal SARIMAX Model...' + colorful.END)
    #     # try:
    #     ml_dict[name]['model'], ml_dict[name]['forecast'], rmse, norm_rmse = build_sarimax_model(ts_df[target], stats_scoring, seasonality,
    #                                             seasonal_period, p_max, d_max, q_max,
    #                                             forecast_period,verbose)
    #     # except:
    #     #     print('    SARIMAX model error: predictions not available.')
    #     #     score_val = np.inf
    #     if score_type == 'rmse':
    #         score_val = rmse
    #     else:
    #         score_val = norm_rmse
    #     ml_dict[name][score_type] = score_val
    #     ########### Let's build a VAR Model - but first we have to shift the predictor vars ####
    #     name = 'VAR'
    #     if len(preds) == 0:
    #         print('No VAR model since number of predictors is zero')
    #         rmse = np.inf
    #         norm_rmse = np.inf
    #     else:
    #         try:
    #             if df_orig.shape[1] > 1:
    #                 preds = [x for x in list(df_orig) if x not in [target]]
    #                 print(colorful.BOLD + '\nRunning VAR Model...' + colorful.END)
    #                 print('    Shifting %d predictors by 1 to align prior predictor values with current target values...'
    #                                         %len(preds))
    #                 ts_df[preds] = ts_df[preds].shift(1)
    #                 ts_df.dropna(axis=0,inplace=True)
    #                 ml_dict[name]['model'], ml_dict[name]['forecast'], rmse, norm_rmse = build_var_model(ts_df[[target]+preds],stats_scoring,
    #                                             forecast_period, p_max, q_max)
    #             else:
    #                 print(colorful.BOLD + '\nNo predictors available. Skipping VAR model...' + colorful.END)
    #                 score_val = np.inf
    #         except:
    #             print('    VAR model error: predictions not available.')
    #             rmse = np.inf
    #             norm_rmse = np.inf
    #     ################################################################
    #     if score_type == 'rmse':
    #         score_val = rmse
    #     else:
    #         score_val = norm_rmse
    #     ########################################################################
    #     ml_dict[name][score_type] = score_val
    # elif model_type.lower() in ['ml','all']:
    #     ########## Let's build a Machine Learning Model now with Time Series Data ################
    #     name = 'ML'
    #     if len(preds) == 0:
    #         print('No ML model since number of predictors is zero')
    #         rmse = np.inf
    #         norm_rmse = np.inf
    #     else:
    #         try:
    #             if df_orig.shape[1] > 1:
    #                 preds = [x for x in list(ts_df) if x not in [target]]
    #                 print(colorful.BOLD + '\nRunning Machine Learning Models...' + colorful.END)
    #                 print('    Shifting %d predictors by lag=%d to align prior predictor with current target...'
    #                             % (len(preds), lag))
    #                 # ipdb.set_trace()
    #                 dfxs, target, preds = convert_timeseries_dataframe_to_supervised(ts_df[preds+[target]],
    #                                         preds+[target], target, n_in=lag, n_out=0, dropT=False)
    #                 train = dfxs[:-forecast_period]
    #                 test = dfxs[-forecast_period:]
    #                 best = run_ensemble_model(train[preds], train[target], 'TimeSeries',
    #                                           score_type, verbose)
    #                 bestmodel = best[0]
    #                 ml_dict[name]['model'] = bestmodel
    #                 ### Certain models dont have random state => so dont do this for all since it will error
    #                 #best.set_params(random_state=0)
    #                 ml_dict[name]['forecast'] = bestmodel.fit(train[preds],train[target]).predict(test[preds])
    #                 rmse, norm_rmse = print_dynamic_rmse(test[target].values,
    #                                             bestmodel.predict(test[preds]),
    #                                             train[target].values)
    #                 #### Plotting actual vs predicted for RF Model #################
    #                 plt.figure(figsize=(5, 5))
    #                 plt.scatter(train.append(test)[target].values,
    #                             np.r_[bestmodel.predict(train[preds]), bestmodel.predict(test[preds])])
    #                 plt.xlabel('Actual')
    #                 plt.ylabel('Predicted')
    #                 plt.show()
    #                 ############ Draw a plot of the Time Series data ######
    #                 time_series_plot(dfxs[target], chart_time=time_interval)
    #             else:
    #                 print(colorful.BOLD + '\nNo predictors available. Skipping Machine Learning model...' + colorful.END)
    #                 score_val = np.inf
    #         except:
    #             print('    For ML model, evaluation score is not available.')
    #             score_val = np.inf
    #     ################################################################
    #     if score_type == 'rmse':
    #         score_val = rmse
    #     else:
    #         score_val = norm_rmse
    #         rmse = np.inf
    #         norm_rmse = np.inf
    #     ########################################################################
    #     ml_dict[name][score_type] = score_val
    # else:
    #     print('The model_type should be either stats, prophet, ml or all. Your input is not available.')
    #     return ml_dict
    # ######## Selecting the best model based on the lowest rmse score ######
    # f1_stats = {}
    # for key, val in ml_dict.items():
    #     f1_stats[key] = ml_dict[key][score_type]
    # best_model_name = min(f1_stats.items(), key=operator.itemgetter(1))[0]
    # print(colorful.BOLD + '\nBest Model is:' + colorful.END)
    # print('    %s' % best_model_name)
    # best_model = ml_dict[best_model_name]['model']
    # #print('    Best Model Forecasts: %s' %ml_dict[best_model_name]['forecast'])
    # print('    Best Model Score: %0.2f' % ml_dict[best_model_name][score_type])
    return ml_dict

##########################################################
#Defining AUTO_TIMESERIES here
##########################################################


if	__name__	== "__main__":
    version_number = '0.2.0'
    print("""Running Deep Timeseries version: %s...Call by using:
        auto_ts.Auto_Timeseries(trainfile, ts_column,
                            sep=',', target=None, score_type='rmse', forecast_period=2,
                            time_interval='Month', non_seasonal_pdq=None, seasonality=False,
                            seasonal_period=12, seasonal_PDQ=None,
                            verbose=0)
    To get detailed charts of actuals and forecasts, set verbose = 1""" % version_number)
else:
    version_number = '0.2.0'
    print("""Imported Deep_Timeseries version: %s. Call by using:
        auto_ts.Auto_Timeseries(trainfile, ts_column,
                            sep=',', target=None, score_type='rmse', forecast_period=2,
                            time_interval='Month', non_seasonal_pdq=None, seasonality=False,
                            seasonal_period=12, seasonal_PDQ=None,
                            verbose=0)
    To get detailed charts of actuals and forecasts, set verbose = 1""" % version_number)
