#coding=utf-8
from distutils.core import setup

setup(
    name='baizhanSuperMath1111',    #对外我们模块的名字
    version='1.0',  #版本号
    description='这是第一个对外发布的模块，仅用于测试',   #描述
    author='xianhe',    #作者
    author_email='154879878@qq.com',
    py_modules=['baizhanSuperMath.demo1','baizhanSuperMath.demo2']  #要发布的模块
)