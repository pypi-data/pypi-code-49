"""
    导入顺序:
        1. 第三方库 2.本地类 3.本地函数 4.本地常量 5.本地变量
"""

# 库包版本相关
from kw618._version import (
    __name__, __description__, __version__, __author__,
)

# 导入常用的固定路径(多平台通用)
from kw618._file_path import *



# kw618库包中需要用到的所有第三方库
hard_dependencies = (
    # requests相关
    "sys", "os", "retry", "traceback", "pysnooper", "user_agent", "random", "requests",
    "threading", "multiprocessing", "scrapy", "urllib", "smtplib", "uuid", "email", "execjs",
    "copy", "exchangelib", "urllib3", "selenium",
    # pandas相关
    "numpy", "pandas", "math", "collections", "swifter", "pymongo", "warnings",
    # pymongo相关
    "re", "json", "time", "pymongo", "redis",
    )

# 判断依赖包是否存在
missing_dependencies = []
for dependency in hard_dependencies:
    try:
        if dependency == "numpy":  # 1. 使用语句的方式import
            import numpy as np
        elif dependency == "pandas":
            import pandas as pd
        elif dependency == "warnings":
            import warnings
            warnings.filterwarnings("ignore")
        else:
            # __import__(dependency)  # 2. 使用函数方式import: 可以用str类型作为参数传入
            exec("import {}".format(dependency))
    except ImportError as e:
        missing_dependencies.append("{0}: {1}".format(dependency, str(e)))
if missing_dependencies:
    raise ImportError(
        "无法导入所需依赖包:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies



# 导入所有模块中的所有全局变量/函数/类
# (这些都是"kw618"这个 package namespace 底下的 API )
    ## 1. 第三方库封装模块
        ##### (pandas的__init__.py 中 即使要全部导入也是一个个导,不会使用*)
from kw618.k_pandas.utils_pandas import *
from kw618.k_pymongo.utils_pymongo import *
from kw618.k_pymysql.utils_pymysql import *
from kw618.k_requests.utils_requests import *
from kw618.k_requests.my_cookies import *
    ## 2. 工作相关模块
from kw618.ziru.std_price_system import *
from kw618.ziru.utils_ziru import *
    ## 3. 导入自己写的外部脚本 (不存在于kw618库内的) (需要先添加python默认搜索路径)
    ## 把各种需要的、重要的包(package) 加入到python的默认搜索路径中 (导入个人使用的package)
if os.path.exists(f"{FILE_PATH_FOR_ZIRU_CODE}/97_Exec_Script"):
    sys.path.append(f"{FILE_PATH_FOR_ZIRU_CODE}/97_Exec_Script")
    from 获取house_id的各类参考价格_0730.Get_Stdprice import *
    from 爬取自如price系统最低成本价_0724.Crawl_Costprice import crawl_all_costprice
if os.path.exists(f"{FILE_PATH_FOR_ZIRU_CODE}/98_Utlis"):
    sys.path.append(f"{FILE_PATH_FOR_ZIRU_CODE}/98_Utlis")
    # from k01_Split_Table import *  # 不太常用，暂不开启



# 导入通用变量/常量
    ## pandas
today_obj = pd.to_datetime("today")
today_date = today_obj.strftime("%Y-%m-%d") # 转成“2019-02-28”这样的str形式
this_time = today_obj.strftime("%X") # 转成“2019-02-28”这样的str形式
yesterday_obj = today_obj - pd.to_timedelta("1 d")
yesterday_date = yesterday_obj.strftime("%Y-%m-%d") # 转成“20190228”这样的str形式
df = import_data(in_file_path=f"{FILE_PATH_FOR_KW618}/k_pandas/df_test.csv")

    ## pymongo
client = pymongo.MongoClient(HOST)
db = client["zufang_001"]
remote_client = pymongo.MongoClient("121.40.240.153")
remote_db = remote_client["zufang_001"]

    ## redis
r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

    ## requests
req = myRequest().req




































##
