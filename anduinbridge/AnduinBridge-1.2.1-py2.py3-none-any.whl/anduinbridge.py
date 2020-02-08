"""AnduinBridge enables remote processes to call Anduin injected DB routines by wrapping routines in REST API. """
#!/usr/bin/env python

from __future__ import print_function
import sys
import os
import json
import threading
import re
import time
try: # IronPython modules
    from System.Diagnostics import Process
    from Queue import Queue
    __ANDUIN_ENV__ = True
except ImportError: # Python 2/3 modules
    __ANDUIN_ENV__ = False
try:  # Python 3 modules
    from queue import Queue
    from urllib.request import urlopen, Request
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:  # Python 2 modules
    from urllib2 import urlopen, Request
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

# Fix issues with decoding HTTP responses
reload(sys)
# pylint: disable=no-member
sys.setdefaultencoding('utf8')

def _is_primitive(var):
    """ Determine if input is primitive. """
    return isinstance(var, (int, float, bool, str))

def _net2dict(obj):
    """ Convert .net object into Python dictionary. """
    attrs = (name for name in dir(obj) if not name.startswith('_') and _is_primitive(obj.__getattribute__(name)))
    obj_dict = dict()
    for attribute in attrs:
        val = obj.__getattribute__(attribute)
        # IronPython json uses incorrect boolean so change to int
        val = int(val) if isinstance(val, bool) else val
        obj_dict[attribute] = val
    return obj_dict

class RESTRequestHandler(BaseHTTPRequestHandler):
    """ Simple Rest Server using only built-in Python modules. """
    def __init__(self, *args, **kwargs):
        self.routes = kwargs.get('routes')
        if 'routes' in kwargs:
            del kwargs['routes']
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
    def do_HEAD(self):
        self.handle_method('HEAD')
    def do_GET(self):
        self.handle_method('GET')
    def do_POST(self):
        self.handle_method('POST')
    def do_PUT(self):
        self.handle_method('PUT')
    def do_DELETE(self):
        self.handle_method('DELETE')
    def get_payload(self):
        payload_len = int(self.headers.getheader('content-length', 0))
        payload = self.rfile.read(payload_len)
        payload = json.loads(payload)
        return payload
    def handle_method(self, method):
        route = self.get_route()
        if route is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('Route not found\n')
            return
        if method == 'HEAD':
            self.send_response(200)
            if 'media_type' in route:
                self.send_header('Content-type', route['media_type'])
            self.end_headers()
            return
        if method in route:
            content = route[method](self)
            if content is not None:
                self.send_response(200)
                if 'media_type' in route:
                    self.send_header('Content-type', route['media_type'])
                self.end_headers()
                if method != 'DELETE':
                    self.wfile.write(json.dumps(content))
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write('Not found\n')
        else:
            self.send_response(405)
            self.end_headers()
            self.wfile.write(method + ' is not supported\n')
    def get_route(self):
        for path, route in self.routes.iteritems():
            if re.match(path, self.path):
                return route
        return None

def get_anduin_data(anduin_globals):
    """ Extracts Anduin configs (dut, station, specs, traveler) """
    configs = dict(dut={}, station={}, specs={}, traveler={})
    # On Anduin get real configs
    if __ANDUIN_ENV__:
        # Get DUT configs
        lcl_dut = _net2dict(anduin_globals['slot'].Dut)
        configs['dut'].update(lcl_dut)
        # Get Station configs
        lcl_station = _net2dict(anduin_globals['station'])
        kv_key = 'translateKeyValDictionary'
        station_constants = anduin_globals[kv_key](anduin_globals['station'].Constants)
        lcl_station.update(station_constants)
        configs['station'].update(lcl_station)
        # Get specs
        for spec_name, spec_dict in anduin_globals['TestSpecs'].iteritems():
            full_spec_dict = dict(lsl=None, usl=None, details='')
            full_spec_dict.update(spec_dict.copy())
            if "counts_in_result" in full_spec_dict:
                # IronPython json uses incorrect boolean so change to string
                full_spec_dict["counts"] = str(full_spec_dict["counts_in_result"])
                full_spec_dict["counts_in_result"] = full_spec_dict["counts"]
            configs['specs'][spec_name] = full_spec_dict
        # Get traveler
        configs['traveler'].update(anduin_globals['traveler'])
    # Get dummy configs
    else:
        configs['dut'] = anduin_globals.get('dut', {})
        configs['specs'] = anduin_globals.get('specs', {})
        configs['station'] = anduin_globals.get('station', {})
        configs['traveler'] = anduin_globals.get('traveler', {})
    return configs

def add_test_results(anduin_globals, results):
    ''' Handle processing list of DB results '''
    error = None
    results = results if isinstance(results, list) else [results]
    for result in results:
        try:
            add_test_result(anduin_globals, result)
        except Exception as err:  # pylint: disable=broad-except
            error = err
    return error

def add_test_result(anduin_globals, result):
    ''' Handle processing individual DB result '''
    rst_name = result.get('name', None)
    rst_args = result.get('args', [])
    # Special case for storing files (enables supplying src url)
    if rst_name == 'AddResultFile':
        rst_name = 'AddResultText'
        args = rst_args
        if len(args) == 3:
            fname = args[0]
            src_url = args[1]
            dst_path = args[2]
            dst_folder = os.path.dirname(dst_path)
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)
            with open(dst_path, 'wb') as fp:
                fp.write(urlopen(src_url).read())
            rst_args = [fname, 'Link', str.format('{:s}', dst_path)]
        elif len(args) == 2:
            rst_args = [args[0], 'Link', args[1]]
        else:
            raise Exception('AddResultFile: args must be [name, url, dst].')
    if rst_name in anduin_globals:
        anduin_globals[rst_name](*rst_args)
    else:
        print('ADD DB RESULT:', rst_name, rst_args)
        time.sleep(0.01) # Simulate database transactions

def run_to_completion(proxy, timeout=30, poll_delay=1):
    try:
        start_timeout = timeout
        while proxy.is_alive() and start_timeout > 1:
            time.sleep(poll_delay)
            if os.getenv('DEBUG', False):
                print(proxy.test_status)
            if start_timeout <= 0:
                raise Exception('Start test request timeout occurred.')
            if proxy.test_status['state'] in ['IDLE']:
                start_timeout -= poll_delay
            elif proxy.test_status['state'] in ['EXCEPTION', 'FAILED', 'PASSED']:
                # Wait for server to finish processing DB results
                if not proxy.processing_results():
                    proxy.shutdown()
                    proxy.join()
                else:
                    print('Still processing DB results...')
        # Verify test results
        test_status = proxy.test_status
        if test_status.get('state') == 'EXCEPTION':
            raise Exception('Test failed due to exception {0}.'.format(test_status.get('error')))
        elif test_status.get('state') in ['FAILED', 'PASSED']:
            return test_status
        else:
            err = test_status.get('error', 'N/A')
            raise Exception('Test failed due to premature exit (Details: {0}).'.format(err))
    except KeyboardInterrupt:
        if proxy:
            proxy.shutdown()
            proxy.join()
        raise Exception('Test failed due to being killed.')
    except Exception as err:
        raise err

def perform_request(uri, payload=None, attempts=3):
    numAttempts = 0
    while True:
        try:
            req = Request(uri, payload) if payload else Request(uri)
            response = urlopen(req)
            if response.code > 299:
                raise Exception('Response {0} ({1})'.format(response.msg, response.code))
            return response
        except Exception as err:
            time.sleep(0.1)
            numAttempts += 1
            if os.getenv('DEBUG'):
                print('request failed w/ error', err, numAttempts)
            if numAttempts >= attempts:
                raise err

class AnduinRestClient(object):
    """ Acts as Anduin DB proxy via REST client. """
    def __init__(self, anduin_globals, address, port, poll_delay=2):
        self.anduin_globals = anduin_globals
        self.address = address
        self.port = port
        self.poll_delay = poll_delay

    def clear_test_request(self):
        try:
            perform_request('http://{}:{}/api/v1/test/clear'.format(self.address, self.port), json.dumps(dict()))
        except Exception as err:
            raise Exception('Clear test request failed w/ error: {}'.format(err))

    def start_test_request(self, test):
        try:
            perform_request('http://{}:{}/api/v1/test/start'.format(self.address, self.port), json.dumps(test))
        except Exception as err:
            raise Exception('Start test request failed w/ error: {}'.format(err))

    def get_test_results(self, offset=0):
        try:
            response = perform_request('http://{}:{}/api/v1/test/results?offset={}'.format(
                self.address, self.port, offset
            ))
            return json.loads(response.read())
        except Exception as err:
            raise Exception('Failed getting test results w/ error: {}'.format(err))

    def get_test_status(self):
        try:
            response = perform_request('http://{}:{}/api/v1/test/status'.format(self.address, self.port))
            return json.loads(response.read())
        except Exception as err:
            raise Exception('Failed getting test status w/ error: {}'.format(err))

    def stop_test_request(self):
        try:
            perform_request('http://{}:{}/api/v1/test/stop'.format(self.address, self.port), json.dumps(dict()), 2)
        except Exception as err:
            raise Exception('Stop test request failed w/ error: {}'.format(err))

    def run_to_completion(self, test, timeout=30):
        # Request test start
        self.clear_test_request()
        self.start_test_request(test)

        # Wait until test finishes or timeout occurs
        is_running = True
        start_timeout = timeout
        status = dict(state='IDLE')
        results = []
        while is_running:
            time.sleep(self.poll_delay)
            status = self.get_test_status()
            if os.getenv('DEBUG'):
                print(status)
            if start_timeout <= 0:
                raise Exception('Test start request timeout')
            if status is None or status.get('state') in [None, 'IDLE']:
                start_timeout -= self.poll_delay
            elif status and status.get('state') in ['EXCEPTION', 'FAILED', 'PASSED']:
                is_running = False
            else:
                start_timeout = timeout
                is_running = True
            # Retreive and save any new results (DB routines are VERY slow - hide as much latency)
            new_results = self.get_test_results(offset=len(results))
            new_results = new_results.get('results', []) if new_results else []
            add_test_results(self.anduin_globals, new_results)
            results += new_results
        if status.get('error'):
            raise Exception('Test raised following error: {}'.format(status['error']))
        return status, results

class AnduinDBWorker(threading.Thread):
    """ Threaded DB worker to handle calling global DB functions w/ results in queue. """
    def __init__(self, anduin_globals, rst_queue):
        super(AnduinDBWorker, self).__init__()
        self.anduin_globals = anduin_globals
        self.rst_queue = rst_queue
    def run(self):
        print('Anduin DB worker started')
        while True:
            result = self.rst_queue.get()
            # A None result implies we are done
            if result is None:
                break
            try:
                add_test_result(self.anduin_globals, result)
            except Exception as err:
                print('Failed processing DB task w/ error', err)
            finally:
                self.rst_queue.task_done()
        print('Anduin DB worker finished')

class AnduinRestServer(threading.Thread):
    """ Acts as Anduin DB proxy via REST server. """
    def __init__(self, anduin_globals, port):
        super(AnduinRestServer, self).__init__()
        self.anduin_globals = anduin_globals
        self.port = port
        self.event_lock = threading.Lock()
        self.test_status = dict(
            id=None, name=None, state='IDLE', progress=0,
            message=None, error=None, timestamp=None
        )
        self.test_results = []
        self.server = None
        # Handle processing DB results via threaded queue
        self.db_queue = Queue()
        self.db_worker = AnduinDBWorker(self.anduin_globals, self.db_queue)
        return

    def processing_results(self):
        return self.db_queue and not self.db_queue.empty()

    def get_test_status(self, handler=None):
        return self.test_status

    def set_test_status(self, handler):
        data = handler if isinstance(handler, dict) else handler.get_payload()
        with self.event_lock:
            self.test_status.update(data)
            self.test_status['timestamp'] = int(time.time())
            print(self.test_status)
        return {}

    def get_test_results(self, handler):
        return {}

    def add_test_results_request(self, handler):
        results = handler.get_payload()
        results = results if isinstance(results, list) else [results]
        with self.event_lock:
            for result in results:
                self.db_queue.put(result)
            self.test_results += results
        return {}

    def shutdown(self):
        """ Shutdown REST server"""
        if self.server:
            with self.event_lock:
                self.server.shutdown()
                self.server.socket.close()
        self.server = None
        self.test_results = []
        if self.db_worker:
            self.db_queue.put(None)
            self.db_worker.join()
        self.db_worker = None

    def run(self):
        delegate = self
        class AnduinRESTRequestHandler(RESTRequestHandler):
            def __init__(self, *args, **kwargs):
                # pylint: disable=return-in-init
                routes = {
                    r'^/$': {'file': 'web/index.html', 'media_type': 'text/html'},
                    r'^/api/v1/test/results$': {'GET': delegate.get_test_results, 'POST': delegate.add_test_results_request, 'media_type': 'application/json'},
                    r'^/api/v1/test/status$': {'GET': delegate.get_test_status, 'POST': delegate.set_test_status, 'media_type': 'application/json'}
                }
                kwargs['routes'] = routes
                return RESTRequestHandler.__init__(self, *args, **kwargs)

        self.set_test_status(dict(
            id=None, name=None, state='IDLE', progress=0,
            message=None, passed=None, error=None
        ))

        self.db_worker.start()
        self.server = HTTPServer(('0.0.0.0', self.port), AnduinRESTRequestHandler)
        self.test_results = []
        print('Anduin DB REST API running on port: ', self.port)
        self.server.serve_forever()
