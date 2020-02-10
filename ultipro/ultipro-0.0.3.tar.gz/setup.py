from setuptools import setup

with open("README.md", "r") as fh:
    long_description= fh.read()

setup(
    name='ultipro',
    version='0.0.3',
    author='Brian Call',
    author_email='callbrian@gmail.com',
    description='Python Client for the UltiPro SOAP API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/puppetlabs/ultipro-soap-python',
    license='Apache 2.0',
    packages=['ultipro', 'ultipro.services'],
    install_requires=[
        'backoff',
        'click',
        'configparser',
        'pandas',
        'pandas_gbq',
        'zeep'
    ],
    keywords=['UltiPro', 'SOAP API', 'Wrapper', 'Client'],
    entry_points={
        'console_scripts': [
            'ultipro=ultipro.cli:cli',
        ],
    },
    python_requires='>=3.6',
)
