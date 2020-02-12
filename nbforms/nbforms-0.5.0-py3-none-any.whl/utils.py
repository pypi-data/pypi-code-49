#################################
##### Utils for nbforms API #####
#################################

import hashlib
import hmac
import secrets
import random

HMAC_KEY = secrets.token_bytes(32)

def hash_string(s):
    hashed = hmac.new(HMAC_KEY, s.encode(), hashlib.sha512).hexdigest()
    len_selection = random.choice(range(10, 20))
    return "".join([random.choice(hashed) for _ in range(len_selection)])
