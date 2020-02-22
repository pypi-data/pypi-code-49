import ipaddress

def ascii_bytes(value):
    return bytes(value, encoding='ascii')

def ascii_str(value):
    return str(value, encoding='ascii')

def ip_int_to_ascii(ip_int):
    return str(ipaddress.ip_address(ip_int))

def ip_ascii_to_int(ip):
    return int(ipaddress.ip_address(ip))

