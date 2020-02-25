from fundquant.dao.jsl_data import get_his_data
import pickle

from fundquant.model.preprocess.preprocess import percent


def feature_gen(etf_code, his_count=5 * 252):
    etf_df = get_his_data(etf_code, his_count)
    etf_df.sort_values(by='dt', ascending=True, inplace=True)
    etf_df.reset_index(drop=True, inplace=True)
    last_idx = etf_df.shape[0] - 1

    current = etf_df.iloc[last_idx]

    last_5y = etf_df.iloc[max(last_idx + 1 - 5 * 252, 0):last_idx + 1]
    last_3y = etf_df.iloc[max(last_idx + 1 - 3 * 252, 0):last_idx + 1]
    last_2y = etf_df.iloc[max(last_idx + 1 - 2 * 252, 0):last_idx + 1]
    last_1y = etf_df.iloc[max(last_idx + 1 - 1 * 252, 0):last_idx + 1]
    last_6m = etf_df.iloc[max(last_idx + 1 - 126, 0):last_idx + 1]
    last_3m = etf_df.iloc[max(last_idx + 1 - 63, 0):last_idx + 1]
    last_1m = etf_df.iloc[max(last_idx + 1 - 21, 0):last_idx + 1]
    last_2w = etf_df.iloc[max(last_idx + 1 - 10, 0):last_idx + 1]
    last_1w = etf_df.iloc[max(last_idx + 1 - 5, 0):last_idx + 1]

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
    pe_mv_6m = last_6m['pe'].astype(float).mean()
    pe_mv_3m = last_3m['pe'].astype(float).mean()
    pe_mv_2w = last_2w['pe'].astype(float).mean()
    pe_mv_1w = last_1m['pe'].astype(float).mean()
    pe_mv_div_1_6m = pe_mv_1w / pe_mv_6m
    pe_mv_div_1_3m = pe_mv_1w / pe_mv_3m
    pe_mv_div_1_2w = pe_mv_1w / pe_mv_2w

    # 方差
    pe_5y_std = last_5y['pe'].astype(float).std()

    pe_3y_std_rt = last_3y['pe'].astype(float).std() / pe_5y_std
    pe_2y_std_rt = last_2y['pe'].astype(float).std() / pe_5y_std
    pe_1y_std_rt = last_1y['pe'].astype(float).std() / pe_5y_std
    pe_6m_std_rt = last_6m['pe'].astype(float).std() / pe_5y_std
    pe_3m_std_rt = last_3m['pe'].astype(float).std() / pe_5y_std
    pe_1m_std_rt = last_1m['pe'].astype(float).std() / pe_5y_std
    pe_2w_std_rt = last_2w['pe'].astype(float).std() / pe_5y_std
    pe_1w_std_rt = last_1w['pe'].astype(float).std() / pe_5y_std

    return [[pe_5y_percent, pe_3y_percent, pe_2y_percent, pe_1y_percent, pe_6m_percent, pe_3m_percent, pe_1m_percent,
             pe_2w_percent, pe_1w_percent,

             pb_5y_percent, pb_3y_percent, pb_2y_percent, pb_1y_percent, pb_6m_percent, pb_3m_percent, pb_1m_percent,
             pb_2w_percent, pb_1w_percent,

             pe_pb_div_5y, pe_pb_div_3y, pe_pb_div_2y, pe_pb_div_1y, pe_pb_div_6m, pe_pb_div_3m, pe_pb_div_1m,
             pe_pb_div_2w,

             pe_mv_div_1_6m, pe_mv_div_1_3m, pe_mv_div_1_2w,

             pe_3y_std_rt, pe_2y_std_rt, pe_1y_std_rt, pe_6m_std_rt, pe_3m_std_rt, pe_1m_std_rt, pe_2w_std_rt,
             pe_1w_std_rt
             ]]


if __name__ == '__main__':
    feature = feature_gen(159901)
    model = pickle.load(open('../lgbmodel/2019-11.lgb', 'rb'))
    predict = model.predict_proba(feature)[0][1]
    print('model', model)
    print(predict)
