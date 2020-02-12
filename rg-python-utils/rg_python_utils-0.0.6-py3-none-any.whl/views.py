from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


class RGPluginsUtil:

    @staticmethod
    @require_http_methods(["POST"])
    def enable_logs(request):
        pass

    @staticmethod
    @require_http_methods(["GET"])
    def disable_logs(request):
        return JsonResponse({})

    @staticmethod
    @require_http_methods(["GET"])
    def get_log_status(request):
        return JsonResponse({"log_status": True})
