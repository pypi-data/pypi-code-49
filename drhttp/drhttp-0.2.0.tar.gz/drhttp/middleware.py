from django.utils.deprecation import MiddlewareMixin

from .defines import DRHTTP_HEADER_USER

class DjangoUserMiddleware(MiddlewareMixin):
    """
    This middleware puts user's primary key value (if authenticated)
    in DRHTTP_HEADER_USER response header
    """
    def process_response(self, request, response):
        
        if hasattr(request, "user") and request.user.pk:
            response[DRHTTP_HEADER_USER] = str(request.user.pk)
            
        return response