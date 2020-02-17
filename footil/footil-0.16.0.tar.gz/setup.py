from distutils.core import setup

setup(
    name='footil',
    version='0.16.0',
    packages=['footil', 'footil.lib'],
    license='LGPLv3',
    url='https://github.com/focusate/footil',
    description="Various Python helpers for other projects",
    long_description=open('README.rst').read(),
    install_requires=['yattag', 'python-dateutil', 'verboselogs'],
    maintainer='Andrius Laukavičius',
    maintainer_email='dev@focusate.eu',
    python_requires='>=3.5',
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
