"""
This module prints a simple greeting message.
"""
class Hello(object):
    """
    Return a greeting message
    """
    def __init__(self, msg="Hello World!"):
        """Initialise the variables for the object"""
        self.message = msg

    def __str__(self):
        """Convert the output of the class to a string and return it """
        return self.message

H1 = Hello("Hello World!")
print(H1)

H2 = Hello("Goodbye World!")
print(H2)
