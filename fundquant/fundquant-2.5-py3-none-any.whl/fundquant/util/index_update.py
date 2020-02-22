import datetime

import pymysql

from fundquant.data_get.xq_data import XqApi
from fundquant.util.date_util import today_plus


def etf_head_complete(code: str, exchange: str = 'SH'):
    code = str(code).zfill(6)

    if code.find('SZ') >= 0 or code.find('SH') >= 0:
        return code

    if code.find('512') == 0 or code.find('510') == 0:
        return 'SH' + code

    if code.find('159') == 0:
        return 'SZ' + code

    if code.find('3') == 0:
        return 'SZ' + code


def upert_etf_data(etf_code, etf_name, dt, index_code, index_name, close_price):
    conn = pymysql.connect(user='root', password='', database='quant', charset='utf8')
    cursor = conn.cursor()
    sql = "select etf_code, etf_name, index_code, index_name from jsl_etf_data where etf_code='{}' and dt = '{}' " \
        .format(etf_code, dt)
    cursor.execute(sql)
    conn.commit()
    if len(cursor.fetchall()) == 0:
        try:
            sql = " insert into jsl_etf_data(`etf_code`, `etf_name`, `dt`,`index_code`, `index_name`, `close_price`) " \
                  " values('{}', '{}', '{}', '{}', '{}', {}) " \
                .format(etf_code, etf_name, dt, index_code, index_name, close_price)
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(etf_code, etf_name, dt, " error:", e)

    else:
        sql = " update jsl_etf_data set close_price={} where etf_code='{}' and dt='{}' " \
            .format(close_price, etf_code, dt)
        cursor.execute(sql)
        conn.commit()


def close_price_update_tmp():
    conn = pymysql.connect(user='root', password='', database='quant', charset='utf8')
    cursor = conn.cursor()
    sql = "select etf_code, etf_name, index_id, index_name from jsl_etf_list where index_id <> '-' "
    cursor.execute(sql)
    conn.commit()

    etf_codes = []

    for item in cursor.fetchall():
        etf_code = item[0]
        etf_name = item[1]
        index_code = item[2]
        index_name = item[3]

        df = XqApi().get_his_k_data(etf_head_complete(etf_code), today_plus(-20 * 360), today_plus(0),
                                    return_column=['date', 'close'])

        etf_codes.append(etf_code)
        print('start update: ', etf_code)
        for item in df.values:
            dt = item[0]
            close_price = item[1]

            upert_etf_data(etf_code, etf_name, dt, index_code, index_name, close_price)
        print('codes: ', etf_codes)


def data_dump():
    conn = pymysql.connect(user='root', password='', database='quant', charset='utf8')
    cursor = conn.cursor()
    sql = '''
    select etf_code, etf_name, t1.index_code as index_code, index_name, dt, pe, pb
    from (select etf_code, etf_name, index_id as index_code, index_name from jsl_etf_list where index_id <> '-') as t1
    join index_data as t2 where t1.index_code = t2.index_code
    '''
    cursor.execute(sql)
    conn.commit()
    for item in cursor.fetchall():
        etf_code = item[0]
        etf_name = item[1]
        index_code = item[2]
        index_name = item[3]
        dt = (datetime.datetime.strptime(item[4], '%Y-%m-%d') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        pe = item[5]
        pb = item[6]

        select_sql = "select * from jsl_etf_data where etf_code='{}' and dt='{}' ".format(etf_code, dt)
        cursor.execute(select_sql)
        conn.commit()
        if len(cursor.fetchall()) == 0:
            insert_sql = " insert into jsl_etf_data(`etf_code`, `etf_name`, `dt`, `index_code`, `index_name`, `pe`, `pb`) " \
                         " values('{}', '{}', '{}', '{}', '{}', {}, {}) " \
                .format(etf_code, etf_name, dt, index_code, index_name, pe, pb)
            cursor.execute(insert_sql)
            conn.commit()
        else:
            update_sql = " update jsl_etf_data set " \
                         " etf_name='{}', index_code='{}', index_name='{}', pe={}, pb={} " \
                         " where etf_code='{}' and dt='{}' " \
                .format(etf_name, index_code, index_name, pe, pb, etf_code, dt)
            cursor.execute(update_sql)
            conn.commit()


if __name__ == '__main__':
    # data_dump()
    print("dump done")
    print('start price update')
    close_price_update_tmp()
