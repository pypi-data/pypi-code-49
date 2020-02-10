from setuptools import setup, find_packages

cmdclass = {}


def readme():
    with open('README.rst') as f:
        return f.read()


version = "0.1"

setup(
    name="avatica-python",
    version=version,
    description="Avatica database adapter for Python",
    long_description=readme(),
    author="wangyonghe",
    author_email="yonghe.wang@joowing.com",
    url="https://bitbucket.org/lalinsky/python-phoenixdb",
    license="Apache 2",
    packages=find_packages(),
    include_package_data=True,
    cmdclass=cmdclass,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'protobuf>=3.0.0',
    ]
)
