import openhtf.plugs as plugs
from openhtf.util import conf

import time

import serial
from serial.threaded import ReaderThread

import threading
from queue import Queue
from asyncio import Protocol

class ComportInterface(Protocol):
    """An interface to a comport.
    
    Allows reading and writing. A background thread reads any data that comes in 
    and those lines can be accessed using the `next_line` function.
    
    """

    def __init__(self, comport, baudrate=115200):
        self.comport = comport
        self.baudrate = baudrate

        self._serial = None
        self._reader = None
        self._line_buffer = ""
        self._read_lines = Queue()
        self._timeout_timer = None
        self._last_receive_time = None

        self.timeout = 0.5
        self.eol = "\n"

    def tearDown(self):
        """Tear down the plug instance."""
        self.close()

    def close(self):
        if self._reader is not None and self._serial.is_open:
            self._reader.close()
            self._reader = None

    def open(self, _serial=None):
        self.close()
        if not _serial:
            _serial = serial.Serial(self.comport, self.baudrate, timeout=self.timeout)
        self._serial = _serial
        self._reader = ReaderThread(self._serial, lambda: self)
        self._reader.start()

    def write(self, string):
        """Write the string into the comport."""
        return self._reader.write(string.encode('utf8'))

    def data_received(self, data):
        if self._timeout_timer is not None:
            self._timeout_timer.cancel()
        
        force_clear = False
        if self.check_receive_delta() and data is None and self._line_buffer:
            force_clear = True

        data_to_queue = None

        if not data:
            data = b''

        string = data.decode('utf8')
        if force_clear or string.endswith(self.eol) or (self._line_buffer + string).endswith(self.eol):
            data_to_queue = self._line_buffer + string
            self._line_buffer = ""
        else:
            self._line_buffer += string
        
        self._timeout_timer = threading.Timer(self.timeout, self.no_data_received)
        self._timeout_timer.start()

        if data_to_queue:
            self._read_lines.put(data_to_queue)

    def no_data_received(self):
        return self.data_received(None)

    def check_receive_delta(self):
        if self._last_receive_time:
            delta = time.time() - self._last_receive_time
        else:
            delta = 0

        self._last_receive_time = time.time()

        return delta > self.timeout

    def next_line(self, timeout=10):
        """ Waits up to timeout seconds and return the next line available in the buffer.
        """
        return self._read_lines.get(timeout=timeout)

    def eof_received(self):
        pass

def declare_comport_plug(comport_conf_name, comport_conf_baudrate=None):
    """Creates a new plug class that will retrieve the comport name and baudrate (optionaly) from the openhtf conf.
    
    **Parameters:**
    
    * **comport_conf_name** - The name of the conf value that holds the comport name.
    * **comport_conf_baudrate** - (optional) The name of the conf value that holds the comport baudrate.
    
    **Returns:**
    
    A class that inherits from OpenHTF BasePlug and ComportInterface. This returned class can be used
    as a plug to feed into an OpenHTF test.
    
    """
    conf.declare(comport_conf_name, description='Declared comport accessor name')

    if comport_conf_baudrate is not None:
        conf.declare(comport_conf_baudrate, description='Declared comport baudrate')

    class ComportPlug(ComportInterface, plugs.BasePlug):
        def __init__(self):
            if comport_conf_baudrate is None:
                baudrate = 115200
            else:
                baudrate = conf[comport_conf_baudrate]

            super(ComportPlug, self).__init__(conf[comport_conf_name], baudrate)

    return ComportPlug
