import setuptools

setuptools.setup(
    name='starsheep',
    version='0.9',
    author='Maciej Nabozny',
    author_email='contact@cloudover.io',
    description='Starsheep YAML interpreter',
    long_description='This is YAML based database modilng tools based on Dinemic',
    long_description_content_type="text/markdown",
    url='https://starsheep.io',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    install_requires=[
        'dinemic',
    ],
    scripts=[
        'bin/starsheep',
        'bin/starsheep-cli',
    ]
)
