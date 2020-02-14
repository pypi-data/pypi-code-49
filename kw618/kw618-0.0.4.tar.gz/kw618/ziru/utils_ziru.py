
"""
notes:
    该文件作为所有ziru相关的、可重复使用的api接口！！
    初衷：写了太多自如相关的函数，但是都不够标准化，没有统一的api规范，
         导致重复造了多个轮子来实现类似的功能，低效不可持续利用！！
         现在，想要通过“规范化、标准化”，让类似的功能集成在一个万能的函数中！！
         （可以把性能作为代价，但一定要让函数变得容易调用、方便记忆）

exec_cmd:
    ## 快速编辑标准价对应表
    vim /root/kerwin/MyBox/MyKernel/python_default_path/ziru/estate_std_price.csv
    ps aux
    kill -s 9 <pid>
    nohup python3 -u /root/kerwin/MyBox/MyCode/Business/Ziru/97_Exec_Script/主动调价_0730/Approve_Pricing.py > /root/Approve_Pricing.log &
"""



# TODO:  构建 ”标准户型“ 字段，通过pandas矢量化的方法来实现，性能可以提高上百倍！！！
            # 所以不到万不得已，尽量不要使用apply来逐行执行！！


# TODO:  求标准价的函数 --->> 升级版（可以进而计算大盘系数、6.0系数、成本系数、特殊系数？？等除了空置系数外的系数！！）



# 价格名称由大到小：楼盘标准价 >  户型标准价 >  id标准价  >  id空置标准价 > 修正尾数价格
# estate_std_price > std_price > id_std_price > id_idle_std_price > modified_price

def normalized_filed_for_huxing(df):
    """
    required_fields: 楼盘名称、面积、卧室名称、是否有独卫、是否有阳台
    """
    # 标准化"友家房源"的id户型字段
    df["面积"] = df["面积"].astype("int").astype("str")
    df["朝向"] = df["卧室名称"].str.extract(r"(\w+)卧")
    df["朝向"] = df["朝向"].str.replace("^西南$", "南", regex=True)
    df["朝向"] = df["朝向"].str.replace("^东南$", "南", regex=True)
    df["朝向"] = df["朝向"].str.replace("^西北$", "东西", regex=True)
    df["朝向"] = df["朝向"].str.replace("^东北$", "东西", regex=True)
    df["朝向"] = df["朝向"].str.replace("^南北$", "东西", regex=True)
    df["朝向"] = df["朝向"].str.replace("^东$", "东西", regex=True)
    df["朝向"] = df["朝向"].str.replace("^西$", "东西", regex=True)
    df["id户型"] = df["楼盘名称"] +"-"+ df["是否有独卫"] +"-"+ df["是否有阳台"] +"-"+ df["朝向"] +"-"+ df["面积"]

    return df


def revise_tail_number(m_price, revise_type="medium"):
    """
    function: 把价格的尾数按照规则变成 3、6、9结尾的价格
    revise_type:
        round_up/round_down/medium
    """

    if pd.api.types.is_number(m_price):
        m_price = int(m_price)
        remainder = m_price % 100
        if revise_type == "medium":
            if remainder < 10:
                modified_price = int(m_price/100)*100 - 10
            elif remainder < 45:
                modified_price = int(m_price/100)*100 + 30
            elif remainder < 75:
                modified_price = int(m_price/100)*100 + 60
            elif remainder < 100:
                modified_price = int(m_price/100)*100 + 90
        elif revise_type == "round_up":
            if remainder <= 30:
                modified_price = int(m_price/100)*100 + 30
            elif remainder <= 60:
                modified_price = int(m_price/100)*100 + 60
            elif remainder <= 90:
                modified_price = int(m_price/100)*100 + 90
            elif remainder < 100:
                modified_price = int(m_price/100)*100 + 130
        elif revise_type == "round_down":
            if remainder < 30:
                modified_price = int(m_price/100)*100 - 10
            elif remainder < 60:
                modified_price = int(m_price/100)*100 + 30
            elif remainder < 90:
                modified_price = int(m_price/100)*100 + 60
            elif remainder < 100:
                modified_price = int(m_price/100)*100 + 90
    else:
        print(m_price)
        modified_price = "无法修正其尾数价格"

    return modified_price

# revise_tail_number(3.33)
# sys.exit()




# TODO:  每天早上先把价格梳理一遍，之后的续约、标准价、二次调价都可以参考这部分总的价格参考表！！！
# TODO:  后续在业务发起调价的时候，也可以在邮件中展示这部分信息（最全面的价格参考表）（甚至可以包括dk价格）
# TODO:  也就是完成当年的设想：给我一个house_id，实现一秒返回所有相关的价格字段！！
            ## 包括但不局限于： 目前调价表中的所有字段、蛋壳相关的价格、待租量、补贴量？、url跳转到类似户型的价格
            ##（面积上下2平内？或者直接呈现该楼盘的所有户型？）











        #####















#
