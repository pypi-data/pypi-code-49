from setuptools import setup, find_packages
import pulseapi_integration

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pulseapi_integration",
    version=pulseapi_integration.__version__,
    author="Ostapets Vladislav",
    author_email="vlad12344444@gmail.com",
    description="Wrapper around pulseapi",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['pulseapi_integration', 'RobotMovingPannel'],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.18.1',
        'PyQt5==5.14.1',
        'requests==2.22.0',
    ]
)