import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-floating-windows',
    version='0.7',
    packages=['floating_windows'],
    include_package_data=True,
    license='BSD License',
    description='Floating windows for use as pop-ups, modal or separate sources of information in a user graphical '
                'interface.',
    long_description=README,
    url='https://github.com/MEADez/btc-floating-windows',
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
