from distutils.core import setup

with open('test.txt','r',encoding="utf8")as f:
    dire = f.read()
setup(
    name="mysqlfast",
    version=1.0,
    description=dire,
    author='zhugxu',
    author_email='zhu_gxu@qq.com',
    py_modules={
        "mysqlfast.MysqlConnect"
    }

)

