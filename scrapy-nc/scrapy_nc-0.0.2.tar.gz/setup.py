from setuptools import setup, find_packages


setup(
    name='scrapy_nc',
    version='0.0.2',
    url='https://github.com/fantasy/scrapy_nc',
    description='Scrapy plugins in NoCode',
    author='fantasy614@nocode.com',
    packages=['pipelines'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Framework :: Scrapy',
    ],
    install_requires=['scrapy'],
    requires=['scrapy (>=0.24.5)'],
)
