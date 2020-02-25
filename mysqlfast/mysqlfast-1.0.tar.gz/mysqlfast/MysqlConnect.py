import pymysql
import re

class MysqlZhu:
    """
    auther:zhu
    类用于连接mysql数据库
    类创建即连接
    类消失即关闭数据库
    """

    def __init__(self,host='localhost',port = 3306,database="jing_dong",
                                user='zhu',password='zhuguanxu',charset='utf8'):
        """
        初始化方法
        """    
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset
        self.__cursor = None
        self.__connect = None
        self.__get_mysql_cursor()
    def __del__(self):
        self.__close()
    def __get_mysql_cursor(self):
        """
        创建对象后直接获取游标即可使用
        """
        data_dict = {
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "user": self.user,
            "password": self.password,
            "charset": self.charset
        }
        # 连接数据库
        try:
            self.__connect = pymysql.connect(**data_dict)
            self.__cursor = self.__connect.cursor()
        except Exception as ex:
            print(ex)
            self.__cursor = None
        else:
            print("-----------连接成功！！-----------")


    # 执行sql语句
    def execute_sql(self, sql):
        # 查询语句
        if not self.__cursor:
            return False
        sql_del_pace = re.sub(' +','',sql,count=1)
        # pace1 = sql.replace(" ","")
        # print(sql_del_pace)
        re_result = re.match("[^ ]*", sql_del_pace, re.I).group()
        if re_result.lower()[:6] == "select":
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        else:
            # 执行更新、插入、修改语句
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("----完成----")
        
                     
    def __close(self):
        """
        关闭数据库连接
        """
        self.__cursor.close()
        self.__connect.close()
        print("-----------数据库关闭!-----------")
