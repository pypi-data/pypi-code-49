import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="objectit_airflow_monitoring",
    version="0.0.5",
    author="Linton",
    author_email="linton@example.org",
    description="Integrates Slack, Email, Rollbar and others to Airflow and sends notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)