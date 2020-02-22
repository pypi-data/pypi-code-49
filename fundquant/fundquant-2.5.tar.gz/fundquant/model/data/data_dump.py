import pandas as pd
from sqlalchemy import create_engine


def data_dump(path):
    engine = create_engine('mysql+pymysql://root@localhost:3306/quant')
    select_sql = ' select etf_code, index_code, dt, close_price, pe, pb from jsl_etf_data ' \
                 ' where close_price > 0 and pe > 0 and pb > 0 '
    df = pd.read_sql_query(select_sql, engine)
    df.to_csv(path, index=False)


if __name__ == '__main__':
    data_dump('./data_dump.csv')
