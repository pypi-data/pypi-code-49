import setuptools

long_desc = open("README.rst").read()

setuptools.setup(
    name='dom_query',
    version='0.0.4',
    packages=('dom_query', ),

    description="CSS selector syntax for python minidom "
                "and compatible DOM implementations",
    long_description=long_desc,

    # url git
    url='https://gitlab.com/geusebi/dom_query',

    python_requires='>=3.6',
    install_requires=tuple(),

    author='Giampaolo Eusebi',
    author_email='giampaolo.eusebi@gmail.com',

    license='GNU LGPL 3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
