from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

class ErrorResponse(Response):
    @staticmethod
    def create(errors):
        if isinstance(errors.args[0], str):
            return Response({'detail': errors.args[0]}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': errors.args[0]}, status=HTTP_400_BAD_REQUEST)