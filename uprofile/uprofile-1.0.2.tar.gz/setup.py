import codecs
from setuptools import find_packages, setup

with codecs.open('README.md', 'r', 'utf8') as reader:
    long_description = reader.read()

with codecs.open('requirements.txt', 'r', 'utf8') as reader:
    install_requires = list(map(lambda x: x.strip(), reader.readlines()))

setup(
    name='uprofile',
    version='1.0.2',
    packages=find_packages(),
    url='https://gitlab.leihuo.netease.com/shangyue/uprofile',
    license='MIT',
    author='shangyue',
    author_email='shangyue@corp.netease.com',
    description='cprofile with graphviz',
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
