from django.utils import timezone
import datetime
from django.db import models, connection


class DBTimestampMixin:

    def get_dbtimestamp(self):
        return timezone.now()

    def pre_save(self, model_instance, add):
        if self.auto_now or (self.auto_now_add and add):
            value = self.get_dbtimestamp()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(DBTimestampMixin, self).pre_save(model_instance, add)


class DateTimeField(models.DateTimeField, DBTimestampMixin):

    def get_dbtimestamp(self):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            with connection.cursor() as cursor:
                cursor.execute("SELECT CURRENT_TIMESTAMP()")
                return cursor.fetchone()[0]
        return super(DateTimeField, self).get_dbtimestamp()


class TimeField(models.TimeField, DBTimestampMixin):

    def get_dbtimestamp(self):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            with connection.cursor() as cursor:
                cursor.execute("SELECT CURRENT_TIME()")
                return cursor.fetchone()[0]
        return datetime.datetime.now().time()


class DateField(models.DateField, DBTimestampMixin):

    def get_dbtimestamp(self):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            with connection.cursor() as cursor:
                cursor.execute("SELECT CURRENT_DATE()")
                return cursor.fetchone()[0]
        return datetime.date.today()
