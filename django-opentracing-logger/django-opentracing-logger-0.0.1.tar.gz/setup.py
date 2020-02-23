import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django-opentracing-logger',
    version='0.0.1',
    install_requires=[
        "Django>=1.11"
    ],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    license='BSD License',
    description='django opentracing SDK based on logger which focus on ease to use',
    long_description=README,
    url='https://github.com/FingerLiu/django-opentracing-logger',
    author='liupeng',
    author_email='liupeng@luojilab.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
