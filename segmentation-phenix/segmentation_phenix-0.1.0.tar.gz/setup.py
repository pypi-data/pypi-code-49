import sysconfig

import numpy as np
from Cython.Distutils import build_ext
from setuptools import setup, Extension

our_flags = ["-march=native", "-std=c++11", "-DNDEBUG", "-Ofast", "-Wcpp"]

ext_modules = [
    Extension("segmentation_phenix.segmentation", ["segmentation_phenix/segmentation.pyx", ],
              language="c++",
              include_dirs=[np.get_include(), sysconfig.get_config_var('INCLUDEDIR')],
              extra_compile_args=our_flags,
              extra_link_args=["-std=c++11"],
              ),
]

setup(
    name="segmentation_phenix",
    packages=["segmentation_phenix"],
    version='0.1.0',
    description='Mixture model segmentation for Phenix images',
    author='Matej Usaj',
    author_email='m.usaj@utoronto.ca',
    url='https://github.com/mmasinas/segmentation_phenix',
    download_url='https://github.com/mmasinas/segmentation_phenix/archive/master.zip',
    keywords=['mixture', 'model', 'segmentation'],
    classifiers=[],
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
    install_requires=['cython', 'scikit-image', 'numpy'],
)
