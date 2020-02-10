import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobaiauto", # Replace with your own username
    version="2.4.1",
    author="Tser",
    author_email="807447312@qq.com",
    description="xiaobaiauto framework 简化Web与接口等自动化实现及日志搜集、报告生成、邮件发送等功能",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/big_touch/xiaobaidoc",
    packages=setuptools.find_packages(),
    keywords="xiaobai auto automation test framework",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
    	"selenium",
        "pyquery",
        "requests",
        "pyyaml",
        "Appium-Python-Client",
        "gevent"
    ],
    package_data={
        'xiaobaiauto': [
            'auto.cp38-win_amd64.pyd',
            'HTMLTestRunner.py',
            'autogenertor.cp38-win_amd64.pyd',
            'autorunner.cp38-win_amd64.pyd'
        ],
    },
    entry_points={'console_scripts': [
        'autogenertor = xiaobaiauto.genertor:main',
        'autorunner = xiaobaiauto.runner:main',
    ]},
)


#python auto_setup.py sdist bdist_wheel

#python -m twine upload dist/*