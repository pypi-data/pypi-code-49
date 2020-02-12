from distutils.command.build_py import build_py
import glob
import os
import os.path
import pathlib
import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    sys.exit("Please use Python version 3.6 or higher.")

project_dir = os.path.dirname(os.path.abspath(__file__))
version_file_path = os.path.join(project_dir, "__version__.py")
readme_file_path = os.path.join(project_dir, "../README.md")

# path to xain proto
proto_path = "../protobuf/"

# get version
version = {}
with open(version_file_path) as fp:
    exec(fp.read(), version)


# get readme
with open(readme_file_path, "r") as fp:
    readme = fp.read()


# Handle protobuf
class BuildPyCommand(build_py):
    def run(self):
        # we need to import this here or else these packages would have to be
        # installed in the system before we could run the setup.py
        import grpc_tools
        from grpc_tools import protoc

        # get the path of grpc_tools protofiles
        grpc_path = grpc_tools.__path__[0]

        proto_files = []
        for path in get_proto_paths():
            proto_files.extend(collect_protos(path))

        os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

        for proto_file in proto_files:
            command = [
                "grpc_tools.protoc",
                # path to google .proto files
                f"--proto_path={grpc_path}/_proto",
                # path to xain .proto files
                f"--proto_path={proto_path}",
                "--python_out=./",
                "--grpc_python_out=./",
                proto_file,
            ]

            print("Building proto_file {}".format(proto_file))
            if protoc.main(command) != 0:
                raise Exception("error: {} failed".format(command))

        build_py.run(self)


def collect_protos(path):
    return [name.replace(f"{proto_path}/", "") for name in glob.glob(path)]


def get_proto_paths():
    return ["../protobuf/xain_proto/fl/*.proto", "../protobuf/xain_proto/np/*.proto"]


setup_requires = [
    "grpcio-tools~=1.23",  # Apache License 2.0
]

install_requires = [
    "numpy~=1.15",  # BSD
    "protobuf~=3.9",  # BSD
]

tests_require = [
    "pytest==5.3.2",  # MIT license
]

dev_require = [
    "twine==2.0.0",  # Apache License 2.0
    "wheel==0.33.6",  # MIT
    "isort==4.3.21",  # MIT
]

setup(
    name="xain-proto",
    version=version["__version__"],
    description="XAIN Protocol Buffers",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/xainag/xain-proto",
    author=["XAIN AG"],
    author_email="services@xain.io",
    license="Apache License Version 2.0",
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(exclude=["tests"]),
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require, "dev": dev_require + tests_require,},
    cmdclass={"build_py": BuildPyCommand},
)
