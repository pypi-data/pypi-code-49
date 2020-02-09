import logging
from django.conf import settings
from .adapters import *

logger = logging.getLogger(__name__)


class BaseCompiler:
    adapter_class = None

    def treverse_urls(self, root_pattern):
        patterns = []
        for pattern in root_pattern:
            try:
                patterns += self.treverse_urls(pattern.url_patterns)
            except:
                patterns.append(pattern)
        return patterns

    @staticmethod
    def apiview_filter(view_callback):
        if hasattr(view_callback, "view_class"):
            if hasattr(view_callback.view_class, "serializer_class"):
                return True
        return False

    def get_all_serializer_data(self, additional_serializers=[]):
        root_urlconf = __import__(settings.ROOT_URLCONF)
        all_urlpatterns = root_urlconf.urls.urlpatterns
        url_patterns = self.treverse_urls(all_urlpatterns)
        serializers = [
            p.callback.view_class.serializer_class
            for p in url_patterns
            if self.apiview_filter(p.callback)
        ] + additional_serializers
        data = [
            self.adapter_class(serializer).get_transformed_data()
            for serializer in serializers
        ]
        data = [val for sublist in data for val in sublist]
        return data

    def generate_field(self, data):
        return "Not Implemented"

    def generate_serializer_body(self, serializer_data):
        return "Not Implemented"

    def generate(self, additional_serializers=[]):
        return "Not Implemented"


class TypeScriptCompiler(BaseCompiler):
    adapter_class = SerializerAdapter

    def generate_field(self, data):
        if data["type"] in DRF_LIST_FIELDS:
            dtype = f"Array<{data['child']}>"
        else:
            dtype = data["openapi_type"]

        if data["nullable"]:
            dtype = f"{dtype} | null"
        return f"\t{'readonly ' if data['read_only'] else ''}{data['name']}{'?' if not data['required'] and not data['read_only'] else ''}: {dtype};"

    def generate_serializer_body(self, serializer_data):
        return "\n".join(
            [
                f"export interface {serializer_data['name']} {{",
                *[
                    self.generate_field(field)
                    for field in serializer_data["fields"].values()
                ],
                "}",
            ]
        )

    def generate(self, additional_serializers=[]):
        data = self.get_all_serializer_data(additional_serializers)
        interface = [self.generate_serializer_body(sbody) for sbody in data]
        return "\n\n".join(interface)
