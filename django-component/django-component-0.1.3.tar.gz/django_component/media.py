from typing import Literal

from django import template
from django.forms.widgets import Media
from django.utils.safestring import mark_safe

from secrets import token_hex

CONTEXT_KEY = "__django_component"


def media_tag(media_type: Literal["css", "js"]):
    def media(parser, token):
        nodelist = parser.parse()
        return MediaNode(media_type, nodelist)

    return media


def ensure_context_media(context):
    if not CONTEXT_KEY in context:
        context[CONTEXT_KEY] = {"media": Media()}


def add_media(context, media):
    ensure_context_media(context)
    context[CONTEXT_KEY]["media"] += media


class MediaNode(template.Node):
    def __init__(self, media_type: Literal["css", "js"], nodelist):
        self.media_type = media_type
        self.nodelist = nodelist

    def render(self, context):
        rendered = self.nodelist.render(context)
        return self.render_media(context) + rendered

    def render_media(self, context):
        tags = []
        if CONTEXT_KEY in context:
            media = context[CONTEXT_KEY]["media"]
            if self.media_type == "css":
                tags = media.render_css()
            elif self.media_type == "js":
                tags = media.render_js()
        return "".join(tags)
