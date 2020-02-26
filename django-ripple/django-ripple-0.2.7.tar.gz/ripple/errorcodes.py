from rest_framework import status
from rest_framework.response import Response

class Err:
    def __init__(self, error_code, status=status.HTTP_401_UNAUTHORIZED):
        self.error_code = error_code
        self.status = status

    def __str__(self):
        return self.error_code

    def __call__(self, message=None):
        data = {
            'error_code': self.error_code,
            'detail': message or '',
        }
        
        return Response(data, self.status)


ERR_USER_EXISTS = Err("ERR_USER_EXISTS")
ERR_USER_NOT_FOUND = Err("ERR_USER_EXISTS")
ERR_AUTH_FAIL = Err("ERR_AUTH_FAIL")
ERR_INVALID_PASSWORD = Err("ERR_VALIDATION_ERROR")

ERR_SUPPLIER_NOT_FOUND = Err("ERR_SUPPLIER_NOT_FOUND")
ERR_TARIFF_NOT_FOUND = Err("ERR_TARIFF_NOT_FOUND")
