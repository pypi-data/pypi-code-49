from setuptools import setup, find_packages


setup(
    name='envrpt',
    version='0.1.0',
    description='Analyzes the packages installed in a Python environment',
    long_description=open('README.rst', 'r').read(),
    keywords='virtual environment package dependency analysis',
    author='Jason Simeone',
    author_email='jay@classless.net',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Development Status :: 4 - Beta',
    ],
    url='https://github.com/jayclassless/envrpt',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'envrpt = envrpt.cli:main',
        ],
    },
    install_requires=[
        'pip>=10',
    ],
)

