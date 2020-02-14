from setuptools import setup

def readme():
    with open("README.rst") as f:
        README = f.read()
    return README

setup(
    name='CrawlerCodePythonTools',
    version='1.1.10',
    packages=['pythontools.core', 'pythontools.identity', 'pythontools.sockets', 'pythontools.telegrambot', 'pythontools.dev', 'pythontools.webbot', 'pythontools.gui'],
    url='https://github.com/CrawlerCode',
    license='',
    author='CrawlerCode',
    author_email='',
    description='',
    long_description=readme(),
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=["colorama", "telegram", "python-telegram-bot", "cloudpickle", "PyQt5", "selenium"]
)
