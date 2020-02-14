# -*- coding: jinja2 -*-
# flake8: noqa

# {% set attrs = ['a', 'b', 'c'] %}

class MyClass:
    def __init__(
        self,
        # {% for attr in attrs %}
        {{attr}},
        # {% endfor %}
    ):
        # {% for attr in attrs %}
        self.{{attr}} = {{attr}}
        # {% endfor %}
