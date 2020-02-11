import inspect

from django import forms
from django.forms.utils import ErrorList
import os
from django.conf import settings

from codemirror import CodeMirrorFormField, CodeMirrorTextarea
from codemirror import addon


def mode_choices():
    mode_dir = os.path.join(settings.BASE_DIR, 'mirror/static/codemirror/mode')
    mode = os.listdir(mode_dir)
    return zip(mode, mode)


def addon_choices():
    return list(
        map(lambda x: (x[0], x[0]),
            filter(lambda v: 'Base' not in v[0], inspect.getmembers(addon, inspect.isclass))))


class CodeMirrorForm(forms.Form):
    mode = forms.ChoiceField(
        label='mode',
        required=True,
        choices=mode_choices(),
    )
    addon = forms.MultipleChoiceField(
        label='addon',
        required=False,
        choices=addon_choices(),
    )

    # code = CodeMirrorFormField(
    #     required=False,
    # )

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, field_order=None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        if data:
            mode = data.get('mode')
            addons = data.get('addon', [])[:]
            for i, add in enumerate(addons):
                addons[i] = getattr(addon, add)
        else:
            mode = None
            addons = ()

        widget = CodeMirrorTextarea(
            mode=mode,
            addon_js=addons,
            theme='twilight'
        )
        self.fields['code'] = CodeMirrorFormField(
            widget=widget,
            required=False,
        )
