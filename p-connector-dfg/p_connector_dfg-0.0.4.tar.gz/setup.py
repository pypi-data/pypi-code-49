import setuptools

import p_connector_dfg

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name=p_connector_dfg.__name__,
    version=p_connector_dfg.__version__,
    author=p_connector_dfg.__author__,
    author_email=p_connector_dfg.__author_email__,
    description="Privacy-preserving Process Discovery Using Connector Method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m4jidRafiei/privacyAware-ConnectorMethod_DFG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pm4py==1.2.0',
        'pandas==0.24.2',
        'pycrypto==2.6.1',
        'numpy==1.17.3'
    ],
    project_urls={
        'Source': 'https://github.com/m4jidRafiei/privacyAware-ConnectorMethod_DFG'
    }
)