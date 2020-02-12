
class GeneralMiddleware(object):

    def before(self, request):
        pass

    def key(self):
        return 'general'

    def value(self, request, response):
        return {
            'status_code': response.status_code,
            'content_type': response.get('Content-Type', ''),
            'endpoint': request.get_full_path()
        }

