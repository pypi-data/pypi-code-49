"""
Build information base class
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import sys
import os
from abc import abstractmethod
from src.pykrete.logging import make_logger_by_verbose_arg, fatal


class BuildInfo:
    """Represents the selected build mode

    :property release: True for Release mode, False otherwise
    :property upload: True for Upload of build, False otherwise
    """
    def __init__(self):
        self._logger = make_logger_by_verbose_arg('BuildMode')
        self.release = self._is_release()
        self.upload = self.release or 'candidate' in sys.argv
        self._forced = self._is_forced()
        self.upload |= self._forced

    @abstractmethod
    def make_version(self):
        """Makes the version string for this build

        :return: The version string
        """

    @staticmethod
    def _is_release():
        """Checks whether this is a Release build

        :return: True for release build, False otherwise
        :exception Exception: Release mode requested outside of the master branch
        """
        release = 'release' in sys.argv
        if release and not os.environ['CI_COMMIT_REF_NAME'] == 'master':
            fatal('Only master branch can run release build')
        return release

    def _is_forced(self):
        """Checks if upload is manually forced

        :return: True if manually forced, False otherwise
        :exception FileExistsError: system forced the build, but the manual force still exists
        """
        marker_file = 'FORCE_UPLOAD.txt'
        self._logger.debug('Checking for %s', os.path.join(os.getcwd(), marker_file))
        file_exists = os.path.isfile(marker_file)
        if file_exists and self.upload:
            fatal(f'Remove manual commit file [{marker_file}]', self._logger, FileExistsError)
        return file_exists

    def __str__(self):
        """Gets a string representation of this object"""
        return ''.join([
            'Release' if self.release else 'Candidate'
            ' build with',
            ' forced' if self._forced else ('' if self.upload else 'out'),
            ' upload of version ',
            self.make_version()])
