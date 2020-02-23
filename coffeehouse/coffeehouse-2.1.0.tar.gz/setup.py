from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='coffeehouse',
    version='2.1.0',
    description='Official CoffeeHouse API Wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['coffeehouse', 'coffeehouse.lydia'],
    package_dir={
        'coffeehouse': 'coffeehouse'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.info',
    url='https://coffeehouse.intellivoid.info/',
    install_requires=[
        'requests>=2.3.0'
    ]
)
