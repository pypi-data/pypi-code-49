import setuptools
import importlib

ctrlv = importlib.import_module("ctrl-v")

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='ctrl-v',
    version='0.1.0',
    license='MIT',
    author='Bitto Bennichan',
    author_email='bittobennichan@protonmail.com',
    description='Code snippet store',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=("tests",)),
    py_modules=['ctrl-v'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'beautifulsoup4',
        'Flask-Login',
        'Flask-MDE >= 1.2.0',
        'pymdown-extensions',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'html5lib',
        'Markdown',
        'waitress',
        'bleach'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ctrl-v = ctrlv:main'
        ]
    }
)
