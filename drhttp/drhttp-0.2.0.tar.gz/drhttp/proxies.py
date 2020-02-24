class IteratableProxy:
    """
        This class proxies a iteratable object and calls callback
        each time the proxied object is iterated
        iterated_callback takes an argument : the data being returned by iteration
        iteration_ended_callback take no argument
    """
    def __init__(self, proxied, iterated_callback, iteration_ended_callback):
        self.proxied = iter(proxied)
        self.iterated_callback = iterated_callback
        self.iteration_ended_callback = iteration_ended_callback

    def __iter__(self):
        return self

    def __next__(self):
        try:
            data = next(self.proxied)
            self.iterated_callback(data)
            return data
        except StopIteration as exception:
            self.iteration_ended_callback()
            raise exception
    
    next = __next__

class ReadableProxy:
    """
        This class proxies a readable file-like object and calls callback
        each time the proxied object is read
        read_callback takes an argument : the bytes being read
    """
    def __init__(self, proxied, read_callback):
        self.proxied = proxied
        self.read_callback = read_callback
    
    def __getattr__(self, name):
        if name in ['read', 'readline', 'readlines']:
            return getattr(self, name)
        else:
            return getattr(self.proxied, name)

    def read(self, *args, **kwargs):
        return self.proxied_method('read', *args, **kwargs)

    def readline(self, *args, **kwargs):
        return self.proxied_method('readline', *args, **kwargs)

    def readlines(self, *args, **kwargs):
        return self.proxied_method('readlines', *args, **kwargs)

    def proxied_method(self, method_name, *args, **kwargs):
        method = getattr(self.proxied, method_name)
        data = method(*args, **kwargs)
        if method_name == 'readlines':
            for d in data:
                self.read_callback(d)
        else:
            self.read_callback(data)
        return data
