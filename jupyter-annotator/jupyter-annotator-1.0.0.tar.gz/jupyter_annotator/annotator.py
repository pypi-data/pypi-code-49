"""
Code logic:
    The annotator first reads in the field names in the problem and stores them in a list to preseve the order of occurrence.
    Then, for each field, the annotator finds its max value length (for layout arrangement) and its type (list, str, dict...). 
    Lastly, it creates a dashboard, which consists of form widgets for each field (right) and a output preview area (left).
    Custom fields can also be inputted when instantiating an annotator using the following format: [(field_name1, type1, max_length1), (field_name2, type2, max_length2)].   
    E.g. [("aaa", list, 15), ("bbb", dict, 180)] 
"""

import json
import ipywidgets as widgets
from ast import literal_eval
from collections import OrderedDict
from .utility import string_to_list, list_to_string, most_common


class Annotator:
    """
    """
    def __init__(self, json_problems, custom_fields=None):
        
        self.problems = json_problems
        self.current_index = 0
        self.fields = []
        self.field_to_length = {}
        self.field_to_type = {}
        
        # Preprocess
        self._get_field_names()
        self._get_field_info()
        if custom_fields:
            self._handle_custom_fields(custom_fields)    
    
    
    def _get_field_names(self):
        """Read the field names from the input problems 
        
        Example (one problem): 
            problem = {'a': 123, 'b':345, 'c':789} --> field_names = ['a', 'b', 'c]'
        """
        for problem in self.problems:
            fields = problem.keys()
            new_fields = [field for field in fields if field not in self.fields]
            self.fields = self.fields + new_fields
    
    
    def _get_field_info(self):
        """Collect the max length of the text of each field for layout preparation, and collect the type of each field
        """
        for field in self.fields:
            self.field_to_length[field] = max([len(str(prob[field])) for prob in self.problems if field in prob])
            self.field_to_type[field] = most_common([type(prob[field]) for prob in self.problems if field in prob])
    
    
    def _handle_custom_fields(self, custom_fields):
        """If there exist custom fields, collect their  information
        """
        for field, field_type, field_length in custom_fields:
            if field not in self.fields:
                self.fields.append(field)
                self.field_to_type[field] = field_type
                self.field_to_length[field] = field_length

        
    def start(self):
        """Initialize the annotation environment and load the values from the current problem (the first problem)
        """
        self.initialize_dashboard()
        self.load_problem_info()

    
    def initialize_dashboard(self):
        """Initialize the annotation environment
        """
        height = 0
  
        # Form widgets
        layout_lg = widgets.Layout(flex='0 1 150px', height='100%', width='90%')
        layout_md = widgets.Layout(flex='0 1 50px', height='100%', width='90%')
        layout_sm = widgets.Layout(flex='0 1 20px', width='90%')        
        
        self.form_widgets = OrderedDict()
        for field in self.fields:
            if self.field_to_length[field] <= 20:
                layout = layout_sm
                height += 20
            elif self.field_to_length[field] <= 100:
                layout = layout_md
                height += 50
            else:
                layout = layout_lg
                height += 150
            self.form_widgets[field] = widgets.Textarea(description=f'{field.capitalize()}: ', layout=layout)
        
        # Buttons
        # The idea of these buttons takes reference from https://github.com/ideonate/jupyter-innotater
        prevbtn = widgets.Button(description='< Previous')
        nextbtn = widgets.Button(description='Next >')
        savebtn = widgets.Button(description='Save')
        restorebtn = widgets.Button(description='Restore')
        prevbtn.on_click(lambda _: self.change_index(-1))
        nextbtn.on_click(lambda _: self.change_index(1))
        savebtn.on_click(self.save)
        restorebtn.on_click(self.restore)
        buttons_layout = widgets.Layout(width='80%', height='35px')
        height += 35
        buttons = widgets.HBox([prevbtn, nextbtn, savebtn, restorebtn], layout=buttons_layout)
        
        # Dashboard
        form_layout = widgets.Layout(width='47%', justify_content ='space-around',  align_items='flex-end')
        preview_layout = widgets.Layout(width='43%')
        dashboard_layout = widgets.Layout(height=f'{height+16*len(self.fields)}px')
        form = widgets.VBox([*self.form_widgets.values(), buttons], layout=form_layout)
        form_output = widgets.interactive_output(self.display_func, self.form_widgets)
        preview = widgets.VBox([form_output], layout=preview_layout)
        dashboard = widgets.HBox([preview, form], layout=dashboard_layout)
        display(dashboard)

        
    def display_func(self, **form_widgets):
        """The display function for interactive_output widget
        """
        output = {}
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type == list:
                output[field] = string_to_list(form_widgets[field])
            elif field_type == dict:
                output[field] = literal_eval(form_widgets[field])
            else:
                output[field] = form_widgets[field]
        print(json.dumps(output, indent=4))

        
    def load_problem_info(self):
        """Load the field values of the current problem
        """
        current_problem = self.problems[self.current_index]
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type==list:
                self.form_widgets[field].value = list_to_string(current_problem[field]) if field in current_problem else ""
            elif field_type==dict:
                self.form_widgets[field].value = str(current_problem[field]) if field in current_problem else '{}'
            else:
                self.form_widgets[field].value = current_problem[field] if field in current_problem else ""
 
 
    def change_index(self, change):
        """Jump to the previous or next problem
        """
        if change < 0 < self.current_index:
            self.current_index -= 1
        elif change > 0 and self.current_index < len(self.problems) -1:
            self.current_index += 1
        
        # Reload the problem info
        self.load_problem_info()
            
            
    def save(self, change):
        """Save the annotations back to the problem
        """
        current_problem = self.problems[self.current_index]
        for field in self.fields:
            field_type = self.field_to_type[field]
            if field_type == list:
                current_problem[field] = string_to_list(self.form_widgets[field].value)
            elif field_type == dict:
                current_problem[field] = literal_eval(self.form_widgets[field].value)
            else:
                current_problem[field] = self.form_widgets[field].value
        
        
    def restore(self, change):
        """Restore 
        """
        # Reload the problem info
        self.load_problem_info()