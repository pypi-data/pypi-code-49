from essentials import socket_ops
import threading, time


class Sender(object):

    def __init__(self, HOST, PORT, send_speed=1, on_data=None, on_close=None):
        super().__init__()
        self.speed = send_speed
        self.host = HOST
        self.port = PORT
        data = {}
        data['g_x'] = 0
        data['g_y'] = 0
        data['g_z'] = 0

        data['a_x'] = 0
        data['a_y'] = 0
        data['a_z'] = 0
        self.data = data
        self.on_close = on_close
        self.TYPE = "SENDER"
        self.on_data = on_data
        self.Socket = socket_ops.Socket_Connector(HOST, PORT, self.recv_data, self.on_close)
        threading.Thread(target=self._z__Sender__, daemon=True).start()

    
    def _z__Sender__(self):
        while self.Socket.running:
            self.Socket.send(self.data)
            time.sleep(2/self.speed)


    def recv_data(self, data):
        if self.on_data:
            self.on_data(data)
        else:
            pass

    def on_close(self):
        print("Connection was closed/reset.")
        if self.on_close:
            self.on_close()
        else:
            pass
        
class Retriever(object):

    def __init__(self, HOST, PORT, on_close=None):
        super().__init__()
        self.host = HOST
        self.port = PORT
        self.on_close = on_close
        self.TYPE = "RETRIEVER"
        data = {}
        data['g_x'] = 0
        data['g_y'] = 0
        data['g_z'] = 0

        data['a_x'] = 0
        data['a_y'] = 0
        data['a_z'] = 0
        self.data = data
        self.Socket = socket_ops.Socket_Server_Host(HOST, PORT, self.new_connection, self.recv_data, self.on_close)

    def new_connection(self, ids):
        print("New Remote Connection:", ids)

    def recv_data(self, data, sender):
        self.data = data

    def on_close(self):
        print("Connection was closed/reset.")
        if self.on_close:
            self.on_close()
        else:
            pass