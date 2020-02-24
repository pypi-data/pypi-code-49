"""
Python build info
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import os
from src.pykrete.args import environ
from .build_info import BuildInfo


class PythonBuildInfo(BuildInfo):
    """Python-specific build info"""
    # pylint: disable=too-few-public-methods
    def make_version(self):
        """Sets the package version from GitLab environment variables:
        CI_VERSION_MAJOR.CI_VERSION_MINOR.CI_PIPELINE_IID
        On any branch other than maser, CI_PIPELINE_ID is preceded by 'rc' instead of '.'

        :return: The version string
        """
        return ''.join(
            [
                environ('CI_VERSION_MAJOR', 'the major version of the package'),
                '.',
                environ('CI_VERSION_MINOR', 'the minor version of the package'),
                '.' if self.release else 'rc',
                os.environ['CI_PIPELINE_IID']
            ])
