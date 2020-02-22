from skbuild import setup

setup(
    name='solv',
    description='A free package dependency solver using a satisfiability algorithm.',
    version='0.7.11',
    license='BSD',
    author='',
    author_email='',
    url='',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['solv'],
    package_dir={
        'solv': 'bindings/python3'
    },
    cmake_args=[
        '-DENABLE_PYTHON3:BOOL=ON',
        '-DENABLE_COMPLEX_DEPS:BOOL=ON',
        '-DENABLE_STATIC:BOOL=ON',
    ],
    cmake_languages=['C'],
)
