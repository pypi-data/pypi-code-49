import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('VERSION', 'r') as fh:
    version = fh.read()

setuptools.setup(
    name='kode_rpc',
    version=version,
    author='KODE',
    author_email='ashelepov@kode-t.ru',
    description='Library to work with RPC',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='==3.8.*',
    install_requires=[
        'aio-pika==6.4.1'
    ]
)
