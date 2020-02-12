from whatap.trace.mod.application_wsgi import transfer, trace_handler, \
    interceptor_httpc_request, interceptor_sock_connect


def instrument_httplib(module):
    def wrapper(fn):
        @trace_handler(fn)
        def trace(*args, **kwargs):
            # set mtid header
            kwargs['headers'] = transfer(kwargs.get('headers', {}))
            
            # set httpc_url
            httpc_url = args[1]
            callback = interceptor_httpc_request(fn, httpc_url, *args, **kwargs)
            return callback
        
        return trace
    
    module.HTTPConnection.request = wrapper(module.HTTPConnection.request)
    module.HTTPConnection.connect = wrapper(interceptor_sock_connect)

def instrument_httplib2(module):
    def wrapper(fn):
        @trace_handler(fn)
        def trace(*args, **kwargs):
            # set mtid header
            kwargs['headers'] = transfer(kwargs.get('headers', {}))
            
            # set httpc_url
            httpc_url = args[1]
            callback = interceptor_httpc_request(fn, httpc_url, *args, **kwargs)
            return callback
        
        return trace
    
    module.Http.request = wrapper(module.Http.request)
    module.HTTPConnectionWithTimeout.connect = wrapper(interceptor_sock_connect)
    module.HTTPSConnectionWithTimeout.connect = wrapper(interceptor_sock_connect)