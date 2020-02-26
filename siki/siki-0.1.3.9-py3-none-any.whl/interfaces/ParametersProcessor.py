# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: Feb 19, 2020
# LastChg: Feb 19, 2020


from siki.dstruct import DictExtern as dictext
from siki.basics import Exceptions as excepts
from siki.interfaces import StringConverter as strconv


def get_dictval_from_param(xmlnode, param):
    """
    to obtain valid dict type from incoming parameters.
    There are some differences between this method and other methods.
    The returning value consists of multiple pieces of data

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="dictionary">
            <sub name="sub_key1" type="number" default="1" mapping="param_key1" />
            <sub name="sub_key2" type="number" default="2" mapping="param_key2" />
            <sub name="sub_key3" type="number" default="3" mapping="param_key3" />
        </param>
    * [key] the key of the incoming parameter
    * [param(dict)] origin parameters

    Returns:
    * [dict] with the new key-value pair
    """

    final_key = xmlnode.attrib["name"]
    final_val = {}

    for sub in xmlnode: # convert the value

        sub_attrib = sub.attrib

        subdict = None
        key = sub_attrib["mapping"]
        val = param[key]

        if sub_attrib["type"] == "number" and sub_attrib["mapping"] in param.keys():
            subdict = get_numval_from_param(sub_attrib, key, val)
        elif sub_attrib["type"] == "float" and sub_attrib["mapping"] in param.keys():
            subdict = get_floatval_from_param(sub_attrib, key, val)
        elif sub_attrib["type"] == "boolean" and sub_attrib["mapping"] in param.keys():
            subdict = get_boolval_from_param(sub_attrib, key, val)
        elif sub_attrib["type"] == "value" and sub_attrib["mapping"] in param.keys():
            subdict = get_strval_from_param(sub_attrib, key, val)
        else:
            raise excepts.InvalidParamException("cannot detect the type or failed to mapping the key")

        final_val = dictext.union(final_val, subdict)

    return {final_key:final_val}



def get_listval_from_param(xmlnode, key, val):
    """
    to obtain valid list type from incoming parameters

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="list" v_type="number" mapping="param_key"/>
    * [key] the key of the incoming parameter
    * [val] the value of the incoming parameter

    Returns:
    * [dict] with the new key-value pair
    """

    if key != xmlnode["mapping"]: # because list node has no default values, so just return an empty list instead
        return {xmlnode["name"]:[]}

    # in order to distinguish the string list, 
    # we agreed to use comma as segmentation symbol
    # so the incoming list-str should be 1,2,3,4,5,6
    # if the v_type indicates they are numbers

    tokens = val.split("|")

    final_key = xmlnode["name"]
    final_val = []

    if xmlnode["v_type"] == "number": # tokens will be converted to a number list
        for t in tokens:
            final_val.append(strconv.convert_string_number(t))
    elif xmlnode["v_type"] == "float": # tokens will be converted to a float list
        for t in tokens:
            final_val.append(strconv.convert_string_float(t))
    elif xmlnode["v_type"] == "boolean": # tokens will be converted to a boolean list
        for t in tokens:
            final_val.append(strconv.convert_string_boolean(t))        
    else: # tokens will be converted to a string list
        for t in tokens:
            final_val.append(strconv.convert_string_none(t))

    # success
    return {final_key:final_val}


def get_strval_from_param(xmlnode, key, val):
    """
    to obtain valid value from incoming parameters

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="value" default="default" mapping="param_key"/>
    * [key] the key of the incoming parameter
    * [val] the value of the incoming parameter

    Returns:
    * [dict] with the new key-value pair
    """

    if key != xmlnode["mapping"]: # incorrect mapping, return the default to caller
        return {xmlnode["name"]:strconv.convert_string_none(xmlnode["default"])} # to prevent none-str return

    # to prevent none-str or empty string return
    final_key = xmlnode["name"]
    final_val = None
    if val is None or val == '':
        return {xmlnode["name"]:strconv.convert_string_none(xmlnode["default"])} # to prevent none-str return
    else:
        final_val = strconv.convert_string_none(val) # to prevent none-str return

    # success
    return {final_key:final_val}



def get_numval_from_param(xmlnode, key, val):
    """
    to obtain valid value from incoming parameters

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="number" default="0" mapping="param_key"/>
    * [key] the key of the incoming parameter
    * [val] the value of the incoming parameter

    Returns:
    * [dict] with the new key-value pair
    """    

    if key != xmlnode["mapping"]: # incorrect mapping, return the default to caller
        return {xmlnode["name"]:strconv.convert_string_number(xmlnode["default"])}

    # to prevent none-str or empty string return
    final_key = xmlnode["name"]
    final_val = None
    if val is None or val == '':
        return {xmlnode["name"]:strconv.convert_string_number(xmlnode["default"])}
    else:
        final_val = strconv.convert_string_number(val)

    # success
    return {final_key:final_val}



def get_floatval_from_param(xmlnode, key, val):
    """
    to obtain valid value from incoming parameters

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="float" default="0.0" mapping="param_key"/>
    * [key] the key of the incoming parameter
    * [val] the value of the incoming parameter

    Returns:
    * [dict] with the new key-value pair
    """ 

    if key != xmlnode["mapping"]: # incorrect mapping, return the default to caller
        return {xmlnode["name"]:strconv.convert_string_float(xmlnode["default"])}

    # to prevent none-str or empty string return
    final_key = xmlnode["name"]
    final_val = None
    if val is None or val == '':
        return {xmlnode["name"]:strconv.convert_string_float(xmlnode["default"])}
    else:
        final_val = strconv.convert_string_float(val)

    # success
    return {final_key:final_val}


def get_boolval_from_param(xmlnode, key, val):
    """
    to obtain valid value from incoming parameters

    Args:
    * [xmlnode(xml, dict)], an xml description record something like 
        <param name="the_key" type="boolean" default="false" mapping="param_key"/>
    * [key] the key of the incoming parameter
    * [val] the value of the incoming parameter

    Returns:
    * [dict] with the new key-value pair
    """

    if key != xmlnode["mapping"]: # incorrect mapping, return the default to caller
        return {xmlnode["name"]:strconv.convert_string_boolean(xmlnode["default"])}

    # to prevent none-str or empty string return
    final_key = xmlnode["name"]
    final_val = None
    if val is None or val == '':
        return {xmlnode["name"]:strconv.convert_string_boolean(xmlnode["default"])}
    else:
        final_val = strconv.convert_string_boolean(val)

    # success
    return {final_key:final_val}