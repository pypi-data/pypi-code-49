name = 'jupyter-openbis-server.server'
__author__ = 'Swen Vermeul'
__email__ = 'swen@ethz.ch'
__version__ = '0.1.0'

def _jupyter_server_extension_paths():
    return [{
        "module": "jupyter-openbis-server.main"
    }]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("jupyter-openbis-server module enabled!")
