"""
Media path resolver class that takes a django template to configure where files should be uploaded
within the media repository.
"""

from django.template.base import Template
from django.template.context import Context
from django.utils.deconstruct import deconstructible

from orionframework.media.models import MEDIA_CATEGORY_CHOICES
from orionframework.utils.models import get_choice_label


@deconstructible()
class MediaPathResolver(object):
    parser = None

    def __init__(self, path=None,
                 template="{% if path %}{{path}}/{% endif %}{{parent_type}}/{{parent_id}}/{% if category %}{{category}}/{% endif %}{{filename}}"):
        self.path = path
        self.template = template

    def __call__(self, instance, filename):

        if not self.parser:
            self.parser = Template(self.template)

        category = None

        if instance.category:
            category = get_choice_label(MEDIA_CATEGORY_CHOICES, instance.category)

        if instance.parent_type:
            parent_type = instance.parent_type.model

            parent_id = instance.parent_id

        context = locals()
        context["path"] = self.path

        return self.parser.render(Context(context))
