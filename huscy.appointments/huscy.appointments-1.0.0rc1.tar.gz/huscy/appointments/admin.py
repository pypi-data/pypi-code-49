from django.contrib import admin

from huscy.appointments import models

admin.site.register(models.Appointment)
admin.site.register(models.Invitation)
admin.site.register(models.Reminder)
admin.site.register(models.Resource)
