import fsetools
from fsetools.etc.util import hash_simple


def key():
    return hash_simple(key=b'ofrconsultants', string=fsetools.__version__.encode(), algorithm='sha256', length=30)
    # return None

if __name__ == '__main__':
    print(hash_simple(key=b'ofrconsultants', string=fsetools.__version__.encode(), algorithm='sha256', length=30))
