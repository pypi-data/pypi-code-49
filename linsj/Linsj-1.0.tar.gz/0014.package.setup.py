# 打包
from distutils.core import setup

setup(
    name='Linsj',
    version='1.0',
    description='自定义测试包',
    author="linsj",
    author_email="88109940@qq.com",
    py_modules=['Linsj.demo1', 'Linsj.demo2']
)

# 进入这个文件的目录，执行
# python ./0014.package.setup.py sdist
