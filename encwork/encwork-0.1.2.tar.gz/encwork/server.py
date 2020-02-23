# Created by MysteryBlokHed on 21/02/2020.
import socket
from datetime import datetime
from math import ceil
from time import sleep

from .encryption import *
from .exceptions import *

HEADERSIZE = 16
global peer_public_key
global latest_message
global latest_time
peer_public_key = None
latest_message = ""
latest_time = datetime.now()