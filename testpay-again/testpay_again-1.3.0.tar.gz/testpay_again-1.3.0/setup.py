import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="testpay_again",
    version="1.3.0",
    description="Testpay Python Client",
    url="https://github.com/soumya-vats/test-repo-python",
    author="Team Testpay",
    license="MIT",
    packages=setuptools.find_packages(),
    keywords='Testpay payment gateway india',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",

        # List of supported Python versions
        # Make sure that this is reflected in .travis.yml as well
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
 )
