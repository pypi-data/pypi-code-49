# default lib imports
import socket
import threading
import json
import logging

# module imports
from .ReservedBytes import ReservedBytes
from .Packet import Packet


# Client class
class Client:
    # an exception raised when the client ends the connection, useful so the manager knows if a given client has
    # ended communications at any point
    class ConnectionEnd(Exception):
        pass

    # an exception raised when the client fails to get the client's info
    class InvalidInfo(Exception):
        pass

    def __init__(self, connection: socket, address: tuple, logging_level: int = logging.DEBUG):
        # client logger
        self.logger = logging.getLogger("UNKNOWN ID - IP: " + str(address[0]))
        self.logger_level = logging.DEBUG
        self.logger.setLevel(self.logger_level)

        # a lock preventing multiple threads from using the __connection at the same time
        self.connection_lock = threading.RLock()

        # socket object representing the connection between the client and the server
        self.__connection = connection

        # IP address of the client
        self.address = address

        # the uuid of the client
        self.uuid = None

        # the type of client the client is
        self.type = None

        # the bonus data which varies by client
        self.data = None

    # end the connection with the client
    def end(self, raise_exception: bool = False):
        # logging output
        self.logger.info("Ending connection.")

        try:
            # tell the client the connection is ending
            self.__connection.send(Packet(ReservedBytes.END_CONNECTION.value))

        finally:
            # shutdown the socket connection
            self.__connection.shutdown(socket.SHUT_RDWR)

            # close the socket connection
            self.__connection.close()

            if raise_exception:
                # raise a connection end error
                raise self.ConnectionEnd

    # send data to the client
    def send(self, packet: Packet):
        # init the lock
        with self.connection_lock:
            try:
                # send the string to to the client
                return self.__connection.send(packet.bytes)

            # in case of a socket error return None
            except socket.error:
                return None

    # receives data from a client (optional timeout)
    def recv(self, timeout: int = 15):
        # init the lock
        with self.connection_lock:
            # if a timeout is specified then set the timeout
            if timeout is not None:
                self.__connection.settimeout(timeout)

            # blank response
            response = None

            # put the recv in a try catch to check for a timeout
            try:
                # read data from buffer
                response = self.__connection.recv(4096)

            # in case of socket timeout
            except socket.timeout:
                return None

            # in case of another socket error
            except socket.error:
                return None

            finally:
                # return data
                return response

    # gets the client's info (returns None if successful)
    def get_data(self, timeout: int = 15):
        # logging output
        self.logger.info("(Client) Sending getinfo request.")

        # init the lock
        with self.connection_lock:
            # ask the client for their data if the send fails then end the connection
            if self.send(Packet(ReservedBytes.GET_DATA.value)) is None:
                self.end(True)

            # await client response containing their info
            response = self.recv(timeout=timeout)

            # if the response returned None because of an error end the connection
            if response is None:
                self.end(True)

            # split the response using "##" as the delimiter
            response = response.decode().split("##")

            print(response)

            # if the response is not 3 pieces of data raise an error
            if len(response) != 3:
                # logging output
                self.logger.info("(Client) Getinfo response invalid formatting.")

                raise self.InvalidInfo

            # get the clients UUID
            client_uuid = response[0]

            # update the client's logger info
            self.logger = logging.getLogger(client_uuid)
            self.logger.setLevel(self.logger_level)

            # check if the UUID is 36 char long to only allow proper UUIDs
            if len(client_uuid) != 36:
                # logging output
                self.logger.info("(Client) UUID invalid length, should be 36 characters.")

                raise self.InvalidInfo

            # get the client's type
            client_type = response[1]

            # convert the data from a JSON string to a python dict
            try:
                # get the clients JSON data and convert it to a dict
                client_data = json.loads(response[2])
            except json.JSONDecodeError:
                # logging output
                self.logger.info("(Client) Failed to parse JSON.")

                # in case the JSON data provided is formatted incorrectly
                raise self.InvalidInfo

            print("STORING RETRIEVED DATA")
            # store the retrieved data
            self.uuid = client_uuid
            self.type = client_type
            self.data = client_data
            return None

    # check the heartbeat of the client returns None if client has a heartbeat
    def heartbeat(self, heartbeat_timeout: int = 15):
        # logging output
        self.logger.info("(Client) Sending heartbeat request.")

        # init the lock
        with self.connection_lock:
            # send the heartbeat command if it fails end the connection
            if self.send(Packet(ReservedBytes.HEARTBEAT.value)) is None:
                self.end(True)

            # await a "beat" response or await timeout error
            beat = self.recv(timeout=heartbeat_timeout)

            # if the recv fails then end the client connection
            if beat is None:
                # logging output
                self.logger.info("(Client) Failed heartbeat check.")

                self.end(True)

            # if the client's response is not beat then return a incorrect response
            if beat == Packet(ReservedBytes.HEARTBEAT.value).bytes:
                # logging output
                self.logger.info("(Client) Passed heartbeat check.")

                # return the alive response
                return True
            else:
                # logging output
                self.logger.info("(Client) Failed heartbeat check.")

                # end the connection if the response is incorrect
                self.end(True)

    # client info as a dict
    def return_data(self):
        if self.data is not None:
            return {
                "uuid": self.uuid,
                "type": self.type,
                "data": self.data
            }
        else:
            return None
