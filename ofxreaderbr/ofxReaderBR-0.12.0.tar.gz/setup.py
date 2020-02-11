from distutils.core import setup

setup(
    name='ofxReaderBR',
    packages=['ofxReaderBR',
              'ofxReaderBR.model',
              'ofxReaderBR.reader',
              'ofxReaderBR.reader.pdf'],
    version='0.12.0',
    license='MIT',
    description='Convert ofx + xlsx to xlsx - pt_BR',
    author='Fintask',
    author_email='admin@fintask.com.br',
    url='https://github.com/Fintask/ofxReaderBR/',
    download_url='https://github.com/Fintask/ofxReaderBR/archive/v0.12.0.tar.gz',
    keywords=['ofx', 'xlsx'],
    install_requires=[
        'et-xmlfile',
        'jdcal',
        'openpyxl',
        'ofxtoolslambda',
        'pytz',
        'lxml',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
