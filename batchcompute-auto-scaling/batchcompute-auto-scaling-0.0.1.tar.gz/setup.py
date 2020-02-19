
from setuptools import setup, find_packages

NAME = 'batchcompute-auto-scaling'

VERSION = '0.0.1'


setup(
    name = NAME,
    version =  VERSION,
    keywords = ('batchcompute-auto-scaling','batchcompute','autoscaling', 'deadline'),
    description = 'Aliyun batchcompute auto scaling for deadline',
    license = 'MIT License',

    url = 'http://www.aliyun.com/product/batchcompute',
    author='lingjiu',
    author_email='lingjiu.hlz@alibaba-inc.com',

    packages=find_packages('src'),
    package_dir = {'' : 'src'},
    package_data = {
       'auto_scaling': ['conf/config.ini', 'Deadline/*.py']
    },

    platforms = 'any',
    install_requires = ['batchcompute>=2.1.0'],

    entry_points='''
        [console_scripts]
        autoscaling=auto_scaling.main:main
    '''
)
