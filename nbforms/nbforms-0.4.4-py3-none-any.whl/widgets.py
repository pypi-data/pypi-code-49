####################################
##### nbforms Question Widgets #####
####################################

from ipywidgets import RadioButtons, SelectMultiple, Text, Textarea, RadioButtons, HBox, Label

class MultipleChoiceQuestion:
    def __init__(self, config):
        self._question = config["question"]
        self._options = config["options"]

    def to_widget_tuple(self):
        return Label(self._question), RadioButtons(
            options=self._options
        )

class CheckboxQuestion:
    def __init__(self, config):
        self._question = config["question"]
        self._options = config["options"]

    def to_widget_tuple(self):
        return Label(self._question), SelectMultiple(
            options=self._options
        )

class TextQuestion:
    def __init__(self, config):
        self._question = config["question"]
        try:
            self._placeholder = config["placeholder"]
        except KeyError:
            self._placeholder = "Type something"

    def to_widget_tuple(self):
        return Label(self._question), Text(
            placeholder=self._placeholder
        )

class TextAreaQuestion:
    def __init__(self, config):
        self._question = config["question"]
        try:
            self._placeholder = config["placeholder"]
        except KeyError:
            self._placeholder = "Type something"

    def to_widget_tuple(self):
        return Label(self._question), Textarea(
            placeholder=self._placeholder
        )

TYPE_MAPPING = {
    'multiplechoice': MultipleChoiceQuestion,
    'checkbox': CheckboxQuestion,
    'text': TextQuestion,
    'paragraph': TextAreaQuestion
}
