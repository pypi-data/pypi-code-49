"""
Pykrete logger tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import unittest

from src.pykrete.logging import make_logger


class PykreteLoggerUnitTests(unittest.TestCase):
    """Test pykrete's logger module"""
    def test_logger_default_stdout(self):
        """Verifies that only info is sent to stdout
        """
        logger = make_logger('default_stdout', False)
        logger.info('You should see this info')
        logger.debug('You shouldn\'t see this debug')
        logger.info(self.longMessage)  # how can I test this?

    def test_logger_verbose_stdout(self):
        """Verifies that both debug and info are sent to stdout when verbose output is requested
        """
        logger = make_logger('default_stdout', True)
        logger.info('You should see this info')
        logger.debug('You should see this debug as well')
        logger.info(self.longMessage)  # how can I test this?

    def test_logger_stderr(self):
        """Verifies that only info is sent to stdout
        """
        logger = make_logger('default_stdout', False)
        logger.error('You should see this error')
        logger.critical('You should see this critical')
        logger.exception('You should see this exception')
        logger.info(self.longMessage)  # how can I test this?


if __name__ == '__main__':
    unittest.main()
