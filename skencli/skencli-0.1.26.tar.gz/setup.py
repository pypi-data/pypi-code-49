import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='skencli',
    version='0.1.26',
    author='Sken.ai',
    author_email='author@sken.ai',
    description='Sken CLI for running scanners',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://sken.ai/',
	install_requires=[
		'PyYAML>=5.1.2',
		'boto3>=1.10.26',
		'docker>=4.1.0',
		'netifaces>=0.10.9',
		'wget>=3.2',
        'requests>=2.7.0'
	],
	include_package_data=True,
    packages=setuptools.find_packages(),
	entry_points = {
        'console_scripts': ['skencli=skencli.sken_runner:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=2.7',
)