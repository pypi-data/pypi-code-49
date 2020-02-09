from django.contrib import admin

from . import models


@admin.register(models.DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'user', 'the_date')
    raw_id_fields = ('party', 'user')
    readonly_fields = ('party',)
