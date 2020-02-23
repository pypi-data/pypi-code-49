import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyramco',
    version='0.9.62',
    author='Jeremey Bingham',
    author_email='info@mansard.net',
    description='A complete wrapper class for the RAMCO API',
    install_requires=['requests'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mansard/pyramco',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.7',
    py_modules=['pyramco'],
    entry_points='''
        [console_scripts]
        pyramco = pyramco:pyramco
    '''
)