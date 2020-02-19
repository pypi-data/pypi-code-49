from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext as _

from .models import NamedCondition


class UserConditionFilter(SimpleListFilter):
    """Filters using computed dynamic conditions from DB"""

    title = _("Condition")
    parameter_name = 'user_condition'

    def lookups(self, request, model_admin):
        return [(cond.id, cond.name) for cond in NamedCondition.objects.filter(as_filter=True)]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        cond = NamedCondition.objects.filter(id=self.value())[0]

        return cond.filter_queryset(queryset)


class UserConditionFilter1(UserConditionFilter):
    """Filters using computed dynamic conditions from DB"""
    parameter_name = 'user_condition1'
