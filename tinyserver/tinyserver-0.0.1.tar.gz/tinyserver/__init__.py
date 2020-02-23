from http.server import BaseHTTPRequestHandler, HTTPServer

class miniRequestHandler(BaseHTTPRequestHandler):
    _message = ''

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self._write(self.message())

    def do_POST(self):
        self.do_GET()

    def _write(self, message, encoding='utf8'):
        self.wfile.write(bytes(message, encoding))

    def message(self):
        return self._message

class miniServer(HTTPServer):
    def __init__(self, message='miniServer is up', port=8080, ip="0.0.0.0", request_handler=miniRequestHandler):
        request_handler._message = message
        super().__init__((ip, port), request_handler)
        self.serve_forever()

if __name__ == '__main__':
    miniServer() 
