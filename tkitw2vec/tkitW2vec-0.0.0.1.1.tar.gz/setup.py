# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from os import path as os_path
import time
this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]
long_description="""

这里是说明
tkit包word2vec相关

 
"""
setup(
    name='tkitW2vec',
    version='0.0.0.1.1',
    description='tkit包word2vec相关',
    author='Terry Chan',
    author_email='napoler2008@gmail.com',
    url='https://terry-toolkit.terrychan.org/zh/master/',
    # install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'gensim==3.8.1',
        'pkuseg==0.0.22',
        'pandas==1.0.1',
        'numpy==1.18.1',
        'tkitFile==0.0.1.2',
    ],
    packages=['tkitW2vec'])

"""
pip freeze > requirements.txt #不好使用下一个
pipreqs ./


python3 setup.py sdist
#python3 setup.py install
python3 setup.py sdist upload
"""