from setuptools import setup

version = '0.8'


setup(
    name='envvarconf',
    version=version,
    packages=[
        'envvarconf',
    ],
    url='https://github.com/a1fred/envvarconf',
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    description='Show your coins portfolio',
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite="tests",
)
