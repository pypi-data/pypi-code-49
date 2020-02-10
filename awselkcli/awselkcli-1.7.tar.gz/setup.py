from setuptools import setup, find_packages

setup(
    name='awselkcli',
    version='1.7',
    description='All the AWS functionality we use in our projects',
    author='Benlolo Noam',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='AWS utils cli wrapper',
    packages=find_packages(),
    install_requires=['boto3', 'elasticsearch', 'requests_aws4auth']
)
