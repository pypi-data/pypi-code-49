"""
Copyright 2020, Enzo Busseti.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
    
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np
import pandas as pd


def featurize_price_movements(data, past_lags, future_lags,
                              Open='Open', Max='Max', Min='Min',
                              Volume='Volume', BuyVolume='BuyVolume',
                              timestamps=None):

    # TODO: extend to many assets

    # timestamps are the ts's for which we produce a line
    # if it is None we produce a line for every
    # ts in the index

    # if buy_volume is None we don't compute imbalance

    if timestamps is None:
        timestamps = data.index

    T = len(timestamps)

    # returns, max, min, volume, sigma, imbalance
    #N_fea = len(past_lags) * (3 + (BuyVolume is not None))
    #N_tar = len(future_lags) * (3 + (BuyVolume is not None))

    #features_targets = np.empty(T, N_fea + N_tar)
    features_targets = pd.DataFrame(index=timestamps)

    past_lags = sorted(past_lags)

    logopen = np.log(data[Open])
    logmax = np.log(data[Max])
    logmin = np.log(data[Min])

    for i, el in enumerate(past_lags):
        start = past_lags[i]
        end = past_lags[i + 1] if i < (len(past_lags) - 1) else 0

        features_targets[f'r_{start}_{end}'] = logopen.diff(end - start).shift(-end)
        # features_targets[f'sigma_{start}_{end}'] =
        # np.abs(features_targets[f'r_{start}_{end}'])
        features_targets[f'max_{start}_{end}'] = \
            logmax.rolling(end - start).max().shift(-end + 1) - \
            logopen.shift(-start)
        features_targets[f'min_{start}_{end}'] = \
            logmin.rolling(end - start).min().shift(-end + 1) - \
            logopen.shift(-start)
        features_targets[f'imbalance_{start}_{end}'] = \
            df[BuyVolume].rolling(end - start).sum().shift(-end + 1) / \
            df[Volume].rolling(end - start).sum().shift(-end + 1)
        # features_targets[f'imbalance_{start}_{end}'].fillna(0.)
#         features_targets[f'volume_{start}_{end}'] = \
#             df[Volume].rolling(end-start).sum().shift(-end+1)
#         features_targets[f'buyvolume_{start}_{end}'] = \
#             df[BuyVolume].rolling(end-start).sum().shift(-end+1)

        #print(start, end)

    future_lags = sorted(future_lags)

    for i, el in enumerate(future_lags):
        start = future_lags[i - 1] if i > 0 else 0
        end = future_lags[i]

        features_targets[f'r_{start}_{end}'] = logopen.diff(end - start).shift(-end)
        # features_targets[f'sigma_{start}_{end}'] =
        # np.abs(features_targets[f'r_{start}_{end}'])
        features_targets[f'max_{start}_{end}'] = \
            np.log(data[Max]).rolling(
                end - start).max().shift(-end + 1) - logopen.shift(-start)
        features_targets[f'min_{start}_{end}'] = \
            logmin.rolling(end - start).min().shift(-end + 1) - \
            logopen.shift(-start)
        features_targets[f'imbalance_{start}_{end}'] = \
            df[BuyVolume].rolling(end - start).sum().shift(-end + 1) / \
            df[Volume].rolling(end - start).sum().shift(-end + 1)
        # features_targets[f'imbalance_{start}_{end}'].fillna(0.)
#         features_targets[f'volume_{start}_{end}'] = \
#             df[Volume].rolling(end-start).sum().shift(-end+1)
#         features_targets[f'buyvolume_{start}_{end}'] = \
#             df[BuyVolume].rolling(end-start).sum().shift(-end+1)

        #print(start, end)

    return features_targets
