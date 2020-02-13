from django.db.models import ForeignKey, CASCADE


class FK(ForeignKey):
    def __init__(self, verbose_name, to, on_delete=CASCADE, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, **kwargs):
        super().__init__(to=to,
                         on_delete=on_delete,
                         related_name=related_name,
                         related_query_name=related_query_name,
                         limit_choices_to=limit_choices_to,
                         parent_link=limit_choices_to,
                         to_field=to_field,
                         db_constraint=db_constraint,
                         verbose_name=verbose_name,
                         **kwargs)
