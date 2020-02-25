#!/usr/bin/env python
"""
Classes for using pymavlink and mavutil from within a PyQt application
"""

from __future__   import print_function

from pymavlink    import mavutil
from argparse     import ArgumentParser
from builtins     import object
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QSocketNotifier

import time, sys, os

# To be addressed:
#   how to detach from QSocketNotifier
#   how to identify socket error conditions, since they happen in mavutil
#   how to convey the timestamps from the file (when reading a file)

class UqtMavFileRecvWorker(QObject):
    """Worker thread for reading from a file and emitting MAVLink messages as Qt Signals"""

    finished = pyqtSignal()

    def __init__(self, mavfile, rxMsgSignal, msg_types=None ):
        super(self.__class__, self).__init__()

        self.msg_types = msg_types
        self.mavfile = mavfile
        self.rxMsgSignal = rxMsgSignal

    @pyqtSlot()
    def worker(self):
        """This is the actual thread service loop"""
        self.running = True
        nRx = 0
        while self.running:
            try:
                msg = self.mavfile.recv_msg()
                if msg:
                    self.rxMsgSignal.emit(msg, time.time())
                    nRx += 1
                else:
                    break
            except Exception as error:
                print(f'{error}' )
                #self.running = False
                #break

        self.rxMsgSignal.emit(None, 0)
        self.finished.emit()

class UqtMavConn(object):
    '''
    Container for MAVLink connection objects provided by pymavlink and mavutil

    In mavutil, there is a class called mavfile. Several classes are derived
    from it:
       - mavudp
       - mavtcp
       - mavtcpin
       - mavserial
       - mavmcast
       - mavlogfile
       - mavchildexec

    mavfile *has* a mavlink, so all the mavfiles have a protocol object that is
    the exact same class. So mavutil.mavfile (a connection) has a mavlink.mavlink
    (a protocol - or rather a dialect, if you are familiar with mavlink)

    mavutil.mavlink_connection() is the factory for mavfiles.

    That's all pretty good, and not neccessary to improve upon. However, I
    want to eliminate some of the cut-and-paste I do when putting together
    apps, and also create a pattern for usage within Qt. So that's what this 
    is.

    So, UqtMavConn is an object that has a mavfile. It has methods for:

    - providing command line args so the client app can make those available
    - managing receive scheduling in the Qt environment

    Client is a Qt app with a UqtMavConn, and wants to receive in the Qt main loop
    via a signal. We will provide this service either via a worker thread or a
    QSocketNotifier, as dictated by the characteristics of the underlying mavfile.
    '''
    def __init__(self, cmdLineArgs=None, rxMsgSignal=None, recvMatch=None):
        self.mavfile = None

        self.rxMsgSignal = None
        self.rxMsgSignal = rxMsgSignal
        self.recvMatch = recvMatch
        self.notifier = None

        portStr = None
        dialectStr = None
        baud = None
        serial = False
        if cmdLineArgs:
            if cmdLineArgs.mavlink_version:
                # mavutil reads os.environ instead of taking args for some things
                if cmdLineArgs.mavlink_version == '1.0':
                    del(os.environ['MAVLINK20'])
                elif cmdLineArgs.mavlink_version == '2.0':
                    os.environ['MAVLINK20'] = '1'

            if cmdLineArgs.mavlink_dialect:
                dialectStr = cmdLineArgs.mavlink_dialect

            if cmdLineArgs.mavlink_port:
                portStr = cmdLineArgs.mavlink_port
                if 'serial:' in portStr:
                    serial = True
                    portStr = portStr[7:]
                    commaIx = portStr.find(',') 
                    if commaIx > 0:
                        baudStr = portStr[commaIx+1:]
                        baud = int(baudStr)
                        portStr = portStr[:commaIx]
                elif 'file:' in portStr:
                    portStr = portStr[5:]

        if portStr:
            if dialectStr:
                os.environ['MAVLINK_DIALECT'] = dialectStr
            
            try:
                # create a mavlink connection
                if serial and baud:
                    self.mavfile = mavutil.mavlink_connection(portStr, baud=baud, dialect=dialectStr )
                else:
                    self.mavfile = mavutil.mavlink_connection(portStr, dialect=dialectStr )
            except IOError:
                pass

        if self.mavfile:
            # save self.mavfile.mav as self.mavlink so users can do:
            #  mavConn = UqtMavConn(args)
            #  mavConn.mavlink.arbitrary_mavlink_method()
            self.mavlink = self.mavfile.mav
            print ( "MAVLink instantiation successful" )

            # Set up receive handling
            self.register_qt_recv_signal(self.rxMsgSignal, recvMatch=self.recvMatch)

    def register_qt_recv_signal(self, rxMsgSignal, recvMatch=None):
        """The client is a Qt app, and wants to receive the messages specified in recvMatch
         via the rxMsgSignal
        """
        self.rxMsgSignal = rxMsgSignal
        self.recvMatch = recvMatch

        if self.mavfile:
            if isinstance(self.mavfile, mavutil.mavmmaplog):
                self.thread = QThread()
                self.recvWorker = UqtMavFileRecvWorker(self.mavfile, self.rxMsgSignal, self.recvMatch)
                self.recvWorker.moveToThread(self.thread)
                self.recvWorker.finished.connect(self.thread.quit)                
                self.thread.started.connect(self.recvWorker.worker)
                self.thread.start()

            elif type(self.mavfile) in [ mavutil.mavserial ]:
                fd = self.get_file_descriptor()
                if fd >= 0:
                    self.notifier = QSocketNotifier(fd, QSocketNotifier.Read)
                    self.notifier.activated.connect(self.can_read)

            elif type(self.mavfile) in [ mavutil.mavudp, mavutil.mavtcp, mavutil.mavtcpin,
                                         mavutil.mavmcast, mavutil.mavlogfile, mavutil.mavlogfile ]:
                fd = self.get_file_descriptor()
                if fd:
                    self.notifier = QSocketNotifier(fd.fileno(), QSocketNotifier.Read)
                    self.notifier.activated.connect(self.can_read)
            elif isinstance(self.mavfile, mavutil.mavchildexec):
                pass

    def can_read(self):
        try:
            msg = self.mavfile.recv_msg()
            if msg:
                self.rxMsgSignal.emit(msg, time.time())
            else:
                self.rxMsgSignal.emit(None, 0)

        except Exception as error:
            print(f'{__name__}: {error}' )
            self.rxMsgSignal.emit(None, 0)

    def get_file_descriptor(self):
        '''
        return the file descriptor of the mavutil.mavfile for use in select()
        '''
        fileDescriptor = -1
        if self.mavfile:
            if isinstance(self.mavfile, mavutil.mavudp):
                fileDescriptor = self.mavfile.port
            elif isinstance(self.mavfile, mavutil.mavtcp):
                fileDescriptor = self.mavfile.port
            elif isinstance(self.mavfile, mavutil.mavtcpin):
                fileDescriptor = self.mavfile.port
            elif isinstance(self.mavfile, mavutil.mavserial):
                fileDescriptor = self.mavfile.port.fileno()
            elif isinstance(self.mavfile, mavutil.mavmcast):
                fileDescriptor = self.mavfile.port
            elif isinstance(self.mavfile, mavutil.mavlogfile):
                fileDescriptor = self.mavfile.port
            elif isinstance(self.mavfile, mavutil.mavchildexec):
                fileDescriptor = self.mavfile.port

        return fileDescriptor

    @staticmethod
    def make_args():
        '''
        Return an args to be used as 'parent' in another ArgumentParser
        These args are for UqtMavConn to use
        '''
        mavArgParser = ArgumentParser(add_help=False)

        '''
        TBD: the mavlink-port arg needs to support everything (?)that mavutil.mavlink_connection() supports
        def mavlink_connection(device, baud=115200, source_system=255, source_component=0,
                               planner_format=None, write=False, append=False,
                               robust_parsing=True, notimestamps=False, input=True,
                               dialect=None, autoreconnect=False, zero_time_base=False,
                               retries=3, use_native=default_native,
                               force_connected=False, progress_callback=None):
        '''

        help = 'serial:DEV[,BAUD] | udp:IP:PORT | tcp:IP:PORT | file:FILE | auto.\
                Example: --mavlink-port serial:/dev/ttyUSB0,9600'
        mavArgParser.add_argument("--mavlink-port", metavar='PORT', help=help)

        mavArgParser.add_argument("--mavlink-dialect", metavar='DIALECT',
                                   help='Example: --mavlink-dialect standard')

        mavArgParser.add_argument("--mavlink-version", metavar='VERSION',
                                   help='Example: --mavlink-version 2.0')
        return mavArgParser

# Test Code
def main():

    mavArgParser = UqtMavConn.make_args()
    
    parser = ArgumentParser(parents=[mavArgParser])
    parser.add_argument('-x', '--test', help='Test Argument placeholder', default='Test')
    parsedArgs,unparsedArgs = parser.parse_known_args()

    conn = UqtMavConn(cmdLineArgs=parsedArgs)
    if conn:
        nMessages = 0
        while True:
            m = conn.mavfile.recv_match()

            # If there's no match, it means we're done processing the log.
            if m is None:
                break

            # Ignore any failed messages
            if m.get_type() == 'BAD_DATA':
                continue
            nMessages += 1

        print ( "RX {n} messages".format(n=nMessages))

if __name__ == '__main__':
    main()
