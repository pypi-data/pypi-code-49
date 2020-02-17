import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='cej-utils',
    version='0.0.4',
    author='Overjet AI',
    author_email='caidan@overjet.ai',
    description='Bundle of functions to help calculate various metrics.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/overjetdental/cej-utils',
    packages=setuptools.find_packages(),
    install_requires=[
        'imantics>=0.1.12',
        'numpy>=1.18.1',
        'Shapely==1.7.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
