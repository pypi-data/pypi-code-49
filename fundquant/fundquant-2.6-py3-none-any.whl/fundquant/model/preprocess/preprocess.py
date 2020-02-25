import numpy as np
import pandas as pd

from fundquant.model.data.data_dump import data_dump


def percent(df: pd.DataFrame, col: str, current: float) -> float:
    percent = df[df[col] <= current].shape[0] / df.shape[0]
    return round(percent, 3)


def gen_label(csv_path):
    data_df = pd.read_csv(csv_path)

    data_with_label_df = pd.DataFrame()
    first = True
    for etf_code in set(data_df['etf_code']):
        etf_df = data_df[data_df['etf_code'] == etf_code]
        if etf_df.shape[0] < 5 * 252:
            continue
        etf_df.sort_values(by='dt', ascending=True, inplace=True)
        etf_df.reset_index(drop=True, inplace=True)
        # label process
        raws = []
        for idx in range(5 * 252, etf_df.shape[0] - 5):
            current = etf_df.iloc[idx]
            after_5d = etf_df.iloc[idx + 5]
            label = -2
            change_percent = after_5d['close_price'] / current['close_price'] - 1

            # if max_change_percent >= 0.01:
            #     label = 1
            if change_percent <= -0.01:
                label = 0
            elif change_percent >= 0.01:
                label = 1

            raws.append([current['dt'], label])

        label = pd.DataFrame(data=np.array(raws), columns=['dt', 'label'])

        etf_df = etf_df.merge(label, on='dt', how='left')
        etf_df['label'].fillna(-3, inplace=True)
        if first:
            data_with_label_df = etf_df
            first = False
        else:
            data_with_label_df = pd.concat([data_with_label_df, etf_df])
    print('data_with_label shape: ', data_with_label_df.shape)
    print('label-count', data_with_label_df['label'].value_counts())
    data_with_label_df.to_csv('../data/data_with_label.csv', index=False)


def gen_feature(csv_path):
    data_df = pd.read_csv(csv_path)

    train_test_df = pd.DataFrame()
    first = True
    for etf_code in set(data_df['etf_code']):
        etf_df = data_df[data_df['etf_code'] == etf_code]
        etf_df.sort_values(by='dt', ascending=True, inplace=True)
        etf_df.reset_index(drop=True, inplace=True)
        # label process
        raws = []
        for idx in range(5 * 252, etf_df.shape[0] - 5):
            current = etf_df.iloc[idx]
            last_5y = etf_df.iloc[max(idx + 1 - 5 * 252, 0):idx + 1]
            last_3y = etf_df.iloc[max(idx + 1 - 3 * 252, 0):idx + 1]
            last_2y = etf_df.iloc[max(idx + 1 - 2 * 252, 0):idx + 1]
            last_1y = etf_df.iloc[max(idx + 1 - 1 * 252, 0):idx + 1]
            last_6m = etf_df.iloc[max(idx + 1 - 126, 0):idx + 1]
            last_3m = etf_df.iloc[max(idx + 1 - 63, 0):idx + 1]
            last_1m = etf_df.iloc[max(idx + 1 - 21, 0):idx + 1]
            last_2w = etf_df.iloc[max(idx + 1 - 10, 0):idx + 1]
            last_1w = etf_df.iloc[max(idx + 1 - 5, 0):idx + 1]

            pe_5y_percent = percent(last_5y, 'pe', current['pe'])
            pe_3y_percent = percent(last_3y, 'pe', current['pe'])
            pe_2y_percent = percent(last_2y, 'pe', current['pe'])
            pe_1y_percent = percent(last_1y, 'pe', current['pe'])
            pe_6m_percent = percent(last_6m, 'pe', current['pe'])
            pe_3m_percent = percent(last_3m, 'pe', current['pe'])
            pe_1m_percent = percent(last_1m, 'pe', current['pe'])
            pe_2w_percent = percent(last_2w, 'pe', current['pe'])
            pe_1w_percent = percent(last_1w, 'pe', current['pe'])

            pb_5y_percent = percent(last_5y, 'pb', current['pb'])
            pb_3y_percent = percent(last_3y, 'pb', current['pb'])
            pb_2y_percent = percent(last_2y, 'pb', current['pb'])
            pb_1y_percent = percent(last_1y, 'pb', current['pb'])
            pb_6m_percent = percent(last_6m, 'pb', current['pb'])
            pb_3m_percent = percent(last_3m, 'pb', current['pb'])
            pb_1m_percent = percent(last_1m, 'pb', current['pb'])
            pb_2w_percent = percent(last_2w, 'pb', current['pb'])
            pb_1w_percent = percent(last_1w, 'pb', current['pb'])

            # subtract
            pe_pb_div_5y = pe_5y_percent / pb_5y_percent
            pe_pb_div_3y = pe_3y_percent / pb_3y_percent
            pe_pb_div_2y = pe_2y_percent / pb_2y_percent
            pe_pb_div_1y = pe_1y_percent / pb_1y_percent
            pe_pb_div_6m = pe_6m_percent / pb_6m_percent
            pe_pb_div_3m = pe_3m_percent / pb_3m_percent
            pe_pb_div_1m = pe_1m_percent / pb_1m_percent
            pe_pb_div_2w = pe_2w_percent / pb_2w_percent

            # 价格均线
            pe_mv_6m = last_6m['pe'].mean()
            pe_mv_3m = last_3m['pe'].mean()
            pe_mv_2w = last_2w['pe'].mean()
            pe_mv_1w = last_1m['pe'].mean()
            mv_div_1_6m = pe_mv_1w / pe_mv_6m
            mv_div_1_3m = pe_mv_1w / pe_mv_3m
            mv_div_1_2w = pe_mv_1w / pe_mv_2w

            # 方差
            pe_5y_std = last_5y['pe'].std()

            pe_3y_std_rt = last_3y['pe'].std() / pe_5y_std
            pe_2y_std_rt = last_2y['pe'].std() / pe_5y_std
            pe_1y_std_rt = last_1y['pe'].std() / pe_5y_std
            pe_6m_std_rt = last_6m['pe'].std() / pe_5y_std
            pe_3m_std_rt = last_3m['pe'].std() / pe_5y_std
            pe_1m_std_rt = last_1m['pe'].std() / pe_5y_std
            pe_2w_std_rt = last_2w['pe'].std() / pe_5y_std
            pe_1w_std_rt = last_1w['pe'].std() / pe_5y_std

            raw = [
                current['dt'],
                pe_5y_percent, pe_3y_percent, pe_2y_percent, pe_1y_percent, pe_6m_percent,
                pe_3m_percent, pe_1m_percent, pe_2w_percent, pe_1w_percent,

                pb_5y_percent, pb_3y_percent, pb_2y_percent, pb_1y_percent, pb_6m_percent,
                pb_3m_percent, pb_1m_percent, pb_2w_percent, pb_1w_percent,

                pe_pb_div_5y, pe_pb_div_3y, pe_pb_div_2y, pe_pb_div_1y, pe_pb_div_6m,
                pe_pb_div_3m, pe_pb_div_1m, pe_pb_div_2w,

                mv_div_1_6m, mv_div_1_3m, mv_div_1_2w,
                pe_3y_std_rt, pe_2y_std_rt, pe_1y_std_rt, pe_6m_std_rt,
                pe_3m_std_rt, pe_1m_std_rt, pe_2w_std_rt, pe_1w_std_rt
            ]

            raws.append(raw)

        feature = pd.DataFrame(data=np.array(raws),
                               columns=['dt',
                                        'pe_5y_percent', 'pe_3y_percent', 'pe_2y_percent', 'pe_1y_percent',
                                        'pe_6m_percent',
                                        'pe_3m_percent', 'pe_1m_percent', 'pe_2w_percent', 'pe_1w_percent',

                                        'pb_5y_percent', 'pb_3y_percent', 'pb_2y_percent', 'pb_1y_percent',
                                        'pb_6m_percent',
                                        'pb_3m_percent', 'pb_1m_percent', 'pb_2w_percent', 'pb_1w_percent',

                                        'pe_pb_div_5y', 'pe_pb_div_3y', 'pe_pb_div_2y', 'pe_pb_div_1y', 'pe_pb_div_6m',
                                        'pe_pb_div_3m', 'pe_pb_div_1m', 'pe_pb_div_2w',

                                        'pe_mv_div_1_6m', 'pe_mv_div_1_3m', 'pe_mv_div_1_2w',

                                        'pe_3y_std_rt', 'pe_2y_std_rt', 'pe_1y_std_rt', 'pe_6m_std_rt',
                                        'pe_3m_std_rt', 'pe_1m_std_rt', 'pe_2w_std_rt', 'pe_1w_std_rt'
                                        ])

        etf_df = etf_df[['dt', 'label']].merge(feature, on='dt', how='left')
        if first:
            train_test_df = etf_df
            first = False
        else:
            train_test_df = pd.concat([train_test_df, etf_df])

    print('train_test_df shape: ', train_test_df.shape)
    train_test_df.to_csv('../data/train_test.csv', index=False)


if __name__ == '__main__':
    # data_dump('./data_dump.csv')
    gen_label('../data/data_dump.csv')
    print('gen label done')
    gen_feature('../data/data_with_label.csv')
