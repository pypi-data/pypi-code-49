from distutils.core import setup, Extension

module = Extension('carconfig', sources = ['src/CANMessageType.cpp', 'src/Config.cpp', 'src/FieldType.cpp', 'py_defs.cpp'], include_dirs=["include"], libraries=["yaml-cpp"], extra_compile_args=['-std=c++11'])

setup(name="carconfig", version="1.0.3", description="This is carconfig.", ext_modules=[module])
