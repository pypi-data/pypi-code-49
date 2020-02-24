from typing import cast, Sequence, Union, Any, Mapping, Optional
from .openapi import *
from dataclasses import is_dataclass, fields

_TO_DICT_SUBS = {'_license': 'license', '_format': 'format', '_in': 'in', '_ref': '$ref', '_not': 'not', '_type': 'type', '_default': 'default'}

def convert_to_str(d: Any) -> str:
    if not isinstance(d, str):
        raise ValueError('%s is not a string' % str(d))
    return cast(str, d)

def convert_to_sequence_str(d: Any) -> Sequence[str]:
    if not isinstance(d, list):
        raise ValueError('%s is not a list' % str(d))
    for x in d:
        if not isinstance(x, str):
            raise ValueError('%s is not a str' % str(x))
    return cast(str, d)

def convert_to_Responses(d: Any) -> Responses:
    responses: Responses
    if not isinstance(d, dict):
        raise ValueError('obj must be of type `dict`, instead got %s' % str(type(d)))
    else:
        _ret = dict()
        for k, v in d.items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('obj can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Response(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                raise e #ValueError('%s\nKey %s has a value %s which cannot be cast to Union[Response, Reference].' % (str(e), k, str(v)))
        responses = cast(Responses, _ret)
    return responses

def convert_to_Callback(d: Any) -> Callback:
    callback: Callback
    if not isinstance(d, dict):
        raise ValueError('obj must be of type `dict`, instead got %s' % str(type(d)))
    else:
        _ret = dict()
        for k, v in d.items():
            if type(k) != str:
                raise ValueError('obj can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_PathItem(v)
            except Exception as e:
                raise ValueError('%s\nKey %s has a value %s which cannot be cast to PathItem.' % (str(e), k, str(v)))
        callback = cast(Callback, _ret)
    return callback

def convert_to_Paths(d: Any) -> Paths:
    paths: Paths
    if not isinstance(d, dict):
        raise ValueError('obj must be of type `dict`, instead got %s' % str(type(d)))
    else:
        _ret = dict()
        for k, v in d.items():
            if type(k) != str:
                raise ValueError('obj can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_PathItem(v)
            except Exception as e:
                raise ValueError('%s\nKey %s has a value %s which cannot be cast to PathItem.' % (str(e), k, str(v)))
        paths = cast(Paths, _ret)
    return paths

def convert_to_SecurityRequirement(d: Any) -> SecurityRequirement:
    securityRequirement: SecurityRequirement
    if not isinstance(d, dict):
        raise ValueError('obj must be of type `dict`, instead got %s' % str(type(d)))
    else:
        _ret = dict()
        for k, v in d.items():
            if type(k) != str:
                raise ValueError('obj can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_sequence_str(v)
            except:
                raise ValueError('Key %s has a value %s which cannot be cast to PathItem.' % (k, str(v)))
        securityRequirement = cast(SecurityRequirement, _ret)
    return securityRequirement

def convert_to_SecurityScheme(d: Any) -> SecurityScheme:
    try:
        return convert_to_APIKeySecurityScheme(d)
    except:
        try:
            return convert_to_HTTPSecurityScheme(d)
        except:
            try:
                return convert_to_OAuth2SecurityScheme(d)
            except:
                try:
                    return convert_to_OpenIdConnectSecurityScheme(d)
                except:
                    if isinstance(d, str):
                        return cast(str, d)
                    else:
                        raise ValueError('%s is not a valid SecurityScheme' % str(d))

def convert_to_Any(d: Any) -> Any:
    return d

def convert_to_Discriminator(d: Any) -> Discriminator:
    if not isinstance(d, dict):
        raise ValueError("Discriminator must be a dictionary")
    propertyName: str
    if 'propertyName' not in d:
        raise ValueError('propertyName must be defined for Discriminator')
    if not isinstance(d['propertyName'], str):
        raise ValueError('propertyName must be of type `str` in Discriminator, instead got %s' % str(type(d['propertyName'])))
    propertyName = cast(str, d['propertyName'])
    mapping: Optional[Mapping[str, str]]
    if 'mapping' not in d:
        mapping = None
    elif not isinstance(d['mapping'], dict):
        raise ValueError('mapping must be of type `dict` in Discriminator, instead got %s' % str(type(d['mapping'])))
    else:
        _ret = dict()
        for k, v in d['mapping'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('mapping in Discriminator can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_str(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nmapping in Discriminator at key %s has a value %s which cannot be cast to str.' % (str(e), k, str(v)))
                raise e
        mapping = cast(Mapping[str, str], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Discriminator(
        propertyName=propertyName,
        mapping=mapping,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_ExternalDocumentation(d: Any) -> ExternalDocumentation:
    if not isinstance(d, dict):
        raise ValueError("ExternalDocumentation must be a dictionary")
    url: str
    if 'url' not in d:
        raise ValueError('url must be defined for ExternalDocumentation')
    if not isinstance(d['url'], str):
        raise ValueError('url must be of type `str` in ExternalDocumentation, instead got %s' % str(type(d['url'])))
    url = cast(str, d['url'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in ExternalDocumentation, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return ExternalDocumentation(
        url=url,
        description=description,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_XML(d: Any) -> XML:
    if not isinstance(d, dict):
        raise ValueError("XML must be a dictionary")
    name: Optional[str]
    if 'name' not in d:
        name = None
    elif not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in XML, instead got %s' % str(type(d['name'])))
    else:
        name = cast(str, d['name'])
    namespace: Optional[str]
    if 'namespace' not in d:
        namespace = None
    elif not isinstance(d['namespace'], str):
        raise ValueError('namespace must be of type `str` in XML, instead got %s' % str(type(d['namespace'])))
    else:
        namespace = cast(str, d['namespace'])
    prefix: Optional[str]
    if 'prefix' not in d:
        prefix = None
    elif not isinstance(d['prefix'], str):
        raise ValueError('prefix must be of type `str` in XML, instead got %s' % str(type(d['prefix'])))
    else:
        prefix = cast(str, d['prefix'])
    attribute: Optional[bool]
    if 'attribute' not in d:
        attribute = None
    elif not isinstance(d['attribute'], bool):
        raise ValueError('attribute must be of type `bool` in XML, instead got %s' % str(type(d['attribute'])))
    else:
        attribute = cast(bool, d['attribute'])
    wrapped: Optional[bool]
    if 'wrapped' not in d:
        wrapped = None
    elif not isinstance(d['wrapped'], bool):
        raise ValueError('wrapped must be of type `bool` in XML, instead got %s' % str(type(d['wrapped'])))
    else:
        wrapped = cast(bool, d['wrapped'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return XML(
        name=name,
        namespace=namespace,
        prefix=prefix,
        attribute=attribute,
        wrapped=wrapped,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Reference(d: Any) -> Reference:
    if not isinstance(d, dict):
        raise ValueError("Reference must be a dictionary")
    _ref: str
    if '$ref' not in d:
        raise ValueError('$ref must be defined for Reference')
    if not isinstance(d['$ref'], str):
        raise ValueError('$ref must be of type `str` in Reference, instead got %s' % str(type(d['$ref'])))
    _ref = cast(str, d['$ref'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Reference(
        _ref=_ref,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Schema(d: Any) -> Schema:
    if not isinstance(d, dict):
        raise ValueError("Schema must be a dictionary")
    title: Optional[str]
    if 'title' not in d:
        title = None
    elif not isinstance(d['title'], str):
        raise ValueError('title must be of type `str` in Schema, instead got %s' % str(type(d['title'])))
    else:
        title = cast(str, d['title'])
    multipleOf: Optional[float]
    if 'multipleOf' not in d:
        multipleOf = None
    elif not isinstance(d['multipleOf'], float):
        raise ValueError('multipleOf must be of type `float` in Schema, instead got %s' % str(type(d['multipleOf'])))
    else:
        multipleOf = cast(float, d['multipleOf'])
    maximum: Optional[float]
    if 'maximum' not in d:
        maximum = None
    elif not isinstance(d['maximum'], float):
        raise ValueError('maximum must be of type `float` in Schema, instead got %s' % str(type(d['maximum'])))
    else:
        maximum = cast(float, d['maximum'])
    exclusiveMaximum: Optional[Union[bool, int]]
    if 'exclusiveMaximum' not in d:
        exclusiveMaximum = None
    elif (not isinstance(d['exclusiveMaximum'], bool)) and (not isinstance(d['exclusiveMaximum'], int)):
        raise ValueError('exclusiveMaximum must be of type `bool` or `int` in Schema, instead got %s' % str(type(d['exclusiveMaximum'])))
    else:
        exclusiveMaximum = cast(Union[bool, int], d['exclusiveMaximum'])
    minimum: Optional[float]
    if 'minimum' not in d:
        minimum = None
    elif not isinstance(d['minimum'], float):
        raise ValueError('minimum must be of type `float` in Schema, instead got %s' % str(type(d['minimum'])))
    else:
        minimum = cast(float, d['minimum'])
    exclusiveMinimum: Optional[Union[bool, int]]
    if 'exclusiveMinimum' not in d:
        exclusiveMinimum = None
    elif (not isinstance(d['exclusiveMinimum'], bool)) and (not isinstance(d['exclusiveMinimum'], int)):
        raise ValueError('exclusiveMinimum must be of type `bool` or `int` in Schema, instead got %s' % str(type(d['exclusiveMinimum'])))
    else:
        exclusiveMinimum = cast(Union[bool, int], d['exclusiveMinimum'])
    maxLength: Optional[int]
    if 'maxLength' not in d:
        maxLength = None
    elif not isinstance(d['maxLength'], int):
        raise ValueError('maxLength must be of type `int` in Schema, instead got %s' % str(type(d['maxLength'])))
    else:
        maxLength = cast(int, d['maxLength'])
    minLength: Optional[int]
    if 'minLength' not in d:
        minLength = None
    elif not isinstance(d['minLength'], int):
        raise ValueError('minLength must be of type `int` in Schema, instead got %s' % str(type(d['minLength'])))
    else:
        minLength = cast(int, d['minLength'])
    pattern: Optional[str]
    if 'pattern' not in d:
        pattern = None
    elif not isinstance(d['pattern'], str):
        raise ValueError('pattern must be of type `str` in Schema, instead got %s' % str(type(d['pattern'])))
    else:
        pattern = cast(str, d['pattern'])
    maxItems: Optional[int]
    if 'maxItems' not in d:
        maxItems = None
    elif not isinstance(d['maxItems'], int):
        raise ValueError('maxItems must be of type `int` in Schema, instead got %s' % str(type(d['maxItems'])))
    else:
        maxItems = cast(int, d['maxItems'])
    minItems: Optional[int]
    if 'minItems' not in d:
        minItems = None
    elif not isinstance(d['minItems'], int):
        raise ValueError('minItems must be of type `int` in Schema, instead got %s' % str(type(d['minItems'])))
    else:
        minItems = cast(int, d['minItems'])
    uniqueItems: Optional[bool]
    if 'uniqueItems' not in d:
        uniqueItems = None
    elif not isinstance(d['uniqueItems'], bool):
        raise ValueError('uniqueItems must be of type `bool` in Schema, instead got %s' % str(type(d['uniqueItems'])))
    else:
        uniqueItems = cast(bool, d['uniqueItems'])
    maxProperties: Optional[int]
    if 'maxProperties' not in d:
        maxProperties = None
    elif not isinstance(d['maxProperties'], int):
        raise ValueError('maxProperties must be of type `int` in Schema, instead got %s' % str(type(d['maxProperties'])))
    else:
        maxProperties = cast(int, d['maxProperties'])
    minProperties: Optional[int]
    if 'minProperties' not in d:
        minProperties = None
    elif not isinstance(d['minProperties'], int):
        raise ValueError('minProperties must be of type `int` in Schema, instead got %s' % str(type(d['minProperties'])))
    else:
        minProperties = cast(int, d['minProperties'])
    required: Optional[Sequence[str]]
    if 'required' not in d:
        required = None
    elif not isinstance(d['required'], list):
        raise ValueError('required must be of type `list` in Schema, instead got %s' % str(type(d['required'])))
    else:
        _ret = []
        for k in d['required']:
            try:
                _ret.append(convert_to_str(k))
            except Exception as e:
                #raise ValueError('%s\nrequired in Schema has a value %s which cannot be cast to str.' % (str(e), str(k)))
                raise e
        required = cast(Sequence[str], _ret)
    enum: Optional[Sequence[Any]]
    if 'enum' not in d:
        enum = None
    elif not isinstance(d['enum'], list):
        raise ValueError('enum must be of type `list` in Schema, instead got %s' % str(type(d['enum'])))
    else:
        _ret = []
        for k in d['enum']:
            try:
                _ret.append(convert_to_Any(k))
            except Exception as e:
                #raise ValueError('%s\nenum in Schema has a value %s which cannot be cast to Any.' % (str(e), str(k)))
                raise e
        enum = cast(Sequence[Any], _ret)
    allOf: Optional[Sequence[Union[Schema, Reference]]]
    if 'allOf' not in d:
        allOf = None
    elif not isinstance(d['allOf'], list):
        raise ValueError('allOf must be of type `dict` in Schema, instead got %s' % str(type(d['allOf'])))
    else:
        _ret = []
        for k in d['allOf']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Schema(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                #raise ValueError('%s\nallOf in Schema has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), str(k)))
                raise e
        allOf = cast(Sequence[Union[Schema, Reference]], _ret)
    oneOf: Optional[Sequence[Union[Schema, Reference]]]
    if 'oneOf' not in d:
        oneOf = None
    elif not isinstance(d['oneOf'], list):
        raise ValueError('oneOf must be of type `dict` in Schema, instead got %s' % str(type(d['oneOf'])))
    else:
        _ret = []
        for k in d['oneOf']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Schema(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                #raise ValueError('%s\noneOf in Schema has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), str(k)))
                raise e
        oneOf = cast(Sequence[Union[Schema, Reference]], _ret)
    anyOf: Optional[Sequence[Union[Schema, Reference]]]
    if 'anyOf' not in d:
        anyOf = None
    elif not isinstance(d['anyOf'], list):
        raise ValueError('anyOf must be of type `dict` in Schema, instead got %s' % str(type(d['anyOf'])))
    else:
        _ret = []
        for k in d['anyOf']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Schema(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                #raise ValueError('%s\nanyOf in Schema has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), str(k)))
                raise e
        anyOf = cast(Sequence[Union[Schema, Reference]], _ret)
    items: Optional[Union[Sequence[Union[Schema, Reference]], Schema, Reference]]
    if 'items' not in d:
        items = None
    elif not isinstance(d['items'], list):
        try:
            items = convert_to_Reference(d['items'])
        except:
            try:
                items = convert_to_Schema(d['items'])
            except Exception as e:
                #raise ValueError('%s\nitems in Schema cannot be cast to Union[Schema, Reference].' % str(e))
                raise e
    else:
        _ret = []
        for k in d['items']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Schema(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                # raise ValueError('%s\nitems in items has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), str(k)))
                raise e
        items = cast(Sequence[Union[Schema, Reference]], _ret)
    properties: Optional[Mapping[str, Union[Schema, Reference]]]
    if 'properties' not in d:
        properties = None
    elif not isinstance(d['properties'], dict):
        raise ValueError('properties must be of type `dict` in Schema, instead got %s' % str(type(d['properties'])))
    else:
        _ret = dict()
        for k, v in d['properties'].items():
            if type(k) != str:
                raise ValueError('properties in Schema can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Schema(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nproperties in Schema at key %s has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), k, str(v)))
                raise e
        properties = cast(Mapping[str, Union[Schema, Reference]], _ret)
    additionalProperties: Optional[Union[Schema, Reference, bool]]
    if 'additionalProperties' not in d:
        additionalProperties = None
    else:
        try:
            additionalProperties = convert_to_Reference(d['additionalProperties'])
        except:
            try:
                additionalProperties = convert_to_Schema(d['additionalProperties'])
            except:
                if isinstance(d['additionalProperties'], bool):
                    additionalProperties = d['additionalProperties']
                else:
                    raise ValueError('additionalProperties in additionalProperties cannot be cast to Union[Schema, Reference].')
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Schema, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    default: Optional[Any]
    if 'default' not in d:
        default = None
    else:
        try:
            default = convert_to_Any(d['default'])
        except Exception as e:
            #raise ValueError('%s\ndefault must be of type `Any` in Schema, instead got %s' % (str(e), str(type(d['default']))))
            raise e
    nullable: Optional[bool]
    if 'nullable' not in d:
        nullable = None
    elif not isinstance(d['nullable'], bool):
        raise ValueError('nullable must be of type `bool` in Schema, instead got %s' % str(type(d['nullable'])))
    else:
        nullable = cast(bool, d['nullable'])
    discriminator: Optional[Discriminator]
    if 'discriminator' not in d:
        discriminator = None
    else:
        try:
            discriminator = convert_to_Discriminator(d['discriminator'])
        except Exception as e:
            #raise ValueError('%s\ndiscriminator must be of type `Discriminator` in Schema, instead got %s' % (str(e), str(type(d['discriminator']))))
            raise e
    readOnly: Optional[bool]
    if 'readOnly' not in d:
        readOnly = None
    elif not isinstance(d['readOnly'], bool):
        raise ValueError('readOnly must be of type `bool` in Schema, instead got %s' % str(type(d['readOnly'])))
    else:
        readOnly = cast(bool, d['readOnly'])
    writeOnly: Optional[bool]
    if 'writeOnly' not in d:
        writeOnly = None
    elif not isinstance(d['writeOnly'], bool):
        raise ValueError('writeOnly must be of type `bool` in Schema, instead got %s' % str(type(d['writeOnly'])))
    else:
        writeOnly = cast(bool, d['writeOnly'])
    example: Optional[Any]
    if 'example' not in d:
        example = None
    else:
        try:
            example = convert_to_Any(d['example'])
        except Exception as e:
            #raise ValueError('%s\nexample must be of type `Any` in Schema, instead got %s' % (str(e), str(type(d['example']))))
            raise e
    externalDocs: Optional[ExternalDocumentation]
    if 'externalDocs' not in d:
        externalDocs = None
    else:
        try:
            externalDocs = convert_to_ExternalDocumentation(d['externalDocs'])
        except Exception as e:
            #raise ValueError('%s\nexternalDocs must be of type `ExternalDocumentation` in Schema, instead got %s' % (str(e), str(type(d['externalDocs']))))
            raise e
    deprecated: Optional[bool]
    if 'deprecated' not in d:
        deprecated = None
    elif not isinstance(d['deprecated'], bool):
        raise ValueError('deprecated must be of type `bool` in Schema, instead got %s' % str(type(d['deprecated'])))
    else:
        deprecated = cast(bool, d['deprecated'])
    xml: Optional[XML]
    if 'xml' not in d:
        xml = None
    else:
        try:
            xml = convert_to_XML(d['xml'])
        except Exception as e:
            #raise ValueError('%s\nxml must be of type `XML` in Schema, instead got %s' % (str(e), str(type(d['xml']))))
            raise e
    _format: Optional[str]
    if 'format' not in d:
        _format = None
    elif not isinstance(d['format'], str):
        raise ValueError('format must be of type `str` in Schema, instead got %s' % str(type(d['format'])))
    else:
        _format = cast(str, d['format'])
    _type: Optional[str]
    if 'type' not in d:
        _type = None
    elif not isinstance(d['type'], str):
        raise ValueError('type must be of type `str` in Schema, instead got %s' % str(type(d['type'])))
    else:
        _type = cast(str, d['type'])
    _not: Optional[Union[Schema, Reference]]
    if 'not' not in d:
        _not = None
    elif not isinstance(d['not'], dict):
        raise ValueError('not must be of type `dict` in Schema, instead got %s' % str(type(d['not'])))
    else:
        try:
            _not = convert_to_Reference(d['not'])
        except:
            try:
                _not = convert_to_Schema(d['not'])
            except Exception as e:
                # raise ValueError('%s\nnot in Schema has a value %s which cannot be cast to Union[Schema, Reference].' % str(e))
                raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Schema(
        title=title,
        multipleOf=multipleOf,
        maximum=maximum,
        exclusiveMaximum=exclusiveMaximum,
        minimum=minimum,
        exclusiveMinimum=exclusiveMinimum,
        maxLength=maxLength,
        minLength=minLength,
        pattern=pattern,
        maxItems=maxItems,
        minItems=minItems,
        uniqueItems=uniqueItems,
        maxProperties=maxProperties,
        minProperties=minProperties,
        required=required,
        enum=enum,
        allOf=allOf,
        oneOf=oneOf,
        anyOf=anyOf,
        items=items,
        properties=properties,
        additionalProperties=additionalProperties,
        description=description,
        default=default,
        nullable=nullable,
        discriminator=discriminator,
        readOnly=readOnly,
        writeOnly=writeOnly,
        example=example,
        externalDocs=externalDocs,
        deprecated=deprecated,
        xml=xml,
        _format=_format,
        _type=_type,
        _not=_not,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Contact(d: Any) -> Contact:
    if not isinstance(d, dict):
        raise ValueError("Contact must be a dictionary")
    name: Optional[str]
    if 'name' not in d:
        name = None
    elif not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in Contact, instead got %s' % str(type(d['name'])))
    else:
        name = cast(str, d['name'])
    url: Optional[str]
    if 'url' not in d:
        url = None
    elif not isinstance(d['url'], str):
        raise ValueError('url must be of type `str` in Contact, instead got %s' % str(type(d['url'])))
    else:
        url = cast(str, d['url'])
    email: Optional[str]
    if 'email' not in d:
        email = None
    elif not isinstance(d['email'], str):
        raise ValueError('email must be of type `str` in Contact, instead got %s' % str(type(d['email'])))
    else:
        email = cast(str, d['email'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Contact(
        name=name,
        url=url,
        email=email,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_License(d: Any) -> License:
    if not isinstance(d, dict):
        raise ValueError("License must be a dictionary")
    name: str
    if 'name' not in d:
        raise ValueError('name must be defined for License')
    if not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in License, instead got %s' % str(type(d['name'])))
    name = cast(str, d['name'])
    url: Optional[str]
    if 'url' not in d:
        url = None
    elif not isinstance(d['url'], str):
        raise ValueError('url must be of type `str` in License, instead got %s' % str(type(d['url'])))
    else:
        url = cast(str, d['url'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return License(
        name=name,
        url=url,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Info(d: Any) -> Info:
    if not isinstance(d, dict):
        raise ValueError("Info must be a dictionary")
    title: str
    if 'title' not in d:
        raise ValueError('title must be defined for Info')
    if not isinstance(d['title'], str):
        raise ValueError('title must be of type `str` in Info, instead got %s' % str(type(d['title'])))
    title = cast(str, d['title'])
    version: str
    if 'version' not in d:
        raise ValueError('version must be defined for Info')
    if not isinstance(d['version'], str):
        raise ValueError('version must be of type `str` in Info, instead got %s' % str(type(d['version'])))
    version = cast(str, d['version'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Info, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    termsOfService: Optional[str]
    if 'termsOfService' not in d:
        termsOfService = None
    elif not isinstance(d['termsOfService'], str):
        raise ValueError('termsOfService must be of type `str` in Info, instead got %s' % str(type(d['termsOfService'])))
    else:
        termsOfService = cast(str, d['termsOfService'])
    contact: Optional[Contact]
    if 'contact' not in d:
        contact = None
    else:
        try:
            contact = convert_to_Contact(d['contact'])
        except Exception as e:
            #raise ValueError('%s\ncontact must be of type `Contact` in Info, instead got %s' % (str(e), str(type(d['contact']))))
            raise e
    _license: Optional[License]
    if 'license' not in d:
        _license = None
    else:
        try:
            _license = convert_to_License(d['license'])
        except Exception as e:
            #raise ValueError('%s\nlicense must be of type `License` in Info, instead got %s' % (str(e), str(type(d['license']))))
            raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Info(
        title=title,
        version=version,
        description=description,
        termsOfService=termsOfService,
        contact=contact,
        _license=_license,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_ServerVariable(d: Any) -> ServerVariable:
    if not isinstance(d, dict):
        raise ValueError("ServerVariable must be a dictionary")
    enum: Optional[Sequence[str]]
    if 'enum' not in d:
        enum = None
    elif not isinstance(d['enum'], list):
        raise ValueError('enum must be of type `list` in ServerVariable, instead got %s' % str(type(d['enum'])))
    else:
        _ret = []
        for k in d['enum']:
            try:
                _ret.append(convert_to_str(k))
            except Exception as e:
                #raise ValueError('%s\nenum in ServerVariable has a value %s which cannot be cast to str.' % (str(e), str(k)))
                raise e
        enum = cast(Sequence[str], _ret)
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in ServerVariable, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    _default: str
    if 'default' not in d:
        raise ValueError('default must be defined for ServerVariable')
    if not isinstance(d['default'], str):
        raise ValueError('default must be of type `str` in ServerVariable, instead got %s' % str(type(d['default'])))
    _default = cast(str, d['default'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return ServerVariable(
        enum=enum,
        description=description,
        _default=_default,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Server(d: Any) -> Server:
    if not isinstance(d, dict):
        raise ValueError("Server must be a dictionary")
    url: str
    if 'url' not in d:
        raise ValueError('url must be defined for Server')
    if not isinstance(d['url'], str):
        raise ValueError('url must be of type `str` in Server, instead got %s' % str(type(d['url'])))
    url = cast(str, d['url'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Server, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    variables: Optional[Mapping[str, ServerVariable]]
    if 'variables' not in d:
        variables = None
    elif not isinstance(d['variables'], dict):
        raise ValueError('variables must be of type `dict` in Server, instead got %s' % str(type(d['variables'])))
    else:
        _ret = dict()
        for k, v in d['variables'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('variables in Server can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_ServerVariable(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nvariables in Server at key %s has a value %s which cannot be cast to ServerVariable.' % (str(e), k, str(v)))
                raise e
        variables = cast(Mapping[str, ServerVariable], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Server(
        url=url,
        description=description,
        variables=variables,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Link(d: Any) -> Link:
    if not isinstance(d, dict):
        raise ValueError("Link must be a dictionary")
    operationId: Optional[str]
    if 'operationId' not in d:
        operationId = None
    elif not isinstance(d['operationId'], str):
        raise ValueError('operationId must be of type `str` in Link, instead got %s' % str(type(d['operationId'])))
    else:
        operationId = cast(str, d['operationId'])
    operationRef: Optional[str]
    if 'operationRef' not in d:
        operationRef = None
    elif not isinstance(d['operationRef'], str):
        raise ValueError('operationRef must be of type `str` in Link, instead got %s' % str(type(d['operationRef'])))
    else:
        operationRef = cast(str, d['operationRef'])
    parameters: Optional[Mapping[str, Any]]
    if 'parameters' not in d:
        parameters = None
    elif not isinstance(d['parameters'], dict):
        raise ValueError('parameters must be of type `dict` in Link, instead got %s' % str(type(d['parameters'])))
    else:
        _ret = dict()
        for k, v in d['parameters'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('parameters in Link can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_Any(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nparameters in Link at key %s has a value %s which cannot be cast to Any.' % (str(e), k, str(v)))
                raise e
        parameters = cast(Mapping[str, Any], _ret)
    requestBody: Optional[Any]
    if 'requestBody' not in d:
        requestBody = None
    else:
        try:
            requestBody = convert_to_Any(d['requestBody'])
        except Exception as e:
            #raise ValueError('%s\nrequestBody must be of type `Any` in Link, instead got %s' % (str(e), str(type(d['requestBody']))))
            raise e
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Link, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    server: Optional[Server]
    if 'server' not in d:
        server = None
    else:
        try:
            server = convert_to_Server(d['server'])
        except Exception as e:
            #raise ValueError('%s\nserver must be of type `Server` in Link, instead got %s' % (str(e), str(type(d['server']))))
            raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Link(
        operationId=operationId,
        operationRef=operationRef,
        parameters=parameters,
        requestBody=requestBody,
        description=description,
        server=server,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Example(d: Any) -> Example:
    if not isinstance(d, dict):
        raise ValueError("Example must be a dictionary")
    summary: Optional[str]
    if 'summary' not in d:
        summary = None
    elif not isinstance(d['summary'], str):
        raise ValueError('summary must be of type `str` in Example, instead got %s' % str(type(d['summary'])))
    else:
        summary = cast(str, d['summary'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Example, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    value: Optional[Any]
    if 'value' not in d:
        value = None
    else:
        try:
            value = convert_to_Any(d['value'])
        except Exception as e:
            #raise ValueError('%s\nvalue must be of type `Any` in Example, instead got %s' % (str(e), str(type(d['value']))))
            raise e
    externalValue: Optional[str]
    if 'externalValue' not in d:
        externalValue = None
    elif not isinstance(d['externalValue'], str):
        raise ValueError('externalValue must be of type `str` in Example, instead got %s' % str(type(d['externalValue'])))
    else:
        externalValue = cast(str, d['externalValue'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Example(
        summary=summary,
        description=description,
        value=value,
        externalValue=externalValue,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Encoding(d: Any) -> Encoding:
    if not isinstance(d, dict):
        raise ValueError("Encoding must be a dictionary")
    contentType: Optional[str]
    if 'contentType' not in d:
        contentType = None
    elif not isinstance(d['contentType'], str):
        raise ValueError('contentType must be of type `str` in Encoding, instead got %s' % str(type(d['contentType'])))
    else:
        contentType = cast(str, d['contentType'])
    headers: Optional[Mapping[str, Header]]
    if 'headers' not in d:
        headers = None
    elif not isinstance(d['headers'], dict):
        raise ValueError('headers must be of type `dict` in Encoding, instead got %s' % str(type(d['headers'])))
    else:
        _ret = dict()
        for k, v in d['headers'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('headers in Encoding can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_Header(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nheaders in Encoding at key %s has a value %s which cannot be cast to Header.' % (str(e), k, str(v)))
                raise e
        headers = cast(Mapping[str, Header], _ret)
    style: Optional[str]
    if 'style' not in d:
        style = None
    elif not isinstance(d['style'], str):
        raise ValueError('style must be of type `str` in Encoding, instead got %s' % str(type(d['style'])))
    else:
        style = cast(str, d['style'])
    explode: Optional[bool]
    if 'explode' not in d:
        explode = None
    elif not isinstance(d['explode'], bool):
        raise ValueError('explode must be of type `bool` in Encoding, instead got %s' % str(type(d['explode'])))
    else:
        explode = cast(bool, d['explode'])
    allowReserved: Optional[bool]
    if 'allowReserved' not in d:
        allowReserved = None
    elif not isinstance(d['allowReserved'], bool):
        raise ValueError('allowReserved must be of type `bool` in Encoding, instead got %s' % str(type(d['allowReserved'])))
    else:
        allowReserved = cast(bool, d['allowReserved'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Encoding(
        contentType=contentType,
        headers=headers,
        style=style,
        explode=explode,
        allowReserved=allowReserved,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_MediaType(d: Any) -> MediaType:
    if not isinstance(d, dict):
        raise ValueError("MediaType must be a dictionary")
    schema: Optional[Union[Schema, Reference]]
    if 'schema' not in d:
        schema = None
    elif not isinstance(d['schema'], dict):
        raise ValueError('schema must be of type `dict` in MediaType, instead got %s' % str(type(d['schema'])))
    else:
        try:
            schema = convert_to_Reference(d['schema'])
        except:
            try:
                schema = convert_to_Schema(d['schema'])
            except Exception as e:
                # raise ValueError('%s\nschema in MediaType has a value %s which cannot be cast to Union[Schema, Reference].' % str(e))
                raise e
    example: Optional[Any]
    if 'example' not in d:
        example = None
    else:
        try:
            example = convert_to_Any(d['example'])
        except Exception as e:
            #raise ValueError('%s\nexample must be of type `Any` in MediaType, instead got %s' % (str(e), str(type(d['example']))))
            raise e
    examples: Optional[Mapping[str, Union[Example, Reference]]]
    if 'examples' not in d:
        examples = None
    elif not isinstance(d['examples'], dict):
        raise ValueError('examples must be of type `dict` in MediaType, instead got %s' % str(type(d['examples'])))
    else:
        _ret = dict()
        for k, v in d['examples'].items():
            if type(k) != str:
                raise ValueError('examples in MediaType can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Example(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nexamples in MediaType at key %s has a value %s which cannot be cast to Union[Example, Reference].' % (str(e), k, str(v)))
                raise e
        examples = cast(Mapping[str, Union[Example, Reference]], _ret)
    encoding: Optional[Mapping[str, Encoding]]
    if 'encoding' not in d:
        encoding = None
    elif not isinstance(d['encoding'], dict):
        raise ValueError('encoding must be of type `dict` in MediaType, instead got %s' % str(type(d['encoding'])))
    else:
        _ret = dict()
        for k, v in d['encoding'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('encoding in MediaType can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_Encoding(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nencoding in MediaType at key %s has a value %s which cannot be cast to Encoding.' % (str(e), k, str(v)))
                raise e
        encoding = cast(Mapping[str, Encoding], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return MediaType(
        schema=schema,
        example=example,
        examples=examples,
        encoding=encoding,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Header(d: Any) -> Header:
    if not isinstance(d, dict):
        raise ValueError("Header must be a dictionary")
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Header, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    required: Optional[bool]
    if 'required' not in d:
        required = None
    elif not isinstance(d['required'], bool):
        raise ValueError('required must be of type `bool` in Header, instead got %s' % str(type(d['required'])))
    else:
        required = cast(bool, d['required'])
    deprecated: Optional[bool]
    if 'deprecated' not in d:
        deprecated = None
    elif not isinstance(d['deprecated'], bool):
        raise ValueError('deprecated must be of type `bool` in Header, instead got %s' % str(type(d['deprecated'])))
    else:
        deprecated = cast(bool, d['deprecated'])
    allowEmptyValue: Optional[bool]
    if 'allowEmptyValue' not in d:
        allowEmptyValue = None
    elif not isinstance(d['allowEmptyValue'], bool):
        raise ValueError('allowEmptyValue must be of type `bool` in Header, instead got %s' % str(type(d['allowEmptyValue'])))
    else:
        allowEmptyValue = cast(bool, d['allowEmptyValue'])
    style: Optional[str]
    if 'style' not in d:
        style = None
    elif not isinstance(d['style'], str):
        raise ValueError('style must be of type `str` in Header, instead got %s' % str(type(d['style'])))
    else:
        style = cast(str, d['style'])
    explode: Optional[bool]
    if 'explode' not in d:
        explode = None
    elif not isinstance(d['explode'], bool):
        raise ValueError('explode must be of type `bool` in Header, instead got %s' % str(type(d['explode'])))
    else:
        explode = cast(bool, d['explode'])
    allowReserved: Optional[bool]
    if 'allowReserved' not in d:
        allowReserved = None
    elif not isinstance(d['allowReserved'], bool):
        raise ValueError('allowReserved must be of type `bool` in Header, instead got %s' % str(type(d['allowReserved'])))
    else:
        allowReserved = cast(bool, d['allowReserved'])
    schema: Optional[Union[Schema, Reference]]
    if 'schema' not in d:
        schema = None
    elif not isinstance(d['schema'], dict):
        raise ValueError('schema must be of type `dict` in Header, instead got %s' % str(type(d['schema'])))
    else:
        try:
            schema = convert_to_Reference(d['schema'])
        except:
            try:
                schema = convert_to_Schema(d['schema'])
            except Exception as e:
                # raise ValueError('%s\nschema in Header has a value %s which cannot be cast to Union[Schema, Reference].' % str(e))
                raise e
    content: Optional[Mapping[str, MediaType]]
    if 'content' not in d:
        content = None
    elif not isinstance(d['content'], dict):
        raise ValueError('content must be of type `dict` in Header, instead got %s' % str(type(d['content'])))
    else:
        _ret = dict()
        for k, v in d['content'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('content in Header can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_MediaType(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\ncontent in Header at key %s has a value %s which cannot be cast to MediaType.' % (str(e), k, str(v)))
                raise e
        content = cast(Mapping[str, MediaType], _ret)
    example: Optional[Any]
    if 'example' not in d:
        example = None
    else:
        try:
            example = convert_to_Any(d['example'])
        except Exception as e:
            #raise ValueError('%s\nexample must be of type `Any` in Header, instead got %s' % (str(e), str(type(d['example']))))
            raise e
    examples: Optional[Mapping[str, Union[Example, Reference]]]
    if 'examples' not in d:
        examples = None
    elif not isinstance(d['examples'], dict):
        raise ValueError('examples must be of type `dict` in Header, instead got %s' % str(type(d['examples'])))
    else:
        _ret = dict()
        for k, v in d['examples'].items():
            if type(k) != str:
                raise ValueError('examples in Header can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Example(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nexamples in Header at key %s has a value %s which cannot be cast to Union[Example, Reference].' % (str(e), k, str(v)))
                raise e
        examples = cast(Mapping[str, Union[Example, Reference]], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Header(
        description=description,
        required=required,
        deprecated=deprecated,
        allowEmptyValue=allowEmptyValue,
        style=style,
        explode=explode,
        allowReserved=allowReserved,
        schema=schema,
        content=content,
        example=example,
        examples=examples,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Operation(d: Any) -> Operation:
    if not isinstance(d, dict):
        raise ValueError("Operation must be a dictionary")
    responses: Responses
    if 'responses' not in d:
        raise ValueError('responses must be defined for Operation')
    try:
        responses = convert_to_Responses(d['responses'])
    except Exception as e:
        #raise ValueError('%s\nresponses must be of type `Responses` in Operation, instead got %s' % (str(e), str(type(d['responses']))))
        raise e
    tags: Optional[Sequence[str]]
    if 'tags' not in d:
        tags = None
    elif not isinstance(d['tags'], list):
        raise ValueError('tags must be of type `list` in Operation, instead got %s' % str(type(d['tags'])))
    else:
        _ret = []
        for k in d['tags']:
            try:
                _ret.append(convert_to_str(k))
            except Exception as e:
                #raise ValueError('%s\ntags in Operation has a value %s which cannot be cast to str.' % (str(e), str(k)))
                raise e
        tags = cast(Sequence[str], _ret)
    summary: Optional[str]
    if 'summary' not in d:
        summary = None
    elif not isinstance(d['summary'], str):
        raise ValueError('summary must be of type `str` in Operation, instead got %s' % str(type(d['summary'])))
    else:
        summary = cast(str, d['summary'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Operation, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    externalDocs: Optional[ExternalDocumentation]
    if 'externalDocs' not in d:
        externalDocs = None
    else:
        try:
            externalDocs = convert_to_ExternalDocumentation(d['externalDocs'])
        except Exception as e:
            #raise ValueError('%s\nexternalDocs must be of type `ExternalDocumentation` in Operation, instead got %s' % (str(e), str(type(d['externalDocs']))))
            raise e
    operationId: Optional[str]
    if 'operationId' not in d:
        operationId = None
    elif not isinstance(d['operationId'], str):
        raise ValueError('operationId must be of type `str` in Operation, instead got %s' % str(type(d['operationId'])))
    else:
        operationId = cast(str, d['operationId'])
    parameters: Optional[Sequence[Union[Parameter, Reference]]]
    if 'parameters' not in d:
        parameters = None
    elif not isinstance(d['parameters'], list):
        raise ValueError('parameters must be of type `dict` in Operation, instead got %s' % str(type(d['parameters'])))
    else:
        _ret = []
        for k in d['parameters']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Parameter(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                #raise ValueError('%s\nparameters in Operation has a value %s which cannot be cast to Union[Parameter, Reference].' % (str(e), str(k)))
                raise e
        parameters = cast(Sequence[Union[Parameter, Reference]], _ret)
    requestBody: Optional[Union[RequestBody, Reference]]
    if 'requestBody' not in d:
        requestBody = None
    elif not isinstance(d['requestBody'], dict):
        raise ValueError('requestBody must be of type `dict` in Operation, instead got %s' % str(type(d['requestBody'])))
    else:
        try:
            requestBody = convert_to_Reference(d['requestBody'])
        except:
            try:
                requestBody = convert_to_RequestBody(d['requestBody'])
            except Exception as e:
                # raise ValueError('%s\nrequestBody in Operation has a value %s which cannot be cast to Union[RequestBody, Reference].' % str(e))
                raise e
    callbacks: Optional[Mapping[str, Union[Callback, Reference]]]
    if 'callbacks' not in d:
        callbacks = None
    elif not isinstance(d['callbacks'], dict):
        raise ValueError('callbacks must be of type `dict` in Operation, instead got %s' % str(type(d['callbacks'])))
    else:
        _ret = dict()
        for k, v in d['callbacks'].items():
            if type(k) != str:
                raise ValueError('callbacks in Operation can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Callback(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\ncallbacks in Operation at key %s has a value %s which cannot be cast to Union[Callback, Reference].' % (str(e), k, str(v)))
                raise e
        callbacks = cast(Mapping[str, Union[Callback, Reference]], _ret)
    deprecated: Optional[bool]
    if 'deprecated' not in d:
        deprecated = None
    elif not isinstance(d['deprecated'], bool):
        raise ValueError('deprecated must be of type `bool` in Operation, instead got %s' % str(type(d['deprecated'])))
    else:
        deprecated = cast(bool, d['deprecated'])
    security: Optional[Sequence[SecurityRequirement]]
    if 'security' not in d:
        security = None
    elif not isinstance(d['security'], list):
        raise ValueError('security must be of type `list` in Operation, instead got %s' % str(type(d['security'])))
    else:
        _ret = []
        for k in d['security']:
            try:
                _ret.append(convert_to_SecurityRequirement(k))
            except Exception as e:
                #raise ValueError('%s\nsecurity in Operation has a value %s which cannot be cast to SecurityRequirement.' % (str(e), str(k)))
                raise e
        security = cast(Sequence[SecurityRequirement], _ret)
    servers: Optional[Sequence[Server]]
    if 'servers' not in d:
        servers = None
    elif not isinstance(d['servers'], list):
        raise ValueError('servers must be of type `list` in Operation, instead got %s' % str(type(d['servers'])))
    else:
        _ret = []
        for k in d['servers']:
            try:
                _ret.append(convert_to_Server(k))
            except Exception as e:
                #raise ValueError('%s\nservers in Operation has a value %s which cannot be cast to Server.' % (str(e), str(k)))
                raise e
        servers = cast(Sequence[Server], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Operation(
        responses=responses,
        tags=tags,
        summary=summary,
        description=description,
        externalDocs=externalDocs,
        operationId=operationId,
        parameters=parameters,
        requestBody=requestBody,
        callbacks=callbacks,
        deprecated=deprecated,
        security=security,
        servers=servers,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Response(d: Any) -> Response:
    if not isinstance(d, dict):
        raise ValueError("Response must be a dictionary")
    description: str
    if 'description' not in d:
        raise ValueError('description must be defined for Response')
    if not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Response, instead got %s' % str(type(d['description'])))
    description = cast(str, d['description'])
    headers: Optional[Mapping[str, Union[Header, Reference]]]
    if 'headers' not in d:
        headers = None
    elif not isinstance(d['headers'], dict):
        raise ValueError('headers must be of type `dict` in Response, instead got %s' % str(type(d['headers'])))
    else:
        _ret = dict()
        for k, v in d['headers'].items():
            if type(k) != str:
                raise ValueError('headers in Response can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Header(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nheaders in Response at key %s has a value %s which cannot be cast to Union[Header, Reference].' % (str(e), k, str(v)))
                raise e
        headers = cast(Mapping[str, Union[Header, Reference]], _ret)
    content: Optional[Mapping[str, MediaType]]
    if 'content' not in d:
        content = None
    elif not isinstance(d['content'], dict):
        raise ValueError('content must be of type `dict` in Response, instead got %s' % str(type(d['content'])))
    else:
        _ret = dict()
        for k, v in d['content'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('content in Response can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_MediaType(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\ncontent in Response at key %s has a value %s which cannot be cast to MediaType.' % (str(e), k, str(v)))
                raise e
        content = cast(Mapping[str, MediaType], _ret)
    links: Optional[Mapping[str, Union[Link, Reference]]]
    if 'links' not in d:
        links = None
    elif not isinstance(d['links'], dict):
        raise ValueError('links must be of type `dict` in Response, instead got %s' % str(type(d['links'])))
    else:
        _ret = dict()
        for k, v in d['links'].items():
            if type(k) != str:
                raise ValueError('links in Response can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Link(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nlinks in Response at key %s has a value %s which cannot be cast to Union[Link, Reference].' % (str(e), k, str(v)))
                raise e
        links = cast(Mapping[str, Union[Link, Reference]], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Response(
        description=description,
        headers=headers,
        content=content,
        links=links,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Parameter(d: Any) -> Parameter:
    if not isinstance(d, dict):
        raise ValueError("Parameter must be a dictionary")
    name: str
    if 'name' not in d:
        raise ValueError('name must be defined for Parameter')
    if not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in Parameter, instead got %s' % str(type(d['name'])))
    name = cast(str, d['name'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Parameter, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    required: Optional[bool]
    if 'required' not in d:
        required = None
    elif not isinstance(d['required'], bool):
        raise ValueError('required must be of type `bool` in Parameter, instead got %s' % str(type(d['required'])))
    else:
        required = cast(bool, d['required'])
    deprecated: Optional[bool]
    if 'deprecated' not in d:
        deprecated = None
    elif not isinstance(d['deprecated'], bool):
        raise ValueError('deprecated must be of type `bool` in Parameter, instead got %s' % str(type(d['deprecated'])))
    else:
        deprecated = cast(bool, d['deprecated'])
    allowEmptyValue: Optional[bool]
    if 'allowEmptyValue' not in d:
        allowEmptyValue = None
    elif not isinstance(d['allowEmptyValue'], bool):
        raise ValueError('allowEmptyValue must be of type `bool` in Parameter, instead got %s' % str(type(d['allowEmptyValue'])))
    else:
        allowEmptyValue = cast(bool, d['allowEmptyValue'])
    style: Optional[str]
    if 'style' not in d:
        style = None
    elif not isinstance(d['style'], str):
        raise ValueError('style must be of type `str` in Parameter, instead got %s' % str(type(d['style'])))
    else:
        style = cast(str, d['style'])
    explode: Optional[bool]
    if 'explode' not in d:
        explode = None
    elif not isinstance(d['explode'], bool):
        raise ValueError('explode must be of type `bool` in Parameter, instead got %s' % str(type(d['explode'])))
    else:
        explode = cast(bool, d['explode'])
    allowReserved: Optional[bool]
    if 'allowReserved' not in d:
        allowReserved = None
    elif not isinstance(d['allowReserved'], bool):
        raise ValueError('allowReserved must be of type `bool` in Parameter, instead got %s' % str(type(d['allowReserved'])))
    else:
        allowReserved = cast(bool, d['allowReserved'])
    schema: Optional[Union[Schema, Reference]]
    if 'schema' not in d:
        schema = None
    elif not isinstance(d['schema'], dict):
        raise ValueError('schema must be of type `dict` in Parameter, instead got %s' % str(type(d['schema'])))
    else:
        try:
            schema = convert_to_Reference(d['schema'])
        except:
            try:
                schema = convert_to_Schema(d['schema'])
            except Exception as e:
                # raise ValueError('%s\nschema in Parameter has a value %s which cannot be cast to Union[Schema, Reference].' % str(e))
                raise e
    content: Optional[Mapping[str, MediaType]]
    if 'content' not in d:
        content = None
    elif not isinstance(d['content'], dict):
        raise ValueError('content must be of type `dict` in Parameter, instead got %s' % str(type(d['content'])))
    else:
        _ret = dict()
        for k, v in d['content'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('content in Parameter can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_MediaType(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\ncontent in Parameter at key %s has a value %s which cannot be cast to MediaType.' % (str(e), k, str(v)))
                raise e
        content = cast(Mapping[str, MediaType], _ret)
    example: Optional[Any]
    if 'example' not in d:
        example = None
    else:
        try:
            example = convert_to_Any(d['example'])
        except Exception as e:
            #raise ValueError('%s\nexample must be of type `Any` in Parameter, instead got %s' % (str(e), str(type(d['example']))))
            raise e
    examples: Optional[Mapping[str, Union[Example, Reference]]]
    if 'examples' not in d:
        examples = None
    elif not isinstance(d['examples'], dict):
        raise ValueError('examples must be of type `dict` in Parameter, instead got %s' % str(type(d['examples'])))
    else:
        _ret = dict()
        for k, v in d['examples'].items():
            if type(k) != str:
                raise ValueError('examples in Parameter can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Example(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nexamples in Parameter at key %s has a value %s which cannot be cast to Union[Example, Reference].' % (str(e), k, str(v)))
                raise e
        examples = cast(Mapping[str, Union[Example, Reference]], _ret)
    _in: str
    if 'in' not in d:
        raise ValueError('in must be defined for Parameter')
    if not isinstance(d['in'], str):
        raise ValueError('in must be of type `str` in Parameter, instead got %s' % str(type(d['in'])))
    _in = cast(str, d['in'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Parameter(
        name=name,
        description=description,
        required=required,
        deprecated=deprecated,
        allowEmptyValue=allowEmptyValue,
        style=style,
        explode=explode,
        allowReserved=allowReserved,
        schema=schema,
        content=content,
        example=example,
        examples=examples,
        _in=_in,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_RequestBody(d: Any) -> RequestBody:
    if not isinstance(d, dict):
        raise ValueError("RequestBody must be a dictionary")
    content: Mapping[str, MediaType]
    if 'content' not in d:
        raise ValueError('content must be present in RequestBody')
    elif not isinstance(d['content'], dict):
        raise ValueError('content must be of type `dict` in RequestBody, instead got %s' % str(type(d['content'])))
    else:
        _ret = dict()
        for k, v in d['content'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('content in RequestBody can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_MediaType(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s content in RequestBody at key %s has a value %s which cannot be cast to MediaType.' % (str(e), k, str(v)))
                raise e
        content = cast(Mapping[str, MediaType], _ret)
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in RequestBody, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    required: Optional[bool]
    if 'required' not in d:
        required = None
    elif not isinstance(d['required'], bool):
        raise ValueError('required must be of type `bool` in RequestBody, instead got %s' % str(type(d['required'])))
    else:
        required = cast(bool, d['required'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return RequestBody(
        content=content,
        description=description,
        required=required,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_APIKeySecurityScheme(d: Any) -> APIKeySecurityScheme:
    if not isinstance(d, dict):
        raise ValueError("APIKeySecurityScheme must be a dictionary")
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in APIKeySecurityScheme, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    name: str
    if 'name' not in d:
        raise ValueError('name must be defined for APIKeySecurityScheme')
    if not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in APIKeySecurityScheme, instead got %s' % str(type(d['name'])))
    name = cast(str, d['name'])
    _type: str
    if 'type' not in d:
        raise ValueError('type must be defined for APIKeySecurityScheme')
    if not isinstance(d['type'], str):
        raise ValueError('type must be of type `str` in APIKeySecurityScheme, instead got %s' % str(type(d['type'])))
    _type = cast(str, d['type'])
    _in: str
    if 'in' not in d:
        raise ValueError('in must be defined for APIKeySecurityScheme')
    if not isinstance(d['in'], str):
        raise ValueError('in must be of type `str` in APIKeySecurityScheme, instead got %s' % str(type(d['in'])))
    _in = cast(str, d['in'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return APIKeySecurityScheme(
        description=description,
        name=name,
        _type=_type,
        _in=_in,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_HTTPSecurityScheme(d: Any) -> HTTPSecurityScheme:
    if not isinstance(d, dict):
        raise ValueError("HTTPSecurityScheme must be a dictionary")
    scheme: str
    if 'scheme' not in d:
        raise ValueError('scheme must be defined for HTTPSecurityScheme')
    if not isinstance(d['scheme'], str):
        raise ValueError('scheme must be of type `str` in HTTPSecurityScheme, instead got %s' % str(type(d['scheme'])))
    scheme = cast(str, d['scheme'])
    bearerFormat: Optional[str]
    if 'bearerFormat' not in d:
        bearerFormat = None
    elif not isinstance(d['bearerFormat'], str):
        raise ValueError('bearerFormat must be of type `str` in HTTPSecurityScheme, instead got %s' % str(type(d['bearerFormat'])))
    else:
        bearerFormat = cast(str, d['bearerFormat'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in HTTPSecurityScheme, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    _type: str
    if 'type' not in d:
        raise ValueError('type must be defined for HTTPSecurityScheme')
    if not isinstance(d['type'], str):
        raise ValueError('type must be of type `str` in HTTPSecurityScheme, instead got %s' % str(type(d['type'])))
    _type = cast(str, d['type'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return HTTPSecurityScheme(
        scheme=scheme,
        bearerFormat=bearerFormat,
        description=description,
        _type=_type,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_ImplicitOAuthFlow(d: Any) -> ImplicitOAuthFlow:
    if not isinstance(d, dict):
        raise ValueError("ImplicitOAuthFlow must be a dictionary")
    authorizationUrl: str
    if 'authorizationUrl' not in d:
        raise ValueError('authorizationUrl must be defined for ImplicitOAuthFlow')
    if not isinstance(d['authorizationUrl'], str):
        raise ValueError('authorizationUrl must be of type `str` in ImplicitOAuthFlow, instead got %s' % str(type(d['authorizationUrl'])))
    authorizationUrl = cast(str, d['authorizationUrl'])
    scopes: Mapping[str, str]
    if 'scopes' not in d:
        raise ValueError('scopes must be present in ImplicitOAuthFlow')
    elif not isinstance(d['scopes'], dict):
        raise ValueError('scopes must be of type `dict` in ImplicitOAuthFlow, instead got %s' % str(type(d['scopes'])))
    else:
        _ret = dict()
        for k, v in d['scopes'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('scopes in ImplicitOAuthFlow can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_str(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s scopes in ImplicitOAuthFlow at key %s has a value %s which cannot be cast to str.' % (str(e), k, str(v)))
                raise e
        scopes = cast(Mapping[str, str], _ret)
    refreshUrl: Optional[str]
    if 'refreshUrl' not in d:
        refreshUrl = None
    elif not isinstance(d['refreshUrl'], str):
        raise ValueError('refreshUrl must be of type `str` in ImplicitOAuthFlow, instead got %s' % str(type(d['refreshUrl'])))
    else:
        refreshUrl = cast(str, d['refreshUrl'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return ImplicitOAuthFlow(
        authorizationUrl=authorizationUrl,
        scopes=scopes,
        refreshUrl=refreshUrl,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_PasswordOAuthFlow(d: Any) -> PasswordOAuthFlow:
    if not isinstance(d, dict):
        raise ValueError("PasswordOAuthFlow must be a dictionary")
    tokenUrl: str
    if 'tokenUrl' not in d:
        raise ValueError('tokenUrl must be defined for PasswordOAuthFlow')
    if not isinstance(d['tokenUrl'], str):
        raise ValueError('tokenUrl must be of type `str` in PasswordOAuthFlow, instead got %s' % str(type(d['tokenUrl'])))
    tokenUrl = cast(str, d['tokenUrl'])
    refreshUrl: Optional[str]
    if 'refreshUrl' not in d:
        refreshUrl = None
    elif not isinstance(d['refreshUrl'], str):
        raise ValueError('refreshUrl must be of type `str` in PasswordOAuthFlow, instead got %s' % str(type(d['refreshUrl'])))
    else:
        refreshUrl = cast(str, d['refreshUrl'])
    scopes: Optional[Mapping[str, str]]
    if 'scopes' not in d:
        scopes = None
    elif not isinstance(d['scopes'], dict):
        raise ValueError('scopes must be of type `dict` in PasswordOAuthFlow, instead got %s' % str(type(d['scopes'])))
    else:
        _ret = dict()
        for k, v in d['scopes'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('scopes in PasswordOAuthFlow can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_str(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nscopes in PasswordOAuthFlow at key %s has a value %s which cannot be cast to str.' % (str(e), k, str(v)))
                raise e
        scopes = cast(Mapping[str, str], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return PasswordOAuthFlow(
        tokenUrl=tokenUrl,
        refreshUrl=refreshUrl,
        scopes=scopes,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_ClientCredentialsFlow(d: Any) -> ClientCredentialsFlow:
    if not isinstance(d, dict):
        raise ValueError("ClientCredentialsFlow must be a dictionary")
    tokenUrl: str
    if 'tokenUrl' not in d:
        raise ValueError('tokenUrl must be defined for ClientCredentialsFlow')
    if not isinstance(d['tokenUrl'], str):
        raise ValueError('tokenUrl must be of type `str` in ClientCredentialsFlow, instead got %s' % str(type(d['tokenUrl'])))
    tokenUrl = cast(str, d['tokenUrl'])
    refreshUrl: Optional[str]
    if 'refreshUrl' not in d:
        refreshUrl = None
    elif not isinstance(d['refreshUrl'], str):
        raise ValueError('refreshUrl must be of type `str` in ClientCredentialsFlow, instead got %s' % str(type(d['refreshUrl'])))
    else:
        refreshUrl = cast(str, d['refreshUrl'])
    scopes: Optional[Mapping[str, str]]
    if 'scopes' not in d:
        scopes = None
    elif not isinstance(d['scopes'], dict):
        raise ValueError('scopes must be of type `dict` in ClientCredentialsFlow, instead got %s' % str(type(d['scopes'])))
    else:
        _ret = dict()
        for k, v in d['scopes'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('scopes in ClientCredentialsFlow can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_str(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nscopes in ClientCredentialsFlow at key %s has a value %s which cannot be cast to str.' % (str(e), k, str(v)))
                raise e
        scopes = cast(Mapping[str, str], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return ClientCredentialsFlow(
        tokenUrl=tokenUrl,
        refreshUrl=refreshUrl,
        scopes=scopes,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_AuthorizationCodeOAuthFlow(d: Any) -> AuthorizationCodeOAuthFlow:
    if not isinstance(d, dict):
        raise ValueError("AuthorizationCodeOAuthFlow must be a dictionary")
    tokenUrl: str
    if 'tokenUrl' not in d:
        raise ValueError('tokenUrl must be defined for AuthorizationCodeOAuthFlow')
    if not isinstance(d['tokenUrl'], str):
        raise ValueError('tokenUrl must be of type `str` in AuthorizationCodeOAuthFlow, instead got %s' % str(type(d['tokenUrl'])))
    tokenUrl = cast(str, d['tokenUrl'])
    authorizationUrl: str
    if 'authorizationUrl' not in d:
        raise ValueError('authorizationUrl must be defined for AuthorizationCodeOAuthFlow')
    if not isinstance(d['authorizationUrl'], str):
        raise ValueError('authorizationUrl must be of type `str` in AuthorizationCodeOAuthFlow, instead got %s' % str(type(d['authorizationUrl'])))
    authorizationUrl = cast(str, d['authorizationUrl'])
    refreshUrl: Optional[str]
    if 'refreshUrl' not in d:
        refreshUrl = None
    elif not isinstance(d['refreshUrl'], str):
        raise ValueError('refreshUrl must be of type `str` in AuthorizationCodeOAuthFlow, instead got %s' % str(type(d['refreshUrl'])))
    else:
        refreshUrl = cast(str, d['refreshUrl'])
    scopes: Optional[Mapping[str, str]]
    if 'scopes' not in d:
        scopes = None
    elif not isinstance(d['scopes'], dict):
        raise ValueError('scopes must be of type `dict` in AuthorizationCodeOAuthFlow, instead got %s' % str(type(d['scopes'])))
    else:
        _ret = dict()
        for k, v in d['scopes'].items():
            e: Exception = ValueError('')
            if type(k) != str:
                raise ValueError('scopes in AuthorizationCodeOAuthFlow can only have string keys, but encountered %s.' % k)
            try:
                _ret[k] = convert_to_str(v)
            except Exception as ee:
                e = ee
            if k not in _ret:
                #raise ValueError('%s\nscopes in AuthorizationCodeOAuthFlow at key %s has a value %s which cannot be cast to str.' % (str(e), k, str(v)))
                raise e
        scopes = cast(Mapping[str, str], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return AuthorizationCodeOAuthFlow(
        tokenUrl=tokenUrl,
        authorizationUrl=authorizationUrl,
        refreshUrl=refreshUrl,
        scopes=scopes,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_OAuthFlows(d: Any) -> OAuthFlows:
    if not isinstance(d, dict):
        raise ValueError("OAuthFlows must be a dictionary")
    implicit: Optional[ImplicitOAuthFlow]
    if 'implicit' not in d:
        implicit = None
    else:
        try:
            implicit = convert_to_ImplicitOAuthFlow(d['implicit'])
        except Exception as e:
            #raise ValueError('%s\nimplicit must be of type `ImplicitOAuthFlow` in OAuthFlows, instead got %s' % (str(e), str(type(d['implicit']))))
            raise e
    password: Optional[PasswordOAuthFlow]
    if 'password' not in d:
        password = None
    else:
        try:
            password = convert_to_PasswordOAuthFlow(d['password'])
        except Exception as e:
            #raise ValueError('%s\npassword must be of type `PasswordOAuthFlow` in OAuthFlows, instead got %s' % (str(e), str(type(d['password']))))
            raise e
    clientCredentials: Optional[ClientCredentialsFlow]
    if 'clientCredentials' not in d:
        clientCredentials = None
    else:
        try:
            clientCredentials = convert_to_ClientCredentialsFlow(d['clientCredentials'])
        except Exception as e:
            #raise ValueError('%s\nclientCredentials must be of type `ClientCredentialsFlow` in OAuthFlows, instead got %s' % (str(e), str(type(d['clientCredentials']))))
            raise e
    authorizationCode: Optional[AuthorizationCodeOAuthFlow]
    if 'authorizationCode' not in d:
        authorizationCode = None
    else:
        try:
            authorizationCode = convert_to_AuthorizationCodeOAuthFlow(d['authorizationCode'])
        except Exception as e:
            #raise ValueError('%s\nauthorizationCode must be of type `AuthorizationCodeOAuthFlow` in OAuthFlows, instead got %s' % (str(e), str(type(d['authorizationCode']))))
            raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return OAuthFlows(
        implicit=implicit,
        password=password,
        clientCredentials=clientCredentials,
        authorizationCode=authorizationCode,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_OAuth2SecurityScheme(d: Any) -> OAuth2SecurityScheme:
    if not isinstance(d, dict):
        raise ValueError("OAuth2SecurityScheme must be a dictionary")
    flows: OAuthFlows
    if 'flows' not in d:
        raise ValueError('flows must be defined for OAuth2SecurityScheme')
    try:
        flows = convert_to_OAuthFlows(d['flows'])
    except Exception as e:
        #raise ValueError('%s\nflows must be of type `OAuthFlows` in OAuth2SecurityScheme, instead got %s' % (str(e), str(type(d['flows']))))
        raise e
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in OAuth2SecurityScheme, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    _type: str
    if 'type' not in d:
        raise ValueError('type must be defined for OAuth2SecurityScheme')
    if not isinstance(d['type'], str):
        raise ValueError('type must be of type `str` in OAuth2SecurityScheme, instead got %s' % str(type(d['type'])))
    _type = cast(str, d['type'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return OAuth2SecurityScheme(
        flows=flows,
        description=description,
        _type=_type,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_OpenIdConnectSecurityScheme(d: Any) -> OpenIdConnectSecurityScheme:
    if not isinstance(d, dict):
        raise ValueError("OpenIdConnectSecurityScheme must be a dictionary")
    openIdConnectUrl: str
    if 'openIdConnectUrl' not in d:
        raise ValueError('openIdConnectUrl must be defined for OpenIdConnectSecurityScheme')
    if not isinstance(d['openIdConnectUrl'], str):
        raise ValueError('openIdConnectUrl must be of type `str` in OpenIdConnectSecurityScheme, instead got %s' % str(type(d['openIdConnectUrl'])))
    openIdConnectUrl = cast(str, d['openIdConnectUrl'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in OpenIdConnectSecurityScheme, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    _type: str
    if 'type' not in d:
        raise ValueError('type must be defined for OpenIdConnectSecurityScheme')
    if not isinstance(d['type'], str):
        raise ValueError('type must be of type `str` in OpenIdConnectSecurityScheme, instead got %s' % str(type(d['type'])))
    _type = cast(str, d['type'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return OpenIdConnectSecurityScheme(
        openIdConnectUrl=openIdConnectUrl,
        description=description,
        _type=_type,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_PathItem(d: Any) -> PathItem:
    if not isinstance(d, dict):
        raise ValueError("PathItem must be a dictionary")
    summary: Optional[str]
    if 'summary' not in d:
        summary = None
    elif not isinstance(d['summary'], str):
        raise ValueError('summary must be of type `str` in PathItem, instead got %s' % str(type(d['summary'])))
    else:
        summary = cast(str, d['summary'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in PathItem, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    servers: Optional[Sequence[Server]]
    if 'servers' not in d:
        servers = None
    elif not isinstance(d['servers'], list):
        raise ValueError('servers must be of type `list` in PathItem, instead got %s' % str(type(d['servers'])))
    else:
        _ret = []
        for k in d['servers']:
            try:
                _ret.append(convert_to_Server(k))
            except Exception as e:
                #raise ValueError('%s\nservers in PathItem has a value %s which cannot be cast to Server.' % (str(e), str(k)))
                raise e
        servers = cast(Sequence[Server], _ret)
    parameters: Optional[Sequence[Union[Parameter, Reference]]]
    if 'parameters' not in d:
        parameters = None
    elif not isinstance(d['parameters'], list):
        raise ValueError('parameters must be of type `dict` in PathItem, instead got %s' % str(type(d['parameters'])))
    else:
        _ret = []
        for k in d['parameters']:
            _lr = len(_ret)
            e: Exception = ValueError('')
            try:
                _ret.append(convert_to_Reference(k))
            except:
                try:
                    _ret.append(convert_to_Parameter(k))
                except Exception as ee:
                    e = ee
            if _lr == len(_ret):
                #raise ValueError('%s\nparameters in PathItem has a value %s which cannot be cast to Union[Parameter, Reference].' % (str(e), str(k)))
                raise e
        parameters = cast(Sequence[Union[Parameter, Reference]], _ret)
    get: Optional[Operation]
    if 'get' not in d:
        get = None
    else:
        try:
            get = convert_to_Operation(d['get'])
        except Exception as e:
            #raise ValueError('%s\nget must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['get']))))
            raise e
    put: Optional[Operation]
    if 'put' not in d:
        put = None
    else:
        try:
            put = convert_to_Operation(d['put'])
        except Exception as e:
            #raise ValueError('%s\nput must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['put']))))
            raise e
    post: Optional[Operation]
    if 'post' not in d:
        post = None
    else:
        try:
            post = convert_to_Operation(d['post'])
        except Exception as e:
            #raise ValueError('%s\npost must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['post']))))
            raise e
    delete: Optional[Operation]
    if 'delete' not in d:
        delete = None
    else:
        try:
            delete = convert_to_Operation(d['delete'])
        except Exception as e:
            #raise ValueError('%s\ndelete must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['delete']))))
            raise e
    options: Optional[Operation]
    if 'options' not in d:
        options = None
    else:
        try:
            options = convert_to_Operation(d['options'])
        except Exception as e:
            #raise ValueError('%s\noptions must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['options']))))
            raise e
    head: Optional[Operation]
    if 'head' not in d:
        head = None
    else:
        try:
            head = convert_to_Operation(d['head'])
        except Exception as e:
            #raise ValueError('%s\nhead must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['head']))))
            raise e
    patch: Optional[Operation]
    if 'patch' not in d:
        patch = None
    else:
        try:
            patch = convert_to_Operation(d['patch'])
        except Exception as e:
            #raise ValueError('%s\npatch must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['patch']))))
            raise e
    trace: Optional[Operation]
    if 'trace' not in d:
        trace = None
    else:
        try:
            trace = convert_to_Operation(d['trace'])
        except Exception as e:
            #raise ValueError('%s\ntrace must be of type `Operation` in PathItem, instead got %s' % (str(e), str(type(d['trace']))))
            raise e
    _ref: Optional[str]
    if '$ref' not in d:
        _ref = None
    elif not isinstance(d['$ref'], str):
        raise ValueError('$ref must be of type `str` in PathItem, instead got %s' % str(type(d['$ref'])))
    else:
        _ref = cast(str, d['$ref'])
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return PathItem(
        summary=summary,
        description=description,
        servers=servers,
        parameters=parameters,
        get=get,
        put=put,
        post=post,
        delete=delete,
        options=options,
        head=head,
        patch=patch,
        trace=trace,
        _ref=_ref,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Components(d: Any) -> Components:
    if not isinstance(d, dict):
        raise ValueError("Components must be a dictionary")
    schemas: Optional[Mapping[str, Union[Schema, Reference]]]
    if 'schemas' not in d:
        schemas = None
    elif not isinstance(d['schemas'], dict):
        raise ValueError('schemas must be of type `dict` in Components, instead got %s' % str(type(d['schemas'])))
    else:
        _ret = dict()
        for k, v in d['schemas'].items():
            if type(k) != str:
                raise ValueError('schemas in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Schema(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nschemas in Components at key %s has a value %s which cannot be cast to Union[Schema, Reference].' % (str(e), k, str(v)))
                raise e
        schemas = cast(Mapping[str, Union[Schema, Reference]], _ret)
    responses: Optional[Mapping[str, Union[Response, Reference]]]
    if 'responses' not in d:
        responses = None
    elif not isinstance(d['responses'], dict):
        raise ValueError('responses must be of type `dict` in Components, instead got %s' % str(type(d['responses'])))
    else:
        _ret = dict()
        for k, v in d['responses'].items():
            if type(k) != str:
                raise ValueError('responses in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Response(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nresponses in Components at key %s has a value %s which cannot be cast to Union[Response, Reference].' % (str(e), k, str(v)))
                raise e
        responses = cast(Mapping[str, Union[Response, Reference]], _ret)
    parameters: Optional[Mapping[str, Union[Parameter, Reference]]]
    if 'parameters' not in d:
        parameters = None
    elif not isinstance(d['parameters'], dict):
        raise ValueError('parameters must be of type `dict` in Components, instead got %s' % str(type(d['parameters'])))
    else:
        _ret = dict()
        for k, v in d['parameters'].items():
            if type(k) != str:
                raise ValueError('parameters in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Parameter(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nparameters in Components at key %s has a value %s which cannot be cast to Union[Parameter, Reference].' % (str(e), k, str(v)))
                raise e
        parameters = cast(Mapping[str, Union[Parameter, Reference]], _ret)
    examples: Optional[Mapping[str, Union[Example, Reference]]]
    if 'examples' not in d:
        examples = None
    elif not isinstance(d['examples'], dict):
        raise ValueError('examples must be of type `dict` in Components, instead got %s' % str(type(d['examples'])))
    else:
        _ret = dict()
        for k, v in d['examples'].items():
            if type(k) != str:
                raise ValueError('examples in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Example(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nexamples in Components at key %s has a value %s which cannot be cast to Union[Example, Reference].' % (str(e), k, str(v)))
                raise e
        examples = cast(Mapping[str, Union[Example, Reference]], _ret)
    requestBodies: Optional[Mapping[str, Union[RequestBody, Reference]]]
    if 'requestBodies' not in d:
        requestBodies = None
    elif not isinstance(d['requestBodies'], dict):
        raise ValueError('requestBodies must be of type `dict` in Components, instead got %s' % str(type(d['requestBodies'])))
    else:
        _ret = dict()
        for k, v in d['requestBodies'].items():
            if type(k) != str:
                raise ValueError('requestBodies in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_RequestBody(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nrequestBodies in Components at key %s has a value %s which cannot be cast to Union[RequestBody, Reference].' % (str(e), k, str(v)))
                raise e
        requestBodies = cast(Mapping[str, Union[RequestBody, Reference]], _ret)
    headers: Optional[Mapping[str, Union[Header, Reference]]]
    if 'headers' not in d:
        headers = None
    elif not isinstance(d['headers'], dict):
        raise ValueError('headers must be of type `dict` in Components, instead got %s' % str(type(d['headers'])))
    else:
        _ret = dict()
        for k, v in d['headers'].items():
            if type(k) != str:
                raise ValueError('headers in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Header(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nheaders in Components at key %s has a value %s which cannot be cast to Union[Header, Reference].' % (str(e), k, str(v)))
                raise e
        headers = cast(Mapping[str, Union[Header, Reference]], _ret)
    securitySchemes: Optional[Mapping[str, Union[SecurityScheme, Reference]]]
    if 'securitySchemes' not in d:
        securitySchemes = None
    elif not isinstance(d['securitySchemes'], dict):
        raise ValueError('securitySchemes must be of type `dict` in Components, instead got %s' % str(type(d['securitySchemes'])))
    else:
        _ret = dict()
        for k, v in d['securitySchemes'].items():
            if type(k) != str:
                raise ValueError('securitySchemes in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_SecurityScheme(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nsecuritySchemes in Components at key %s has a value %s which cannot be cast to Union[SecurityScheme, Reference].' % (str(e), k, str(v)))
                raise e
        securitySchemes = cast(Mapping[str, Union[SecurityScheme, Reference]], _ret)
    links: Optional[Mapping[str, Union[Link, Reference]]]
    if 'links' not in d:
        links = None
    elif not isinstance(d['links'], dict):
        raise ValueError('links must be of type `dict` in Components, instead got %s' % str(type(d['links'])))
    else:
        _ret = dict()
        for k, v in d['links'].items():
            if type(k) != str:
                raise ValueError('links in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Link(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\nlinks in Components at key %s has a value %s which cannot be cast to Union[Link, Reference].' % (str(e), k, str(v)))
                raise e
        links = cast(Mapping[str, Union[Link, Reference]], _ret)
    callbacks: Optional[Mapping[str, Union[Callback, Reference]]]
    if 'callbacks' not in d:
        callbacks = None
    elif not isinstance(d['callbacks'], dict):
        raise ValueError('callbacks must be of type `dict` in Components, instead got %s' % str(type(d['callbacks'])))
    else:
        _ret = dict()
        for k, v in d['callbacks'].items():
            if type(k) != str:
                raise ValueError('callbacks in Components can only have string keys, but encountered %s.' % k)
            e: Exception = ValueError('')
            try:
                _ret[k] = convert_to_Reference(v)
            except:
                try:
                    _ret[k] = convert_to_Callback(v)
                except Exception as ee:
                    e = ee
            if k not in _ret:
                #raise ValueError('%s\ncallbacks in Components at key %s has a value %s which cannot be cast to Union[Callback, Reference].' % (str(e), k, str(v)))
                raise e
        callbacks = cast(Mapping[str, Union[Callback, Reference]], _ret)
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Components(
        schemas=schemas,
        responses=responses,
        parameters=parameters,
        examples=examples,
        requestBodies=requestBodies,
        headers=headers,
        securitySchemes=securitySchemes,
        links=links,
        callbacks=callbacks,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_Tag(d: Any) -> Tag:
    if not isinstance(d, dict):
        raise ValueError("Tag must be a dictionary")
    name: str
    if 'name' not in d:
        raise ValueError('name must be defined for Tag')
    if not isinstance(d['name'], str):
        raise ValueError('name must be of type `str` in Tag, instead got %s' % str(type(d['name'])))
    name = cast(str, d['name'])
    description: Optional[str]
    if 'description' not in d:
        description = None
    elif not isinstance(d['description'], str):
        raise ValueError('description must be of type `str` in Tag, instead got %s' % str(type(d['description'])))
    else:
        description = cast(str, d['description'])
    externalDocs: Optional[ExternalDocumentation]
    if 'externalDocs' not in d:
        externalDocs = None
    else:
        try:
            externalDocs = convert_to_ExternalDocumentation(d['externalDocs'])
        except Exception as e:
            #raise ValueError('%s\nexternalDocs must be of type `ExternalDocumentation` in Tag, instead got %s' % (str(e), str(type(d['externalDocs']))))
            raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return Tag(
        name=name,
        description=description,
        externalDocs=externalDocs,
        _x=_x if len(_x) > 0 else None
    )

def convert_to_OpenAPIObject(d: Any) -> OpenAPIObject:
    if not isinstance(d, dict):
        raise ValueError("OpenAPIObject must be a dictionary")
    openapi: str
    if 'openapi' not in d:
        raise ValueError('openapi must be defined for OpenAPIObject')
    if not isinstance(d['openapi'], str):
        raise ValueError('openapi must be of type `str` in OpenAPIObject, instead got %s' % str(type(d['openapi'])))
    openapi = cast(str, d['openapi'])
    info: Info
    if 'info' not in d:
        raise ValueError('info must be defined for OpenAPIObject')
    try:
        info = convert_to_Info(d['info'])
    except Exception as e:
        #raise ValueError('%s\ninfo must be of type `Info` in OpenAPIObject, instead got %s' % (str(e), str(type(d['info']))))
        raise e
    paths: Paths
    if 'paths' not in d:
        raise ValueError('paths must be defined for OpenAPIObject')
    try:
        paths = convert_to_Paths(d['paths'])
    except Exception as e:
        #raise ValueError('%s\npaths must be of type `Paths` in OpenAPIObject, instead got %s' % (str(e), str(type(d['paths']))))
        raise e
    externalDocs: Optional[ExternalDocumentation]
    if 'externalDocs' not in d:
        externalDocs = None
    else:
        try:
            externalDocs = convert_to_ExternalDocumentation(d['externalDocs'])
        except Exception as e:
            #raise ValueError('%s\nexternalDocs must be of type `ExternalDocumentation` in OpenAPIObject, instead got %s' % (str(e), str(type(d['externalDocs']))))
            raise e
    servers: Optional[Sequence[Server]]
    if 'servers' not in d:
        servers = None
    elif not isinstance(d['servers'], list):
        raise ValueError('servers must be of type `list` in OpenAPIObject, instead got %s' % str(type(d['servers'])))
    else:
        _ret = []
        for k in d['servers']:
            try:
                _ret.append(convert_to_Server(k))
            except Exception as e:
                #raise ValueError('%s\nservers in OpenAPIObject has a value %s which cannot be cast to Server.' % (str(e), str(k)))
                raise e
        servers = cast(Sequence[Server], _ret)
    security: Optional[Sequence[SecurityRequirement]]
    if 'security' not in d:
        security = None
    elif not isinstance(d['security'], list):
        raise ValueError('security must be of type `list` in OpenAPIObject, instead got %s' % str(type(d['security'])))
    else:
        _ret = []
        for k in d['security']:
            try:
                _ret.append(convert_to_SecurityRequirement(k))
            except Exception as e:
                #raise ValueError('%s\nsecurity in OpenAPIObject has a value %s which cannot be cast to SecurityRequirement.' % (str(e), str(k)))
                raise e
        security = cast(Sequence[SecurityRequirement], _ret)
    tags: Optional[Sequence[Tag]]
    if 'tags' not in d:
        tags = None
    elif not isinstance(d['tags'], list):
        raise ValueError('tags must be of type `list` in OpenAPIObject, instead got %s' % str(type(d['tags'])))
    else:
        _ret = []
        for k in d['tags']:
            try:
                _ret.append(convert_to_Tag(k))
            except Exception as e:
                #raise ValueError('%s\ntags in OpenAPIObject has a value %s which cannot be cast to Tag.' % (str(e), str(k)))
                raise e
        tags = cast(Sequence[Tag], _ret)
    components: Optional[Components]
    if 'components' not in d:
        components = None
    else:
        try:
            components = convert_to_Components(d['components'])
        except Exception as e:
            #raise ValueError('%s\ncomponents must be of type `Components` in OpenAPIObject, instead got %s' % (str(e), str(type(d['components']))))
            raise e
    _x = { k: v for k,v in d.items() if k[:2] == "x-" }
    return OpenAPIObject(
        openapi=openapi,
        info=info,
        paths=paths,
        externalDocs=externalDocs,
        servers=servers,
        security=security,
        tags=tags,
        components=components,
        _x=_x if len(_x) > 0 else None
    )


def convert_from_openapi(d: Any) -> Any:
    if is_dataclass(d):
        return {
            **({ k: v for k, v in d._x.items() } if hasattr(d, '_x') and (d._x is not None) else {}),
            **{
                _TO_DICT_SUBS.get(k, k): convert_from_openapi(getattr(d, k)) for k in [r.name for r in fields(d)] if (k != '_x') and (getattr(d, k) is not None)
            }
        }
    elif isinstance(d, dict):
        return { k: convert_from_openapi(v) for k, v in d.items() }
    elif isinstance(d, list):
        return [convert_from_openapi(x) for x in d]
    else:
        return d

convert_to_openapi = convert_to_OpenAPIObject
