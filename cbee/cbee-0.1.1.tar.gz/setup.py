import setuptools

import cbee

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='cbee',
    version=cbee.version,
    packages=setuptools.find_packages(exclude=("tests",)),

    author='David Cavazos',
    author_email='dcavazosw@gmail.com',
    description='C/C++ build tools and package manager.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bee-field/cbee',

    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'cbee = cbee.cli:main'
        ],
    },

    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: C',
        'Programming Language :: C++',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Compilers',
    ],
)
