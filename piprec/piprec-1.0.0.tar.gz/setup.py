import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piprec",
    version="1.0.0",
    author="Vladas",
    author_email="2262803m@student.gla.ac.uk",
    project_urls={
        'Source Code': 'https://github.com/VladasX/PipRec'
    },
    description="Recommender system for Python libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['piprec'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    python_requires='>=3',
    install_requires=[
        'requests',
        'argparse',
        'gensim',
        'nltk',
        'scipy<=1.3.2', # 1.4.0 breaks jensen-shannon distance function
        'numpy>=1.15.0',
        'anytree',
        'tabulate',
        'spacy>=2.2.2',
        'beautifulsoup4',
        'en-core-web-sm-mirror',
    ],
    package_data = {
        '': ['*.dictionary', '*.db', '*.model', '*.npy', '*.id2word', '*.state', '*.pkl', '*.txt', '*.json'],
    },
    entry_points={
        "console_scripts": [
            "piprec = piprec.recommender:main",
        ]
    },
)