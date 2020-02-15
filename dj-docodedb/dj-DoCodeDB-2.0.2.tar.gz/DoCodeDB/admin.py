from django.contrib import admin

from .models import Tsendgrid

# Register your models here.
class TsendgridAdmin(admin.ModelAdmin):
    list_display = ('id', 'key')

admin.site.register(Tsendgrid, TsendgridAdmin)