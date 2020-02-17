from collections import OrderedDict
from copy import deepcopy

from flex_forms.components import BaseStaticFlexField





class StaticFlexFieldsMetaclass(type):
    """
    Metaclass for collecting StaticFlexField fields from parent classes and assigning them to
    static_fields class variable.
    """

    def __new__(mcs, name, bases, attrs):
        static_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, BaseStaticFlexField):
                static_fields.append((key, value))
                attrs.pop(key)
        attrs['static_fields'] = OrderedDict(static_fields)

        new_class = super().__new__(mcs, name, bases, attrs)

        # Walk through the MRO.
        static_fields = OrderedDict()
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, 'static_fields'):
                static_fields.update(base.static_fields)
            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in static_fields:
                    static_fields.pop(attr)

        new_class.static_class_fields = static_fields

        return new_class
