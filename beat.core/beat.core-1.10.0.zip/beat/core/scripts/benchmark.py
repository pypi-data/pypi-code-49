from ..agent import MessageHandler
from ..dataformat import DataFormat
from ..data import DataSource
from ..inputs import RemoteInput
from ..inputs import Input
from ..inputs import InputGroup
from ..inputs import InputList
import numpy as np
import pkg_resources
import time
import zmq


prefix = pkg_resources.resource_filename(__name__, "../test/prefix")
print(prefix)


class CustomDataSource(DataSource):
    def __init__(self, nb_data_units, dataformat):
        self.nb_data_units = nb_data_units
        self.current = 0
        self.dataformat = dataformat
        self.file = open("benchmark.data", "rb")
        self.unpack = True

    def next(self):
        self.file.seek(0)
        packed = self.file.read()

        if self.unpack:
            data = self.dataformat.type()
            data.unpack(packed)
        else:
            data = packed

        result = (data, self.current, self.current)

        self.current += 1
        return result

    def hasMoreData(self):
        return self.current < self.nb_data_units

    def reset(self):
        self.current = 0
        self.unpack = True


def main():
    dataformat = DataFormat(prefix, "user/empty_1d_array_of_integers/1")

    data = dataformat.type(
        value=np.random.randint(100000, size=(1000000,), dtype=np.int32)
    )

    with open("benchmark.data", "wb") as f:
        f.write(data.pack())

    # -----------------------

    data_source = CustomDataSource(10000, dataformat)

    print("Nb Data units:       %d" % data_source.nb_data_units)

    t1 = time.time()

    while data_source.hasMoreData():
        data = data_source.next()

    t2 = time.time()

    print(
        "Datasource (unpack): %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()

    # -----------------------

    data_source.unpack = False

    t1 = time.time()

    while data_source.hasMoreData():
        data = data_source.next()

    t2 = time.time()

    print(
        "Datasource (packed): %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()

    # -----------------------

    input = Input("a", "user/empty_1d_array_of_integers/1", data_source)

    t1 = time.time()

    while input.hasMoreData():
        data = input.next()

    t2 = time.time()

    print(
        "Input (unpack):      %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()

    # -----------------------

    data_source.unpack = False

    t1 = time.time()

    while input.hasMoreData():
        data = input.next()

    t2 = time.time()

    print(
        "Input (packed):      %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()

    # -----------------------

    group = InputGroup("channel")
    group.add(input)

    input_list = InputList()
    input_list.add(group)

    server_context = zmq.Context()
    server_socket = server_context.socket(zmq.PAIR)
    address = "tcp://127.0.0.1"
    port = server_socket.bind_to_random_port(address)
    address += ":%d" % port

    message_handler = MessageHandler(input_list, server_context, server_socket)

    client_context = zmq.Context()
    client_socket = client_context.socket(zmq.PAIR)
    client_socket.connect(address)

    remote_input = RemoteInput("a", dataformat, client_socket)

    remote_group = InputGroup("channel", restricted_access=False)
    remote_group.add(remote_input)

    remote_input_list = InputList()
    remote_input_list.add(remote_group)

    message_handler.start()

    t1 = time.time()

    while remote_input.hasMoreData():
        data = remote_input.next()

    t2 = time.time()

    print(
        "Remote (unpack):     %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()

    # -----------------------

    data_source.unpack = False
    # message_handler.unpack = False

    t1 = time.time()

    while remote_input.hasMoreData():
        data = remote_input.next()

    t2 = time.time()

    print(
        "Remote (packed):     %.3fs (%.3fms/unit)"
        % (t2 - t1, (t2 - t1) * 1000.0 / data_source.nb_data_units)
    )

    data_source.reset()
