import struct, socket, threading, json, os, pickle
from essentials import tokening

def SocketDownload(sock):
    """
        Helper function for Socket Classes
    """
    try:
        data = b""
        payload_size = struct.calcsize(">L")
        while True:
            while len(data) < payload_size:
                data += sock.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += sock.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            xData = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            return xData
    except:
        raise ConnectionError("Connection Error")

def SocketUpload(sock, data):
    """
        Helper function for Socket Classes
    """
    try:
        data = pickle.dumps(data, 0)
        size = len(data)
        sock.sendall(struct.pack(">L", size) + data)
    except:
        raise ConnectionError("Connection Error")

def HostServer(HOST, PORT, connections=5):
    """
        Helper function for Socket Classes
    """
    PORT = int(os.getenv('PORT', PORT))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(connections)
    return sock

def ConnectorSocket(HOST, PORT, timeout=5):
    """
        Helper function for Socket Classes
    """
    
    return  socket.create_connection((HOST, PORT), timeout)

class Socket_Server_Host:
    def __init__(self, HOST, PORT, on_connection_open, on_data_recv, on_connection_close=False, daemon=True, autorun=True, connections=5):
        """Host your own Socket server to allows connections to this computer.

        Parameters
        ----------
        HOST (:obj:`str`): Your hosting IP Address for this server.

        PORT (:obj:`int`): Which port you'd like to host this server on.

        on_connection_open (:obj:`def`): The function to call when you get a new connection.

        on_data_recv (:obj:`def`): The function to call when you receive data from a connection.

        on_connection_close (:obj:`def`, optional): The function to call when a connection is closed.

        daemon (:obj:`bool`, optional): If you'd like the server to close when the python file closes or is interrupted. 

        autorun (:obj:`bool`, optional): Will run the server on init.

        connections (:obj:`int`, optional): How many connections to allow at one time. To be used with autorun = True

        Attributes
        ----------

        running (:obj:`bool`): Is the server still running.

        connections (:obj:`dict`): Holds all connection threads.

        on_connection_open (:obj:`def`): Holds the function you specified to use, can be over written. NOTE: Overwriting this will not overwrite old connection values.

        on_connection_close (:obj:`def`): Holds the function you specified to use, can be over written. NOTE: Overwriting this will not overwrite old connection values.

        on_data_recv (:obj:`def`): Holds the function you specified to use, can be over written. NOTE: Overwriting this will not overwrite old connection values.

        """
        self.on_connection_open = on_connection_open
        self.on_connection_close = on_connection_close
        self.on_data_recv = on_data_recv
        self.HOST = HOST
        self.PORT = PORT
        self.connections = {}
        self.running = False
        if autorun:
            self.Run(connections, daemon)
        
    def Run(self, connections=5, daemon=True):
        """
        Will start the server on the specified host, port and listening count.

        This setup allows you to shutdown, change, and restart the server.

        Parameters
        ----------

        connections (:obj:`int`): How many connections to accept at one time


        :rtype: None

        """
        self.server = HostServer(self.HOST, self.PORT, connections)
        self.running = True
        self.broker = threading.Thread(target=self.ConnectionBroker, daemon=daemon)
        self.broker.start()

    def ConnectionBroker(self):
        """
        Server background task for accepting connections, you'll not need to use this.

        :rtype: None

        """
        while self.running:
            try:
                conn, addr = self.server.accept()
                conID = tokening.CreateToken(12, self.connections)
                connector = Socket_Server_Client(conn, addr, conID, self.on_data_recv, on_close=self.close_connection)
                self.connections[conID] = connector
                self.on_connection_open(connector)
            except Exception as e:
                self.running = False
                raise e
                
    def close_connection(self, connection):
        """
        Server background task for clearing connections and notifying the parent file, you'll not need to use this.

        :rtype: None

        """
        try:
            self.on_connection_close(connection)
        except:
            pass
        del self.connections[connection.conID]

    def Shutdown(self):
        """
        Shutdown the server and close all connections.

        :rtype: None

        """
        self.running = False
        for con in self.connections:
            self.connections[con].shutdown()
        self.connections = {}

    def CloseConnection(conID):
        """
        Shortcut to close a certain connection.

        Can also be used as Server.connections[conID].shutdown()

        :rtype: None

        """
        self.connections[conID].shutdown()

class Socket_Server_Client:

    def __init__(self, socket, addr, conID, on_data, on_close):
        """Host your own Socket server to allows connections to this computer.

        Parameters
        ----------
        socket (:obj:`socket connection`): opened socket to remote connection

        addr (:obj:`str`): address of the remote connection

        conID (:obj:`def`): The connection ID of the remote connection

        on_data (:obj:`def`): The function to call when you receive data from a connection.

        on_close (:obj:`def`, optional): The function to call when a connection is closed.

        Attributes
        ----------

        socket (:obj:`socket connection`): opened socket to remote connection

        addr (:obj:`str`): address of the remote connection

        conID (:obj:`def`): The connection ID of the remote connection

        on_data (:obj:`def`): The function to call when you receive data from a connection.

        on_close (:obj:`def`, optional): The function to call when a connection is closed.

        running (:obj:`bool`): Is the server still running.

        """
        self.socket = socket
        self.addr = addr
        self.conID = conID
        self.on_data = on_data
        self.on_close = on_close
        self.running = True
        threading.Thread(target=self.__data_rev__, daemon=True).start()

    def shutdown(self):
        """
        Shuts down this connection and removes any place it is still stored. Completes the on_close event.

        :rtype: None

        """

        try:
            self.on_close(self)
        except:
            pass
        self.running = False
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        

    def send(self, data):
        """
        Send data to the remote connection.

        :rtype: None

        """
        if self.running == False:
            raise ConnectionResetError("No Connection")

        try:
            SocketUpload(self.socket, data)
        except:
            self.shutdown()

    def __data_rev__(self):
        """
        Server background task for accepting data and run the on_data event, you'll not need to use this.

        :rtype: None

        """
        while self.running:
            try:
                data = SocketDownload(self.socket)
            except:
                self.shutdown()
                return
            self.on_data(data, self)

class Socket_Connector:

    def __init__(self, HOST, PORT, on_data_recv, on_connection_close, timeout=5):
        """Host your own Socket server to allows connections to this computer.

        Parameters
        ----------
        HOST (:obj:`str`): The hosting IP Address for the server.

        PORT (:obj:`int`): The port the server is using.

        on_data_recv (:obj:`def`): The function to call when you receive data from a connection.

        on_connection_close (:obj:`def`, optional): The function to call when a connection is closed.

        Attributes
        ----------

        running (:obj:`bool`): Is the server still running.

        on_connection_close (:obj:`def`): Holds the function you specified to use, can be over written.

        on_data_recv (:obj:`def`): Holds the function you specified to use, can be over written.

        """
        self.running = True
        self.HOST = HOST
        self.PORT = PORT
        self.on_connection_close = on_connection_close
        self.socket = ConnectorSocket(HOST, PORT, timeout)
        self.on_data_recv = on_data_recv
        threading.Thread(target=self.__data_rev__, daemon=True).start()

    def send(self, data):
        """
        Send data to the remote connection.

        :rtype: None

        """
        if self.running == False:
            raise ConnectionResetError("No Connection")
        try:
            SocketUpload(self.socket, data)
        except:
            self.shutdown()

    def shutdown(self):
        """
        Shuts down this connection. Completes the on_close event.

        :rtype: None

        """
        self.running = False
        self.on_connection_close(self)
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
    
    def __data_rev__(self):
        """
        Client background task for accepting data and run the on_data event, you'll not need to use this.

        :rtype: None

        """
        while self.running:
            try:
                data = SocketDownload(self.socket)
            except:
                self.shutdown()
                return
            self.on_data_recv(data)