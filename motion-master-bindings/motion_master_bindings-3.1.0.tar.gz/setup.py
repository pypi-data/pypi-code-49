import os

import setuptools
from distutils.command.clean import clean

with open('README.md', 'r') as fh:
    long_description = fh.read()


class CleanCommand(clean):
    """Custom logic for the clean command."""

    def run(self):
        clean.run(self)
        targets = [
            './dist',
            './build',
            './*.egg-info',
        ]
        os.system('rm -vrf %s' % ' '.join(targets))


setuptools.setup(
    name='motion_master_bindings',
    version='3.1.0',
    author='Synapticon GmbH',
    author_email='support@synapticon.com',
    description="Python bindings for connecting to the Synapticon Motion Master",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://www.synapticon.com",
    packages=setuptools.find_packages(),
    install_requires=['rx', 'motion-master-proto', 'pyzmq'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'clean': CleanCommand
    },
    # This dependency comes from the Rx package.
    python_requires='>=3.6',
)
