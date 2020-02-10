from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

packages = find_packages(exclude=['tests*'])

setup(
    name='pvlv_database',
    version='0.0.7',
    license='LGPLv3',

    author='AbbestiaDC',
    author_email='not.simone.scuola@outlook.com',
    description='Database connector for Pavlov',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/The-Pavlov-Project/Pavlov-Database',

    packages=packages,

    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],

    python_requires='>=3.6',
    install_requires=[
        'pymongo',
        'dnspython',
    ],
)
