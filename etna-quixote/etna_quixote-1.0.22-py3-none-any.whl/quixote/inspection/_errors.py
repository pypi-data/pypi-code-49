"""
Internal module providing exception types for in-job failures
"""

from textwrap import dedent


class KOError(Exception):
    """
    Exception class representing a step failure caused by the student
    """
    pass


class InternalError(Exception):
    """
    Exception class representing a step failure caused by an internal error
    """
    pass


class TimeoutError(Exception):
    """
    Exception class representing an error related to a timeout when executing a process
    """

    def __init__(self, cause: Exception):
        self.__cause__ = cause

    def __str__(self):
        cmd = self.__cause__.cmd if isinstance(self.__cause__.cmd, str) else " ".join(self.__cause__.cmd)
        return dedent(f"""
        process '{cmd}' did not terminate before a timeout of {self.__cause__.timeout} seconds expired
        stdout: {self.__cause__.output}
        stderr: {self.__cause__.stderr}
        """)
