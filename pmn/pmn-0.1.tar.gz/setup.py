from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pmn',
    version='0.1',
    packages=['pmn'],
    url='https://github.com/ivanjermakov/pmn',
    license='MIT',
    author='Ivan Ermakov',
    author_email='ivanjermakov1@gmail.com',
    description='terminal process manager for Linux',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['anytree', 'psutil', 'click'],
    scripts=['bin/pmn']
)
