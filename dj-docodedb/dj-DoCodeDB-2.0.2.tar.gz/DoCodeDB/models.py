from django.db import models

# Create your models here.

# Modelo para almacenar las credenciales de SendGrid
class Tsendgrid(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    key = models.CharField(max_length=255, blank=True, null=True)