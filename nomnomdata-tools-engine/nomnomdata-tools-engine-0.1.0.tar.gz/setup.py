import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nomnomdata-tools-engine",
    version="0.1.0",
    author="Nom Nom Data",
    author_email="info@nomnomdata.com",
    description="Package containing tooling for developing nominode engines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/nomnomdata/tools/nomnomdata-tools-engine",
    packages=setuptools.find_namespace_packages(),
    classifiers=["Programming Language :: Python :: 3.7"],
    install_requires=[
        "docker>=3.5.1",
        "boto3>=1.9.33",
        "sqlparse>=0.2.4",
        "PyYAML>=3.10",
        "gitpython>=2.1.11",
        "docker-compose>=1.22.0",
        "paramiko>=2.4.2",
        "jinja2",
        "Cerberus>=1.2",
        "python-dotenv==0.10.3",
        "requests!=2.11.0,!=2.12.2,!=2.18.0,<2.21,>=2.6.1",
        "nomnomdata-cli>=0.1.0",
    ],
    entry_points={
        "nomnomdata.cli_plugins": {"engine_tools=nomnomdata.tools.engine.cli:cli"}
    },
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False,
)
