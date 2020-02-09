"""
    This software is a part of backupmysystemusb2usb and its functionality is
    to backup one usb key to another usb with the same space disk
    Author: Stéphane Bressani <s.bressani@bluewin.ch>
"""
import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


GNU = 'GNU Lesser General Public License v3 or later (LGPLv3+)'

setup(
    name='backupmysystemusb2usb',
    version='1.0.3',
    description='Backup a usb key to another usb key with the same space disk',
    long_description=(read('README.rst')),
    url='https://github.com/stephaneworkspace/backupmysystemusb2usb.git',
    author='Stéphane Bressani',
    author_email='s.bressani@bluewin.ch',
    license='cc0',
    packages=find_packages(include=['backupmysystemusb2usb',
                                    'backupmysystemusb2usb.*']),
    install_requires=[
        'PyYAML==5.1.2',
    ],
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ' + GNU,
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Mirroring',
        'Topic :: Utilities'
    ],
)
