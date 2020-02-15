from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='pspring-aws',
    version='0.0.33',
    license='TBD',
    author='Vasudevan Palani',
    author_email='vasudevan.palani@gmail.com',
    url='https://github.com/vasudevan-palani/pspring-aws',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pspringaws'],
    install_requires=['boto3>1.9','pspring>=0.0.1','realtime-aws-secretsmngr>=0.0.3', 'PyYAML>=5.3'],
    include_package_data=True,
    description="A framework to do a better development.",
)
