# -*- coding: utf-8 -*-

import sys
import nwae.broadcaster.config.Config as cf
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket, WebSocketError
import threading
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
import queue
from nwae.broadcaster.AggregateServer import AggregateServer
from nwae.broadcaster.BroadcastThread import BroadcastThread

#
# Feed aggregated by AggregateServer will be re-broadcasted by Broadcast Server
#
def Start_Broadcast_Server():
    obj = BroadcastServer()
    return obj

#
# Rebroadcasts feed aggregated in AggregateServer
#
class BroadcastServer:

    DEFAULT_CONFIG_FILE = '/usr/local/git/nwae/nwae.broadcaster/app.data/config/broadcaster.cf'

    # This is a thread safe implementation, so no need to worry about multiple threads
    # https://docs.python.org/3/library/queue.html
    feed_queue = queue.Queue(
        maxsize = 10000
    )
    client_subscribers_list = []
    mutex_client_subscribers_list = threading.Lock()

    class AggregateServerThread(threading.Thread):
        def __init__(self, config):
            self.config = config
            super().__init__()
            self.stoprequest = threading.Event()
            return

        def run(self):
            AggregateServer(
                feed_queue = BroadcastServer.feed_queue,
                config = self.config
            ).run_aggregate_server()
            Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Chat Aggregator API started successfully.'
            )

    #
    # Startup Initialization. Read configurations from command line.
    # The first thing we do is to process command line parameters, account, port, etc.
    # This function should be called first thing at __init__()
    #
    def __init_command_line_parameters(self):
        configfile = None
        try:
            #
            # Run like '/usr/local/bin/python3.6 -m nwae.broadcaster.BroadcastServer configfile=... port=...'
            #
            # Default values
            command_line_params = {
                cf.Config.PARAM_CONFIGFILE: None,
                cf.Config.PARAM_PORT_BROADCASTER: None
            }
            args = sys.argv

            for arg in args:
                arg_split = arg.split('=')
                if len(arg_split) == 2:
                    param = arg_split[0].lower()
                    value = arg_split[1]
                    if param in list(command_line_params.keys()):
                        command_line_params[param] = value

            return command_line_params
        except Exception as ex:
            errmsg = str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)\
                     + ': Error reading app config file "' + str(configfile)\
                     + '". Exception message ' + str(ex)
            Log.critical(errmsg)
            raise Exception(errmsg)

    def __init__(self):
        cmdline_params = self.__init_command_line_parameters()
        self.config = cf.Config.get_cmdline_params_and_init_config_singleton(
            Derived_Class = cf.Config,
            default_config_file = BroadcastServer.DEFAULT_CONFIG_FILE
        )
        #
        # Overwrite config file port if on command line, port is specified
        #
        if cmdline_params[cf.Config.PARAM_PORT_BROADCASTER] is not None:
            Log.important(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Overwriting port in config file "'
                + str(self.config.get_config(param=cf.Config.PARAM_PORT_BROADCASTER))
                + '" with port specified on command line as "'
                + str(cmdline_params[cf.Config.PARAM_PORT_BROADCASTER]) + '".'
            )
            self.config.param_value[cf.Config.PARAM_PORT_BROADCASTER] = cmdline_params[cf.Config.PARAM_PORT_BROADCASTER]

        # For gunicorn to access, and will never change without a restart
        self.port = int(self.config.get_config(param=cf.Config.PARAM_PORT_BROADCASTER))
        self.host = '0.0.0.0'

        # Start Chat Aggregator in background
        BroadcastServer.AggregateServerThread(config=self.config).start()
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Aggregator Server starting in the background..'
        )

        # Broadcast Thread
        BroadcastThread(
            client_subscribers_list = BroadcastServer.client_subscribers_list,
            mutex_client_subscribers_list = BroadcastServer.mutex_client_subscribers_list,
            feed_queue = BroadcastServer.feed_queue
        ).start()
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Broadcast Thread starting in the background..'
        )

        return

    def run(self):
        Log.info(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Starting Broadcast Server on ' + str(self.host) + ':' + str(self.port)
        )
        server = WSGIServer(
            (self.host, self.port),
            BroadcastServer.ClientWsHandler,
            handler_class = WebSocketHandler
        )
        server.serve_forever()

    #
    # Created for each connection
    #
    @staticmethod
    def ClientWsHandler(
            environ,
            start_response
    ):
        path = environ["PATH_INFO"]
        Log.debug(
            str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Environ: ' + str(environ)
        )

        if path == "/livestream":
            try:
                remote_addr = environ['HTTP_X_REAL_IP']
            except Exception:
                Log.error(
                    str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': No key "HTTP_X_REAL_IP" in environ.'
                )
                try:
                    remote_addr = environ['HTTP_X_FORWARDED_FOR']
                except Exception:
                    Log.error(
                        str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                        + ': No key "HTTP_X_FORWARDED_FOR" in environ.'
                    )
                    remote_addr = environ['REMOTE_ADDR']

            remote_port = environ['REMOTE_PORT']
            Log.important(
                str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': New livestream connection from "' + str(remote_addr)
                + ':' + str(remote_port) + '". Full environ: ' + str(environ)
            )
            client_socket = environ['wsgi.websocket']
            if type(client_socket) is WebSocket:
                try:
                    BroadcastServer.mutex_client_subscribers_list.acquire()
                    subscriber = {
                        'socket': client_socket,
                        'remote_addr': remote_addr,
                        'remote_port': remote_port
                    }
                    BroadcastServer.client_subscribers_list.append(subscriber)
                    Log.important(
                        str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                        + ': Socket ' + str(remote_addr) + ':' + str(remote_port) + ' added to subscribers list.'
                    )
                except Exception as ex_add_client_socket:
                    Log.error(
                        str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                        + ': Error adding client socket ' + str(remote_addr) + ':' + str(remote_port)
                        + ' to subscribers list: ' + str(ex_add_client_socket)
                        + '. Closing socket.'
                    )
                    client_socket.close()
                    return
                finally:
                    BroadcastServer.mutex_client_subscribers_list.release()

                while True:
                    try:
                        message = client_socket.receive()
                        Log.info(
                            str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                            + ': Received: ' + str(message)
                        )
                        # TODO Do async handling here
                        if sys.version_info >= (3, 7, 0):
                            # asyncio.run(todo_handler())
                            pass
                        client_socket.send('Got your message ' + str(message))
                    except Exception as ex_socket:
                        Log.error(
                            str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                            + ': Error socket connection: ' + str(ex_socket)
                        )
                        break

                Log.important('Remote ' + str(remote_addr) + ':' + str(remote_port) + ' finished.')
            else:
                Log.error(
                    str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Wrong type, expecting WebSocket type, got "'
                    + str(type(client_socket)) + '" instead.'
                )
        else:
            Log.error(
                str(__name__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Wrong request path "' + str(path) + '"'
            )
            return 'Wrong request path "' + str(path) + '". Start Response "' + str(start_response) + '"'
            # return app(environ, start_response)


if __name__ == '__main__':
    # One time initialization applies to all modules
    Log.LOGLEVEL = Log.LOG_LEVEL_DEBUG_1
    print(str(__name__) + ': Using log file path "' + str(Log.LOGFILE))
    Log.DEBUG_PRINT_ALL_TO_SCREEN = True

    svr = Start_Broadcast_Server()
    svr.run()
