import pandas as pd

class DataBase:
    columns = {'date', 'stockid', 'open', 'close'}
    def __init__(self):
        self.open = None
        self.close = None

class DataPandas(DataBase):
    def __init__(self, data):
        super().__init__()
        if not isinstance(data, pd.DataFrame):
            raise ValueError('data must be DataFrame')
        data = data.copy()
        data.columns = [c.lower() for c in data.columns]
        assert self.columns.issubset(data.columns), f'data must contain {self.columns}!'
        data.rename({'date': 'trade_dt', 'stockid': 'sid'}, axis=1, inplace=True)
        data['trade_dt'] = pd.to_datetime(data['trade_dt'])
        self.open = data.pivot(values='open', index='trade_dt', columns='sid')
        self.close = data.pivot(values='close', index='trade_dt', columns='sid')
