import re
from setuptools import setup, Command


def get_requirements():
    req = []
    deps = []
    with open("REQUIREMENTS", "r") as f:
        for l in  f.readlines():
            l = l.strip()
            if l.startswith("#"):
                continue
            elif l.startswith("git+"):
                deps.append(l)
            else:
                req.append(l)
    return req, deps


with open('adsocket_transport/version.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

reqs, deps = get_requirements()


with open("README.md", "r") as fh:
    long_description = fh.read()


class TeamCityVersionCommand(Command):

    description = "Report package version to TeamCity"
    user_options = []

    def initialize_options(self):
        """NOOP"""
        pass

    def finalize_options(self):
        """NOOP"""
        pass

    def run(self):
        """
        Echo the teamcity service message
        """
        print(
            "##teamcity[buildNumber '{}-{{build.number}}']"
            .format(version)
        )


setup(
    name="adsocket-transport",
    cmdclass={
        'tc_version': TeamCityVersionCommand
    },
    install_requires=reqs,
    dependency_links=deps,
    packages=['adsocket_transport', 'adsocket_transport.broker'],
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    license='MIT',
    description="ADSocket transport library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "aioredis": ["aioredis==1.3.1"],
    },
    version=version,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
)
