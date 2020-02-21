from distutils.core import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pybbucket',
    packages=['pybbucket'],
    version='1.0.1',
    license='MIT',
    description='A Python wrapper for the Bitbucket Cloud REST API 2.0 version.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Akshay Maldhure',
    author_email='akshaymaldhure@gmail.com',
    url='https://github.com/akshayamaldhure',
    download_url='https://github.com/akshayamaldhure/pybbucket/archive/v1.0.1.tar.gz',
    keywords=['bitbucket', 'bitbucketapi', 'pybitbucket'],
    install_requires=[
        'pybbucket',
        'requests'
    ],
    classifiers=[],
)
