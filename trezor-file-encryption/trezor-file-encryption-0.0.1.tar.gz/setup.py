import setuptools
from trezor_file_encryption import __version__

install_requires = [
    'trezor==0.11.6',
    'colorama==0.4.3',
    'pycryptodome==3.9.6'
]

with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='trezor-file-encryption',
    version=__version__,
    author='dnsge',
    author_email='dnsge.personal@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/dnsge/',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Security"
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['trezorenc=trezor_file_encryption.command_line:main']
    }
)
