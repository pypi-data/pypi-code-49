import importlib

from django.conf import settings

def _from_django_settings(settings_name, default):
    import_string = getattr(settings, settings_name)
    if import_string is None:
        import_string = default

    module_path, class_name = import_string.rsplit('.', 1)

    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def get_signup_serializer():
    return _from_django_settings('SIGNUP_SERIALIZER', 'ripple.serializers.SignUpSerializer')


def get_user_serializer():
    return _from_django_settings('USER_SERIALIZER', 'ripple.serializers.UserSerializer')
