from django.template import Library
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.db import models

register = Library()

@register.simple_tag
def sprintf(template, args):
    print(template, args)
    return template % args

@register.simple_tag
def string_format(template, *args, **kwargs):
    return template.format(*args, **kwargs)

@register.simple_tag
def admin_url(item, view):
    app_label = item._meta.app_label
    model_name = item._meta.model_name
    return reverse("admin:{0}_{1}_{2}".format(app_label, model_name, view), kwargs={"object_id": item.pk})

@register.simple_tag
def if_cookie(request, name, exist_value, not_exist_value):
    if name in request.COOKIES:
        return exist_value
    else:
        return not_exist_value

@register.simple_tag
def get_cookie(request, name, default=""):
    if name in request.COOKIES:
        return request.COOKIES.get(name)
    else:
        return default

@register.simple_tag
def has_cookie(request, name):
    if name in request.COOKIES:
        return True
    else:
        return False

@register.simple_tag
def if_setting(name, exist_value, not_exist_value):
    if hasattr(settings, name):
        return exist_value
    else:
        return not_exist_value

@register.simple_tag
def get_setting(name, default=""):
    if hasattr(settings, name):
        return getattr(settings, name)
    else:
        return default

@register.simple_tag
def has_setting(name):
    return hasattr(settings, name)


@register.simple_tag
def model_select_include(opts, template_name, **context):
    if isinstance(opts, dict):
        app_label = opts["app_label"]
        model_name = opts["model_name"]
    else:
        if isinstance(opts, models.Model):
            opts = opts._meta
        app_label = opts.app_label
        model_name = opts.model_name
    templates = [
        "admin/{0}/{1}/{2}".format(app_label, model_name, template_name),
        "admin/{0}/{1}".format(app_label, template_name),
        "admin/{0}".format(template_name),
    ]
    return render_to_string(templates, context)
