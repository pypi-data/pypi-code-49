from distutils.core import setup

version = '0.0.7'

setup(
    name='simple-iso',
    packages=['iso'],
    scripts=['bin/iso8601'],
    version=version,
    license='MIT',
    description='Code for ISO specs, starting with ISO 8601 but may or may not grow',
    long_description='Code for ISO specs, starting with ISO 8601 but may or may not grow',
    author='Dean Kayton',
    author_email='hello@dnk8n.dev',
    url='https://gitlab.com/dnk8n/simple-iso',
    download_url=f'https://gitlab.com/dnk8n/simple-iso/-/archive/v{version}/simple-iso-v{version}.tar.gz',
    keywords=['iso', 'iso8601', 'datetime', 'conversion'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
