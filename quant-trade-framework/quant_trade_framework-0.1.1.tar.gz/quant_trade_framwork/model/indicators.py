# -*-coding:utf-8 -*-

# @Time    : 2020/2/10 22:11
# @File    : Indicators.py
# @User    : yangchuan
# @Desc    :
from dataclasses import dataclass,asdict
from datetime import datetime

@dataclass
class DailyValue:
    record_datetime:datetime
    value_in_usdt:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class DailyReturn:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class TotalAnnualizedReturns:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class BenchmarkIndex:
    symbol:str
    record_datetime:datetime
    price:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class AnnualisedBenchmarkReturn:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class CumulativePortfolioReturn:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class CumulativeBenchmarkReturn:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

@dataclass
class AlgorithmVolatility:
    record_datetime:datetime
    percent:float

    def __init__(self):
        pass

    def to_dict(self):
        return asdict(self)

