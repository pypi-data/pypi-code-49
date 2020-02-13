# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DatepickerByInclusion(Component):
    """A DatepickerByInclusion component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- date (string; optional): The value displayed in the input.
- datesIncluded (list; optional): The value displayed in the input."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, date=Component.UNDEFINED, datesIncluded=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'date', 'datesIncluded']
        self._type = 'DatepickerByInclusion'
        self._namespace = 'datepicker_by_inclusion'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'date', 'datesIncluded']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DatepickerByInclusion, self).__init__(**args)
