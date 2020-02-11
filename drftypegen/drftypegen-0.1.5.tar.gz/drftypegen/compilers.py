import logging
from django.conf import settings
from .adapters import *

from pprint import pformat

logger = logging.getLogger(__name__)


class BaseCompiler:
    adapter_class = None

    def generate_field(self, data):
        return "Not Implemented"

    def generate_serializer_body(self, serializer_data):
        return "Not Implemented"

    def generate(self, additional_serializers=[]):
        return "Not Implemented"


TS_TYPE_MAP = {
    "integer": "number",
    "float": "number",
    "decimal": "string",
    "json": "any",
}


class TypeScriptCompiler(BaseCompiler):
    def __init__(self, adapter_class=SerializerAdapter):
        self.adapter_class = adapter_class

    def generate_field(self, data):
        if data["type"] in DRF_LIST_FIELDS:
            dtype = f"Array<{data['child']}>"
        elif data["type"] == "StreamField":
            dtype = f"Array<{' | '.join(data['openapi_type'])}>"
        else:
            dtype = TS_TYPE_MAP.get(data["openapi_type"], data["openapi_type"])

        if data["nullable"]:
            dtype = f"{dtype} | null"
        return f"\t{'readonly ' if data['read_only'] else ''}{data['name']}{'?' if not data['required'] and not data['read_only'] else ''}: {dtype};"

    def generate_serializer_body(self, serializer_data):
        # logger.critical(serializer_data)
        if serializer_data.get("stream", False):
            type = " | ".join([d["openapi_type"] for d in serializer_data["fields"]])
            return f"type {serializer_data['name']} = {type};"
        else:
            try:
                values = serializer_data["fields"].values()
            except:
                values = serializer_data["fields"]
            return "\n".join(
                [
                    f"export interface {serializer_data['name']} {{",
                    *[self.generate_field(field) for field in values],
                    "}",
                ]
            )

    def generate(self, additional_serializers=[]):
        data = self.adapter_class.get_all_serializer_data(additional_serializers)
        interface = [self.generate_serializer_body(sbody) for sbody in data]
        return "\n\n".join(interface)
