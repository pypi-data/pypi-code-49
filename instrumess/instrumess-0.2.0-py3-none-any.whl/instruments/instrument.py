# -*- coding: utf-8 -*-
"""
Created on Tuesday 11-February-2020 at 15:56

@author: Rastko Pajković
"""

from abc import ABC, abstractmethod
import visa
import instrumess.utilities.validate as validate

class Instrument(ABC):
    """Class for all instrument drivers that requires suclasses to implement three basic methods:
    init
    close 
    reset

    """
    def __init__(self, address=None, name=None):
        """Initiate the instrument with the GPIB address and name"""
        self._address = address
        self._name = name
        self._rm = visa.ResourceManager()
        
    def __enter__(self):
        """Part of the 'with' environment, intializes the communication"""
        self.instr = self._rm.open_resource(self._address)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Part of the 'with' environment, closes the communication"""
        self.instr.control_ren(0)  # go to local
        self.instr.close()         # close visa connection

    def write(self, command):
        """Write a command to the instruments"""
        self.instr.write(command)

    def read(self):
        """Read a command to the instruments"""
        return self.instr.read()

    def query(self, command):
        """Query a command to the instruments"""
        return self.instr.query(command)

    @staticmethod
    def prop(set_command, docs,
             in_range=None,
             in_set=None,
             name='Value',
             ):
        """Property generator with in_range/set validation
        
        Parameters
        ----------
        set_command : STR
            Command to communicate with the instrument, example: ':OUTP {:s}'
        docs : STR
            Documentation string for property setter
        in_range : list, tuple
            (min, max) range validator for the property values
        in_set : list, dict
            [allowed_values] discrete validator for the property values
        
        Returns
        -------
        Property
            Property of the Instrument class
        """
        # check that function arguments have been supplied properly
        conditions = 0
        if in_range is not None:
            conditions += 1
            condition = in_range
            check_validity = validate.in_range  # set validator function
            allowed_values = in_range
        if in_set is not None:
            conditions += 1
            condition = in_set
            check_validity = validate.in_set  # set validator function
            try:
                allowed_values = in_set.keys()
            except AttributeError:
                allowed_values = in_set
        if conditions != 1:
            raise ValueError('You can set either in_range or in_set, '
                             'not both or neither')

        def fget(self):
            if in_range is not None:
                print('{} takes values from {} to {}'.format(name,
                                                             min(in_range),
                                                             max(in_range)))
            if in_set is not None:
                print('{} must be set element: {}'.format(name, allowed_values))
            return allowed_values

        def fset(self, value):
            value = check_validity(value, condition, name)
            self.write(set_command.format(value))
            # print(value)

        # Add the specified document string to the getter
        fget.__doc__ = docs

        return property(fget, fset)

    @staticmethod
    def prop_2arg(set_command, docs,
                  in_range=None,
                  in_set=None,
                  name='Value'):
        """Property generator that takes 2 or more arguments for the set method
        
        Parameters
        ----------
        set_command : STR
            Command to communicate with the instrument, example: ':OUTP {:s}'
        docs : STR
            Documentation string for property setter
        in_range : list, tuple
            (min, max) range validator for the property values
        in_set : list, dict
            [allowed_values] discrete validator for the property values
        
        Returns
        -------
        Property
            Property of the Instrument class
        """
        # check that function arguments have been supplied properly
        conditions = 0
        if in_range is not None:
            conditions += 1
            condition = in_range
            check_validity = validate.in_range  # set validator function
            allowed_values = in_range
        if in_set is not None:
            conditions += 1
            condition = in_set
            check_validity = validate.in_set  # set validator function
            try:
                allowed_values = in_set.keys()
            except AttributeError:
                allowed_values = in_set
        if conditions != 1:
            raise ValueError('You can set either in_range or in_set, '
                             'not both or neither')

        def fget(self):
            if in_range is not None:
                print('{} takes values from {} to {}'.format(name,
                                                             min(in_range),
                                                             max(in_range)))
            if in_set is not None:
                print('{} can be {}'.format(name, allowed_values))
            return allowed_values

        def fset(self, values):
            # in this version you expect iterable values!
            values=list(values)
            values[-1] = check_validity(values[-1], condition, name)
            # print(set_command.format(*values))
            self.write(set_command.format(*values))

        # Add the specified document string to the getter
        fget.__doc__ = docs

        return property(fget, fset)