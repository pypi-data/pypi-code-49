from setuptools import setup, find_packages

setup(
    # 以下为必需参数
    name='spider911',  # 模块名
    version='1.0.0',  # 当前版本
    description='A sample Python spider project for 91video',  # 简短描述
    py_modules=["spider911"], # 单文件模块写法
    # ckages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法


    # 以下均为可选参数
    long_description="",# 长描述
    url='https://github.com/p697/91tvspider', # 主页链接
    author='cavano cat', # 作者名
    author_email='254139147@qq.com', # 作者邮箱
    classifiers=[
        'Development Status :: 3 - Alpha',  # 当前开发进度等级（测试版，正式版等）

        'Intended Audience :: Developers', # 模块适用人群
        'Topic :: Software Development :: Build Tools', # 给模块加话题标签

        'License :: OSI Approved :: MIT License', # 模块的license

        'Programming Language :: Python :: 3',
    ],
    keywords='spider 91tv',  # 模块的关键词，使用空格分割
    install_requires=['requests', 'psutil'], # 依赖模块

    
)   
