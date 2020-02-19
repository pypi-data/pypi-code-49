from distutils.core import setup, Extension
import platform


include_dirs = ["include"]
extra_args = []
library_dirs = []

if platform.system() == "Windows":
    extra_args += ['/std:c++14']
    include_dirs += ["win/include"]
    library_dirs += ["win/lib64"]
else:
    extra_args += ['-std=c++11']

module = Extension('carconfig', sources = ['src/CANMessageType.cpp', 'src/Config.cpp', 'src/FieldType.cpp', 'src/Node.cpp', 'py_defs.cpp'], include_dirs=include_dirs, library_dirs=library_dirs, libraries=["yaml-cpp"], extra_compile_args=extra_args)

setup(name="carconfig", version="1.0.5", description="This is carconfig.", ext_modules=[module])
