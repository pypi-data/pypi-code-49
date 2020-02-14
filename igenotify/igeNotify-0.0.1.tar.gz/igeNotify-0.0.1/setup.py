import setuptools
from setuptools import setup, Extension, find_packages
import os
from os import path
from codecs import open

curr_dir = path.abspath(path.dirname(__file__))

sfc_module = Extension('igeNotify',
                    sources=[                                                
                        'src/win32/NotifyImpl.cpp',
                        'src/Notify.cpp',
						'igeNotify.cpp',
                    ],
                    include_dirs=['include'],
                    library_dirs=[],
			        libraries=[])

setup(name='igeNotify', version='0.0.1',
		description= 'Python extension for local notification.',
		author=u'Indigames',
		author_email='dev@indigames.net',
		packages=find_packages(),
		ext_modules=[sfc_module],
		long_description=open(path.join(curr_dir, 'README.md')).read(),
        long_description_content_type='text/markdown',
        url='https://indigames.net/',
		license='MIT',
		classifiers=[
			'Intended Audience :: Developers',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			#'Operating System :: MacOS :: MacOS X',
			#'Operating System :: POSIX :: Linux',
			'Operating System :: Microsoft :: Windows',
			'Topic :: Games/Entertainment',
		],
        # What does your project relate to?
        keywords='Notification Notify Indigames',
      )
