from distutils.core import setup

setup(
    name='commontaskz',
    packages=['commontaskz'],
    version='0.5.18',
    license='MIT',
    description='Common Prefect Tasks to query systems & process results',
    author='Aliza Rayman',  # Type in your name
    author_email='aliza.rayman@zirra.com',  # Type in your E-Mail
    url='https://github.com/zirra-com/commontaskz',  # Provide either the link to your github or to your website
    download_url='https://github.com/zirra-com/commontaskz/archive/v0.5.18.tar.gz',  # I explain this later on
    keywords=['TASKS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'slackclient',
        'prefect',
        'datetime',
        'requests',
        'lz4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)