from distutils.core import setup, Extension

module = Extension('carconfig', sources = ['src/CANMessageType.cpp', 'src/Config.cpp', 'src/FieldType.cpp', 'py_defs.cpp'], include_dirs=["include"], libraries=["boost_python3", "yaml-cpp"])

setup(name="carconfig", version="1.0.1", description="This is carconfig.", ext_modules=[module])
