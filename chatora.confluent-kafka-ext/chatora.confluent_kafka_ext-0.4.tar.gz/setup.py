import codecs
import pathlib
from runpy import run_path

from setuptools import (
    setup,
    find_namespace_packages,
)

PKG_ROOT_DIR_PATH = pathlib.PosixPath(__file__).parent

_install_requires = [
    'setuptools >= 41.0.1',
    'pip >= 19.1.1',
    'wheel >= 0.33.4',
    'packaging >= 19.0',

    'avro-python3 >= 1.9.0',
    'confluent-kafka >= 1.0.1',
    'expbackoff >= 0.1.1',
    'fastavro >= 0.22.2',
    'fasteners >= 0.15',
    'requests >= 2.22.0',
    'simplejson >= 3.16.0',
    'structlog >= 19.1.0',
    'urllib3 >= 1.24.1',

    'chatora.util >= 0.2.5',
]

_extras_require = {
    'dev': [
        'bumpversion >= 0.5.3',
        'check-manifest >= 0.39',
        'colorama >= 0.4.1',
    ],
}

_setup_requires = [
]

_tests_require = [
]

_dependency_links = [
]

_package_data = {
    '': ('LICENSE.txt',),
}

_ext_modules = [
]

_cmdclass = {
}

_entry_points = {
}

_scripts = [
]

data_files = [
]


try:
    with codecs.open(filename=PKG_ROOT_DIR_PATH / 'README.md', encoding='utf-8') as f:
        README = f.read()
except FileNotFoundError:
    README = ''

try:
    with codecs.open(filename=PKG_ROOT_DIR_PATH / 'CHANGES.md', encoding='utf-8') as f:
        CHANGES = f.read()
except FileNotFoundError:
    CHANGES = ''


setup(
    name='chatora.confluent_kafka_ext',
    version=run_path(
        PKG_ROOT_DIR_PATH / 'chatora' / 'confluent_kafka_ext' / '_pkg_info.py',
    )['__version__'],
    description='Apache Kafka and Schema Registry client libraries for Python on top of confluent-kafka-python.',
    long_description=(README + '\n\n' + CHANGES).strip(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/takaomag/chatora.confluent_kafka_ext',
    download_url='https://github.com/takaomag/chatora.confluent_kafka_ext/releases',
    project_urls={
        'source code': 'https://github.com/takaomag/chatora.confluent_kafka_ext',
        'issues': 'https://github.com/takaomag/chatora.confluent_kafka_ext/issues',
        'documentation': 'https://github.com/takaomag/chatora.confluent_kafka_ext/blob/master/README.md',
    },
    author='Takao Magoori',
    author_email='takaomag@users.noreply.github.com',
    maintainer='Takao Magoori',
    maintainer_email='takaomag@users.noreply.github.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Cython',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        'Kafka', 'Confluent Platform', 'Schema Registry', 'Avro',
    ],
    packages=find_namespace_packages(
        include=('chatora.*',),
        exclude=(
            'tests', 'tests.*', '*.tests', '*.tests.*',
            'test', 'test.*', '*.test', '*.test.*',
            'scala', 'scala.*',
        ),
    ),
    include_package_data=True,
    package_data=_package_data,
    data_files=data_files,
    zip_safe=True,
    python_requires=','.join((
        '>=3.7',
    )),
    install_requires=_install_requires,
    extras_require=_extras_require,
    setup_requires=_setup_requires,
    tests_require=_tests_require,
    dependency_links=_dependency_links,
    ext_modules=_ext_modules,
    cmdclass=_cmdclass,
    entry_points=_entry_points,
    scripts=_scripts,
)
