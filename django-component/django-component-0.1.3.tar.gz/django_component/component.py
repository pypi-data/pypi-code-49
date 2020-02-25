from django.forms.widgets import MediaDefiningClass
from django.template.base import Context


class Component(metaclass=MediaDefiningClass):
    template: str = ""

    def context(self, *args, **kwargs):
        return kwargs

    def render(self, context: Context, children: str, *args, **kwargs) -> str:
        context.update(self.context(*args, **kwargs))
        context.update({"children": children})
        template = context.template.engine.get_template(self.template)
        return template.render(context)
