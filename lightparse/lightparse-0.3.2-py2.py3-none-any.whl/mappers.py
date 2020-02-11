"""
Helpers and stock mappers to use with lightparse Parser.

rename decorator to rename the mapper function and have it show in the help
with better name.

Some ready made mappers to show how to write more of them. As of writing this,
only one exists, file_exists to check file existence.

In addition, any other converting function can be used as a mapper as long as
it throws ValueError on invalid string input and potentially converts the
string to another value. Remember to return the input value back if the mapper
is only validating input. This includes functions such as: int, float and long.
"""
import os


def rename(newname):
    """
    Decorator to rename mapping functions to have a different name.
    """
    def decorator(func):
        func.__name__ = newname
        return func
    return decorator


@rename("file")
def file_exists(value):
    """
    Validates that the file exists.
    """
    if not os.path.exists(value):
        raise ValueError("No such file or directory: {}".format(value))
    return value
