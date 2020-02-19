
from django.contrib import admin

import nested_admin

from .models import Condition, NamedCondition, TerminalCondition


class TerminalConditionInline(nested_admin.NestedTabularInline):
    model = TerminalCondition
    readonly_fields = ("variable_description",)
    extra = 0


inlines = []
inline_depth = 10
for i in range(inline_depth):
    if i > 0:
        inline_classes = [TerminalConditionInline, inlines[i - 1]]
    else:
        inline_classes = [TerminalConditionInline]
    inlines.append(
        type(
            'Condition%sInline' % i,
            (nested_admin.NestedTabularInline,),
            {
                'model': Condition,
                'fields': ('negate', 'operation',),
                'inlines': inline_classes,
                'extra': 0,

            },
        ),
    )
ConditionInline = inlines[inline_depth - 1]


# @admin.register(TerminalCondition)
# class TerminalConditionAdmin(nested_admin.NestedModelAdmin):
#     list_display = ('variable', 'operation', 'value', 'condition')


@admin.register(NamedCondition)
class NamedConditionAdmin(nested_admin.NestedModelAdmin):
    save_as = True
    list_display = ('name', 'as_filter', 'on_dashboard', 'condition_string')
    # filter_horizontal = ('conds',)
    inlines = [ConditionInline, ]

    ordering = ('name',)
