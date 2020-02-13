import pkgutil
import socket
from contextlib import closing

version_file_content = pkgutil.get_data('spintop.compat', 'VERSION' )
VERSION = version_file_content.decode().strip()
    
def format_exception(e):
    return e.__class__.__name__ + ': ' + str(e)
    

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]