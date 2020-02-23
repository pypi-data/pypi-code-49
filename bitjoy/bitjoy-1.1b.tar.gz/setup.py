import setuptools

with open('README.md') as file:
    long_description = file.read()

setuptools.setup(
    name='bitjoy',
    version='1.1',
    license='MIT',
    description='Bit, Bytes and Logical Gates Abstraction.',
    author='Matheus Sena Vasconcelos',
    author_email='sena.matheus14@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/senavs/BitJoy',
    keywords=['bitjoy', 'bit', 'bytes', 'logical-operators',
              'int_to_bytes', 'half-adder', 'full-adder',
              'boolean', 'gates', 'abstraction'],
    packages=['bitjoy', 'bitjoy.dtypes', 'bitjoy.utils'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_required='>=3.6'
)
