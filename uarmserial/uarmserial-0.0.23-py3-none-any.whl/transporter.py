import socket
import sys
import threading
import time

class Transport:
    def __init__(self):
        self.lock = threading.Lock()
        self.sock = None
        self.serverAddr = None
        self.clientAddr = None
        self.clientSock = None

    def init(self, port, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverAddr = (addr, int(port))

        try:
            self.sock.bind(self.serverAddr)
        except socket.error:
            print("[uarm_serial] - Failed to bind socket.")
            raise

        self.sock.listen(1)

        try:
            self.clientSock, self.clientAddr = self.sock.accept()
        except socket.error:
            print("[uarm_serial] - Failed to accept socket connection.")
            raise

    def receive(self):
        return self.clientSock.recv(4096).decode()

    def send(self, message):
        self.lock.acquire()

        try:
            message = message + "\n"
            self.clientSock.sendall(message.encode())
        except IOError:
            print("[uarm_serial] - Socket transmission failed.")
        finally:
            self.lock.release()

    def close(self):
        self.lock.acquire()

        try:
            self.sock.close()
            self.clientSock.close()
        except socket.error:
            print("[uarm_serial] - Failed to close socket.")
            raise
        finally:
            self.lock.release()
