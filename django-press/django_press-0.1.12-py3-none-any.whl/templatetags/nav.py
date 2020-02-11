from django import template
from django_press.models import Page

register = template.Library()


@register.inclusion_tag('django_press/nav/main.html', takes_context=True)
def nav(context, core, **kwargs):
    nav_pages = Page.objects.filter(in_nav=True, publish=True).all()
    return {
        'nav_pages': nav_pages,
        'core': core,
        **kwargs,
    }
