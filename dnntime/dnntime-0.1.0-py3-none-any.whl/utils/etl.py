import numpy as np
import pandas as pd
from random import randint
import copy
import ipdb
from sklearn.preprocessing import MinMaxScaler, StandardScaler, power_transform
from statsmodels.tsa.seasonal import seasonal_decompose
from tscv import gap_train_test_split


##### This function loads a time series data and sets the index as a time series
# def load_ts_data(filename, ts_column='', target='', sep=',', dt_index=True):
def load_ts_data(filename, ts_column):
    """
    This function loads a given filename into a pandas dataframe and sets the
    ts_column as a Time Series index. Note that filename should contain the full
    path to the file.
    """
    # if dt_index:
    try:
        df = pd.read_csv(filename, index_col=ts_column, parse_dates=True)
    except ValueError:
        print("Load failed. Please specify ts_column= and target=, or set dt_index=False.")
        return
    # else:
    #     df = pd.read_csv(filename)

    # if isinstance(filename, str):
    #     codes_list = ['utf-8', 'iso-8859-1', 'cp1252', 'latin1']
    #     print('First loading %s and then setting %s as date time index...' % (filename, ts_column))
    #     for codex in codes_list:
    #         try:
    #             df = pd.read_csv(filename, index_col=None, sep=sep, encoding=codex)
    #             df.index = pd.to_datetime(df.pop(ts_column))
    #             break
    #         except:
    #             print('    Encoder %s or Date time type not working for reading this file...' % codex)
    #             continue
    # else:
    #     ### If filename is not a string, it must be a dataframe and can be loaded
    #     dft = copy.deepcopy(filename)
    #     try:
    #         dft.index = pd.to_datetime(dft.pop(ts_column))
    #         preds = [x for x in list(dft) if x not in [target]]
    #         df = dft[[target]+preds]
    #     except:
    #         print('Error: Could not convert Time Series column to an index. Please check your input and try again')
    #         return dft
    return df


# def clean_ts_data(df, ts_column='', target='', as_freq='H', allow_neg=True, \
#                   dt_index=True, fill='linear', type='reg'):
def clean_ts_data(df, target, as_freq='H', allow_neg=True, fill='linear', type='reg'):

    dtc = df.copy()

    # if dt_index:
        # dt = dtc.index
        # Make sure DateTimeIndex is sorted just in case:
        # dtc.sort_index(inplace=True)
    # else:
    #     dt = dtc[ts_column]
    #     # Make sure time-series col is sorted just in case:
    #     dtc.sort_values(by=[ts_column], inplace=True)

    # 1) Sort DateTimeIndex is asc order just in case it hasn't been done
    dtc.sort_index(inplace=True)
    # 2) Check no duplicate time-series point, otherwise keep only first one
    if dtc.index.duplicated().sum() > 0:
        dtc = dtc.loc[~dtc.index.duplicated(keep='first')]
    # 3) Add freq to time-series col or index if it doesn't exist
    if not isinstance(dtc.index, pd.DatetimeIndex):
        f_idx = pd.date_range(start=dtc.index.min(), end=dtc.index.max(), freq=as_freq) \
                  .tz_localize(None)
        dtc.set_index(f_idx, inplace=True)
    elif dtc.index.freq is None:
        f_idx = pd.date_range(start=dtc.index.min(), end=dtc.index.max(), freq=as_freq) \
                  .tz_localize(None)
        if len(dtc) == len(f_idx):
            dtc.set_index(f_idx, inplace=True)
        else:
            dtc = dtc.reindex(f_idx)
    # 4) Convert target col type to float is not already and removing any puncuations
    if type == 'reg' and dtc[target].dtype.kind != 'f':
        dtc[target] = dtc[target].str.replace('[^\d\.]', '').astype(np.float32)
    # 5) Replace any negative number as NaN if target negative numbers are not allowed
    if not allow_neg:
        dtc[target][dtc[target] < 0] = np.NaN
    # 6) Fill the missing targetvalues via given interpolation in-place
    if dtc[target].isnull().sum() > 0:
        dtc[target].interpolate(fill, inplace=True)

    return dtc


def normalize(df, y, scale='minmax'):
    if scale == 'minmax':
        scaler = MinMaxScaler()
    elif scale == 'standard':
        scaler = StandardScaler()
    df_norm = df.copy()
    df_norm[y] = scaler.fit_transform(df)
    return df_norm, scaler


def log_power_transform(df, y, method='box-cox', standardize=True):
    if method == 'log':
        return df.transform(np.log)
    else:
        df_pwr = df.copy()
        df_pwr[y] = power_transform(df, method=method, standardize=standardize)
        return df_pwr


def decompose(df, y, type='deseasonalize', model='additive'):
    ets = seasonal_decompose(df[y], model)
    ets_idx = ets.trend[ets.resid.notnull()].index
    if type == 'deseasonalize' and model == 'additive':
        trans = ets.trend[ets_idx] + ets.resid[ets_idx]
        removed = ets.seasonal[ets_idx]
    elif type == 'deseasonalize' and model == 'multiplicative':
        trans = ets.trend[ets_idx] * ets.resid[ets_idx]
        removed = ets.seasonal[ets_idx]
    elif type == 'detrend' and model == 'additive':
        trans = ets.seasonal[ets_idx] + ets.resid[ets_idx]
        removed = ets.trend[ets_idx]
    elif type == 'detrend' and model == 'multiplicative':
        trans = ets.seasonal[ets_idx] * ets.resid[ets_idx]
    elif model == 'additive':
        trans = ets.resid[ets_idx]
        removed = ets.trend[ets_idx] + ets.seasonal[ets_idx]
    else:
        trans = ets.resid[ets_idx]
        removed = ets.trend[ets_idx] * ets.seasonal[ets_idx]

    df_trans = trans.to_frame(name=y)
    return df_trans, removed


def split_data(data, n_test, n_val, n_input, n_output=1, g_min=0, g_max=0):
    X, y, t = make_supervised(data, n_input, n_output)
    gap = randint(int(g_min*len(X)), int(g_max*len(X)))
    # ipdb.set_trace()
    X_train0, X_test, y_train0, y_test = gap_train_test_split(X, y, test_size=n_test, \
                                                            gap_size=gap)
    _, _, t_train0, t_test = gap_train_test_split(X, t, test_size=n_test, \
                                                 gap_size=gap)
    # Train, test split
    if n_val == 0:
        orig = (X, y, t)
        train = (X_train0, y_train0, t_train0)
        test = (X_test, y_test, t_test)
        return orig, train, test
    # Train, val, test split
    else:
        X_train, X_val, y_train, y_val = gap_train_test_split(X_train0, y_train0, test_size=n_val, \
                                                              gap_size=gap)
        _, _, t_train, t_val = gap_train_test_split(X_train0, t_train0, test_size=n_val, \
                                                    gap_size=gap)
        orig = (X, y, t)
        train = (X_train, y_train, t_train)
        val = (X_val, y_val, t_val)
        test = (X_test, y_test, t_test)
        return orig, train, val, test


def time_series_split(ts_df):
    """
    This utility splits any dataframe sent as a time series split using the sklearn function.
    """
    from sklearn.model_selection import TimeSeriesSplit
    tscv = TimeSeriesSplit(n_splits=2)
    train_index, test_index = list(tscv.split(ts_df))[1][0], list(tscv.split(ts_df))[1][1]
    ts_train, ts_test = ts_df[ts_df.index.isin(train_index)], ts_df[
                        ts_df.index.isin(test_index)]
    print(ts_train.shape, ts_test.shape)
    return ts_train, ts_test


# Credit: Machine Learning Mastery (Deep Learning in Time-Series Forecasting)
def make_supervised(data, n_input, n_output):
    # flatten data
    # data = train.reshape((train.shape[0]*train.shape[1], train.shape[2]))
    X, y, t = list(), list(), list()
    in_start = 0
    # step over the entire history one time step at a time
    for _ in range(len(data)):
        # define the end of the input sequence
        in_end = in_start + n_input
        out_end = in_end + n_output
        # ensure we have enough data for this instance
        if out_end <= len(data):
            x_input = data[in_start:in_end].to_numpy()
            # x_input = data[in_start:in_end, 0]
            x_input = x_input.reshape((len(x_input), 1))
            X.append(x_input)
            y.append(data[in_end:out_end].to_numpy())
            t.append(data.index[in_end].to_numpy())
        # move along one time step
        in_start += 1
    return np.array(X), np.array(y), np.array(t)


def convert_timeseries_dataframe_to_supervised(df, namevars, target, n_in=1, n_out=0, dropT=True):
    """
    Transform a time series in dataframe format into a supervised learning dataset while
    keeping dataframe intact.
    Arguments:
        df: A timeseries dataframe that you want to convert to Supervised dataset.
        namevars: columns that you want to lag in the data frame. Other columns will be untouched.
        target: this is the target variable you intend to use in supervised learning
        n_in: Number of lag periods as input (X).
        n_out: Number of future periods (optional) as output for the taget variable (y).
        dropT: Boolean - whether or not to drop columns at time 't'.
        Returns:
        df: This is the transformed data frame with the time series columns laggged.
        Note that the original columns are dropped if you set the 'dropT' argument to True.
        If not, they are preserved.
    This Pandas DataFrame of lagged time series data is immediately available for supervised learning.
    """
    df = df[:]
    # Notice that we will create a sequence of columns from name vars with suffix (t-n,... t-1), etc.
    drops = []
    for i in range(n_in, -1, -1):
        if i == 0:
            for var in namevars:
                addname = var + '(t)'
                df.rename(columns={var:addname}, inplace=True)
                drops.append(addname)
        else:
            for var in namevars:
                addname = var + '(t-' + str(i) + ')'
                df[addname] = df[var].shift(i)
    ## forecast sequence (t, t+1,... t+n)
    if n_out == 0:
        n_out = False
    for i in range(1, n_out):
        for var in namevars:
            addname = var + '(t+' + str(i) + ')'
            df[addname] = df[var].shift(-i)
    #	drop rows with NaN values
    df.dropna(inplace=True, axis=0)
    #	put it all together
    target = target+'(t)'
    if dropT:
        ### If dropT is true, all the "t" series of the target column (in case it is in the namevars)
        ### will be removed if you don't want the target to learn from its "t" values.
        ### Similarly, we will also drop all the "t" series of name_vars if you set dropT to Trueself.
        try:
            drops.remove(target)
        except:
            pass
        df.drop(drops, axis=1, inplace=True)
    preds = [x for x in list(df) if x not in [target]]
    return df, target, preds
    ############


def find_max_min_value_in_a_dataframe(df, max_min='min'):
    """
    This returns the lowest or highest value in a df and its row value where it can be found.
    Unfortunately, it does not return the column where it is found. So not used much.
    """
    if max_min == 'min':
        return df.loc[:, list(df)].min(axis=1).min(), df.loc[:, list(df)].min(axis=1).idxmin()
    else:
        return df.loc[:, list(df)].max(axis=1).max(), df.loc[:, list(df)].min(axis=1).idxmax()
