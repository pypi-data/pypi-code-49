from webob import Request

class RequestLogger:

    # Defaults
    code_check_point = "1"
    service_name = None
    log_level = "info"
    encoding = 'utf-8'

    def __init__(self, app, log_level="info", service_name=""):
        self.wrap_app = self.app = app 
        self.set_code_check_point(log_level.lower())
        self.service_name = service_name.lower()
        self.log_level = log_level.lower()
        self.encoding = 'utf-8'

    def __call__(self,environ,start_response):
        request = Request(environ)
        def custom_start_response(status, headers, exc_info=None):
            if status.startswith(self.code_check_point):
                print('{"level":"'+self.log_level+'","service":"'+self.service_name+'","message":"","uri":"'+request.path_qs+'","responseCode":'+status.split(" ")[0]+',"requestId":"'+request.headers.get("request-id","")+'"}')
            return start_response(status, headers, exc_info)
        return self.wrap_app(environ, custom_start_response)

    def set_code_check_point(self,log_level):
        if log_level == "error":
            self.code_check_point = "4"
