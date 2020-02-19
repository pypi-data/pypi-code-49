from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class CodeField(CharField):
    description = _("Код")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('default', None)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        del kwargs["db_index"]
        del kwargs['default']
        return name, path, args, kwargs
