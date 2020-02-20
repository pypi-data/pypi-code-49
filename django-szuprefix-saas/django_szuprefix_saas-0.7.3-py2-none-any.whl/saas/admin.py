# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from . import models


def initDepartmentAndManagerWorker(modeladmin, request, queryset):
    from . import helper
    for party in queryset.all():
        helper.initDepartmentAndManagerWorker(party)


initDepartmentAndManagerWorker.short_description = "初始化"


@admin.register(models.Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_active', 'slug', 'create_time')
    actions = (initDepartmentAndManagerWorker,)


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "party", "path")
    raw_id_fields = ("party", "parent")
    list_filter = ("party",)
    search_fields = ("name",)
    readonly_fields = ("path",)


def set_unusable_password(modeladmin, request, queryset):
    for worker in queryset.all():
        user = worker.user
        user.set_unusable_password()
        user.save()


set_unusable_password.short_description = "清除登录密码"


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'party', 'position', 'is_active', 'create_time')
    raw_id_fields = ('party', 'departments', 'user')
    search_fields = ('name', 'number')
    actions = (set_unusable_password,)


@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('party', 'user')
    raw_id_fields = ('party', 'user')
