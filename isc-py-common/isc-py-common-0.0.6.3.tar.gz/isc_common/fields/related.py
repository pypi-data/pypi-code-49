from django.db import models
from django.db.models import PROTECT, CASCADE


class ForeignKeyProtect(models.ForeignKey):
    def __init__(self,
                 to,
                 on_delete=PROTECT,
                 related_name=None,
                 related_query_name=None,
                 limit_choices_to=None,
                 parent_link=False,
                 to_field=None,
                 db_constraint=True,
                 **kwargs):
        super().__init__(to,
                         on_delete,
                         related_name,
                         related_query_name,
                         limit_choices_to,
                         parent_link,
                         to_field,
                         db_constraint,
                         **kwargs)


class ForeignKeyCascade(models.ForeignKey):
    def __init__(self,
                 to,
                 on_delete=CASCADE,
                 related_name=None,
                 related_query_name=None,
                 limit_choices_to=None,
                 parent_link=False,
                 to_field=None,
                 db_constraint=True,
                 **kwargs):
        super().__init__(to,
                         on_delete,
                         related_name,
                         related_query_name,
                         limit_choices_to,
                         parent_link,
                         to_field,
                         db_constraint,
                         **kwargs)
