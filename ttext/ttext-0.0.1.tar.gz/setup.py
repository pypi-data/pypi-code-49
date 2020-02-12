from setuptools import setup, find_packages

setup(
    name='ttext',
    version='0.0.1',
    description='A library for auto-converting URLs, mentions, hashtags, lists, etc. in Twitter text. Also does tweet validation and search term highlighting.',
    author='Gain App',
    author_email='developers@gainapp.com',
    url='https://github.com/BigPropeller/ttext',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    install_requires=[
        'setuptools'
    ],
    license="MIT"
)
