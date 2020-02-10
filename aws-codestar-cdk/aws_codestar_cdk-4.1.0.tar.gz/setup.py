from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='aws_codestar_cdk',
    version='4.1.0',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=find_packages(exclude=['venv', 'test']),
    description=(
        'AWS CDK package that helps deploying a lambda function into CodeStar.'
    ),
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'aws_cdk.core',
        'aws_cdk.aws_iam',
        'aws_cdk.custom_resources',
        'aws_cdk.aws_s3',
        'aws_cdk.aws_s3_deployment',
        'aws-empty-bucket>=2.0.0,<3.0.0'
    ],
    author='Deividas Tamkus, Laimonas Sutkus',
    author_email='dtamkus@gmail.com, laimonas.sutkus@gmail.com',
    keywords='AWS CDK CodeStar',
    url='https://github.com/laimonassutkus/AwsCodeStar.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
