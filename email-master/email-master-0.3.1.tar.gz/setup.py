from setuptools import setup


with open('./README.rst') as f:
    long_description = f.read()

setup(
    name='email-master',
    packages=['email_master'],
    version='0.3.1',
    description='Master Email Parsing Package',
    author='Swimlane',
    author_email="info@swimlane.com",
    long_description=long_description,
    install_requires=[
        "pendulum==1.2.5",
        "compressed-rtf==1.0.5"
        "extract_msg==0.23.2"
    ],
    keywords=['utilities', 'email', 'parsing', 'eml', 'msg'],
    classifiers=[],
)
