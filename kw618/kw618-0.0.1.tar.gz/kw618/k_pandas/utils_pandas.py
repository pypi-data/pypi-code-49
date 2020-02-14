"""
    因为kw618的init中只能导入全局变量/函数/类, 而无法导入类中的函数.
    所以, 其实把该模块作为一个"大的类", 里面都是类中实现某些功能的函数
    所以, docs_2_df 函数, 其实没必要归纳到类中. 这样显得层级很复杂, 而且也不方便外部脚本调用该函数.
"""

import pandas as pd
import numpy as np
import math
import collections
import swifter
import pymongo
import json

import warnings
warnings.filterwarnings("ignore")


def import_data(
    in_file_name="in", end_index=None, field=None, is_df=True,
    in_file_path=None, encoding="gb18030", index_col=None,
    ):
    """
    in:csv文件
    out:df类型/类mongo类型
    function:  csv → df/mongo (默认转出:类mongo)

    notes: in_file_path 的优先级比 in_file_name 高。
    """
    if in_file_path:
        df = pd.read_csv(in_file_path, encoding=encoding, engine='python', index_col=index_col)
    else:
        df = pd.read_csv(FILE_PATH_FOR_DESKTOP+"/{0}.csv".format(in_file_name), encoding=encoding, engine='python', index_col=index_col)
    if is_df:
        return df
    # 1.需要返回的是某个字段的lst格式
    if field:
        field_lst = df[field].values[:end_index] # 得到的是np.array格式
        return list(field_lst) # 用list数据格式来返回
    # 2.返回的是mongo支持的docs
    df = df[:end_index]
    docs = df.T.to_dict().values()
    return docs

def df_2_mongo(df):
    return df.T.to_dict().values() # 即：docs

    #  也可以用于 "mongo → df"
def output_data(
    in_obj, out_file_name="out", ordered_field_lst=None,
    out_file_path=None, output=True, index=False, encoding="gb18030", export_excel=False,
    ):
    """
    in:类mongo/df
    out:csv文件
    function:  1.mongo/df  → csv
               2.mongo → df (这样output设为False即可)

    in_obj:    不管是mongo还是df,自动先转化成df,再用它来转csv

    tips: 如果需要 "mongo → df": output设置为False即可!
    notes: out_file_path 的优先级比 out_file_name 高。

    """

    # 1. 如果不是df类型,先将类mongo的数据,转化成df
    if isinstance(in_obj, pymongo.cursor.Cursor):
        # total_items = []
        # for doc in in_obj:
        #     # items = {i:str(j).strip() for i, j in zip(list(doc.keys()), list(doc.values()))}
        #     # 以下会按照mongo中存着的顺序进行输出!
        #     items = collections.OrderedDict({i:str(j).strip() for i, j in zip(list(doc.keys()), list(doc.values()))})
        #     total_items.append(items)
        # df = pd.DataFrame(total_items)
        df = pd.DataFrame(list(in_obj))
    elif isinstance(in_obj, pd.core.frame.DataFrame):
        df = in_obj

    # 2.确定字段的呈现顺序
    if ordered_field_lst:
        # 如果指定的df字段在df中并不存在,则把该字段remove掉.确保不报错
        for field in ordered_field_lst.copy():
            if field not in df.columns:
                print("字段 {} 不在df中,将其抛弃!".format(field))
                ordered_field_lst.remove(field)
        df = df[ordered_field_lst]  # 指定顺序

    # 3.看是否需要导出csv文件,如果不需要,直接返回df
    if not output:
        return df

    # 4. 最后,将df数据转成csv文件输出
    try:
        if out_file_path:
            if not export_excel:
                df.to_csv(out_file_path, index=index, encoding=encoding)
            else:
                df.to_excel(out_file_path, index=index, encoding=encoding)
        else:
            if not export_excel:
                df.to_csv(FILE_PATH_FOR_DESKTOP+"/{0}.csv".format(out_file_name), index=index, encoding=encoding)
            else:
                df.to_excel(FILE_PATH_FOR_DESKTOP+"/{0}.xlsx".format(out_file_name), index=index, encoding=encoding)
    except Exception as e:
        print(e)
        out_file_name = input("输出文件名出错,请重新键入文件名: ")
        df.to_csv(FILE_PATH_FOR_DESKTOP+"/{0}.csv".format(out_file_name), index=index, encoding=encoding)

    return df


# class KwPd():
#     def __init__(self):
#         pass
#
#     def docs_2_df(self, docs, ordered_field_lst=None):
#         """
#         把mongo的数据转化成df
#         """
#         df = output_data(docs, output=False, ordered_field_lst=ordered_field_lst)
#         return df



def docs_2_df(self, docs, ordered_field_lst=None):
    """
    把mongo的数据转化成df
    """
    df = output_data(docs, output=False, ordered_field_lst=ordered_field_lst)
    return df


# stackoverflow 白嫖来的函数，hhh
def read_mongo(collection, query={}, no_id=True):
    """ Read from Mongo and Store into DataFrame """


    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query, {"_id":0})

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    # if no_id:
    #     del df['_id']

    return df






def avg(lst):
    if isinstance(lst, list):
        if len(lst) <1:
            # raise myError("元素小于1!")
            return 0
    elif isinstance(lst, type(pd.Series())):
        if lst.size <1:
            # raise myError("元素小于1!")
            return 0
    sum = 0
    for count, e in enumerate(lst):
        # print(count, e)
        sum += int(float(e))
    lst_avg = sum/(count+1)
    # print(lst_avg)
    return int(lst_avg)


def merge_df(
    x_name, y_name, out_file_name="out",
    is_df=None, join_field="house_id", output=True):
    """
    function: 不仅可以合并df/csv, 还附带输出csv的功能
    """
    print(">>>1")
    if not is_df:
        # 如果 不是df， 就把这个当做文件名，导入
        x_df = import_data(x_name, is_df=True)
        y_df = import_data(y_name, is_df=True)
    else:
        # 如果 是df， 就直接把传入的x、y当做 df对象来使用
        x_df = x_name
        y_df = y_name
    print(">>>2")
    # pd.merge() 返回的不是df类型，而是function类型。 但这个function可以使用to_csv导出文件
    #  ??????   什么情况？ 之前测试的时候返回的不是df对象，现在测试发现又确实是df对象了。。。见鬼！
    merged_df = pd.merge(x_df, y_df, how="left", on=join_field)
    if not output:
        return merged_df
    print(">>>3")
    merged_df.to_csv(FILE_PATH_FOR_DESKTOP+"/{0}.csv".format(out_file_name), index=False, encoding="gb18030")
    print("合并成功!")

# merge_df("aaa", "bbb", out_file_name="zzzz")
# exit()


# def k_top(lst, top=1):
#     if isinstance(lst, list):
#         if len(lst) <1:
#             # raise myError("元素小于1!")
#             return 0
#     elif isinstance(lst, type(pd.Series())):
#         if lst.size <1:
#             # raise myError("元素小于1!")
#             return 0
#
#     lst = sorted(lst)
#     return lst[top-1]


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for np types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)










def k_divide(lst, piece=5):
    """
    function: 按lst从小到大的顺序, 等分成piece份 小lst 返回
    """
    if isinstance(lst, list):
        if len(lst) <1:
            # raise myError("元素小于1!")
            return 0
    elif isinstance(lst, type(pd.Series())):
        if lst.size <1:
            # raise myError("元素小于1!")
            return 0

    lst = sorted(lst)
    # 1. 打印原lst
    print(lst)
    node_order_lst = []
    node_lst = []
    for count in range(1, piece):
        node_order_value = round(len(lst) * (1/piece) * count) - 1 # 减一别忘了 (另外,这里返回的是顺序值,不是真实值)
        node_order_lst.append(node_order_value)
        node_lst.append(lst[node_order_value])
    # 2. 打印分好piece后的, 节点的顺序
    print(node_order_lst) # 是顺序
    print("值的lst: {}".format(node_lst)) # 是值

    piece_dict = {}
    count = 0
    while True:
        if count == piece:
            break
        elif count == 0:
            piece_dict.update({count+1 : lst[ : node_order_lst[count]+1]})
        elif count == piece-1:
            piece_dict.update({count+1 : lst[node_order_lst[count-1]+1 : ]})
        else:
            piece_dict.update({count+1 : lst[node_order_lst[count-1]+1 : node_order_lst[count]+1]})
        count += 1
    # 3. 打印根据上面的顺序, piece等拆分了lst后的dict
    print(piece_dict)
    return node_lst
    # return piece_dict


    # piece_lst = [] count = 0
    # while True:
    #     if count == piece:
    #         break
    #     elif count == 0:
    #         piece_lst.append(lst[ : node_order_lst[count]+1])
    #     elif count == piece-1:
    #         piece_lst.append(lst[node_order_lst[count-1]+1 : ])
    #     else:
    #         piece_lst.append(lst[node_order_lst[count-1]+1 : node_order_lst[count]+1])
    #     count += 1
    # # 3. 打印根据上面的顺序, piece等拆分了lst后的lst
    # print(piece_lst)
    # return piece_lst

# k_divide([3, 4, 5, 7, 2, 4, 46, 6, 7, 84, 4,5], 5)





if __name__ == '__main__':
    print("start!")
    df = import_data("业务反馈调价", is_df=True)
    print(df)
    print(df.shape)
    print("end!")
