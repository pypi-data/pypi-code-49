from django.db.models import TextField
from django.utils.translation import gettext_lazy as _

from isc_common import delAttr


class DescriptionField(TextField):
    description = _("Описание")

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('null', True)
        kwargs.setdefault('blank', True)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        delAttr(kwargs, 'null')
        delAttr(kwargs, 'blank')
        return name, path, args, kwargs
