import lazy_import
import json
warnings = lazy_import.lazy_module('warnings')
fstorage = lazy_import.lazy_module('futsu.storage')

def path_to_data(path):
    bytes = fstorage.path_to_bytes(path)
    return json.loads(bytes)

def data_to_path(path, data):
    bytes = (json.dumps(data,sort_keys=True,indent=2)+'\n').encode('utf-8')
    fstorage.bytes_to_path(path, bytes)

def file_to_data(fn):
    with open(fn,'r') as fin:
        return json.load(fin)

def data_to_file(fn,data):
    with open(fn,'w') as fout:
        json.dump(data,fout,sort_keys=True,indent=2)
        fout.write('\n')

def json_read(fn):
    warnings.warn('deprecated, use file_to_data(fn)', DeprecationWarning)
    return file_to_data(fn)

def json_write(fn,data):
    warnings.warn('deprecated, use data_to_file(fn,data)', DeprecationWarning)
    data_to_file(fn,data)
