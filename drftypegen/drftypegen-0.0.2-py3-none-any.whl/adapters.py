import logging

from collections import OrderedDict
from rest_framework.fields import *
from rest_framework import serializers as r_s

logger = logging.getLogger(__name__)

DRF_COMPOSITE_FIELDS = ["ListSerializer", "ManyRelatedField"]

DRF_LIST_FIELDS = ["ListSerializer", "ManyRelatedField"]

DRF_COMPOSITE_FIELD_RELATION_NAMES = {"ListSerializer": "child", "ManyRelatedField": "child_relation"}

DRF_FIELDS = {
        BooleanField: "boolean",
        NullBooleanField: "boolean",

        CharField: "string",
        EmailField: "string",
        RegexField: "string",
        SlugField: "string",
        URLField: "string",
        UUIDField: "string",
        FilePathField: "string",
        IPAddressField: "string",

        IntegerField: "integer",
        FloatField: "number",
        DecimalField: "number",

        DateTimeField: "string",
        DateField: "string",
        TimeField: "string",
        DurationField: "string",

        ChoiceField: "string",
        MultipleChoiceField: "string",

        FileField: "string",
        ImageField: "string",

        ListField: "list",
        DictField: "dict",

        JSONField: "json",

        r_s.PrimaryKeyRelatedField: "integer",
        r_s.ManyRelatedField: "list"
    }


class BaseAdapter:

    def __init__(self, serializer):
        self.serializer = serializer
        self.instance = serializer()

    def transform_field(self, field):
        return {
            "read_only": False,
            "write_only": False,
            "required": True,
        }

    def get_serializer_fields(self):
        return OrderedDict([])

    def get_transformed_data(self):
        fields = self.get_serializer_fields()
        nested = []
        data = OrderedDict([])

        for field in fields.items():
            logger.critical(field[0])
            logger.critical(field[1])
            logger.critical("=====")
            field_data = self.transform_field(field)
            data[field[0]] = field_data[0]
            nested += field_data[1]
        if hasattr(self.serializer.Meta, 'model'):
            name = self.serializer.Meta.model.__name__
        else:
            name = self.serializer.__name__
        nested.append({
            'name': name,
            'fields': data
        })
        return nested


class SerializerAdapter(BaseAdapter):
    def get_serializer_fields(self):
        return self.instance.get_fields()

    def transform_field(self, field):
        nested = []
        data = {
            'name': field[0],
            'read_only': field[1].read_only,
            'write_only': field[1].write_only,
            'required': field[1].required,
            'nullable': field[1].allow_null,
        }
        field_class = field[1].__class__
        type_data = DRF_FIELDS.get(field_class, None)
        data['openapi_type'] = type_data
        data['type'] = field_class.__name__
        if data['type'] in DRF_COMPOSITE_FIELDS:
            child_class = getattr(field[1], DRF_COMPOSITE_FIELD_RELATION_NAMES[data["type"]]).__class__
            if child_class.__name__ == "PrimaryKeyRelatedField":
                data['child'] = 'number'
            else:
                nested_data = SerializerAdapter(child_class).get_transformed_data()
                data['child'] = nested_data[0]["name"]
                nested.extend(nested_data)
        return data, nested
