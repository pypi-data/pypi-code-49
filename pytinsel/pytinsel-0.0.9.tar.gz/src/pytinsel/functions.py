import dis
from types import CodeType, FunctionType
from functools import wraps


def hof(func):

    def wrapper(*args, **kwargs):

        _SF = dis.opmap['STORE_FAST'].to_bytes(1, byteorder='little')
        _LC = dis.opmap['LOAD_CONST'].to_bytes(1, byteorder='little')
        _LF = dis.opmap['LOAD_FAST'].to_bytes(1, byteorder='little')
        _PJIF = dis.opmap['POP_JUMP_IF_FALSE'].to_bytes(1, byteorder='little')
        _PJIT = dis.opmap['POP_JUMP_IF_TRUE'].to_bytes(1, byteorder='little')

        byte_code = func.__code__.co_code
        _byte_code = b''

        for i in range(0, len(byte_code), 2):
            ith_byte = bytes([byte_code[i]])
            iplus1th_byte = bytes([byte_code[i + 1]])
            if ith_byte == _LC:
                _byte_code = _byte_code + ith_byte + bytes([int.from_bytes(iplus1th_byte, 'little') + 1])
            else:
                _byte_code = _byte_code + ith_byte + iplus1th_byte

        _co_consts = ((func.__code__.co_consts[0],)) + (args[0],)
        _new_co_consts = _co_consts + func.__code__.co_consts[1:]
        if len(func.__code__.co_consts) > 1:
            _co_consts = _co_consts + func.__code__.co_consts[1:]
        _co_varnames = func.__code__.co_varnames[1:] + ('self',)

        const_load = dis.opmap['LOAD_CONST'].to_bytes(1, byteorder='little') + b'\x01'
        const_store = dis.opmap['STORE_FAST'].to_bytes(1, byteorder='little') + b'\x02'
        __byte_code = const_load + const_store + _byte_code[:]
        ___byte_code = b''
        _is_1st_param_stored = False
        for i in range(0, len(__byte_code), 2):
            ith_byte = bytes([__byte_code[i]])
            iplus1th_byte = bytes([__byte_code[i + 1]])

            if ith_byte == _LF and iplus1th_byte in [b'\x00']:
                ___byte_code = ___byte_code + ith_byte + bytes([len(func.__code__.co_varnames) - 1])
            elif ith_byte == _SF and iplus1th_byte in [b'\x02'] and not _is_1st_param_stored:
                ___byte_code = ___byte_code + ith_byte + bytes([len(func.__code__.co_varnames) - 1])
                _is_1st_param_stored = True
            elif ith_byte == _SF:
                ___byte_code = ___byte_code + ith_byte + bytes([int.from_bytes(iplus1th_byte, 'little') - 1])
            elif ith_byte == _LF:
                ___byte_code = ___byte_code + ith_byte + bytes([int.from_bytes(iplus1th_byte, 'little') - 1])
            elif ith_byte == _PJIF:
                ___byte_code = ___byte_code + ith_byte + bytes([int.from_bytes(iplus1th_byte, 'little') + 4])
            elif ith_byte == _PJIT:
                ___byte_code = ___byte_code + ith_byte + bytes([int.from_bytes(iplus1th_byte, 'little') + 6])
            else:
                ___byte_code = ___byte_code + ith_byte + iplus1th_byte

        _func_code = CodeType(
            func.__code__.co_argcount - 1,
            func.__code__.co_kwonlyargcount,
            func.__code__.co_nlocals,
            func.__code__.co_stacksize,
            func.__code__.co_flags,
            ___byte_code,
            _co_consts,
            func.__code__.co_names,
            _co_varnames,
            func.__code__.co_filename,
            func.__code__.co_name,
            func.__code__.co_firstlineno,
            func.__code__.co_lnotab,
            func.__code__.co_freevars,
            func.__code__.co_cellvars
        )
        return FunctionType(_func_code, func.__globals__)
    return wrapper
