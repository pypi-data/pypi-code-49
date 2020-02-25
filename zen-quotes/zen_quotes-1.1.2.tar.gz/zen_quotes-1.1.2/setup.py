from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zen_quotes',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown',
    version = '1.1.2',
    setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='A sample lib Zen of Python',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='https://github.com/ymussi/zen_quotes',
    keywords = "Mussi",
    install_requires = ['requests'],
    zip_safe=False
    ),