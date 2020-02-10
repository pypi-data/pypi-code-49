import os

# http://www.sphinx-doc.org/en/master/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme(
        'ustackdocs',
        os.path.abspath(os.path.dirname(__file__)),
    )
    return {
        'parallel_read_safe': True,
    }
