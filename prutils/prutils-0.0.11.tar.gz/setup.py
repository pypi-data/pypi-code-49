from setuptools import setup

setup(
    name='prutils',
    version='0.0.11',
    author='sToa',
    author_email='prehisle@gmail.com',
    url='https://my.oschina.net/u/618083',
    description=u'Some of my code that may be used in multiple projects, extract them and form this library',
    packages=['prutils'],
    install_requires=[
        'requests==2.22.0'
    ],
    entry_points={
        'console_scripts': [
            'pru_cmds=prutils.cmds:main',
        ]
    }
)