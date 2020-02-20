import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='experiment-ltt', # Replace with your own username
    version='0.1.3',
    author='Le Tien Thanh',
    author_email='20144075@student.hust.edu.vn',
    description='Experimentation toolbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ltthacker/experiment',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

