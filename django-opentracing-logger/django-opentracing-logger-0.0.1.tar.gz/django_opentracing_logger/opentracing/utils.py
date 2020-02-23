"""
generate_id get_ip .etc
"""
import struct
import socket
import random


def generate_random_id():
    return random.getrandbits(63)


def get_local_ip():
    """
    TODO
    ip = _get_local_ip()
    try:
        res = sum([256 ** j * int(i) for j, i in enumerate(ip.split('.')[::-1])])
    except:
        res = -1062731519
    return res

    :return:
    """
    return -1062731519


def _get_local_ip():
    """Get the local network IP of this machine"""
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except IOError:
        ip = socket.gethostbyname('localhost')
    if ip.startswith('127.'):
        ip = _get_local_ip_by_interfaces()
        if ip is None:
            ip = _get_local_ip_by_socket()
    return ip


def _get_local_ip_by_socket():
    # Explanation : https://stackoverflow.com/questions/166506
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except IOError:
        ip = None
    finally:
        s.close()
    return ip


def _get_local_ip_by_interfaces():
    ip = None
    # Check eth0, eth1, eth2, en0, ...
    interfaces = [
        i + bytes(n) for i in (b'eth', b'en', b'wlan') for n in range(3)
    ]  # :(
    for interface in interfaces:
        try:
            ip = _interface_ip(interface)
            if ip is not None:
                break
        except IOError:
            pass
    return ip


def _interface_ip(interface):
    try:
        import fcntl
        """Determine the IP assigned to us by the given network interface."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(
            fcntl.ioctl(
                sock.fileno(), 0x8915, struct.pack('256s', interface[:15])
            )[20:24]
        )
    except ImportError:
        return None
    # Explanation:
    # http://stackoverflow.com/questions/11735821/python-get-localhost-ip
    # http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python


if __name__ == '__main__':
    print("local ip is ", get_local_ip())
    print("generated id  is ", generate_random_id())
