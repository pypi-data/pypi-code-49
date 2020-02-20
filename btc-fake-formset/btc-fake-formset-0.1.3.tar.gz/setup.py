import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-fake-formset',
    version='0.1.3',
    packages=['fake_formset'],
    include_package_data=True,
    license='BSD License',
    description='Fake Formset designed to display data of one form field (separated by characters) as a set of fields.',
    long_description=README,
    url='https://github.com/MEADez/btc-fake-formset',
    author='MEADez',
    author_email='m3adez@gmail.com',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
