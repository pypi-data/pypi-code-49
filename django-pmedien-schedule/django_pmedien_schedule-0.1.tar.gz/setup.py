from setuptools import setup, find_packages

setup(
    name='django_pmedien_schedule',
    version='0.1',
    packages=find_packages(exclude=['tests*', 'migrations']),
    license='MIT',
    description='Simple schedule implementation',
    long_description=open('README.md').read(),
    install_requires=['django'],
    url='http://www.pmedien.com',
    author='pmedien GmbH',
    author_email='nomail@pmedien.com'
)