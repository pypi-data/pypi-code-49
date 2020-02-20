from setuptools import setup

import geoformat

markdown_path = 'README.md'

with open(markdown_path) as read_me_file:
    read_me_file_txt = read_me_file.read()

setup(
    name='geoformat',
    version=str(geoformat.version(verbose=False)),
    url='https://framagit.org/Guilhain/Geoformat',
    license='MIT',
    author='Guilhain Averlant',
    author_email='g.averlant@mailfence.com',
    description='Geoformat is a GDAL/OGR library overlayer',
    long_description=read_me_file_txt,
    long_description_content_type='text/markdown',
    py_modules=['geoformat', 'geoformat_lib.conversion.geometry_conversion', 'geoformat_lib.explore_data.print_data',
                'geoformat_lib.geoprocessing.connectors.predicates', 'geoformat_lib.geoprocessing.connectors.operations'
                ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: GIS",
    ]
)
