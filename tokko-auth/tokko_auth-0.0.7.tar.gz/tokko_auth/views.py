from django.http import HttpResponse
import json


from tokko_auth.decorators import has_permission
from tokko_auth.models import User
from tokko_auth import settings


def auth_status(request):
    user = (
        json.loads(f"{request.user}")
        if isinstance(request.user, User)
        else f"{request.user}"
    )
    response = {
        "user": user,
        "settings": {
            "is_enable": not settings.AUTH_FULL_DISABLED,
            "fail_safe": settings.AUTH_FAIL_SAFE_ENABLE,
            "api_namespace": settings.AUTH_API_NAMESPACE,
            "userinfo": settings.AUTH_USERINFO_ENABLE,
            "auth_domain": settings.AUTH0_DOMAIN,
            "user_successfully_loaded": hasattr(request.user, "claims"),
        },
    }
    return HttpResponse(json.dumps(response, indent=4), content_type="application/json")


@has_permission('test:testing', has_all=True)
def protected_view(request):
    response = {"message": "Authorized!"}
    return HttpResponse(json.dumps(response, indent=4), content_type="application/json")
