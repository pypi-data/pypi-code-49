import numpy as np
import pandas

from fundquant.dao import jsl_data
from fundquant.domain.etf_track import EtfTrackConfig
import pickle

from fundquant.model.preprocess.feature_gen import feature_gen


class EtfStatistic:
    def __init__(self, etf_tack: EtfTrackConfig):
        self.etf_code = etf_tack.etf_code
        self.etf_name = etf_tack.etf_name
        self.index_code = etf_tack.index_code
        self.index_name = etf_tack.index_name
        self.strategy = etf_tack.strategy
        self.track_days = etf_tack.track_days

        # pe统计 最近10年
        self.pe_less_prob_10y = None  # pe下探概率
        self.pe_less_prob_10y_2w_ago = None
        self.pe_less_prob_10y_1m_ago = None
        self.pe_less_prob_10y_2m_ago = None

        # pe 均线
        self.pe_20d_avg = None
        self.pe_250d_avg = None

        self.pb_less_prob_10y = None  # pb下探概率
        self.pe_median_10y = None
        self.pe_mean_10y = None
        self.last_pe = None
        self.pe_volatility_3y = None

        # 历史
        self.pe_min = None
        self.pe_max = None

        self.real_year = None
        self.last_dt = None
        self.volatility_5y = None
        self.model_up_proba = None
        self.model_down_proba = None

    def compute(self):
        hist_k_df = jsl_data.get_his_data(self.etf_code, 10 * 252)
        hist_k_df = hist_k_df.fillna(0)
        hist_k_df.sort_values(by='dt', ascending=True, inplace=True)
        hist_k_df['pe'] = hist_k_df['pe'].apply(np.float)
        hist_k_df['pb'] = hist_k_df['pb'].apply(np.float)

        if hist_k_df.empty:
            return

        last_dt = hist_k_df.index[-1]
        # pe pb 统计
        pe_df = hist_k_df[['pe']].astype(np.float)
        pb_df = hist_k_df[['pb']].astype(np.float)

        pe_min = pe_df.min()['pe']
        pe_max = pe_df.max()['pe']

        pe_less_prob_10y = len(pe_df[pe_df['pe'] <= pe_df.iloc[-1]['pe']]) / len(pe_df)
        pe_less_prob_10y_2w_ago = len(pe_df[pe_df['pe'] <= pe_df.iloc[-10]['pe']]) / len(pe_df)
        pe_less_prob_10y_2m_ago = len(pe_df[pe_df['pe'] <= pe_df.iloc[-44]['pe']]) / len(pe_df)
        pe_less_prob_10y_1m_ago = len(pe_df[pe_df['pe'] <= pe_df.iloc[-22]['pe']]) / len(pe_df)

        pe_20d_avg = pe_df.iloc[-20:-1]['pe'].mean()
        pe_250d_avg = pe_df.iloc[-250:-1]['pe'].mean()

        pb_less_prob_10y = len(pb_df[pb_df['pb'] <= pb_df.iloc[-1]['pb']]) / len(pb_df)
        pe_median_10y = pe_df.median()['pe']
        pe_mean_10y = pe_df.mean()['pe']
        last_pe = pe_df.iloc[-1]['pe']
        pe_volatility_3y = self.volatility_daily(pe_df.iloc[-3 * 252:], 'pe')

        self.pe_less_prob_10y = round(pe_less_prob_10y * 100, 1)
        self.pe_less_prob_10y_2w_ago = round(pe_less_prob_10y_2w_ago * 100, 1)
        self.pe_less_prob_10y_2m_ago = round(pe_less_prob_10y_2m_ago * 100, 1)
        self.pe_less_prob_10y_1m_ago = round(pe_less_prob_10y_1m_ago * 100, 1)
        self.pb_less_prob_10y = round(pb_less_prob_10y * 100, 1)

        self.pe_20d_avg = round(pe_20d_avg, 1)
        self.pe_250d_avg = round(pe_250d_avg, 1)

        self.pe_median_10y = round(pe_median_10y, 1)
        self.pe_mean_10y = round(pe_mean_10y, 1)
        self.last_pe = round(last_pe, 1)
        self.pe_volatility_3y = round(pe_volatility_3y * 100, 1)
        self.pe_min = round(pe_min, 1)
        self.pe_max = round(pe_max, 1)
        self.real_year = round(len(pe_df) / 252, 1)
        self.last_dt = last_dt

        # 算法预测涨的概率
        model = pickle.load(open('/usr/local/cron_jobs/fund-predict-model/2019-11.lgb', 'rb'))
        feature = feature_gen(self.etf_code)
        proba = model.predict_proba(feature)[0]
        self.model_up_proba = round(proba[1], 2)
        self.model_down_proba = round(proba[0], 2)

    @staticmethod
    def volatility_daily(df: pandas.DataFrame, col) -> float:
        ln_price = np.log2(df[col])
        log_rets = np.diff(ln_price)
        log_rets_std = np.std(log_rets)
        # 单位状态下的波动率
        volatility_per = log_rets_std / log_rets.mean() / np.sqrt(1 / 252)
        # 年波动率
        volatility = log_rets_std * np.sqrt(252)

        return volatility


if __name__ == '__main__':
    for config in EtfTrackConfig.get_etf_config_monitor():
        stat = EtfStatistic(config)
        stat.compute()

        print(stat)
