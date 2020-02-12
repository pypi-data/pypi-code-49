"""Error functions for ccautils module."""
import sys


def formatErrorMsg(funcname, exc):
    """Formatter for error messages.

    Args:
        funcname: str the function name where the error occurred
        exc: Exception

    Returns:
        str:
    """
    ename = type(exc).__name__
    return f"Error in {funcname}: {ename}: {exc}\n"


def errorExit(funcname, exc, errorvalue=1):
    """Exit the program displaying the error text.

    Args:
        funcname: str function name where the error occurred
        exc: Exception
        errorvalue: int exit value
    """
    sys.stderr.write(formatErrorMsg(funcname, exc))
    sys.exit(errorvalue)


def errorRaise(funcname, exc):
    """Reraises the exeption.

    Args:
        funcname: str function name where the error occurred
        exc: Exception

    Raises:
        exc: Exception
    """
    sys.stderr.write(formatErrorMsg(funcname, exc))
    raise (exc)


def errorNotify(funcname, exc):
    """Displays the exception text.

    Args:
        funcname: str function name where the error occurred
        exc: Exception
    """
    sys.stderr.write(formatErrorMsg(funcname, exc))
