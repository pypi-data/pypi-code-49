"""Setup for the kw618 package."""

import setuptools

install_requires = [
    # requests相关
    "retry", "pysnooper", "user_agent", "requests",
    "scrapy", "uuid", "email", "execjs",
    "exchangelib", "urllib3", "selenium",
    # pandas相关
    "numpy", "pandas", "swifter", "pymongo",
    # pymongo相关
    "pymongo", "redis",
]



with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Kerwin Lui",
    author_email="kerwin19950830@gmail.com",
    name='kw618',
    license="MIT",
    description='integrated several packages for kerwin to use',
    version='0.0.2',
    long_description=README,
    url='https://gitee.com/kerwin_van_lui/kw618',
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*", "*.tags*"]),
    python_requires=">=3.6",
    install_requires=install_requires,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
