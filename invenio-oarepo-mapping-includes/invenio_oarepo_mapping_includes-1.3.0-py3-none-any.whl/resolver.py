# patched version of invenio_jsonschemas.utils.resolve_schema
from invenio_jsonschemas.utils import _merge_dicts


def resolve_schema(schema):
    def traverse(schema):
        if isinstance(schema, dict):
            if 'allOf' in schema:
                all_of = schema.pop('allOf')
                for x in all_of:
                    sub_schema = x
                    sub_schema.pop('title', None)
                    sub_schema.pop('$id', None)
                    schema = _merge_dicts(schema, sub_schema)
                schema = traverse(schema)
            elif 'properties' in schema:
                for x in schema.get('properties', []):
                    schema['properties'][x] = traverse(
                        schema['properties'][x])
            elif 'items' in schema:
                schema['items'] = traverse(schema['items'])
        return schema

    return traverse(schema)
