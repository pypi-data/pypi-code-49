"""Provides AbstractScanner class"""

from abc import ABC, abstractmethod

class AbstractScanner(ABC):
    """Provides common interface for scanners"""

    @abstractmethod
    def execute(self):
        """Execute the scan"""

    @staticmethod
    def validate_opts(opts):
        """Validate the scanner options, raising a ValueError if invalid"""
