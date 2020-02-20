from setuptools import setup, find_packages


setup(
    name='plc800stg',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/gisce/plc800stg',
    license='MIT License',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=[
        'lxml',
        'pandas',
    ],
    description='PLC800 STG'
)
