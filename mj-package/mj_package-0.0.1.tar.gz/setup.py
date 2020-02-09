from setuptools import setup, find_packages


import mj_package

setup(
    name = 'mj_package',
    version=mj_package.__version__,
    author = 'Marc Juillard',
    author_email = "dont_ask@gmail.com",
    description = "Personal ml packages",
    long_description = open('README.md').read(),
    # internal package and exclusions
    packages = find_packages(
        exclude=[
            "*tests",
            "*.tests.*",
            "test",
            "log",
            "log.*",
            "*.log",
            "*.log.*"
        ]
    ),
    # package to install
    #install_requires=["pandas==1.0.0"],
    # include MANIFEST.in
    include_package_data = True,
    url='http://gitXXXX',
    # desciption for the boots that're going to classify the lib
    Classifiers =[
        "licence :: WTFPL"],
    # command shell
    entry_points ={
        'console_scripts' : [
            'proclamer= mj_package.core:proclamer',
        ],
    },
    )