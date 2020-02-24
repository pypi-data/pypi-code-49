import hashlib
from time import time
from typing import Dict
import jwt


class JwtHeader:
    def __init__(self, public_key: str, private_key: str, leeway: int = 60):
        self.public_key = public_key
        self.private_key = private_key
        self.leeway = leeway

    def generate(self) -> Dict[str, str]:
        return {'Authorization': 'Bearer ' + self._generate_array()}

    def _generate_array(self) -> str:
        current_time = int(time())
        signature_data = {
            'sub': self.public_key,
            'iat': current_time - self.leeway,
            'exp': current_time + self.leeway,
            'iss': 'yusp-ali',
            'nbf': current_time - self.leeway,
            'jti': hashlib.md5((self.public_key + str(current_time)).encode()).hexdigest(),
        }
        return jwt.encode(signature_data, self.private_key, algorithm='HS256').decode()
