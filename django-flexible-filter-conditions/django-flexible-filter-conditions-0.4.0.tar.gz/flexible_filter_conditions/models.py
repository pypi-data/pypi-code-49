# -*- coding: utf-8 -*-
import datetime
import importlib

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.constraints import CheckConstraint
from django.utils.translation import ugettext_lazy as _


class ConditionValues(object):
    """Iterator that returns values available for Klub Conditions

    Returns tuples (val, val) where val is a string of the form
    model.cid where model is the name of the model in lower case
    and cid is the database column id (name).

    This class is needed to be able to dynamically generate
    a list of values selectable in the Condition forms by
    dynamically introspecting the User and Payment models.
    """

    def __init__(self):
        self._columns = []
        # Special attributes
        self._columns += [_(u"Action"), ('action', "Action: CharField ('daily', 'new-user', 'new-payment')")]
        # Models attributes
        for name, model_name in settings.FLEXIBLE_FILTER_CONDITIONS_FIELD_MAP.items():
            models = importlib.import_module(model_name[0])
            model = getattr(models, model_name[1])

            # DB fields
            columns = []
            for field in model._meta.fields:
                if field.name:
                    val = name + "." + field.name
                    n = field.name
                else:
                    val = name
                    n = name
                columns.append(
                    (
                        val,
                        "%s: %s %s" % (
                            n,
                            field.get_internal_type(),
                            list(zip(*field.choices))[0] if field.choices else "",
                        ),
                    ),
                )
            self._columns.append((name, columns))
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._index = self._index + 1
            return self._columns[self._index]
        except IndexError:
            raise StopIteration


class NamedCondition(models.Model):

    class Meta:
        verbose_name = _("Condition")
        verbose_name_plural = _("Conditions")
        ordering = ('name',)

    name = models.CharField(
        verbose_name=_("Name of condition"),
        max_length=200,
        blank=False,
        null=True,
    )
    as_filter = models.BooleanField(
        verbose_name=_("Display as filter?"),
        help_text=_("Determines whether this condition is available as a filter"
                    "in the table of Users"),
        default=False,
    )
    on_dashboard = models.BooleanField(
        verbose_name=_("Display on dashboard?"),
        help_text=_("Determines whether this condition is available on dashboard"),
        default=False,
    )

    def condition_string(self):
        condition_strings = []
        for condition in self.conditions.all():
            condition_strings.append(condition.condition_string())
        return ", ".join(condition_strings)

    def __str__(self):
        return str(self.name)


class Condition(models.Model):
    """A condition entry and DB model

    Conditions are composed of the left hand side, an operator
    and the right hand side.

    Possible values for either side are:
    1) a value (string, integer...)
    2) a symbolic value -- variable, special value or reference to DB
    (e.g. u.regular)
    3) another condition

    Only one type of left and one type of right hand side value is permitted.
    Not all operators will work with all types of values (e.g. logic operators
    only work on other conditions on both sides)
    """

    class Meta:
        verbose_name = _("Condition")
        verbose_name_plural = _("Conditions")
        constraints = [
            CheckConstraint(
                check=(
                    (Q(named_condition__isnull=False) | Q(conds__isnull=False)) &
                    (Q(named_condition__isnull=True) | Q(conds__isnull=True))
                ),
                name="conds_xor_named_condition_is_null",
            ),
        ]

    OPERATORS = (
        ('and', _(u'and')),
        ('or', _(u'or')),
        ('xor', _(u'xor (one or the other)')),
    )

    # One of variable or conds must be non-null
    negate = models.BooleanField(
        verbose_name=_("Negate"),
        default=False,
    )
    operation = models.CharField(
        verbose_name=_("Operation"),
        choices=OPERATORS,
        max_length=30,
    )
    conds = models.ForeignKey(
        'self',
        related_name='conds_rel',
        # symmetrical=False,
        verbose_name=_("Conditions"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    named_condition = models.ForeignKey(
        'NamedCondition',
        related_name='conditions',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def get_query(self, action=None):
        operation_dict = {
            'and': lambda x, y: x & y,
            'or': lambda x, y: x | y,
            'xor': lambda x, y: (~x & y) | (x & ~y),
        }
        ret_cond = None
        if self.conds_rel:
            for cond in self.conds_rel.all():
                if ret_cond:
                    ret_cond = operation_dict[self.operation](ret_cond, cond.get_query(action))
                else:
                    ret_cond = cond.get_query(action)
        for tcond in self.terminalcondition_set.all():
            if ret_cond:
                ret_cond = operation_dict[self.operation](ret_cond, tcond.get_query(action))
            else:
                ret_cond = tcond.get_query(action)

        if self.negate:
            return ~(ret_cond)
        else:
            return ret_cond

    def condition_string(self):
        prefix = ""
        sufix = ""
        if self.negate:
            prefix = "not("
            sufix = ")"
        op_string = " %s " % self.operation

        condition_list = [condition.condition_string() for condition in self.conds_rel.all()]
        terminalcondition_list = [str(condition) for condition in self.terminalcondition_set.all()]
        return "%s(%s)%s" % (
            prefix,
            op_string.join(condition_list + terminalcondition_list),
            sufix
        )


class TerminalCondition(models.Model):
    """A terminal condition entry and DB model

    Terminal conditions are composed of the left hand side, an operator
    and the right hand side.

    Possible values for either side are:
    1) a value (string, integer...)
    2) a symbolic value -- variable, special value or reference to DB
    (e.g. u.regular)

    Only one type of left and one type of right hand side value is permitted.
    Not all operators will work with all types of values (e.g. logic operators
    only work on other conditions on both sides)
    """

    class Meta:
        verbose_name = _("Terminal condition")
        verbose_name_plural = _("Terminal conditions")

    OPERATORS = (
        ('=', u'='),
        ('!=', u'≠'),
        ('>', '>'),
        ('<', '<'),
        ('>=', '≥'),
        ('<=', '≤'),
        ('containts', _(u'contains')),
        ('icontaints', _(u'contains (case insensitive)')),
        ('isnull', _('variable is null (true or false)')),
        ('in', _('in list variable type (e.g. list.3,44)')),
    )

    variable = models.CharField(
        verbose_name=_("Variable"),
        choices=ConditionValues(),
        help_text=_("Value or variable on left-hand side"),
        max_length=50,
        blank=True,
        null=True,
    )
    operation = models.CharField(
        verbose_name=_("Operation"),
        choices=OPERATORS,
        max_length=30,
    )
    # One of value or conds must be non-null
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_(
            "Value or variable on right-hand side. <br/>"
            "\naction: daily, new-user<br/>"
            "\nDateField: month_ago, one_day, one_week, two_weeks, one_month,"
            " datetime.2010-01-01 00:00, date.2010-01-01, list.3,5<br/>"
            "\nBooleanField: True, False<br/>"
            "\nfor blank value: None or Blank",
        ),
        max_length=50,
        blank=True,
        null=True,
    )
    condition = models.ForeignKey(
        Condition,
        on_delete=models.CASCADE,
    )

    def variable_description(self):
        if self.variable:
            try:
                field_map_key, field_path = self.variable.split(".")
                model_dir, model_name = settings.FLEXIBLE_FILTER_CONDITIONS_FIELD_MAP[field_map_key]
                model = getattr(importlib.import_module(model_dir), model_name)
                field = model._meta.get_field(field_path)
                return getattr(field, 'help_text', getattr(field, 'verbose_name', field))
            except (NameError, ValueError, KeyError):
                try:
                    return eval(self.variable).__doc__
                except NameError:
                    return "action"

    def get_val(self, spec):
        if spec and '.' in spec:
            variable, value = spec.split('.')
        else:
            variable = spec

        spec_dict = {
            'month_ago': datetime.datetime.now() - datetime.timedelta(days=30),
            'one_day': datetime.timedelta(days=1),
            'one_week': datetime.timedelta(days=7),
            'two_weeks': datetime.timedelta(days=14),
            'one_month': datetime.timedelta(days=31),
            'date': lambda value: datetime.datetime.strptime(value, '%Y-%m-%d'),
            'datetime': lambda value: datetime.datetime.strptime(value, '%Y-%m-%d %H:%M'),
            'timedelta': lambda value: datetime.timedelta(days=int(value)),
            'days_ago': lambda value: datetime.datetime.now() - datetime.timedelta(days=int(value)),
            'list': lambda value: value.split(','),
            'true': True,
            'false': False,
            'none': None,
            'blank': '',
        }
        if variable and variable.lower() in spec_dict:
            expression = spec_dict[variable.lower()]
            if hasattr(expression, "__call__"):  # is function
                return expression(value)
            else:
                return expression
        else:
            try:
                return int(spec)
            except (TypeError, ValueError):
                return spec

    def get_querystring(self, spec, operation):
        spec_ = spec.split('.')
        join_querystring = "__".join(spec_[1:])

        operation_map = {
            '=': "",
            '!=': "",
            '<': "__lt",
            '>': "__gt",
            'contains': "__contains",
            'icontains': "__icontains",
            '<=': "__lte",
            '>=': "__gte",
            'isnull': "__isnull",
            'in': "__in",
        }
        return join_querystring + operation_map[operation]

    def get_query(self, action=None):
        if self.variable == 'action':
            if self.value == action:
                return Q()
            else:
                return Q(pk__in=[])  # empty set

        # Elementary conditions
        left = self.get_querystring(self.variable, self.operation)
        right = self.get_val(self.value)
        if self.operation == '!=':
            return ~Q(**{left: right})
        else:
            return Q(**{left: right})

    def __str__(self):
        return "%s %s %s" % (self.variable, self.operation, self.value)


def filter_by_condition(queryset, named_cond):
    for cond in named_cond.conditions.all():
        queryset = queryset.filter(cond.get_query())
    return queryset.distinct()
