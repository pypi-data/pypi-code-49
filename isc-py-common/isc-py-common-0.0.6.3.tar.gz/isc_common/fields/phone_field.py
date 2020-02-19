from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class PhoneField(CharField):
    description = _("Телефон")

    def get_internal_type(self):
        return "CharField"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 50)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs
