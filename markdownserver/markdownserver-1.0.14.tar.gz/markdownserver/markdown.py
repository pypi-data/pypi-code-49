import markdown2


extras = [
    'header-ids',
]


def markdown2html(md):
    return markdown2.markdown(md, extras=extras)

