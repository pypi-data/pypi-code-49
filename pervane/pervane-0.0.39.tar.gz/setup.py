import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pervane",
    version="0.0.39",
    author="hakanu",
    author_email="hi@hakanu.net",
    description="Plain text backed web based note taking and knowledge base building app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hakanu/pervane",
    packages=setuptools.find_packages(),
    install_requires=[
        "flask>=1.1.1",
        "Flask-Caching>=1.8.0",
        "Flask-HTTPAuth>=3.3.0",
        "Flask-Login>=0.4.1",
        "mistune>=0.8.4",
        "Flask-SQLAlchemy>=2.4.1",
        "Flask-User>=1.0.2.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    #scripts=['bin/pervane'],
    entry_points={"console_scripts": ["pervane = pervane.cli:main"]},
    include_package_data=True,
)
