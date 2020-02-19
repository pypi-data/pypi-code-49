#!/usr/bin/env python3
# coding: utf-8

import sys
import traceback

_recvsize = 2 ** 24


def _receive_lines(sock, size=_recvsize):
    while True:
        lines = sock.recv(size).splitlines(keepends=True)
        if not lines:
            break
        for line in lines:
            yield line


def receive_lines(sock, size=_recvsize):
    partial_line = b''
    for line in _receive_lines(sock, size):
        if line.endswith(b'\n'):
            yield partial_line + line
            partial_line = b''
        else:
            partial_line = line
    if partial_line:
        yield partial_line + b'\n'


def split(binstr):
    binstr = binstr.strip()
    parts = binstr.split(maxsplit=1)
    if len(parts) == 2:
        return parts
    return binstr, b''


def asbytes(x):
    x = x or b''
    return x if isinstance(x, bytes) else str(x).encode('utf-8')


def printerr(e):
    print(e.__class__.__name__, e, file=sys.stderr)


def netcat(host, port, content, size=_recvsize):
    # https://stackoverflow.com/a/1909355/2925169
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.sendall(content)
        sock.shutdown(socket.SHUT_WR)
        return sock.recv(size)
    except Exception:
        traceback.print_exc()
    finally:
        sock.close()


def runserver(func, host, port):
    import gevent
    from gevent import socket
    server_sock = socket.socket()
    server_sock.bind((host, port))
    server_sock.listen(500)
    while True:
        sock, _ = server_sock.accept()
        gevent.spawn(func, sock)


class ServerBase(object):
    recvsize = _recvsize
    execute = staticmethod(lambda verb, data: b'')

    def handle(self, line):
        verb, payload = split(line)
        return asbytes(self.execute(verb, payload))

    def runserver(self, host='0.0.0.0', port=8333):
        return runserver(self.serve_client, host, port)

    def serve_client(self, sock):
        import socket
        try:
            req = sock.recv(self.recvsize)
            resp = self.handle(req)
            sock.send(resp)
            sock.shutdown(socket.SHUT_WR)
        except Exception:
            traceback.print_exc()
        finally:
            sock.close()


class PipedServerBase(ServerBase):
    def respond(self, sock, ql):
        try:
            resp = self.handle(ql) + b'\n'
            sock.send(resp)
        except Exception:
            traceback.print_exc()

    def serve_client(self, sock):
        with sock:
            print('sock', sock)
            for ql in receive_lines(sock):
                print('ql', ql)
                self.respond(sock, ql)
