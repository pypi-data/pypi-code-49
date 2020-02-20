import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="salesforcecli",
    version="0.0.5",
    author="Will Watkinson",
    author_email="wjwats4295@gmail.com",
    description="A package to explore a Salesforce org, perform queries, bulk creates, updates and deletes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/wjwatkinson/salesforcecli",
    packages=["sfcli"],
    install_requires=['simple-salesforce',
                      'tabulate',
                      'pandas',
                      'python-dotenv'],
    entry_points={
        'console_scripts': [
            'salesforcecli = sfcli.__main__:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)