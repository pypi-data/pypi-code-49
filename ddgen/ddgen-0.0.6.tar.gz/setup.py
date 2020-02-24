import io

import setuptools

import ddgen
from ddgen.db.h2 import supported_h2_versions

setuptools.setup(name='ddgen',
                 version=ddgen.__version__,
                 packages=['ddgen'],
                 install_requires=['pandas>=0.23', 'numpy>=1.16', 'psycopg2-binary>=2.8.3'],

                 long_description=io.open('README.md', encoding='utf-8').read(),
                 long_description_content_type='text/markdown',

                 author='Daniel Danis',
                 author_email='daniel.gordon.danis@gmail.com',
                 url='https://github.com/ielis/ddgen',
                 description='Library of Python utilities that I needed so many times',
                 license='GPLv3',
                 keywords='bioinformatics genomics',

                 package_data={'ddgen': ['utils/data/hg19.dict',
                                         'utils/data/hg38.dict'] +
                                        ['db/jar/h2-{}.jar'.format(version) for version in supported_h2_versions]},
                 test_suite='tests')
