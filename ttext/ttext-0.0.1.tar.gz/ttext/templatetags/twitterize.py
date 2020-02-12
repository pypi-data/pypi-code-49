try:
    from django.template import Library
    from django.template.defaultfilters import stringfilter
except:
    raise Exception('Django is not installed.')

from ttext import TwitterText

register = Library()

@register.filter(name = 'ttext')
@stringfilter
def ttext(text, search_query = False):
    """
    Parses a text string through the TwitterText auto_link method and if search_query is passed, through the hit_highlight method.
    """
    tt = TwitterText(text)
    if search_query:
        tt.text     =   tt.highlighter.hit_highlight(query = search_query)
    tt.text         =   tt.autolink.auto_link()
    return tt.text
ttext.is_safe = True