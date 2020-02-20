from setuptools import setup, find_packages

setup(
    name='accounting_vod',
    packages=['accounting_vod'],
    version='0.1.1',
    description='Generate VOD XML export for accounting software ',
    author='Boris Savic',
    author_email='boris70@gmail.com',
    url='https://github.com/boris-savic/python-accounting-vod',
    download_url='https://github.com/boris-savic/python-accounting-vod/tarball/0.1.1',
    keywords=['python vod', 'accounting', 'opal'],
    classifiers=[],
    install_requires=[
        'lxml>=4.4.1',
    ]
)
