
import base64

STRING_ENCODING = "utf-8"

def prepare_bytes_for_transport(bytes_):
    return base64.b64encode(bytes_).decode(STRING_ENCODING)

def unpack_bytes_from_transport(bytes_string):
    return base64.b64decode(bytes_string.encode(STRING_ENCODING))

class Singleton(type):
    _instances = {} #WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]