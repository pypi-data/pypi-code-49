from os.path import join, exists, dirname

from yhttp import Application, text, notfound, html
from mako.template import Template

from .cli import Version
from .markdown import markdown2html
from . import indexer

here = dirname(__file__)
templatefilename = join(here, 'master.mako')
staticdirectory = join(here, 'static')
app = Application()
app.cliarguments.append(Version)
app.settings.merge(f'''
root: .
template:
  filename: {templatefilename}
static:
  directory: {staticdirectory}
  route: /static/
''')


@app.when
def ready(app):
    app.template = Template(filename=app.settings.template.filename)
    app.staticdirectory(
        app.settings.static.route,
        app.settings.static.directory,
        insert=0
    )


@app.route(r'/(.*)')
@html
def get(req, path):
    root = app.settings.root
    if not path:
        yield app.template.render(
            toc=indexer.generate(root),
            content=indexer.generate(root),
        )
        return

    filename = join(root, f'{path}.md')
    if not exists(filename):
        raise notfound()

    with open(filename) as f:
        yield app.template.render(
            toc=indexer.generate(root),
            content=markdown2html(f.read()),
        )

