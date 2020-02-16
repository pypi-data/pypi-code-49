"""
    导入顺序:
        0. 版本信息
        1. 常用固定路径
        2. 第三方依赖库
        3. 本pkg下的各个子包/子模块的所有全局namespace
        4. 添加外部脚本的常用路径到"默认搜索路径"
        5. 生成常用变量


    设计哲学:
        1. 注重internal结构: kw618的顶层namespace中, 会把所有子包中常用函数/类导入进来
        2. 不关心external环境: 很多在MyCode中可重复利用的脚本暂时不导入到本模块中.(用到时,自行导入)
           (但会提前加入"默认搜索路径", 可以方便任意路径导入函数/类)
        3. kw618会有两种形式存在:
            一是:本地编辑的代码
                主要应用场景: 本地. 优势:在本地可以快速调整, 快速响应
            二是:pypi服务器存储的已更新上传的代码
                主要应用场景: 阿里云服务器端(remote).
                    劣势:
                        1. 每次更新代码后都要更新上传pypi比较麻烦;(但毕竟remote, 在github上更新也挺麻烦)
                            (需要写一个shell脚本自动化更新上传)
                        2. 每次上传到pypi后, 需要在remote端重新更新kw618库  (pypi网络延迟比git可能更慢.)
                        eg代码:
                            python setup.py sdist bdist_wheel
                            twine upload dist/*
                            pip3 install --upgrade kw618
                    优势: 比github上的版本控制要容易(0.0.4是完全覆盖0.0.3, 而不需要自己处理版本之间diff的问题)


    notes:
        1. 后续想把ziru除名! (ziru应该放在MyCode中的Libs中) (任何与代码有关的资源最好也放在这个目录中,便于调用)
            (巨型log除外) (巨型log会导致git版本控制的内容巨大)
        2. pandas 底下的包和模块绝对不能有"from kw618 import *"/ "import kw618"
            导入kw618只能在外部代码调用kw618库时候出现!! (内部代码不能使用, 否则会导致"循环导入")
            如果在某个脚本中需要"全平台通用路径":
                目前: from kw618._file_path import *
                        (此处以kw618打头, 不知道会不会存在循环导入的问题)
                        (pandas底下的core.frame模块也需要导入core.dtypes.common.is_dict_like)


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
    # 定时任务相关
    "schedule", "csv",
    # python通用utils相关
    "functools",
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
from kw618.k_python.utils_python import *
from kw618.k_requests.utils_requests import *
from kw618.k_requests.my_cookies import *
    ## 2. 工作相关模块
"把工作相关的模块在kw618中废除了!! 移至MyCode中的Libs中"
    ## 3. 添加常用本地路径到默认搜索路径
    ## 不直接导入函数/变量
    ## (会将 MyCode 目录下的重要文件夹添加到 python_path中)
    ## (当项目变得庞大了, 可能会出现同名Crawler项目, 需要单独在各自项目中添加) <toggle>
if os.path.exists(f"{FILE_PATH_FOR_MYCODE}"):
    sys.path.append(f"{FILE_PATH_FOR_MYCODE}")
    sys.path.append(f"{FILE_PATH_FOR_MYCODE}/BusinessProj")
    sys.path.append(f"{FILE_PATH_FOR_MYCODE}/PersonalProj")
"如果这里把Ziru的项目添加到python_path中, 容易在导入时候出现命名空间混乱!"
"(建议Ziru项目: 使用Ziru.Projects... 之类的绝对导入方式)"
# if os.path.exists(f"{FILE_PATH_FOR_ZIRU_CODE}"):
#     sys.path.append(f"{FILE_PATH_FOR_ZIRU_CODE}")
#     sys.path.append(f"{FILE_PATH_FOR_ZIRU_CODE}/Projects")
#     sys.path.append(f"{FILE_PATH_FOR_ZIRU_CODE}/Utils")
"又存在循环调用, 比较头疼....可能需要一个中间中转的脚本...api.py??"
"//k200215:为避免循环导入, 这里只添加默认搜索路径, 不直接在本模块导入函数和变量"



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

    ## sys
# exit = sys.exit








aaa = 111


























##
