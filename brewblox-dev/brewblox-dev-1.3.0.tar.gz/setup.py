from setuptools import find_packages, setup

setup(
    name='brewblox-dev',
    use_scm_version={'local_scheme': lambda v: ''},
    url='https://github.com/BrewBlox/brewblox-dev',
    author='BrewPi',
    author_email='development@brewpi.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='brewblox devops',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'python-dotenv',
        'click',
    ],
    python_requires='>=3.6',
    setup_requires=['setuptools_scm'],
    entry_points={
        'console_scripts': [
            'brewblox-dev = brewblox_dev.__main__:main',
        ]
    }
)
