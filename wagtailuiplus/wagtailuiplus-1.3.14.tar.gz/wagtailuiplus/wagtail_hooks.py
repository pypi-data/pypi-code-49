from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks

@hooks.register('insert_editor_css')
def editor_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('css/wagtailuiplus.css')
    )

@hooks.register('insert_editor_js')
def editor_js():
    return format_html(
        '<script src="{}"></script>',
        static('js/wagtailuiplus.js')
    )
