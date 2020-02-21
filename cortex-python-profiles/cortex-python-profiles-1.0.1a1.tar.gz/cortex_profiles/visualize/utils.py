"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import os
import uuid
from enum import auto, unique

import ipywidgets as widgets
import psutil
from IPython.core.display import display, HTML
from IPython.display import display_javascript, display_html, JSON, Javascript

from cortex_common.utils import EnumWithNamesAsDefaultValue


def button(text):
    """
    Factory method to help create an ipython button
    :param text:
    :return:
    """
    return widgets.Checkbox(
        value=False,
        description=text,
        disabled=False
    )


def container(stuff):
    """
    Wrap stuff in a widget container
    :param stuff:
    :return:
    """
    return widgets.VBox(stuff)


def to_output(content):
    """
    returns how ipython displays content by default
    """
    x = widgets.Output()
    with x:
        display(content)
    return x


def tab_with_content(content_dict):
    """
    Creates a tab with dicts where keys are tabnames and content are the content of the tab ...
    """
    tab = widgets.Tab()
    keys = list(content_dict.keys())
    tab.children = [content_dict[k] for k in keys]
    for (i,title) in enumerate(keys):
        tab.set_title(i, title)
    return tab


def set_id_for_dom_element_of_output_for_current_cell(_id):
    """
    Set a JS id on a cell so we can manipulate it with JS libraries later.
    :param _id:
    :return:
    """
    display(Javascript('console.log(element.get(0)); element.get(0).id = "{}";'.format(_id)))


class InteractableJsonForNotebooks(object):
    """
    Return an interactable JSON for notebooks
    """

    def __init__(self, json_data):
        if isinstance(json_data, (dict, list)):
            self.json_str = json.dumps(json_data)
        elif isinstance(json_data, JSON):
            self.json_str = json.dumps(json_data.data)
        else:
            self.json_str = json_data
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display_html('<div id="{}" style="height: 600px; width:100%;"></div>'.format(self.uuid), raw=True)

        js = """
            require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {{
                renderjson.set_icons('+', '-');
                renderjson.set_show_to_level("2");
                document.getElementById('{}').appendChild(renderjson({}))
            }});
        """

        display_javascript(js.format(self.uuid, self.json_str), raw=True)


def widescreen():
    """
    Make the notebook take the whole screen horizontally
    :return:
    """
    return display(HTML("<style>.container { width:90% !important; }</style>"))


@unique
class Runtimes(EnumWithNamesAsDefaultValue):
    """
    What are the different ways for the code to run?
    """
    LAB = auto()
    NOTEBOOK = auto()
    SKILL = auto()


# TODO - This is NOT CLEAN!
#   - we are detecting if jupyter lab is running based on the name of the parent binary that kicked off the notebook ...
def detect_runtime() -> Runtimes:
    """
    What way is the code currently running
    :return:
    """
    parent_pid = os.getppid()
    if parent_pid == 0:
        return Runtimes.SKILL
    parent_process = psutil.Process(parent_pid)
    if any(["jupyter-lab" in x for x in parent_process.cmdline()]):
        return Runtimes.LAB
    return Runtimes.NOTEBOOK


def return_json_based_on_runtime(runtime:Runtimes=detect_runtime()):
    """
    How should JSONs be visualized based on the current runtime?
    :param runtime:
    :return:
    """
    if runtime == Runtimes.SKILL:
        return lambda x: x # return json as is ...
    elif runtime == Runtimes.LAB:
        return JSON
    elif runtime == Runtimes.NOTEBOOK:
        return InteractableJsonForNotebooks


InteractableJson = return_json_based_on_runtime()