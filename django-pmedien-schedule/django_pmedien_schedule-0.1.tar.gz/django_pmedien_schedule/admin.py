# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import ScheduleGroup, Schedule


class AdminSchedule(admin.ModelAdmin):
    list_filter = ('ref_schedule_group',)

    list_display = (
        'name',
        'active',
        'ref_schedule_group',
        'override_day',
        'start_date',
        'start_time',
        'repeat_duration',
        'last_date',
        'last_time',
    )

    list_editable = ('active',)

    def get_fieldsets(self, request, obj=None):
        time_fields = (
            ('start_date', 'start_time'),
            'repeat_duration',
            'last_time',
        ) if obj and obj.override_day else (
            ('start_date', 'start_time'),
            'repeat_duration',
            ('last_date', 'last_time'),

        )

        day_fields = tuple() if obj and obj.override_day else tuple(
            ['d_{}'.format(i) for i in range(7)]
        )

        return (
            (
                'Override', {
                    'fields': ('override_day',)
                }
            ),
            (
                'Aufgabe', {
                    'fields': ('active', 'name', 'ref_schedule_group')
                }
            ),
            (
                'Zeiten', {
                    'fields': time_fields
                }
            ),
            (
                '' if obj and obj.override_day else 'Wochentage', {
                    'fields': (day_fields,)
                }
            )
        )

    def get_actions(self, request):
        actions = super(AdminSchedule, self).get_actions(request)
        del actions['delete_selected']
        return actions

class AdminHide(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


admin.site.register(Schedule, AdminSchedule)
admin.site.register(ScheduleGroup, AdminHide)
