import setuptools


setuptools.setup(
    name='rivm',
    version='1.1.0',
    description='',
    author='',
    author_email='',
    url='',
    keywords=['rivm', 'aerius', 'nsl', 'monitoring', 'conversion'],
    packages=[
        'rivm',
        'rivm.conversion',
        'rivm.scripts'
    ],
    install_requires=[
        'pandas==0.25.3',
        'geopandas==0.6.3',
        'shapely==1.7.0',
    ],
    extras_require={
        'testing': ['pytest>=3.7.4', 'pytest-cov', 'flake8']
    },
    license='',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'convert_to_aerius = rivm.scripts.convert_to_aerius:main',
            'convert_to_nsl = rivm.scripts.convert_to_nsl:main',
            'convert_to_shp = rivm.scripts.convert_to_shp:main',
        ],
    }
)
