from distutils.core import setup

setup(
    name='datamodelz',
    packages=['datamodelz'],
    version='0.2.16',
    license='MIT',
    description='Data Models to query systems & process results & run checks',
    author='Aliza Rayman',  # Type in your name
    author_email='aliza.rayman@zirra.com',  # Type in your E-Mail
    url='https://github.com/zirra-com/datamodelz',  # Provide either the link to your github or to your website
    download_url='https://github.com/zirra-com/datamodelz/archive/v0.2.16.tar.gz',  # I explain this later on
    keywords=['TASKS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'prefect',
        'datetime',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)