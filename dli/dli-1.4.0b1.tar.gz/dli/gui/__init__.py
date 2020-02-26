import inspect
import functools
import io
import base64
import ipywidgets as widgets

from collections import defaultdict

from contextlib import redirect_stdout
from dli.client import session
from ipywidgets import Layout
from IPython.core.magic import (
    Magics, magics_class, line_magic, cell_magic
)
from IPython import get_ipython
from IPython.display import Javascript, display

from dli.models import DatasetModel, PackageModel


def help(obj):
    print("This is a " + type(obj).__name__ + "\n" + "*"*20,
        "\nIt has these functions:\n" + "\n".join(
          ["." + method_name for method_name in dir(obj)
                  if callable(getattr(obj, method_name))
           and ((not method_name.startswith("_")) or method_name=='__iter__')])
        ,
        "\n\nIt has these properties:\n" + "\n".join(
          ["." + method_name for method_name in dir(obj)
                  if not callable(getattr(obj, method_name))
           and ((not method_name.startswith("_")) or method_name=='__iter__')])
    + "\n\nAnd it looks like this:\n" + str(obj)
         )


def redirect(fun):
    with io.StringIO() as buf, redirect_stdout(buf):
        fun()
        output = buf.getvalue()
        return output


class SelectorWidget:
    def __init__(self, ipython):
        self.ipython = ipython
        self._name_counts = defaultdict(lambda: 0)
        self.packages = []
        self.datasets = []
        self.current_obj = None
        self.dl = None

        self.which_packages = widgets.RadioButtons(
            options=['Only Mine', 'All Packages'],
            disabled=False
        )

        self.button = widgets.Button(
            description='Connect',
            disabled=False,
            button_style='',
            tooltip='Click me',
            icon='check'
        )

        self.button.on_click(self.btn_eventhandler)

        self.copy_button = widgets.Button(
            description='Copy current object',
            disabled=False,
            button_style='',
            tooltip='Click me',
            icon='check',
            layout=Layout(width='100%', height='30px')
        )
        self.copy_button.on_click(self.btn_copyhandler)

        self.api_key = widgets.Text(
            value='',
            placeholder='Enter your api key',
            description='Enter your api key',
            disabled=False,
            layout=Layout(width='100%', height='30px')
        )

        self.env_dd = widgets.Dropdown(
            options=[('Prod', 1), ('UAT', 2), ('QA', 3)],
            value=1,
            description='Environment',
            disabled=False,
            layout=Layout(width='100%')
        )

        self.package_dd = widgets.Select(
            options=[],
            # rows=10,
            description='Packages',
            disabled=False,
            layout=Layout(width='90%')
        )

        self.package_dd.observe(self.on_change_package)

        self.dataset_dd = widgets.Select(
            options=[],
            # rows=10,
            description='Datasets',
            disabled=False,
            layout=Layout(width='90%')
        )

        self.dataset_dd.observe(self.on_change_dataset)

        api_keyl = [self.api_key]
        which = [self.which_packages]
        items = [
            widgets.VBox([self.package_dd], layout=Layout(width='50%')),
            widgets.VBox([self.dataset_dd], layout=Layout(width='50%'))
        ]

        tab_contents = ['.display()', '.shape', '.description', 'print', '__iter__']
        children = [widgets.Textarea(
            value='',
            placeholder='',
            disabled=False,
            layout=Layout(width='100%', height='180px')
        ) for name in tab_contents]

        self.tab = widgets.Tab(
            layout=Layout(width='100%', height='250px')
        )

        self.tab.children = children
        [self.tab.set_title(num, name) for num, name in enumerate(tab_contents)]

        vbox3 = widgets.HBox(which, layout=Layout(width='100%', height='50px'))
        vbox2 = widgets.VBox([widgets.HBox(api_keyl),
                              widgets.HBox([self.env_dd, self.button])])
        vbox = widgets.HBox(items)
        vbox4 = widgets.HBox([self.tab])
        self.root = widgets.VBox([vbox2, vbox3, vbox, vbox4, self.copy_button])

    def _generate_name(self, type_):
        while True:
            self._name_counts[type_] = (
                self._name_counts[type_] + 1
            )

            name = '{}_{}'.format(
                type_, self._name_counts[type_]
            )

            if name not in self.ipython.user_global_ns:
                break
            else:
                return self._generate_name(type_)

        return name

    def btn_copyhandler(self, obj):
        _name_alias = {
            'PackageModel': 'package',
            'DatasetModel': 'dataset',
        }

        name = self._generate_name(
            _name_alias[type(self.current_obj).__name__]
        )

        self.ipython.user_global_ns[name] = self.current_obj
        encoded_code = base64.b64encode(name.encode()).decode()
        display(Javascript("""
            var code = IPython.notebook.insert_cell_{0}('code');
            code.set_text(atob("{1}"));
        """.format('below', encoded_code)))


    def btn_eventhandler(self, obj):
        env_map = {
            '1':'https://catalogue.datalake.ihsmarkit.com/__api',
            '2':'https://catalogue-uat.datalake.ihsmarkit.com/__api',
            '3':'https://catalogue-qa.datalake.ihsmarkit.com/__api'
        }
        
        self.dl = session.start_session(
            self.api_key.value,
            root_url=env_map[str(self.env_dd.value)]
        )
        self.packages = self.dl.packages()
        self.package_dd.options = self.packages
        self.datasets = self.packages[list(self.packages.keys())[0]].datasets()
        self.dataset_dd.options = self.datasets

    def on_change_package(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
     
            self.current_obj = change["new"]
            self.dataset_dd.options = self.current_obj.datasets()
            #current_obj will be overwritten
            self.current_obj = change["new"]
            self.tab.children[0].value = redirect(self.current_obj.display)
            self.tab.children[1].value = str(self.current_obj.shape)
            self.tab.children[2].value = str(self.current_obj.description)
            self.tab.children[3].value = str(self.current_obj.__str__())
            self.tab.children[4].value = "\n".join([str(x) for x in 
                                               self.current_obj.datasets()])

    def on_change_dataset(self, change):
            
        if change['type'] == 'change' and change['name'] == 'value':
            self.current_obj = change["new"]
            self.tab.children[0].value = redirect(self.current_obj.display)
            self.tab.children[1].value = ""
            self.tab.children[2].value = ""
            self.tab.children[3].value = str(self.current_obj.__str__())
            self.tab.children[4].value = "\n".join([str(x) for x in 
                                               self.current_obj.instances.all()])

@magics_class
class DatasetSelectorMagic(Magics):

    @line_magic
    def dataset_selector(self, line):
        disp = SelectorWidget(self.parent)
        self.parent.user_global_ns['_widget'] = disp
        display(disp.root)


def load_ipython_extension(ipython):
    # The `ipython` argument is the currently active `InteractiveShell`
    # instance, which can be used in any way. This allows you to register
    # new magics or aliases, for example.
    ipython.register_magics(DatasetSelectorMagic)

def unload_ipython_extension(ipython):
    # If you want your extension to be unloadable, put that logic here.
    pass


test = {}

def show():
    get_ipython().magic('dataset_selector')


if __name__ != '__main__':
    get_ipython().extension_manager.load_extension('dli.gui')
    show()
