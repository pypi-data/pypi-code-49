from setuptools import setup, find_packages

setup(
    name             = 'andystring',
    version          = '1.0',
    description      = 'For testing deployement',
    author           = 'Sanghyun, Kim',
    author_email     = 'behappytwice@gmail.com',
    url              = 'https://github.com/behappytwice/andystring',
    download_url     = 'https://githur.com/behappytwice/andystring/archive/1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['string util', 'string concatenation'],
    python_requires  = '>=3',
    #package_data     =  {
    #    'pyquibase' : [
    #        'db-connectors/sqlite-jdbc-3.18.0.jar',
    #        'db-connectors/mysql-connector-java-5.1.42-bin.jar',
    #        'liquibase/liquibase.jar'
    #]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)