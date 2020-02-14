"""
系数调整在这里设置.

obj:
1.自动审批时候使用的户型系数
2.获取周边all_price时候使用的户型系数
3.计算面积系数需要的函数.(通用接口)
"""


## 自动审批标准价的时候
auto_approve_STD_COEF = {
    "direction": {
        1: 1.05,  # 东
        2: 1.09,  # 东南
        3: 1.09,  # 南
        4: 1.09,  # 西南
        5: 1.05,  # 西
        6: 1.05,  # 西北
        7: 1,  # 北
        8: 1.05,  # 东北
        9: 1.05,  # 东西
        10: 1.09,  # 南北
    },
    "yangtai": {
        1: 1.06,
        0: 1,
    },
    "duwei": {
        1: 1.23,
        0: 1,
    },
    "youhuajian": {
        1: 0.98,
        0: 1,
    },
    "pub_bathroom_num": {
        1: 1,  # 防错的（其实没用）
        2: 1.02,
        3: 1,
        4: 0.98,
    },
    "orientation": {
        1: "东",  # 东
        2: "南",  # 东南
        3: "南",  # 南
        4: "南",  # 西南
        5: "西",  # 西
        6: "西",  # 西北
        7: "北",  # 北
        8: "东",  # 东北
        9: "东",  # 东西
        10: "南",  # 南北
    },
}

## 自动审批标准价的时候
auto_approve_STD_COEF_V2 = {
    "direction": {
        1: 1.05,  # 东
        2: 1.09,  # 东南
        3: 1.09,  # 南
        4: 1.09,  # 西南
        5: 1.05,  # 西
        6: 1.05,  # 西北
        7: 1,  # 北
        8: 1.05,  # 东北
        9: 1.05,  # 东西
        10: 1.09,  # 南北
    },
    "yangtai": {
        1: 1.06,
        0: 1,
    },
    "duwei": {
        1: 1.23,
        0: 1,
    },
    "youhuajian": {
        1: 0.98,
        0: 1,
    },
    "pub_bathroom_num_coef": {
        1: 1,  # 防错的（其实没用）
        2: 1.02,
        3: 1,
        4: 0.98,
    },
    "orientation": {
        1: "东",  # 东
        2: "南",  # 东南
        3: "南",  # 南
        4: "南",  # 西南
        5: "西",  # 西
        6: "西",  # 西北
        7: "北",  # 北
        8: "东",  # 东北
        9: "东",  # 东西
        10: "南",  # 南北
    },
}


## 主动调价时候用的系数
help_price_STD_COEF = {
    "orientation" : {
        "南" : 1.09,
        "东南" : 1.09,
        "西南" : 1.09,
        "东" : 1.05,
        "东北" : 1.05,
        "西" : 1.05,
        "西北" : 1.05,
        "东西" : 1.05,
        "南北" : 1.05,
        "北" : 1,
        },
    "is_private_balcony" : {
        True : 1.06,
        False : 1,
        },
    "is_private_bathroom" : {
        True : 1.23,
        False : 1,
        },
    "is_partition" : {
        True : 0.98,
        False : 1,
        },
    "public_bathroom_num" : {
        2 : 1.02,
        3 : 1,
        4 : 0.98,
        },
}


## 续约调价时候用的系数
RENEW_STD_COEF = {
    "orientation" : {
        "南" : 1.09,
        "东南" : 1.09,
        "西南" : 1.09,
        "东" : 1.05,
        "东北" : 1.05,
        "西" : 1.05,
        "西北" : 1.05,
        "东西" : 1.05,
        "南北" : 1.05,
        "北" : 1,
        },
    "is_private_balcony" : {
        True : 1.06,
        False : 1,
        },
    "is_private_bathroom" : {
        True : 1.23,
        False : 1,
        },
    "is_partition" : {
        True : 0.98,
        False : 1,
        },
    "public_bathroom_num" : {
        2 : 1.02,
        3 : 1,
        4 : 0.98,
        },
}

# 目前所有的户型标准系数都是一样的，所以直接用STD_COEF 即可
STD_COEF = RENEW_STD_COEF






# 最早的旧版本
# def cal_area_coef(housing_area):
#     housing_area = int(housing_area)
#     if isinstance(housing_area, int):
#         if housing_area > 30:
#             coef = 1.3
#         elif 20 < housing_area <= 30:
#             coef = 1.2 + (housing_area - 20) * 0.01
#         elif 17 <= housing_area <= 20:
#             coef = 1.12 + (housing_area - 16) * 0.02
#         elif 8 <= housing_area < 17:
#             coef = 0.85 + (housing_area - 7) * 0.03
#         elif 6 <= housing_area < 8:
#             coef = 0.75 + (housing_area - 5) * 0.05
#         elif housing_area < 6:
#             coef = 0.75
#     return coef



# 我的版本
# def cal_area_coef(housing_area):
#     housing_area = int(housing_area)
#     if isinstance(housing_area, int):
#         coef_dict = {
#         1:0.7,
#         2:0.7,
#         3:0.7,
#         4:0.7,
#         5:0.74,
#         6:0.8,
#         7:0.84,
#         8:0.88,
#         9:0.91,
#         10:0.94,
#         11:0.97,
#         12:1,
#         13:1.03,
#         14:1.06,
#         15:1.09,
#         16:1.11,
#         17:1.13,
#         18:1.15,
#         19:1.16,
#         20:1.17,
#         21:1.18,
#         22:1.19,
#         23:1.2,
#         24:1.21,
#         25:1.22,
#         26:1.225,
#         27:1.23,
#         28:1.235,
#         29:1.24,
#         30:1.245,
#         }
#         if housing_area > 30:
#             coef = 1.25
#         else:
#             coef = coef_dict.get(housing_area)
#     return coef


# 家轩版本
def cal_area_coef(housing_area):
    housing_area = int(housing_area)
    if isinstance(housing_area, int):
        coef_dict = {
        1:0.6,
        2:0.6,
        3:0.7,
        4:0.7,
        5:0.75,
        6:0.8,
        7:0.84,
        8:0.88,
        9:0.91,
        10:0.94,
        11:0.97,
        12:1,
        13:1.03,
        14:1.06,
        15:1.08,
        16:1.1,
        17:1.12,
        18:1.14,
        19:1.15,
        20:1.16,
        21:1.17,
        22:1.18,
        23:1.19,
        24:1.2,
        25:1.205,
        26:1.21,
        27:1.215,
        28:1.22,
        29:1.225,
        30:1.23,
        }
        if housing_area > 30:
            coef = 1.23
        else:
            coef = coef_dict.get(housing_area)
    return coef



if __name__ == "__main__":
    import json
    print(33)
    d = {}
    for i in range(1, 40):
        coef = round(cal_area_coef(i), 3)
        d.update({i:coef})
    print(d)
    d = json.dumps(d, indent=4)
    print(d)
