from setuptools import setup

setup(
    name='powersupply',
    version='0.3.0',
    packages=['powersupply'],
    url='https://gitlab.com/MartijnBraam/pinepower',
    license='MIT',
    author='Martijn Braam',
    author_email='martijn@brixit.nl',
    description='Tool to display the detailed power status of the PinePhone',
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
    ],
    install_requires=[],
    zip_safe=True,
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'powersupply=powersupply.__main__:main'
        ]
    }
)
