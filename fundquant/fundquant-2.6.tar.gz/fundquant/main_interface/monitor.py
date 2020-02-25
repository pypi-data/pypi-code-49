# -*- coding: utf-8 -*-
import os

import numpy as np
import pandas
import yagmail

from fundquant.domain.etf_track import EtfTrackConfig
from fundquant.domain.send_email import SendEmail
from fundquant.service.etf_value_statistic import EtfStatistic


class IndexMonitor:
    def __init__(self):
        self.sender = '洪西洋@etf.com'
        self.receivers = ['murphyxiaoxi@outlook.com', '858776278@qq.com', '1064120720@qq.com',
                          'zhongmc_me@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.etf_columns = ['ETF代码', 'ETF名称', '买卖建议', 'PE下概率', 'PB下概率', 'ETF数据量', '指数代码', '跟踪指数', 'IDX下概率', '指数数据量']

    def monitor(self):
        etf_stat_df = self._etf_statistic_to_df(self._index_stat_list())

        try:
            etf_stat_df.to_excel('./指数统计指标.xlsx')

            email_list = SendEmail.get_email_list()
            if email_list is not None and len(email_list) > 0:
                self.receivers = email_list

            yag = yagmail.SMTP('858776278@qq.com', 'uurpxchfekfebahj', host='smtp.qq.com', port='465')
            yag.send(self.receivers, '指数跟踪', '跟踪指标和买卖建议见附件', ['./指数统计指标.xlsx'])
        except Exception as e:
            print(e)
        finally:
            os.remove('./指数统计指标.xlsx')

    @staticmethod
    def _index_stat_list():
        stat_list = []

        for config in EtfTrackConfig.get_etf_config_monitor():
            stat = EtfStatistic(config)
            try:
                stat.compute()
            except Exception as e:
                print("代码:", config.index_code, e)
            if stat.real_year is None:
                continue
            if stat.pe_less_prob_10y is None:
                stat.pe_less_prob_10y = 100
            stat_list.append(stat)

        stat_list = list(sorted(stat_list, key=lambda x: x.pe_less_prob_10y))

        return stat_list

    @staticmethod
    def pe_prob_command(less_prob, low_prob=50, high_prob=80):
        if less_prob < low_prob:
            return '分批买入'
        elif less_prob > high_prob:
            return '分批卖出'
        else:
            return '量化买入'

    @staticmethod
    def percent_command(percent, low=50, high=75):
        if percent < low:
            return '建议买入'
        elif percent > high:
            return '建议卖出'
        else:
            return '量化买入'

    @staticmethod
    def position_command(percent, low=50, high=75):
        if percent < low:
            return '0.75以下'
        elif percent > high:
            return '0.15以上'
        else:
            return '量化持仓'

    def _etf_statistic_to_df(self, statistics: list) -> pandas.DataFrame:
        index_code = []
        index_name = []
        etf_code = []
        etf_name = []
        pe_less_prob_10y = []
        pe_less_prob_10y_2m_ago = []
        pe_max_rt = []
        pe_last = []
        pe_mean = []
        pe_max = []
        pb_less_prob_10y = []
        ai_signal = []
        pe_volatility_3y = []
        real_year = []
        last_dt = []

        for stat in statistics:
            index_code.append(stat.index_code)
            index_name.append(stat.index_name)
            etf_code.append(stat.etf_code)
            etf_name.append(stat.etf_name)
            pe_less_prob_10y.append(stat.pe_less_prob_10y)
            pe_less_prob_10y_2m_ago.append(stat.pe_less_prob_10y_2m_ago)
            pe_max_rt.append(round(stat.last_pe * 100 / stat.pe_max, 1))
            pe_last.append(stat.last_pe)
            pe_mean.append(stat.pe_mean_10y)
            pe_max.append(stat.pe_max)
            pb_less_prob_10y.append(stat.pb_less_prob_10y)
            ai_signal.append(self.model_signal_compute(stat.model_up_proba))
            pe_volatility_3y.append(stat.pe_volatility_3y)
            real_year.append(stat.real_year)
            last_dt.append(stat.last_dt)

        df = pandas.DataFrame(
            data=np.array(
                [index_code, index_name, etf_code, etf_name, pe_less_prob_10y,
                 pe_less_prob_10y_2m_ago, pe_max_rt, pe_last, pe_mean, pe_max, pb_less_prob_10y, ai_signal,
                 pe_volatility_3y, real_year, last_dt]).T,
            columns=['指数代码', '指数名称', 'ETF代码', 'ETF名称', 'PE分位',
                     'PE分位2m', 'PE:max_rt', 'PE', 'PE均值', 'PE最大值', 'PB分位', 'AI', '3年波动', '跟踪年数',
                     '最后日期'])
        return df

    @staticmethod
    def model_signal_compute(proba):
        if proba > 0.5:
            return '+:' + str(proba)
        else:
            return '--:' + str(proba)
        # else:
        # return '↔'

    @staticmethod
    def pe_less_prob_ago_signal(cur_pe_prob, pe_ago):
        if cur_pe_prob - pe_ago <= -5:
            return '↓↓'
        elif cur_pe_prob - pe_ago >= 5:
            return '↑↑'
        elif cur_pe_prob - pe_ago <= -2:
            return '↓'
        elif cur_pe_prob - pe_ago >= 2:
            return '↑'
        else:
            return '↔'


if __name__ == '__main__':
    monitor = IndexMonitor()
    monitor.monitor()
