from setuptools import setup
setup(
    name = 'PttSpider',
    packages = ['PttSpider'],
    version = '0.1.7',
    description = 'fetch ptt data',
    author = 'W',
    author_email = 'wang655370@gmail.com',
    url = 'https://github.com/goodboyjj/PttSpider',
    keywords = ['ptt'],
    license='MIT',
    install_requires=[
        'pyquery',
        'requests',
        'fake_useragent'
    ],
    classifiers = [],
    python_requires='>=3.6'
)