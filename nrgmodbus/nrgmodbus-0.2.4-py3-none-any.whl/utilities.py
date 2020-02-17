import struct


def combine_registers(registers):
    """ combine two registers for float output

    for modbus data that is two registers in length

    parameters
    ----------
        registers : list
            a client.read_holding_registers register response
    
    returns
    -------
    float
    """        
    raw = struct.pack('>HH', registers[0], registers[1])

    return struct.unpack('>f', raw)[0]


def combine_u32_registers(registers):
    """ combine two registers for 32-bit int output """
    raw = struct.pack('>HH', registers[0], registers[1])

    return struct.unpack('>I', raw)[0]    


def convert_hex_to_float(value):

    raw = struct.pack('>H', value)

    return struct.unpack('>I', raw)[0]