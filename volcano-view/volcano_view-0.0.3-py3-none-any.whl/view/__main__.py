import argparse
import sys
import codecs
import logging
import http.server
import socketserver
import json
import zipfile

from .web_exc import WebException
from .the_time import IvlDef

WWW_FOLDER = 'www'
_LOG_LEVELS = {
    'all': logging.NOTSET,
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
}


_MIME = {
    'txt': 'text/plain; charset=utf-8',
    'html': 'text/html; charset=utf-8',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpg',
    'json': 'application/json',
    'xml': 'application/xml; charset=utf-8',
}


def configure_logger(env):
    assert env.log, env

    msg_fmt = '%(levelname)s %(asctime)s [%(name)s] %(message)s'

    if env.log == 'none':
        logging.disable(logging.CRITICAL)
    else:
        lev = _LOG_LEVELS.get(env.log, None)
        if lev is None:
            raise SystemExit('Invalid value for logging level: "{}". Use all,debug,info,warn,error.'.format(env.log))
        logging.basicConfig(level=lev, format=msg_fmt)

    logging.addLevelName(logging.CRITICAL, '!!!')
    logging.addLevelName(logging.ERROR, '!! ')
    logging.addLevelName(logging.WARNING, '!  ')
    logging.addLevelName(logging.INFO, '   ')
    logging.addLevelName(logging.DEBUG, '   ')


def configure_my_args(parser):
    parser.add_argument('-l', '--log', help='Log level', default='info', choices=list(_LOG_LEVELS.keys()))
    parser.add_argument('-i', '--iface', help='Listen interface', default='')
    parser.add_argument('-p', '--port', help='Listen port', default=8080, type=int)
    parser.add_argument('-s', '--sim', help='Enable simulation', action='store_true')
    parser.add_argument('--nozip', help='Disable zipped resources', action='store_true')


class LoadException(Exception):
    pass


class Args:
    def __init__(self, args_str):
        self.args = {}
        for a in args_str.split('&'):
            eq = a.find('=')
            if eq==-1:
                self.args[a] = True
            else:
                self.args[a[:eq]] = a[eq+1:]

    def get_str(self, name, default = None):
        val = self._get( name )
        if val is None:
            if default is None:
                raise WebException ('Missing "{}" argument'.format(name), 400)
            return default
        else:
            return val

    def get_bool(self, name, default = None):
        val = self._get( name )
        if val is None:
            if default is None:
                raise WebException ('Missing "{}" argument'.format(name), 400)
            return default
        
        if val=='1':    return True
        elif val=='0':  return False

        raise WebException ('Argument "{}={}" is not a valid boolean (use 0 and 1)'.format(name, val), 400)

    def _get(self, name):
        return  self.args.get(name, None)


class MyHandler(http.server.SimpleHTTPRequestHandler):
    
    Reader = None
    WebPackage = None
    
    error_content_type = _MIME['txt']
    error_message_format = '%(message)s'

    '''
    def do_POST(self):
    '''
    
    def do_GET(self):
        question_mark = self.path.find('?')
        
        if question_mark==-1:
            path = self.path
            args = ''
        else:
            path = self.path[:question_mark]
            args = self.path[question_mark+1:]

        # print('{} -- {} -- {}'.format(self.path, path, args))

        if path=='/' or path=='/index.html':
            self.send_response(301)
            self.send_header('Location', '/www/index.html')
            self.end_headers()
            return
            
        if path.startswith('/www/'):
            self._serve_static(path[5:])
            return
            
        try:
            if path == '/info.json':
                self._parse_info()
            elif path == '/enum_hr.json':
                self._parse_enum_hr()
            elif path == '/enum_qt.json':
                self._parse_enum_qt()
            elif path == '/read.json':
                self._parse_read(Args(args))
            else:
                self.send_error(404, 'Path not found: {}'.format(path))
        except WebException as ex:
            self.send_error(ex.http_code, '{}: {}'.format(path, ex))

    def _serve_static(self, file_path):
        dot = file_path.rfind('.')
        if dot!=-1:
            ext = file_path[dot+1:]
            if ext in _MIME:
                self.sendFile(WWW_FOLDER + '/' + file_path, _MIME[ext])
            else:
                self.sendFile(WWW_FOLDER + '/' + file_path, _MIME['txt'])
        else:
            self.send_error(404, 'File Not Found: {}'.format(file_path))

    def _parse_info(self):
        self._send_json({
            "version":{
                "major": 1,
                "minor": 1,
                "patch": 1,
            }
        })
        
    def _parse_enum_hr(self):
        # args = Args(request)
        # filter = args.get_str('filter', '')
        self._send_json(MyHandler.Reader.read_hr_wx(''))
        
    def _parse_enum_qt(self):
        self._send_json(MyHandler.Reader.read_qt_wx(True))
    
    def _parse_read(self, args):
        hr_ids_str = args.get_str ('hr')
        qt_id = args.get_str ('qt')
        all_ivl_s = args.get_str ('all_ivl')
        sub_ivl_s = args.get_str ('sub_ivl')
        finished = args.get_bool ('finished', False)

        hr_ids = hr_ids_str.split(',')

        try: 
            all_ivl = IvlDef.parse ( all_ivl_s )
            sub_ivl = IvlDef.parse ( sub_ivl_s )
        except ValueError as ex: 
            raise WebException(ex, 400)

        j = MyHandler.Reader.read_data_wx (hr_ids, qt_id, all_ivl, sub_ivl, finished)
        self._send_json(j)

    def _send_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', _MIME['json'])
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def sendFile(self, path, mime):
        try:
            self.send_response(200)
            self.send_header('Content-type', mime)
            self.end_headers()
            
            if MyHandler.WebPackage is None:
                with codecs.open(path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                with MyHandler.WebPackage.open(path) as f:
                    self.wfile.write(f.read())
        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(path))
        

def main() -> int:
    zip = None
    try:
        # Args
        arg_parser = argparse.ArgumentParser()
        configure_my_args(arg_parser)
        env = arg_parser.parse_args()

        # Logging
        configure_logger(env)
        log = logging.getLogger('web')

        if env.sim:
            log.warning('Data will be simulated')
            from .reader_sim import SimulationReader
            MyHandler.Reader = SimulationReader(log)
        else:
            log.info('Data connection to MySQL will be used')
            from .reader_ecosui_db import EcoSUIReader
            MyHandler.Reader = EcoSUIReader(log)

        if env.nozip:
            log.info('Zipped web resources disabled, using source folder')
        else:
            try:
                zip = zipfile.ZipFile('www.zip')
                with zip.open('{}/index.html'.format(WWW_FOLDER), 'r'):
                    log.info('Zip file with web resources tested ok')    # test open
            except Exception as ex:
                log.error(ex)
                return 1
                
            MyHandler.WebPackage = zip

        # reload вызывается также в runtime, поэтому он wx. 
        # попытка загрузки при старте нужна для проверки конфигурации
        try:
            MyHandler.Reader.reload_wx()
        except WebException as ex:
            log.error(ex)
            return 1

        try:
            log.info('Listen on %s:%s', env.iface, env.port)

            with socketserver.TCPServer((env.iface, env.port), MyHandler) as httpd:
                httpd.serve_forever()

            return 0

        except (Warning, LoadException) as ex:
            log.error(ex)
            return 1
    finally:
        logging.shutdown()
        
        if zip:
            try:
                zip.close()
            except:
                pass


if __name__ == '__main__':
    sys.exit(main())
