from setuptools import setup, find_packages


__package__ = 'agcli'
__version__ = '1.5.1'
__licence__ = 'LGPL3'
__author__ = 'Maxime De Wolf'
__url__ = 'https://gitlab.com/MaximeDeWolf/agcli'
__description__ = 'A GUI that helps building instructions for the CLI'

setup(
    #Metadata
    name=__package__,
    version=__version__,
    license=__licence__,

    author=__author__,
    url=__url__,

    description=__description__,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',

        'Topic :: Education :: Computer Aided Instruction (CAI)',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: System :: Shells',

        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        'Programming Language :: Python :: 3.6',
    ],
    keywords='gui cli shell terminal instruction',

    #Requirements
    install_requires=[
        "ruamel.yaml>=0.15",
        "urllib3>=1.23",
        "certifi>=2019.6",
        "wxPython>=4.0",
        "setuptools"
    ],
    python_requires='>=3.6',

    #Configuration
    entry_points={
        "console_scripts": ["agcli=agcli.agcli:cli"]
    },

    packages=find_packages(exclude=['scan_command']),
    include_package_data=True,
    zip_safe=False,

)
#Create the sdist and bsdist archives
##python3 setup.py bdist_wheel sdist

#To install the local test version
##pip3 install --user -e .


# for download the package from Gitlab
##pip3 install --user git+https://gitlab.com/MaximeDeWolf/agcli

# for the default PyPI server
##twine upload dist/*

#Run with the light theme, prefix with:
#GTK_THEME=Adwaita:light
