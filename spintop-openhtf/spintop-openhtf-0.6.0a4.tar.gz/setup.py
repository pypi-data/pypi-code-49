import os
import sys
from glob import glob
from setuptools import setup, find_packages
from setuptools.command.install import install as install_orig
from setuptools.command.develop import develop as develop_orig


HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'src', 'spintop_openhtf', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()

# if not os.path.exists(os.path.join('openhtf', 'openhtf')):
#     raise Exception('Please checkout the openhtf submodule before install.')

compiled_proto_files = glob('src/openhtf/output/proto/*_pb2.py')
if not compiled_proto_files:
    raise Exception('Protobuf files in openhtf where not compiled. Must be done before hand.')

# Find packages under openhtf(git) / openhtf
# Add the package itself

# openhtf_packages = ['openhtf'] + ['openhtf.' + pack for pack in find_packages(where='openhtf/openhtf')]
packages =  find_packages('src')

print(packages)

setup(
    name='spintop-openhtf',
    version=VERSION,
    description='A complete integration to spintop and the SPIN Suite using OpenHTF. OpenHTF is currently vendored-in.',
    author='William Laroche',
    author_email='william.laroche@tackv.ca',
    maintainer='William Laroche',
    maintainer_email='william.laroche@tackv.ca',
    url='https://gitlab.com/tackv/spintop-openhtf',
    package_dir={
        '': 'src',
    },
    packages=packages,
    package_data={
        'examples': [
            'example_attachment.txt',
            'example_config.yaml'
        ],
        'openhtf': [
            'output/proto/*.proto',
            'output/web_gui/dist/*',
            'output/web_gui/dist/css/*',
            'output/web_gui/dist/js/*',
            'output/web_gui/dist/img/*',
            'output/web_gui/*'
        ],
        'spintop_openhtf': [
            'VERSION',
            'callbacks/web_gui/dist/*',
            'callbacks/web_gui/dist/css/*',
            'callbacks/web_gui/dist/js/*',
            'callbacks/web_gui/dist/img/*',
            'callbacks/web_gui/*'
        ]
    },
    install_requires=[
        'appdirs>=1.0.0',
        'oauth2client>=4.1.0',
        'colorama>=0.3.9,<1.0',
        'contextlib2>=0.5.1,<1.0',
        'future>=0.16.0',
        'gspread>=3.1.0',
        'google-api-python-client>=1.7.10',
        'mutablerecords>=0.4.1,<2.0',
        'oauth2client>=4.1.3',
        'protobuf>=3.6.0,<4.0',
        'PyYAML>=5.0',
        'pyOpenSSL>=17.1.0,<18.0',
        'SheetFu>=1.4.1',
        'pyserial>=3.3.0,<4.0',
        'paramiko',
        'jsonschema>=3.0.2',
        'markdown2>=2.3.8'
    ],
    extras_require={
        'server':[ # Allows the different GUI servers. Can still run without GUI.
            'tornado>=4.3,<5.0', 
            'sockjs-tornado>=1.0.3,<2.0',
        ]
    },
    setup_requires=[
        'wheel>=0.29.0,<1.0',
    ],
    tests_require=[
        'mock>=2.0.0',
        'pytest>=2.9.2',
        'pytest-cov>=2.2.1',
    ],
)