#!/usr/bin/env python3
# coding: utf-8


"""
    This module only contains the defintion of getNbByte.

    This method returns the number of byte needed to write a value with
    hexadecimal digits.
"""


from typing import Union


def getNbByte(number: Union[int, str, bytes]) -> int:
    """
        This methods returns the number of byte needed to write a value with
        hexadecimal digits.

        This method change the number in a bytes object and return the number
        of byte used.

        :param number:  The number we want to know the number of byte needed.
        :type number:   Union[int, str, bytes]
        :return:        The number of byte needed.
        :rtype:         int
	"""
    if type(number) == int:					# If number is an int-object, we use the format function to get the associated str-object with hexadecimal digits.
        number = format(number, "x")
    if type(number) == str:					# If number is a str-object, we use the fromhex method from bytes class to get the bytes-object coded in hexadecimal.
        if(len(number) % 2 == 1):				# If the number of digits is odd, we must add ourself a 0 digit at the beginning to have an even number of digit for the bytes.fromhex() method.
            number = "0" + number
        number = bytes.fromhex(number)
    if type(number) != bytes:				# We check that number is a bytes-object.
        raise TypeError("number must be an 'int', a 'bytes' encode with hexadecimal value or a 'str' with hexadecimal digits. number: " + str(number))
    return(len(number))						# The function len() gives us the number of bytes.


if __name__ == "__main__":
    try:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        pass
