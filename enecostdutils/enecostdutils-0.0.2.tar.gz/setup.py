from setuptools import setup, find_packages

setup(
    name='enecostdutils',
    version='0.0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A python package containing all the boiler plate code for Eneco-std utils.',
    long_description='add read me later',
    install_requires=['pyodbc<=4.0.24', 'pandas<=0.23.0'],
    author='Vincent Visser',
    author_email=''
)