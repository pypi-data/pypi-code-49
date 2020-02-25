# -*- coding: utf-8 -*-

import flask
import nwae.broadcaster.config.Config as cf
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe

#
# This API allows all feed processes to send feed to one place
#
app = flask.Flask(__name__)

#
# Aggregates any feed, and puts them to queue, no processing on data.
# We don't run in multithread using gunicorn, as the API call should be
# very fast, as there is no processing involved, just forwarding.
#
class AggregateServer:

    def __init__(
            self,
            # Queue to write feed to
            feed_queue,
            # Config object
            config
    ):
        self.feed_queue = feed_queue
        self.config = config

        # For gunicorn to access, and will never change without a restart
        self.port = int(self.config.get_config(param=cf.Config.PARAM_PORT_AGGREGATOR))

        # Flask app
        self.app_chat_aggregator = app
        self.app_chat_aggregator.config['DEBUG'] = False

        self.__init_rest_urls()
        return

    def __init_rest_urls(self):
        @self.app_chat_aggregator.route('/cagg', methods=['POST','GET'])
        def chat_aggregator():
            if flask.request.method == 'POST':
                request_json = self.get_request_json(method='POST')
            else:
                request_json = flask.request.args.copy()

            Log.info(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Received ' + str(flask.request.method)
                + ' request url "' + str(flask.request.url) + '"'
                + ' from IP ' + str(flask.request.remote_addr)
                + ', JSON: ' + str(request_json)
            )
            try:
                self.feed_queue.put(request_json)
                Log.info(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Item ' + str(request_json) + ' put to broadcast queue.'
                )
            except Exception as ex_put:
                Log.error(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Error putting item to queue. Exception: ' + str(ex_put)
                    + '. Item: ' + str(request_json)
                )
            return 'Ok'

        @self.app_chat_aggregator.errorhandler(404)
        def page_not_found(e):
            Log.critical(str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                            + 'Resource [' + str(flask.request.url) + '] is not valid!')
            return "<h1>404</h1><p>The resource could not be found.</p>", 404

    def get_request_json(
            self,
            method = 'POST'
    ):
        req_json = {}
        if method == 'GET':
            for param_name in flask.request.args:
                req_json[param_name] = str(flask.request.args[param_name])
            return req_json
        else:
            return flask.request.json

    def get_param(self, param_name, method='GET'):
        if method == 'GET':
            if param_name in flask.request.args:
                return str(flask.request.args[param_name])
            else:
                return None
        else:
            try:
                val = flask.request.json[param_name]
                return val
            except Exception as ex:
                Log.critical(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': No param name "' + str(param_name) + '" in request.'
                )
                return None

    def run_aggregate_server(
            self,
            host='0.0.0.0'
    ):
        self.app_chat_aggregator.run(
            host     = host,
            port     = self.port
        )


if __name__ == '__main__':
    # One time initialization applies to all modules
    Log.LOGLEVEL = Log.LOG_LEVEL_DEBUG_1
    print(str(__name__) + ': Using log file path "' + str(Log.LOGFILE))
    Log.DEBUG_PRINT_ALL_TO_SCREEN = True

    config = cf.Config.get_cmdline_params_and_init_config_singleton(
        Derived_Class       = cf.Config,
        default_config_file = '/usr/local/git/nwae/nwae.broadcaster/app.data/config/local.cf'
    )

    import queue
    aggregate_server = AggregateServer(
        feed_queue = queue.Queue,
        config     = config
    )
    # If running from gunicorn, no need to run this (will be started by
    # gunicorn instead with host/port given to gunicorn on the command line)
    aggregate_server.run_aggregate_server()
