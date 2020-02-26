import functools
import json
import os

import pkg_resources
from elasticsearch import VERSION as ES_VERSION
from invenio_base.signals import app_loaded
from jsonpointer import JsonPointer
from jsonref import JsonRef
from pkg_resources import iter_entry_points


def patch_elasticsearch():
    from elasticsearch.client import IndicesClient

    # patch elasticsearch
    old_create_method = IndicesClient.create

    @functools.lru_cache(maxsize=1)
    def load_included_mappings():
        included_mappings = {}
        for ep in iter_entry_points('invenio_oarepo_mapping_includes'):
            package_name = '{}.v{}'.format(ep.module_name, ES_VERSION[0])
            package_name = package_name.split('.', maxsplit=1)
            package_path = package_name[1].replace('.', '/')
            for filename in pkg_resources.resource_listdir(package_name[0], package_path):
                if filename.endswith('.json'):
                    file_data = pkg_resources.resource_string(
                        package_name[0],
                        os.path.join(package_path, filename))
                    included_mappings[filename] = json.loads(file_data.decode("utf-8"))
        return included_mappings

    def included_mappings(mapping_name):
        return load_included_mappings()[mapping_name]

    def create(*args, **kwargs):
        def _resolve_mappings(body):
            # from: https://stackoverflow.com/a/39016088
            def item_generator(json_input, lookup_key):
                if isinstance(json_input, dict):
                    for k, v in list(json_input.items()):
                        if k == lookup_key:
                            yield json_input
                        else:
                            yield from item_generator(v, lookup_key)

                elif isinstance(json_input, list):
                    for item in json_input:
                        yield from item_generator(item, lookup_key)

            for el in item_generator(body, 'type'):
                if '#' in el['type']:
                    # referenced type - split it into filename and jsonpointer
                    el_type = el['type'].split('#', maxsplit=1)

                    # get mapping from loaded mappings
                    mapping = included_mappings(el_type[0])
                    ptr = JsonPointer(el_type[1])
                    included_mapping_type = ptr.resolve(mapping)
                    _resolve_mappings(included_mapping_type)
                    el.update(included_mapping_type)

            for el in item_generator(body, 'allOf'):
                if 'properties' in el:
                    props = {}
                    for el_type in el['allOf']:
                        props.update(el_type.get('properties', {}))

                    el['properties'].update(props)
                    el.pop('allOf')

        _resolve_mappings(kwargs['body'])

        ret = old_create_method(*args, **kwargs)
        print(ret)
        return ret

    IndicesClient.create = create


patch_elasticsearch()


@app_loaded.connect
def patch_jsonschemas(_sender, app, **kwargs):
    with app.app_context():
        from invenio_records.api import _records_state
        from .resolver import resolve_schema

        def patched_validate(data, schema, *args, **kwargs):
            if not isinstance(schema, dict):
                schema = {'$ref': schema}
            schema = JsonRef.replace_refs(schema, loader=_records_state.loader_cls())
            schema = resolve_schema(schema)
            return previous_validate(data, schema, *args, **kwargs)

        if _records_state.validate != patched_validate:
            previous_validate = _records_state.validate
            _records_state.validate = patched_validate


# do not export anything
__all__ = ()
