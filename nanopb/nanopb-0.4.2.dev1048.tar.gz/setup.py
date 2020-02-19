# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nanopb', 'nanopb.generator', 'nanopb.generator.proto']

package_data = \
{'': ['*'],
 'nanopb.generator': ['nanopb/*'],
 'nanopb.generator.proto': ['google/protobuf/*']}

install_requires = \
['protobuf>=3.6']

extras_require = \
{u'grpcio-tools': ['grpcio-tools>=1.26.0rc1']}

entry_points = \
{'console_scripts': ['nanopb_generator = nanopb.generator.nanopb_generator:main_cli',
                     'protoc-gen-nanopb = nanopb.generator.nanopb_generator:main_plugin']}

setup_kwargs = {
    'name': 'nanopb',
    'version': '0.4.2.dev1048',
    'description': 'Nanopb is a small code-size Protocol Buffers implementation in ansi C. It is especially suitable for use in microcontrollers, but fits any memory restricted system.',
    'long_description': 'Nanopb - Protocol Buffers for Embedded Systems\n==============================================\n\n[![Build Status](https://travis-ci.org/nanopb/nanopb.svg?branch=master)](https://travis-ci.org/nanopb/nanopb)\n\nNanopb is a small code-size Protocol Buffers implementation in ansi C. It is\nespecially suitable for use in microcontrollers, but fits any memory\nrestricted system.\n\n* **Homepage:** https://jpa.kapsi.fi/nanopb/\n* **Documentation:** https://jpa.kapsi.fi/nanopb/docs/\n* **Downloads:** https://jpa.kapsi.fi/nanopb/download/\n* **Forum:** https://groups.google.com/forum/#!forum/nanopb\n\n\n\nUsing the nanopb library\n------------------------\nTo use the nanopb library, you need to do two things:\n\n1. Compile your .proto files for nanopb, using `protoc`.\n2. Include *pb_encode.c*, *pb_decode.c* and *pb_common.c* in your project.\n\nThe easiest way to get started is to study the project in "examples/simple".\nIt contains a Makefile, which should work directly under most Linux systems.\nHowever, for any other kind of build system, see the manual steps in\nREADME.txt in that folder.\n\n\n\nUsing the Protocol Buffers compiler (protoc)\n--------------------------------------------\nThe nanopb generator is implemented as a plugin for the Google\'s own `protoc`\ncompiler. This has the advantage that there is no need to reimplement the\nbasic parsing of .proto files. However, it does mean that you need the\nGoogle\'s protobuf library in order to run the generator.\n\nIf you have downloaded a binary package for nanopb (either Windows, Linux or\nMac OS X version), the `protoc` binary is included in the \'generator-bin\'\nfolder. In this case, you are ready to go. Simply run this command:\n\n    generator-bin/protoc --nanopb_out=. myprotocol.proto\n\nHowever, if you are using a git checkout or a plain source distribution, you\nneed to provide your own version of `protoc` and the Google\'s protobuf library.\nOn Linux, the necessary packages are `protobuf-compiler` and `python-protobuf`.\nOn Windows, you can either build Google\'s protobuf library from source (see section below) or use\none of the binary distributions of it. In either case, if you use a separate\n`protoc`, you need to manually give the path to the nanopb generator to the `protoc-gen-nanopb` \nplugin, as follows:\n\n    protoc --plugin=protoc-gen-nanopb=nanopb/generator/protoc-gen-nanopb --nanopb_out=. myprotocol.proto\n\nNote that the above `protoc`-based commands are the 1-command versions of a 2-command process, as described in the ["Nanopb: Basic concepts" document under the section "Compiling .proto files for nanopb"](https://jpa.kapsi.fi/nanopb/docs/concepts.html#compiling-proto-files-for-nanopb). Here is the 2-command process:\n\n    protoc -omyprotocol.pb myprotocol.proto\n    python nanopb/generator/nanopb_generator.py myprotocol.pb\n\n\n\nBuilding [Google\'s protobuf library](https://github.com/protocolbuffers/protobuf) from source\n---------------------------------------------------------------------------------------------\nWhen building Google\'s protobuf library from source, be sure to follow both the C++ installation instructions *and* the Python installation instructions, as *both* are required:\n1. [Protobuf\'s C++ build & installation instructions](https://github.com/protocolbuffers/protobuf/tree/master/src)\n2. [Protobuf\'s Python build & installation instructions](https://github.com/protocolbuffers/protobuf/tree/master/python)  \n- See additional reading [here](https://github.com/nanopb/nanopb/issues/417#issuecomment-517619517) and [here](https://stackoverflow.com/questions/57367265/how-to-compile-nanopb-proto-file-into-h-and-c-files-using-nanopb-and-protobuf/57367543#57367543).\n\n\n\nRunning the tests\n-----------------\nIf you want to perform further development of the nanopb core, or to verify\nits functionality using your compiler and platform, you\'ll want to run the\ntest suite. The build rules for the test suite are implemented using Scons,\nso you need to have that installed (ex: `sudo apt install scons` on Ubuntu). To run the tests:\n\n    cd tests\n    scons\n\nThis will show the progress of various test cases. If the output does not\nend in an error, the test cases were successful.\n\nNote: Mac OS X by default aliases \'clang\' as \'gcc\', while not actually\nsupporting the same command line options as gcc does. To run tests on\nMac OS X, use: `scons CC=clang CXX=clang`. Same way can be used to run\ntests with different compilers on any platform.\n\nFor embedded platforms, there is currently support for running the tests\non STM32 discovery board and [simavr](https://github.com/buserror/simavr)\nAVR simulator. Use `scons PLATFORM=STM32` and `scons PLATFORM=AVR` to run\nthese tests.\n\n\nBuild systems and integration\n-----------------------------\nNanopb C code itself is designed to be portable and easy to build\non any platform. Often the bigger hurdle is running the generator which\ntakes in the `.proto` files and outputs `.pb.c` definitions.\n\nThere exist build rules for several systems:\n\n* **Makefiles**: `extra/nanopb.mk`, see `examples/simple`\n* **CMake**: `extra/FindNanopb.cmake`, see `examples/cmake`\n* **SCons**: `tests/site_scons` (generator only)\n* **Bazel**: `BUILD` in source root\n* **Conan**: `conanfile.py` in source root\n* **PlatformIO**: https://platformio.org/lib/show/431/Nanopb\n* **PyPI/pip**: https://pypi.org/project/nanopb/\n\nAnd also integration to platform interfaces:\n\n* **Arduino**: http://platformio.org/lib/show/1385/nanopb-arduino\n',
    'author': 'Petteri Aimonen',
    'author_email': 'jpa@npb.mail.kapsi.fi',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jpa.kapsi.fi/nanopb/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7',
}


setup(**setup_kwargs)
