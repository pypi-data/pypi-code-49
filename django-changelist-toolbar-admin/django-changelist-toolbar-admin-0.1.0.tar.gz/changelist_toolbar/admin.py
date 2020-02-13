from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.contrib.admin.options import BaseModelAdmin


class Button(object):

    def __init__(self, href, title, target="", klass="", icon=""):
        self.href = href
        self.title = title
        self.target = target
        self.klass = klass
        self.icon = icon

    @classmethod
    def from_dict(cls, data):
        item = cls(**data)
        return item

class ChangelistToolbarAdminMixin(admin.ModelAdmin):

    changelist_toolbar_buttons = []

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["changelist_toolbar_buttons"] = self.get_changelist_toolbar_buttons(request)
        return super().changelist_view(request, extra_context)

    def get_changelist_toolbar_buttons(self, request):
        buttons = []
        for button in self.changelist_toolbar_buttons:
            buttons.append(self.make_changelist_toolbar_button(button, request))
        return buttons

    def make_changelist_toolbar_button(self, button, request):
        if not isinstance(button, Button):
            if isinstance(button, str):
                target = getattr(self, button, None)
                if target:
                    button = target
                else:
                    button = Button(button, button)
            if callable(button):
                result = button(request)
                if isinstance(result, Button):
                    button = result
                elif isinstance(result, dict):
                    button = Button.from_dict(result)
                elif isinstance(result, str):
                    href = result
                    title = getattr(button, "title", href)
                    target = getattr(button, "target", "")
                    klass = getattr(button, "klass", "")
                    icon = getattr(button, "icon", "")
                    button = Button(href, title, target, klass, icon)
                elif isinstance(result, Button):
                    button = result
        if not isinstance(button, Button):
            raise RuntimeError("make_changelist_toolbar_button failed: {0}".format(button))
        info = {
            "href": button.href,
            "title": button.title,
            "target": button.target,
            "klass": button.klass,
            "icon": button.icon,
        }
        return info

    class Media:
        css = {
            "all": [
                "fontawesome/css/all.min.css",
                "changelist_toolbar/css/changelist_toolbar.css",
            ]
        }
