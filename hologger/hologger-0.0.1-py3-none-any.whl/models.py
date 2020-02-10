from django.db import models
from pytz import timezone
from django.conf import settings


class ApiResponse(models.Model):
    ho_logger = True

    status = models.CharField(max_length=30)
    host = models.CharField(max_length=150)
    uri = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    remote_addr = models.CharField(max_length=20)
    header = models.TextField(default="", blank=True)
    body = models.TextField(default="", blank=True)
    response = models.TextField(default="", blank=True)
    pid = models.CharField(max_length=10)
    queries = models.TextField(default="", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "api_response"
        managed = True

    @property
    def created_at_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.created_at.astimezone(korean_timezone)
