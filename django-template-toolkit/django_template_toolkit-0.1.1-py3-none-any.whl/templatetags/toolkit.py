"""django-template-toolkit Tags & Filters"""

from django import template
from django import forms

register = template.Library()


@register.filter
def spacer(value) -> str:
    """Adds leading space if value is not empty"""
    return ' ' + str(value) if value is not None and value else ''


@register.filter
def field_css(field: object, css: str) -> object:
    """Rewrites CSS class attribute for a form field; also adds placeholder attribute"""
    attrs = {
        'class': css
    }
    # Add placeholder if allowed by HTML specification for certain widget types
    # (technically also "tel" and "search" but Django doesn't have widgets for those types)
    if field.field.widget.__class__ in \
            (forms.TextInput, forms.NumberInput, forms.EmailInput, forms.URLInput, forms.PasswordInput):
        attrs['placeholder'] = field.label
    return field.as_widget(attrs=attrs)


@register.filter
def is_field(field: object, value: str = None):
    """If value is not None, returns True if field name matches, otherwise returns field name"""
    f = field.field.__class__.__name__.lower()
    if value is not None:
        return True if f == value else False
    # value is None, so return field name for debug purposes
    return f


@register.filter
def is_widget(field: object, value: str = None):
    """If value is not None, returns True if widget name matches, otherwise returns widget name"""
    w = field.field.widget.__class__.__name__.lower()
    if value is not None:
        return True if w == value else False
    # value is None
    return w


@register.filter
def subset(obj: dict, keys: str):
    """Returns subset of the dictionary object with only the specified keys (as comma separated list)"""
    return [obj[key] for key in keys.split(',')]


@register.filter
def csvlist(value: str, index: int) -> str:
    """Returns a single value from a comma separated list of values"""
    return str(value).split(',')[index]


@register.simple_tag
def get_absolute_url(obj, name, *args) -> str:
    """"Calls get_absolute_url() method on a model object with a name argument"""
    # Note: if you don't need the name argument, just use {{ model.get_absolute_url }} directly
    return obj.get_absolute_url(name, *args)


@register.simple_tag
def call_method(obj, func, *args, **kwargs):
    """Calls method from specified object with arguments"""
    return getattr(obj, func)(*args, **kwargs)


@register.filter
def meta(model, attr: str) -> str:
    """Returns _meta attribute of specified model"""
    return str(getattr(model._meta, attr))


@register.filter
def concat(a: str, b: str) -> str:
    """Concatenate two strings together"""
    #  Existing 'add' filter isn't suitable for strings as it will try to coerce them into integers
    return str(a) + str(b)
