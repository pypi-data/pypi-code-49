from typing import Dict, List, Tuple
import inspect
from abc import ABCMeta, abstractmethod
import numpy as np
from optimeed.core.tools import rgetattr, rsetattr

MODULE_TAG = '__module__'
CLASS_TAG = '__class__'
EXCLUDED_TAGS = [CLASS_TAG, MODULE_TAG]


class SaveableObject(metaclass=ABCMeta):
    """Abstract class for dynamically type-hinted objects.
    This class is to solve the special case where the exact type of an attribute is not known before runtime, yet has to be saved."""

    @abstractmethod
    def get_additional_attributes_to_save(self):
        """Return list of attributes corresponding to object, whose type cannot be determined statically (e.g. topology change)"""
        pass


def _get_object_class(theObj):
    return theObj.__class__.__qualname__


def _get_object_module(theObj):
    module = theObj.__class__.__module__
    if module == str.__class__.__module__:
        return None
    return module


def _object_to_FQCN(theobj):
    """Gets module path of object"""
    module = theobj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return theobj.__class__.__qualname__
    return module + '.' + theobj.__class__.__qualname__
    #
    # return theobj.__module__ + '.' + theobj.__class__.__name__


def _find_class(moduleName, className):
    import importlib
    splitted_name = className.split(".")
    begin = True
    parentClass=None
    for name in splitted_name:
        if begin:
            parentClass = getattr(importlib.import_module(moduleName), name)
            begin = False
        else:
            parentClass = getattr(parentClass, name)
    return parentClass


def json_to_obj(json_dict):
    """Convenience class to create object from dictionary. Only works if CLASS_TAG is valid

    :param json_dict: dictionary loaded from a json file.
    :raise TypeError: if class can not be found
    :raise KeyError: if CLASS_TAG not present in dictionary
    """
    try:
        cls = _find_class(json_dict[MODULE_TAG], json_dict[CLASS_TAG])
        return json_to_obj_safe(json_dict, cls)
    except TypeError:
        raise
    except KeyError:
        raise KeyError("Object class not defined, can not create data. Use from_json_safe method to specify which class to load.")


def json_to_obj_safe(json_dict, cls):
    """Safe class to create object from dictionary.

    :param json_dict: dictionary loaded from a json file
    :param cls: class object to instantiate with dictionary
    """
    if issubclass(cls, List) or issubclass(cls, Tuple):
        list_type = cls.__args__[0]
        instance = list()
        for value in json_dict:
            instance.append(json_to_obj_safe(value, list_type))
        return instance
    elif issubclass(cls, Dict):
        key_type = cls.__args__[0]
        val_type = cls.__args__[1]

        instance = dict()
        for key, value in json_dict.items():
            instance.update(json_to_obj_safe(key, key_type), json_to_obj_safe(value, val_type))
        return instance
    elif issubclass(cls, (float, int, complex, bool, str)):
        return json_dict
    else:  # Object must be instantiated
        theInstance = _instantiates_annotated_object(json_dict, cls)
        return theInstance


def _instantiates_annotated_object(_json_dict, _cls):
    annotations: dict = _cls.__annotations__ if hasattr(_cls, '__annotations__') else None

    # Instantiate the object
    entranceParams = []
    params = inspect.signature(_cls).parameters
    for param in params.values():
        if param.default is param.empty:
            if param.annotation is not param.empty:
                entranceParams.append(param.annotation(None or 0))
            else:
                entranceParams.append(None)
        else:
            entranceParams.append(param.default)
    instance = _cls(*entranceParams)
    # Set object attributes from data items
    if annotations is not None:
        for name, value in _json_dict.items():
            if name not in EXCLUDED_TAGS:
                field_type = annotations.get(name)
                if inspect.isclass(field_type) and isinstance(value, (dict, tuple, list, set, frozenset)):
                    rsetattr(instance, name, json_to_obj_safe(value, field_type))
                else:
                    rsetattr(instance, name, value)
    if isinstance(instance, SaveableObject):
        for additionalAttribute in instance.get_additional_attributes_to_save():
            theSubDict = _json_dict[additionalAttribute]
            try:
                rsetattr(instance, additionalAttribute, json_to_obj(theSubDict))
            except TypeError:
                rsetattr(instance, additionalAttribute, theSubDict)
    return instance


def _get_annotations(theObj):
    annotations: dict = theObj.__annotations__ if hasattr(theObj, '__annotations__') else dict()
    parentClass = theObj.__mro__[1] if hasattr(theObj, '__mro__') else None
    if parentClass is not None and parentClass != object:
        theAnnotations = _get_annotations(parentClass)
        theAnnotations.update(annotations)
        return theAnnotations
    return annotations


def obj_to_json(theObj):
    """Extract the json dictionary from the object. The data saved are automatically detected, using typehints.
     ex: x: int=5 will be saved, x=5 won't.
     Inheritance of annotation is managed by this function
     """
    def _to_json(recObj, is_first=False):
        # annotations: dict = recObj.__annotations__ if hasattr(recObj, '__annotations__') else None
        annotations = _get_annotations(type(theObj))
        if isinstance(recObj, list) or isinstance(recObj, tuple):
            theList = list()
            for elem in recObj:
                theList.append(_to_json(elem))
            return theList
        elif isinstance(recObj, dict):
            output_dict = dict()
            for key in list(recObj):
                output_dict[key] = _to_json(recObj[key])
            return output_dict
        elif isinstance(recObj, int) or isinstance(recObj, float):
            return recObj
        elif isinstance(recObj, str):
            return recObj
        elif np.issubdtype(type(recObj), np.integer) or np.issubdtype(type(recObj), np.floating):
            return recObj
        elif isinstance(recObj, bool):
            return str(recObj).lower()
        elif recObj is None:
            return "null"
        else:  # Item is a user-defined object
            output_dict = dict()
            if recObj is not None:
                if is_first:
                    output_dict[MODULE_TAG] = _get_object_module(recObj)
                    output_dict[CLASS_TAG] = _get_object_class(recObj)

                if annotations is not None:
                    for attribute in annotations:
                        try:
                            value = rgetattr(recObj, attribute)
                            output_dict[attribute] = _to_json(value)
                        except AttributeError:
                            pass
                if isinstance(recObj, SaveableObject):
                    for additionalAttribute in recObj.get_additional_attributes_to_save():
                        output_dict[additionalAttribute] = _to_json(rgetattr(recObj, additionalAttribute), is_first=True)
            return output_dict
    return _to_json(theObj, is_first=True)


def encode_str_json(theStr):
    return theStr.__repr__().replace("\\", "\\\\")[1:-1]


def decode_str_json(theStr):
    return str(theStr.__repr__().replace("\\\\", "\\"))

