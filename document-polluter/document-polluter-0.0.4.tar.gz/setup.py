from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='document-polluter',
    version='0.0.4',
    description='Pollutes documents with terms biased on specific geners',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gregology/document-polluter',
    author='Greg Clarke',
    author_email='greg@gho.st',
    license='MIT',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
    ],
    keywords='stop words machine learning ml bias biased natural language processing nlp',
    packages=find_packages(),
    install_requires=['pyyaml'],
    package_data={
        'document_polluter': [
            'pollution.yaml',
        ]
    }
)
