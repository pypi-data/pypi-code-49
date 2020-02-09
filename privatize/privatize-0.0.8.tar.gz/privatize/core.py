"""
core.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from typelike import Anything, infer_type, Undefined
from os import urandom
from warnings import warn


# noinspection PyMethodParameters,PyMethodMayBeStatic,PyProtectedMember
class _Privatize:
    # Initialize instance of _Privatize
    def __init__(self, private_variable=None, dtype=None, immutable=False):
        """
        Initialize instance of _Privatize

        Parameters
        ----------
        private_variable : str
            Name of private variable
        dtype : str or object
            (Optional) Enforce that `private_variable` is of type `dtype`
        immutable : bool
            Can you change the value of the private variable multiple times? (Default: False)
        """

        # Save the private variable name
        if isinstance(private_variable, str):
            if private_variable[0] != '_':
                warn('private variable should start with underscore')
        else:
            private_variable = self._name_private_variable()
        self.private_variable = private_variable

        # Set the data type
        self.dtype = infer_type(dtype, itemize=True)

        # Should the class only be initialized once?
        self.immutable = immutable

        # Logical booleans for sanity
        self.is_first_run = True

    # Does the private variable exist?
    def _does_private_variable_exist(self, parent):
        """
        Does the parent already have the private variable named?

        Parameters
        ----------
        parent : object
            Parent object

        Returns
        -------
        bool
            Whether or not the parent has the private variable
        """

        return hasattr(parent, self.private_variable)

    # Name the private variable randomly
    def _name_private_variable(self):
        """
        Name the private variable randomly
        """

        return '_' + urandom(3).hex()

    # Rename the private variable
    def _rename_private_variable(self, parent):
        """
        Rename the private variable, usually because the private variable already exists in the parent

        Parameters
        ----------
        parent : object
        """

        # Pick a random name; if it's not in parent, we're good
        while True:
            self.private_variable = self._name_private_variable()
            if not self._does_private_variable_exist(parent):
                break

    # Get the stored value
    def get_value(self, parent):
        """
        Get value of private variable from parent

        Parameters
        ----------
        parent : object
            Parent object

        Returns
        -------
        Anything
            Value of private variable in parent
        """

        # If the private variable has never been set, we have a problem
        if self.is_first_run:
            raise ReferenceError('variable should be set before retrieved')

        # Return private variable to user
        return getattr(parent, self.private_variable, Undefined)

    # Store the value
    def set_value(self, parent, value):
        """
        Set the private variable for the parent

        Parameters
        ----------
        parent : object
            Parent object
        value : Anything
        """
        # If this is the first run, and the variable already exists, give the variable a new name
        if self.is_first_run and self._does_private_variable_exist(parent):
            self._rename_private_variable(parent)

        # Should the value only be set once?
        if self.immutable and self._does_private_variable_exist(parent) and self.get_value(parent) is not Undefined:
            raise AttributeError('can only be set at class initialization')

        # If self.dtype is set, check explicitly that the new value matches that type
        if self.dtype is not None and not isinstance(value, self.dtype):
            raise AttributeError('must be {}'.format(self.dtype))

        # Set the new value
        setattr(parent, self.private_variable, value)
        self.is_first_run = False


# Wrapper function to create _Privatize instance
def privatize(private_variable=None, dtype=None, immutable=False):
    """
    Add a private variable to a parent class

    Rules can be imposed on this private variable, for instance, that only certain data types are allowed,
    or that the private variable is immutable

    Parameters
    ----------
    private_variable : str
        Name of new private variable
    dtype : str or types or tuple of types
        If not None, the variable must be of this type
    immutable : bool
        Should the value be set only on class initialization?

    Returns
    -------
    property
        Instance of built-in :func:`~property` object
    """

    # Initialize _Privatize instance
    obj = _Privatize(private_variable=private_variable, dtype=dtype, immutable=immutable)

    # Return property
    return property(obj.get_value, obj.set_value)
