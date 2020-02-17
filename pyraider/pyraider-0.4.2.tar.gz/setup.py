import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='pyraider',
    version='0.4.2',
    packages=setuptools.find_packages(),    
    author='Raider Source',
    author_email='raidersource@gmail.com',
    description="A small example package for pythonsca",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points ={ 
        'console_scripts': [ 
            'pyraider = pyraider.cli:main'
        ] 
    }, 
    url="https://github.com/raidersource/pyraider",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    keywords = ['SCA', 'pyraider', 'Source Composition Analysis'],   # Keywords that define your package best
    install_requires=[
        'docopt',
        'beautifultable',
        'colored'
    ],
)