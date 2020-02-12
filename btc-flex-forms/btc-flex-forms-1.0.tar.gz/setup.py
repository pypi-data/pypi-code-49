import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-flex-forms',
    version='1.0',
    packages=['flex_forms'],
    include_package_data=True,
    license='BSD License',
    description='Some form mixins, styles and scripts for fast form development.',
    long_description=README,
    url='https://github.com/MEADez/btc-flex-forms',
    author='MEADez',
    author_email='m3adez@gmail.com',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
