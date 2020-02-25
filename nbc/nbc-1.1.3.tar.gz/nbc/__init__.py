"""
Number Base Converter by v01d
"""


from string import digits, ascii_uppercase


SYMBOLS = digits + ascii_uppercase


def convert(number: str, to_base: int, from_base=10):
    """
    :param number: from_base whole number (as String) to convert
    :param to_base: New base [2; 36]
    :param from_base: Old base [2; 36]
    :return: to_base number as a String

    >>> convert('15', 2)
    '1111'
    >>> convert('10F', to_base=8, from_base=16)
    '417'
    >>> convert('1', 30)
    '1'
    >>> convert('17', 16)
    '11'
    >>> convert('0', 2)
    '0'
    """

    if not (2 <= to_base <= 36 and 2 <= from_base <= 36):
        raise ValueError('2 <= to_base, from_base <= 36')

    number = int(number, from_base)
    if number < 0:
        raise ValueError('Number must be non-negative')

    if number == 0:
        return '0'

    mods = []
    while number > 0:
        mods.append(SYMBOLS[number % to_base])
        number //= to_base

    return ''.join(reversed(mods))


if __name__ == '__main__':
    from doctest import testmod
    testmod()
