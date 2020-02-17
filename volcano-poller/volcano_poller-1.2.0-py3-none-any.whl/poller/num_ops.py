
# Raises ValueError
def bcd_to_int(bcd: int) -> int:
    assert isinstance(bcd, int), bcd
    
    lo = bcd & 0x0f
    hi = (bcd >> 4) & 0x0f

    if lo > 9 or hi > 9:
        raise ValueError('Value 0x{:x} is not a valid BCD'.format(bcd))

    return 10 * hi + lo

def make_word(high_byte: int, low_byte: int) -> int:
    assert isinstance(high_byte, int) and (0 <= high_byte <= 0xff), high_byte
    assert isinstance(low_byte, int) and 0 <= low_byte <= 0xff, low_byte
    
    return (high_byte << 8) | low_byte
    

def hi_byte(val: int) -> int:
    assert isinstance(val, int), val
    return (val >> 8) & 0xff


def lo_byte(val: int) -> int:
    assert isinstance(val, int), val
    return val & 0xff
    