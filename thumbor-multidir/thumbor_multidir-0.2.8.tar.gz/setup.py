# coding: utf-8

from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


__version__ = None
exec(open('tc_multidir/_version.py').read())


setup(
    name='thumbor_multidir',
    version=__version__,
    description="Thumbor file loader for multiple paths",
    keywords='imaging face detection feature thumbor file loader',
    author='Benn Eichhorn',
    author_email='beichhor@gmail.com',
    url='https://github.com/benneic/thumbor_multidir',
    license='MIT',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: MacOS',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Multimedia :: Graphics :: Presentation'],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'python-dateutil',
        'six',
        'thumbor>=6.0.0,<7',
    ],
    extras_require={
        "tests": [
            "mock>=1.0.1,<3.0.0",
            "nose",
            "nose-focus",
            "colorama",
            "numpy",
            "flake8",
            "thumbor<7.0.0",
            "preggy>=1.3.0",
            "yanc>=0.3.3",
        ]
    },
    long_description=readme(),
)