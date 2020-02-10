import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-weasy-pdf',
    version='0.2',
    packages=['weasy_pdf'],
    include_package_data=True,
    license='BSD License',
    description='View mixin and template filters for PDF creation from the HTML-template.',
    long_description=README,
    url='https://github.com/MEADez/btc-weasy-pdf',
    author='MEADez',
    author_email='m3adez@gmail.com',
    install_requires=['WeasyPrint'],
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
