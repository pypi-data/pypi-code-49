from setuptools import setup, find_packages


setup(
    name='scrapy-nc',
    version='0.0.1',
    url='https://github.com/fantasy/scrapy_nc',
    description='Scrapy plugins in NoCode',
    author='fantasy614@nocode.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
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
