from os.path import abspath, dirname, join

from setuptools import setup, find_packages

long_description = []

for text_file in ['README.rst', 'CHANGES.rst']:
    with open(join(dirname(abspath(__file__)), text_file), 'r') as f:
        long_description.append(f.read())

setup(
    name='traduki',
    description='SQLAlchemy internationalisation',
    long_description='\n'.join(long_description),
    version='1.3.0',
    author='Paylogic International',
    author_email='developers@paylogic.com',
    license='MIT',
    url='https://github.com/paylogic/traduki',
    install_requires=[
        'SQLAlchemy',
        'six>=1.9.0',
    ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    dependency_links=[],
    include_package_data=True,
    keywords='sqlalchemy i18n internationalisation',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
