from django.template import Library
from .arg_tag import arg_tag
from .media import media_tag

register = Library()

register.tag("arg", arg_tag)
register.tag("components_css", media_tag("css"))
register.tag("components_js", media_tag("js"))
