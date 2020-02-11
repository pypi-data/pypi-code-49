"""Configure the logging system for snippets."""
import logging


class LogConfiguration:
    """Logging configuration.

    Attributes
    -----------
    verbose : bool

    name : str

    """

    def __init__(self, verbose: bool, name: str):
        """Take a bool value."""
        self.verbose = verbose
        self.name = name

    def configure(self) -> None:
        """Update the logging level of :py:attr:`name` logger."""
        logging.basicConfig(
            format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')
        logging.getLogger(self.name).setLevel(
            logging.DEBUG if self.verbose else logging.INFO)
