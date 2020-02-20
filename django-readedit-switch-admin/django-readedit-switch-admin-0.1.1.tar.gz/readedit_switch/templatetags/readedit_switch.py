from django import template
from django.template.context import Context
from django.contrib.admin.templatetags.base import InclusionAdminNode


register = template.Library()


def readedit_switch_submit_row(context):
    add = context['add']
    change = context['change']
    has_add_permission = context['has_add_permission']
    has_change_permission = context["has_change_permission"]
    has_change_permission_real = context["has_change_permission_real"]
    show_save = (has_change_permission and change) or (has_add_permission and add)
    show_edit = (not has_change_permission) and has_change_permission_real and change
    show_delete_link = context["has_delete_permission"]
    show_close = not has_change_permission
    show_cancel = has_change_permission and change
    ctx = Context(context)
    ctx.update({
        "show_save": show_save,
        "show_edit": show_edit,
        "show_delete_link": show_delete_link,
        "show_close": show_close,
        "show_cancel": show_cancel,
    })
    return ctx

@register.tag(name='readedit_switch_submit_row')
def readedit_switch_submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=readedit_switch_submit_row, template_name='django_readedit_switch_admin_submit_row.html')
