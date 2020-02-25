import pandas
import pymysql
import numpy as np


def get_his_data(etf_code, his_count):
    conn = pymysql.connect(user='root', password='', database='quant', charset='utf8')
    etf_code_list = []
    dt = []
    pe = []
    pb = []
    try:
        cursor = conn.cursor()

        sql = "select * from " \
              "( " \
              "     select etf_code, dt, pe, pb from jsl_etf_data " \
              "     where etf_code='{}' and pe > 0 and pb > 0 order by dt desc limit {} " \
              ") as t order by dt asc " \
            .format(etf_code, his_count)

        cursor.execute(sql)
        conn.commit()

        for item in cursor.fetchall():
            etf_code_list.append(item[0])
            dt.append(item[1])
            pe.append(float(item[2]))
            pb.append(float(item[3]))

        df = pandas.DataFrame(data=np.array([etf_code_list, dt, pe, pb]).T,
                              columns=['etf_code', 'dt', 'pe', 'pb'])
        return df.set_index('dt')
    except Exception as e:
        print(e)
        pass
