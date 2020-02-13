from django.forms.models import model_to_dict

from .rg_utils import Util


class BaseModel(object):

    def is_equal(self, other) -> bool:
        if not other:
            return False

        return Util.is_dict_equal(self.get_dict(), other.get_dict())

    def get_dict(self) -> dict:
        return model_to_dict(self)
