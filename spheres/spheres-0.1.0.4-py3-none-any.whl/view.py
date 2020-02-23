from spheres import *
import uuid

########################################################################################

class jsCall:
    def __init__(self, view, name):
        self.view = view
        self.name = name
        
    def __call__(self, *args):
        data = []
        null = False
        again = False
        finished = False

        def __callback__(*returned):
            nonlocal data, null, again, finished
            returned = list(returned)
            if len(returned) == 1\
                    and type(returned[0]) == type({})\
                        and "error" in returned[0]:
                error = returned[0]["error"]
                if error.startswith("client attribute"):
                    null = True
                    finished = True
                    raise NameError("name '%s' of %s is not defined"\
                                     % (error["attribute"],\
                                        type(self.view).__name__))
                elif error.startswith("client object"):
                    sockets.emit("create", {"class": self.view.__js_class__,\
                                            "uuid": self.view.uuid,\
                                            "args": {}})
                    again = True
                    finished = True
            else:
                data = returned
                finished = True
             
        sockets.emit("call", {"uuid": self.view.uuid,\
                              "func": self.name,\
                              "args": args},\
                              callback=__callback__)
        t = 0
        while not finished:
            t += 1
            if t > 200:
                finished = True
                raise Exception("Timed out!")
            sockets.sleep(0.01)
        if again:
            return self.__call__(*args)
        if not null:
            return data[0] if len(data) == 1 else data

########################################################################################

class View(object):
    views = {}
    __slots__ = ["_obj", "__weakref__"]

    def __init__(self, obj, *args, **kwargs):
        object.__setattr__(self, "_obj", obj)
        self.uuid = str(uuid.uuid4())
        View.views[self.uuid] = self

        self.listeners = {}
        self.__outer_class__ = type(self).__name__[:type(self).__name__.index("(")]
        self.__inner_class__ = type(obj)
        self.__js_class__ = kwargs["js_class"]\
                                if "js_class" in kwargs\
                                    else self.__outer_class__
        self.__to_client__ = kwargs["to_client"]\
                                    if "to_client" in kwargs\
                                        else lambda view: str(view)
        self.__from_client__ = kwargs["from_client"]\
                                    if "from_client" in kwargs\
                                        else lambda data: object.__getattribute__(self, "_obj")
        self.requires_flush = ["__delitem__",  "__delslice__", "__setitem__", "__setslice__"]
        if "requires_flush" in kwargs:
            self.requires_flush.extend(kwargs["requires_flush"])

    ########################################################################################

    @property
    def __class__(self):
        return self.__inner_class__

    def get(self):
        return object.__getattribute__(self, "_obj")

    def set(self, value, silent=False):
        if type(value) == self.__inner_class__:
            object.__setattr__(self, "_obj", value)
            if not silent:
                self.flush()
        else:
            raise Exception("can't set %s to %s!" % (self.__inner_class__.__name__,
                                                    type(value).__name__))

    def __lshift__(self, value):
        self.set(value)
        return self

    def flush(self, local=False):
        for uuid, with_func in self.listeners.items():
            if uuid in View.views:
                View.views[uuid] << (with_func(self))
        if not local:
            return jsCall(self, "refresh_from_server")(self.__to_client__(self))

    ########################################################################################

    def refresh_from_client(self, data):
        object.__setattr__(self, "_obj", self.__from_client__(data))
        self.flush(local=True)

    ########################################################################################

    def listen(self, to_whom, with_func):
        to_whom.listeners[self.uuid] = with_func

    def unlisten(self, to_whom):
        del to_whom.listeners[self.uuid]

    ########################################################################################

    def loop_for(self, n, func, rate=1/8, sleep=0.001):
        if n != 0:
            for i in range(n):
                if i % int(1/rate) == 0:
                    self << func(self)
                else:
                    self.set(func(self), silent=True)
                sockets.sleep(sleep)

    ########################################################################################

    def js(self):
        print("workspace.views['%s']" % self.uuid)

    ########################################################################################
    
    def __getattr__(self, name):
        if hasattr(object.__getattribute__(self, "_obj"), name):
            attribute = getattr(object.__getattribute__(self, "_obj"), name)
            if callable(attribute):
                def __wrapper__(*args, **kwargs):
                    args = [object.__getattribute__(arg, "_obj")\
                            if "View" in type(arg).__name__\
                            else arg\
                                for arg in args]
                    kwargs = dict([(key, object.__getattribute__(val, "_obj")\
                            if "View" in type(val).__name__\
                            else val ) for key, val in kwargs.items()])
                    value = attribute(*args)
                    self.flush() if name in self.requires_flush else None
                    return value
                return __wrapper__
            else:
                self.flush() if name in self.requires_flush else None
                return attribute
        else:
            return jsCall(self, name)

    def __delattr__(self, name):
        if hasattr(object.__getattribute__(self, "_obj"), name):
            delattr(object.__getattribute__(self, "_obj"), name)
            self.flush()
        else:
            super().__delattr__(name)

    def __setattr__(self, name, value):
        if hasattr(object.__getattribute__(self, "_obj"), name):
            setattr(object.__getattribute__(self, "_obj"), name, value)
            self.flush()
        else:
            super().__setattr__(name, value)

    ########################################################################################

    def __del__(self):
        sockets.emit("destroy", {"uuid": self.uuid})
    
    def __nonzero__(self):
        return bool(object.__getattribute__(self, "_obj"))

    def __str__(self):
        return str(object.__getattribute__(self, "_obj"))

    def __repr__(self):
        self.flush()
        return repr(object.__getattribute__(self, "_obj"))

    ########################################################################################

    _special_names = [
        '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__', 
        '__contains__', '__delitem__', '__delslice__', '__div__', '__divmod__', 
        '__eq__', '__float__', '__floordiv__', '__ge__', '__getitem__', 
        '__getslice__', '__gt__', '__hash__', '__hex__', '__iadd__', '__iand__',
        '__idiv__', '__idivmod__', '__ifloordiv__', '__ilshift__', '__imod__', 
        '__imul__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', 
        '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', 
        '__long__', '__lt__', '__mod__', '__mul__', '__ne__', #'__lshift__',
        '__neg__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', 
        '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
        '__reversed__', '__rfloorfiv__', '__rlshift__', '__rmod__', #'__repr__',
        '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', 
        '__rtruediv__', '__rxor__', '__setitem__', '__setslice__', '__sub__', 
        '__truediv__', '__xor__', 'next',
    ]

    @classmethod
    def _create_class_proxy(cls, inner_class):        
        def make_method(name):
            def method(self, *args, **kwargs):
                args = [object.__getattribute__(arg, "_obj")\
                            if "View" in type(arg).__name__\
                            else arg\
                                for arg in args]
                kwargs = dict([(key, object.__getattribute__(val, "_obj")\
                            if "View" in type(val).__name__\
                            else val ) for key, val in kwargs.items()])
                value = getattr(object.__getattribute__(self, "_obj"), name)(*args, **kwargs)
                self.flush() if name in self.requires_flush else None
                return value
            return method
        namespace = {}
        for name in cls._special_names:
            if hasattr(inner_class, name):
                namespace[name] = make_method(name)
        return type("%s(%s)" % (cls.__name__, inner_class.__name__), (cls,), namespace)
    
    def __new__(cls, obj, *args, **kwargs):
        try:
            cache = cls.__dict__["_class_proxy_cache"]
        except KeyError:
            cls._class_proxy_cache = cache = {}
        try:
            inner_class = cache[obj.__class__]
        except KeyError:
            cache[obj.__class__] = inner_class = cls._create_class_proxy(obj.__class__)
        inself = object.__new__(inner_class)
        inner_class.__init__(inself, obj, *args, **kwargs)
        return inself