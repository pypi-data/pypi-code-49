#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

import pandas as pd

from napoleontoolbox.file_saver import dropbox_file_saver
from napoleontoolbox.utility import metrics
from numpy.lib.stride_tricks import as_strided as stride

def dd_threshold(data = None, threshold=1., contravariant = -1):
    ratio = data['high'][-1]/data['high'][0]
    if ratio > threshold:
        return contravariant
    else :
        return -contravariant

def reconstitute_signal_perf(data=None, initial_price = 1.):
    data['close_return'] = data['close'].pct_change()
    data['reconstituted_close'] = metrics.from_ret_to_price(data['close_return'],initial_price=initial_price)
    data['perf_return'] = data['close_return'] * data['signal']
    data['reconstituted_perf'] = metrics.from_ret_to_price(data['perf_return'],initial_price=initial_price)
    return data

def roll_wrapper(rolled_df, lookback_window, skipping_size, function_to_apply):
    signal_df = roll(rolled_df, lookback_window).apply(function_to_apply)
    signal_df = signal_df.to_frame()
    signal_df.columns = ['signal_gen']
    signal_df['signal'] = signal_df['signal_gen'].shift()
    rolled_df = pd.merge(rolled_df, signal_df, how='left', left_index=True, right_index= True)
    rolled_df = rolled_df.iloc[skipping_size:]
    return rolled_df

def roll(df, w):
    v = df.values
    d0, d1 = v.shape
    s0, s1 = v.strides
    restricted_length = d0 - (w - 1)
    a = stride(v, (restricted_length, w, d1), (s0, s0, s1))
    rolled_df = pd.concat({
        row: pd.DataFrame(values, columns=df.columns)
        for row, values in zip(df.index[-restricted_length:], a)
    })
    return rolled_df.groupby(level=0)

class AbstractRunner(ABC):
    def __init__(self, starting_date = None, running_date = None, drop_token=None, dropbox_backup = True, hourly_pkl_file_name='hourly_candels.pkl', local_root_directory='../data/', user = 'napoleon'):
        super().__init__()
        self.hourly_pkl_file_name=hourly_pkl_file_name
        self.local_root_directory=local_root_directory
        self.user=user
        self.dropbox_backup = dropbox_backup
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token=drop_token,dropbox_backup=dropbox_backup)
        self.running_date = running_date
        self.starting_date = starting_date

    @abstractmethod
    def runTrial(self,saver, seed,  look_back_window, threshold, contravariant):
        pass


class SimpleSignalRunner(AbstractRunner):
    def runTrial(self, saver, seed,  look_back_window, threshold, contravariant):
        meArg = (seed,  look_back_window, threshold, contravariant)
        meArgList = list(meArg)
        meArgList = [str(it) for it in meArgList]
        savingKey = ''.join(meArgList)
        savingKey = savingKey.replace('[', '')
        savingKey = savingKey.replace(']', '')
        savingKey = savingKey.replace(',', '')
        savingKey = savingKey.replace(' ', '')
        savingKey = savingKey.replace('.', '')
        savingKey = 'T_' + savingKey
        print('Launching computation with parameters : '+savingKey)
        skipping_size = look_back_window
        hourly_df = pd.read_pickle(self.local_root_directory+self.hourly_pkl_file_name)
        hourly_df = roll_wrapper(hourly_df, look_back_window, skipping_size,
                                  lambda x: dd_threshold(data=x, threshold=threshold))
        hourly_df = reconstitute_signal_perf(hourly_df)
        sharpe_strat = metrics.sharpe(hourly_df['perf_return'].dropna(), period=252 * 24, from_ret=True)
        sharpe_under = metrics.sharpe(hourly_df['close_return'].dropna(), period=252 * 24, from_ret=True)
        print('underlying sharpe')
        print(sharpe_under)
        print('strat sharpe')
        print(sharpe_strat)
        hourly_df['turn_over'] = abs(hourly_df['signal'] - hourly_df['signal_gen']) / 2.
        print('average hourly turn over')
        print(hourly_df['turn_over'] .sum() / len(hourly_df))
        saver.saveResults(savingKey, hourly_df['perf_return','turn_over'])






