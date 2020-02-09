from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='labelsync',
    version='0.1.1',
    keywords='label synchronization github gitlab',
    description='Web app for synchronization of issue labels across repositories',
    long_description=long_description,
    author='Krystof Novotny',
    author_email='novotkry@fit.cvut.cz',
    license='WTFPL',
    url='https://github.com/novotkry/mi-pyt-final',
    zip_safe=False,
    packages=find_packages(),
    package_data={
        'labelsync': [
            'templates/*.html',
        ]
    },
    install_requires=[
        'Flask',
        'jinja2',
        'requests',
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest', 'betamax', 'flexmock'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
