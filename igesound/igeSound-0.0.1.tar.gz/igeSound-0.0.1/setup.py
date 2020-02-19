import importlib
try:
    importlib.import_module('numpy')
except ImportError:
	from pip._internal import main as _main
	_main(['install', 'numpy'])

from setuptools import setup, Extension, find_packages
import setuptools
import numpy
import sys
import os
from distutils.sysconfig import get_python_lib
import shutil

# To use a consistent encoding
from codecs import open

from os import path
here = path.abspath(path.dirname(__file__))

audiosource_src = path.join(here, '../../lib/ThirdParty/soloud/src/audiosource')
backend_src = path.join(here, '../../lib/ThirdParty/soloud/src/backend')
core_src = path.join(here, '../../lib/ThirdParty/soloud/src/core')
filter_src = path.join(here, '../../lib/ThirdParty/soloud/src/filter')

sfc_module = Extension('igeSound',
                    sources=[
                        'igeSound.cpp',
                        'Sound.cpp',
                        path.join(audiosource_src, 'monotone/soloud_monotone.cpp'),
                        path.join(audiosource_src, 'noise/soloud_noise.cpp'),
                        # path.join(audiosource_src, 'openmpt/soloud_openmpt.cpp'),
                        path.join(audiosource_src, 'sfxr/soloud_sfxr.cpp'),
                        path.join(audiosource_src, 'speech/darray.cpp'),
                        path.join(audiosource_src, 'speech/klatt.cpp'),
                        path.join(audiosource_src, 'speech/resonator.cpp'),
                        path.join(audiosource_src, 'speech/soloud_speech.cpp'),
                        path.join(audiosource_src, 'speech/tts.cpp'),
                        path.join(audiosource_src, 'tedsid/sid.cpp'),
                        path.join(audiosource_src, 'tedsid/soloud_tedsid.cpp'),
                        path.join(audiosource_src, 'tedsid/ted.cpp'),
                        path.join(audiosource_src, 'vic/soloud_vic.cpp'),
                        path.join(audiosource_src, 'vizsn/soloud_vizsn.cpp'),
                        path.join(audiosource_src, 'wav/dr_impl.cpp'),
                        path.join(audiosource_src, 'wav/soloud_wav.cpp'),
                        path.join(audiosource_src, 'wav/soloud_wavstream.cpp'),
                        path.join(audiosource_src, 'wav/stb_vorbis.c'),
                        
                        path.join(backend_src, 'sdl2_static/soloud_sdl2_static.cpp'),
                        
                        path.join(core_src, 'soloud.cpp'),
                        path.join(core_src, 'soloud_audiosource.cpp'),
                        path.join(core_src, 'soloud_bus.cpp'),
                        path.join(core_src, 'soloud_core_3d.cpp'),
                        path.join(core_src, 'soloud_core_basicops.cpp'),
                        path.join(core_src, 'soloud_core_faderops.cpp'),
                        path.join(core_src, 'soloud_core_filterops.cpp'),
                        path.join(core_src, 'soloud_core_getters.cpp'),
                        path.join(core_src, 'soloud_core_setters.cpp'),
                        path.join(core_src, 'soloud_core_voicegroup.cpp'),
                        path.join(core_src, 'soloud_core_voiceops.cpp'),
                        path.join(core_src, 'soloud_fader.cpp'),
                        path.join(core_src, 'soloud_fft.cpp'),
                        path.join(core_src, 'soloud_fft_lut.cpp'),
                        path.join(core_src, 'soloud_file.cpp'),
                        path.join(core_src, 'soloud_filter.cpp'),
                        path.join(core_src, 'soloud_misc.cpp'),
                        path.join(core_src, 'soloud_queue.cpp'),
                        path.join(core_src, 'soloud_thread.cpp'),
                        
                        path.join(filter_src, 'soloud_bassboostfilter.cpp'),
                        path.join(filter_src, 'soloud_biquadresonantfilter.cpp'),
                        path.join(filter_src, 'soloud_dcremovalfilter.cpp'),
                        path.join(filter_src, 'soloud_echofilter.cpp'),
                        path.join(filter_src, 'soloud_fftfilter.cpp'),
                        path.join(filter_src, 'soloud_flangerfilter.cpp'),
                        path.join(filter_src, 'soloud_freeverbfilter.cpp'),
                        path.join(filter_src, 'soloud_lofifilter.cpp'),
                        path.join(filter_src, 'soloud_robotizefilter.cpp'),
                        path.join(filter_src, 'soloud_waveshaperfilter.cpp'),
                    ],
                    define_macros=[('WITH_SDL2_STATIC', None)],
                    include_dirs=['bin/include', './', './win32', '../../lib/ThirdParty/soloud/include', '../../lib/ThirdParty/sdl2/include'],
                    library_dirs=['bin/win32'],
			        libraries=['SDL2', 'user32', 'Gdi32', 'winmm', 'setupapi', 'shell32', 'advapi32', 'ole32', 'version', 'imm32', 'oleaut32'])

setup(name='igeSound', version='0.0.1',
		description= 'C++ extension Sound for 3D and 2D games.',
		author=u'Indigames',
		author_email='dev@indigames.net',
		packages=find_packages(),
		ext_modules=[sfc_module],
		long_description=open(path.join(here, 'README.md')).read(),
        long_description_content_type='text/markdown',
        
        # The project's main homepage.
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
        keywords='Sound Audio 3D game Indigames',
      )
