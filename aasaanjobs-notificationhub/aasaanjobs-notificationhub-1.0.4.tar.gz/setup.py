from distutils.core import setup

from setuptools import find_packages

setup(
    name='aasaanjobs-notificationhub',
    version='1.0.4',
    packages=find_packages(where='.', exclude=('tests', 'venv', 'dist', )),
    author='Raghav Nayak, Sohel tarir',
    author_email='api@olxpeople.com',
    description='Python client for Aasaanjobs Notification Hub',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aasaanjobs/notification-hub-py-sdk',
    install_requires=[
        "boto3==1.10.4",
        "botocore==1.13.4",
        "protobuf==3.10.0",
        "validate-email==1.3"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.5',
    test_suite='tests',
    test_require=['moto']
)
