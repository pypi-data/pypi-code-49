from psu_base.services import auth_service
from django.conf import settings
from django.urls import reverse


def auth(request):
    auth_object = auth_service.get_auth_object()
    return {'auth': auth_object}


def util(request):
    model = {
        # The home URL (path) depends on existence of URL Context
        'home_url': f"/{settings.URL_CONTEXT}/" if settings.URL_CONTEXT else '/',

        # Does PSU Logo color need to be modified (i.e. heading color is non-white)
        'modify_logo': settings.PSU_LOGO_FILTER is not None,
        'modify_logo_filter': settings.PSU_LOGO_FILTER.replace('filter:', '').strip(' ;') if settings.PSU_LOGO_FILTER else None,
        'modify_logo_calculate': settings.PSU_LOGO_FILTER is None and settings.PRIMARY_FG_COLOR,
    }

    # If white (the default color) was unnecessarily specified, logo doesn't need to be modified
    if model['modify_logo_calculate']:
        if str(settings.PRIMARY_FG_COLOR).lower() in ['white', '#fff', '#ffffff']:
            model['modify_logo_calculate'] = False
        elif settings.PRIMARY_FG_COLOR == (255, 255, 255):
            model['modify_logo_calculate'] = False
        elif settings.PRIMARY_FG_COLOR == (255, 255, 255, 1):
            model['modify_logo_calculate'] = False
        # If filter needs to be calculated, it also needs to be applied
        model['modify_logo'] = model['modify_logo_calculate']

    return model
