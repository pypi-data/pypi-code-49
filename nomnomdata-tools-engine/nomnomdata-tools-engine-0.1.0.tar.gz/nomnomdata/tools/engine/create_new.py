import shutil
from os import makedirs, path

import click
from jinja2 import Template


@click.command()
@click.argument("engine_name", required=True)
def create_new(engine_name):
    """Create a template engine layout based on the given name"""
    t_dir = path.join(path.dirname(__file__), "template")

    def copymap(src, dest):
        if path.basename(src).startswith("ex_"):
            dest = path.join(path.dirname(dest), path.basename(src)[3:])
        with open(src, "r") as infile:
            template = Template(infile.read())
        makedirs(path.dirname(dest), exist_ok=True)
        template = template.render(engine_name=engine_name)
        with open(dest, "w") as outfile:
            outfile.write(template)

    shutil.copytree(t_dir, engine_name, copy_function=copymap)
