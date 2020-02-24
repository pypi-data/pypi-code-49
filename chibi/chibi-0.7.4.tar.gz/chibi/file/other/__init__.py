from .chibi_csv import Chibi_csv
import os
from .chibi_yaml import Chibi_yaml
from .chibi_json import Chibi_json


__all__ = [ 'Chibi_csv', 'Chibi_yaml', 'Chibi_json' ]


def find_correct_class( path, cls ):
    file_name, ext = os.path.splitext( path )
    if ext == '.csv':
        return Chibi_csv
    elif ext in ( '.yml', '.yaml' ):
        return Chibi_yaml
    elif ext == '.json':
        return Chibi_json
    return cls
