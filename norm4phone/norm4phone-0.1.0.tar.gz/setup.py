from setuptools import setup, find_packages

setup(
    name='norm4phone',
    version='0.1.0',
    description='a tool to normalize different writing of phone numbers into standard format',
    license='MIT License',
    url='https://github.com/xuxingya/norm4phone',
    author='xingya.xu',
    author_email='xingya.xu@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'norm4phone':'iso3166Data.json'}
)