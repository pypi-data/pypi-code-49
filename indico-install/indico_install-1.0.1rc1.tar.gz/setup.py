#!/usr/bin/env python3
import os
from subprocess import check_call

from setuptools import find_packages, setup

setup(
    name="indico_install",
    version="1.0.1rc1",
    description="An indico install platform",
    author="Indico",
    author_email="engineering@indico.io",
    packages=find_packages(),
    install_requires=[
        "click",
        "pyyaml==5.1.2",
        "requests",
        "psycopg2-binary",
        "cached_property",
        "setuptools",
        "google-cloud-storage==1.25.0",
    ],
    extras_require={"aks": ["azure-cli"], "eks": ["boto3==1.9.176"]},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        indico=indico_install:indico_cli
    """,
    scripts=["bin/kube", "bin/cluster_info.sh"]
    + [f"bin/kube_bin/{filename}" for filename in os.listdir("bin/kube_bin")],
)

check_call(
    [
        "bash",
        "-c",
        'azcomm=$(command -v az); if ! [ -z "$azcomm" ]; then sed -i "s/^python /python3 /g" $azcomm; fi',
    ]
)
