from django import template
from .component import Component
from .component_tag import make_component_tag

import typing as t


class Library(template.Library):
    def __init__(self):
        super().__init__()

    def component(self, comp: t.Type[Component]):
        component_name = comp.__name__
        self.tag(component_name, make_component_tag(comp, self_closed=False))
        self.tag(component_name + "/", make_component_tag(comp, self_closed=True))
        return comp
