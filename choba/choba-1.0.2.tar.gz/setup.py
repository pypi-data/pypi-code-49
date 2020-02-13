
"""
choba setup
"""

from setuptools import setup, find_packages
VERSION = '1.0.2'


classifiers = """
Environment :: Console
Environment :: Web Environment
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Quality Assurance
Topic :: Software Development :: Testing
""".strip().splitlines()

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name='choba',
    version=VERSION,
    description='Python unittest simplified.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rendra Suroso',
    author_email='rs@cogsci.bandungfe.net',
    url='http://bfi.io',
    py_modules=['__main__'],
    zip_safe=False,
    scripts=[
        'bin/choba',
    ],
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    install_requires=[
        "webtest",
        "coverage",
    ],
    python_requires=">=2.7, !=3.0.*, "
        "!=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    license='MIT',
    classifiers=classifiers
)
