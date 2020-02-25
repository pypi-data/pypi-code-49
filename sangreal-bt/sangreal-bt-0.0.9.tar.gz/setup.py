from setuptools import setup, find_packages

setup(
    name='sangreal-bt',
    version='0.0.9',
    description=('vector backtest'),
    install_requires=[
        'attrs',
        'fastcache',
        'pandas',
        'numpy',
        'matplotlib',
    ],
    # long_description=open('README.rst').read(),
    author='liubola',
    author_email='lby3523@gmail.com',
    # maintainer='<维护人员的名字>',
    # maintainer_email='<维护人员的邮件地址',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/liubola/sangreal-bt',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
