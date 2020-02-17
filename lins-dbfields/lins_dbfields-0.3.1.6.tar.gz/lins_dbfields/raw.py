from django.db import models


class RawMixin:

    def select_format(self, compiler, sql, params):
        sql = self.custom_sql
        sql = str(sql).format(table=self.model._meta.db_table)
        return sql, params


class RawCharField(RawMixin, models.CharField):
    custom_sql = ''

    def __init__(self, verbose_name=None, custom_sql=None, **kwargs):
        self.custom_sql = custom_sql
        super(RawCharField, self).__init__(verbose_name, **kwargs)


class RawIntegerField(RawMixin, models.IntegerField):
    custom_sql = ''

    def __init__(self, verbose_name=None, custom_sql=None, **kwargs):
        self.custom_sql = custom_sql
        super(RawIntegerField, self).__init__(verbose_name, **kwargs)


class RawBigIntegerField(RawMixin, models.BigIntegerField):
    custom_sql = ''

    def __init__(self, verbose_name=None, custom_sql=None, **kwargs):
        self.custom_sql = custom_sql
        super(RawBigIntegerField, self).__init__(verbose_name, **kwargs)


class RawDateTimeField(RawMixin, models.DateTimeField):
    custom_sql = ''

    def __init__(self, verbose_name=None, custom_sql=None, **kwargs):
        self.custom_sql = custom_sql
        super(RawDateTimeField, self).__init__(verbose_name, **kwargs)


class RawBooleanField(RawMixin, models.BooleanField):
    custom_sql = ''

    def __init__(self, verbose_name=None, custom_sql=None, **kwargs):
        self.custom_sql = custom_sql
        super(RawBooleanField, self).__init__(verbose_name, **kwargs)
