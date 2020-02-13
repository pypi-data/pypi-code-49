import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-template-tables',
    version='0.1',
    packages=['template_tables'],
    include_package_data=True,
    license='BSD License',
    description='Some classes for for describing tables with an auto-generated template.',
    long_description=README,
    url='https://github.com/MEADez/btc-template-tables',
    author='MEADez',
    author_email='m3adez@gmail.com',
    install_requires=['django-filter>=2.2.0', 'btc-flex-forms>=1.0'],
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
