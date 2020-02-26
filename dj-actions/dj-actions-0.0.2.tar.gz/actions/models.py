from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import timedelta, datetime
DEFAULT_TTL_MINUTES = 60*24 # 1 day
from actions.util import ACTION_TYPE

class ActionEvent(models.Model):

    action_id = models.CharField(max_length=100)
    actor_id = models.CharField(max_length=100, null=True, blank=True)
    object_id = models.CharField(max_length=100, null=True, blank=True)
    action_context = models.CharField(max_length=30, null=True, blank=True)
    status_code = models.PositiveIntegerField(default=0)
    request_data = JSONField(null=True, blank=True)
    response_data = JSONField(null=True, blank=True)
    response_content = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    duration = models.DecimalField(max_digits=14, decimal_places=10, default=0)

    scheduled_time = models.DateTimeField(null=True, blank=True)  # <- let's consider supporting scheduling actions

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)

    @property
    def action_type(self):
        if self.object_id:
            return ACTION_TYPE.INSTANCE.value
        else:
            return ACTION_TYPE.BULK.value

    @staticmethod
    def archive(self):
        '''
        Archive old action events
        '''
        ttl = getattr(settings, 'DJACTION_TTL_MINUTES', DEFAULT_TTL_MINUTES)
        archive_before_date = datetime.now() - timedelta(minutes=ttl)
        ActionEvent.objects.filter(
            complete=True,
            created_date__gte=archive_before_date
        ).delete()
