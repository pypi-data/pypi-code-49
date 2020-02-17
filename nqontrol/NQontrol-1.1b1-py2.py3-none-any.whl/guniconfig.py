"""gunicorn config file"""

from nqontrol.settings import HOST

workers = 1
bind = f"{HOST}:8000"
timeout = 30
worker_class = "gthread"
threads = 1
debug = True
spew = False
preload_app = True  # incompatible with reload feature
reload = False
