from setuptools import setup, find_packages

NAME = 'forpay_client'
VERSION = '1.0.19'
AUTHOR = 'bozimeile'
EMAIL = 'zz.hacfox@gmail.com'
URL = 'https://github.com/hacfox/forpay_client.git'
DESCRIPTION = 'The client module of Forpay Python sdk'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    license='MIT License',
    packages=find_packages(exclude=['test*']),
    platforms="any",
    keywords=['forpay', 'forpay-client', 'sdk'],
    url=URL,
    install_requires=[
        'pycryptodome>=3.9.4',
        'requests>=2.22.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ],
)
