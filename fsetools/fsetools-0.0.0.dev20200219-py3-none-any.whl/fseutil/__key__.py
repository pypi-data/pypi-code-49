import fseutil
from fseutil.etc.util import hash_simple


def key():
    return hash_simple(key=b'ofrconsultants', string=fseutil.__version__.encode(), algorithm='sha256', length=30)


if __name__ == '__main__':
    print(hash_simple(key=b'ofrconsultants', string=fseutil.__version__.encode(), algorithm='sha256', length=30))
