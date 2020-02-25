import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

HERE = os.path.abspath(os.path.dirname(__file__)) 

jinja_env = Environment(
    loader=FileSystemLoader(os.path.join(HERE, 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)

def get_template(name):
    return jinja_env.get_template(name)