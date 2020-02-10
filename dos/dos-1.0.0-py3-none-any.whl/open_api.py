import collections

from http.client import responses

from dos import prop as open_api_prop
from dos import prop_wrapper as open_api_prop_wrapper


class OpenAPI(collections.OrderedDict):
    def __init__(self, title, version, description=None):
        super(OpenAPI, self).__init__()
        self["_disclaimer"] = []
        self["openapi"] = '3.0.0'
        self["info"] = {
            "version": version,
            "title": title,
            "description": description
        }
        self["tags"] = []
        self["components"] = {
            "responses": {},
            "requestBodies": {},
            "schemas": {}
        }
        self["paths"] = {}

    def add_disclaimer(self, disclaimer):
        self["_disclaimer"].append(
            disclaimer
        )

    def add_contact(self, name=None, url=None, email=None):
        contact = {}

        if name is not None:
            contact["name"] = name

        if url is not None:
            contact["url"] = url

        if email is not None:
            contact["email"] = email

        self["info"]["contact"] = contact

    def add_logo(self, url, background_color, alt_text=None, href=None):
        self["info"]["x-logo"] = {
            "url": url,
            "backgroundColor": background_color,
            "altText": alt_text,
            "href": href
        }

    def add_tag(self, tag_name, tag_description):
        self["tags"].append({
            "name": get_tag_name(tag_name),
            "description": tag_description
        })

    def add_path(self, path):
        self["paths"].update(
            path
        )

    def add_schema(self, path, suffix, schema_dict):

        if isinstance(schema_dict, open_api_prop.Object):
            return self.add_schema(path, suffix, schema_dict.structure)

        if isinstance(schema_dict, open_api_prop.Array):
            return self.add_schema(path, suffix, schema_dict.repeated_structure)

        open_api_schema_dict = {}

        schema_name = path.replace('/', '_')[1:] + "_" + suffix

        open_api_schema_dict[schema_name] = {
            "required": [],
            "properties": {},
            "type": "object",
        }

        for name, prop in schema_dict.items():

            if isinstance(prop, open_api_prop.Prop):

                if prop.required:
                    open_api_schema_dict[schema_name]["required"].append(name)

                if prop.prop_type == open_api_prop.Object.prop_type:
                    open_api_schema_dict[schema_name]["properties"][name] = get_object_dict(self, prop, suffix + "_" + name, path)
                elif prop.prop_type == open_api_prop.Array.prop_type:
                    open_api_schema_dict[schema_name]["properties"][name] = get_array_dict(self, prop, suffix + "_" + name, path)
                else:
                    open_api_schema_dict[schema_name]["properties"][name] = get_prop_dict(prop)

            elif isinstance(prop, open_api_prop_wrapper.PropWrapper):
                if prop.prop_wrapper_type == open_api_prop_wrapper.OpenAPIPropWrapperType.ONE_OF:

                    object_iterator = 0
                    array_iterator = 0

                    dict_of_prop_wrapper_to_add = {
                        "oneOf": []
                    }

                    for list_prop in prop.prop_list:
                        if list_prop.prop_type == open_api_prop.Object.prop_type:
                            full_suffix = suffix + "_" + name + "_object_" + str(object_iterator)
                            dict_of_prop_wrapper_to_add["oneOf"].append(get_object_reference_dict(self, list_prop, full_suffix, path))
                            object_iterator += 1
                        elif list_prop.prop_type == open_api_prop.Array.prop_type:
                            full_suffix = suffix + "_" + name + "_array_" + str(array_iterator)
                            dict_of_prop_wrapper_to_add["oneOf"].append(get_array_dict(self, list_prop, full_suffix, path))
                            array_iterator += 1
                        else:
                            dict_of_prop_wrapper_to_add["oneOf"].append(get_prop_dict(list_prop))

                    open_api_schema_dict[schema_name]["properties"][name] = dict_of_prop_wrapper_to_add

            else:
                raise Exception("prop must be an instance of Prop or PropWrapper!!")

        self["components"]["schemas"].update(
            open_api_schema_dict
        )

        return schema_name

    def add_response(self, response):
        self["components"]["responses"].update(
            response
        )

    def add_request_body(self, request_body):
        self["components"]["requestBodies"].update(
            request_body
        )

    def document(self, module, path, http_method):
        if hasattr(module, 'input_schema') and hasattr(module, 'output_schema'):

            input_schema_name = self.add_schema(path, "input", module.input_schema())

            output_schemas = []
            for section in module.output_schema():
                output_schema_name = self.add_schema(path, str(section.value) + "_output", module.output_schema()[section])
                output_schemas.append({
                    "http_code": section,
                    "schema_name": output_schema_name
                })

            request_body = create_request_body(input_schema_name)

            self.add_request_body(request_body)
            self.add_response(create_response())
            self.add_path(create_path(path, http_method, output_schemas, input_schema_name))


def create_request_body(schema_name):
    return {
        schema_name: {
            "content": {
                "application/json": {
                    "schema": {
                        "$ref": "#/components/schemas/" + schema_name
                    }
                }
            },
            "required": True
        }
    }


def create_response():
    return {
        "ParseError": {
            "description": "When a mask can't be parsed"
        },
        "MaskError": {
            "description": "When any error occurs on mask"
        }
    }


def create_path(path, http_method, output_schemas, input_schema_name):

    # /plan/get -> ["plan", "get"]
    full_url_path = list(filter(lambda a: a != "", path.strip().split('/')))

    path_dict = {
        path: {
            http_method: {
                "responses": {},
                "operationId": path,
                "tags": [
                    get_tag_name(full_url_path[0])
                ]
            }
        }
    }

    path_dict[path][http_method]["requestBody"] = {
        "$ref": "#/components/requestBodies/" + input_schema_name
    }

    for schema in output_schemas:

        description = responses.get(schema["http_code"])

        if description is None:
            raise Exception(f"{schema['http_code']} is not a valid http code!!")

        path_dict[path][http_method]["responses"].update({
            schema["http_code"]: {
                "description": description,
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/" + schema["schema_name"]
                        }
                    }
                }
            }
        })

    return path_dict


def get_prop_dict(prop):

    dictionary = {
        "type": prop.prop_type.value,
        "nullable": prop.nullable,
    }

    if prop.description is not None:
        dictionary["description"] = prop.description

    return dictionary


def get_object_reference_dict(self, prop, suffix, path):
    schema_name = self.add_schema(path, suffix, prop)

    return {
        "$ref": "#/components/schemas/" + schema_name
    }


def get_object_dict(self, prop, suffix, path):
    dict_of_prop_to_add = get_prop_dict(prop)
    dict_of_prop_to_add["allOf"] = [get_object_reference_dict(self, prop, suffix, path)]
    return dict_of_prop_to_add


def get_array_dict(self, prop, suffix, path):
    dict_of_prop_to_add = get_prop_dict(prop)

    if (prop.repeated_structure.prop_type == open_api_prop.Object.prop_type or
            prop.repeated_structure.prop_type == open_api_prop.Array.prop_type):
        nested_schema_name = self.add_schema(path, suffix, prop.repeated_structure)
        dict_of_prop_to_add["items"] = {"$ref": "#/components/schemas/" + nested_schema_name}
    else:
        dict_of_prop_to_add["items"] = {
            "type": str(prop.repeated_structure.prop_type.value) + "s"
        }

    return dict_of_prop_to_add


def get_tag_name(initial_name):
    return initial_name.lower().replace("_", " ").title()
