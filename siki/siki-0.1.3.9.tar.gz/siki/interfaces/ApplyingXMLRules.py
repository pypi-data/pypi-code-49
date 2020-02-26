# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Created: Feb 07, 2020
# LastChg: Feb 26, 2020

import re
import xml.etree.ElementTree as etree

from siki.basics import FileUtils as fu
from siki.basics import Exceptions as excepts
from siki.basics import Validators as valid
from siki.interfaces import ParametersProcessor as proc

from siki.dstruct import DictExtern


class ApplyingXMLRules(object):



    def __init__(self, filename):
        if not fu.isfile(filename):
            raise excepts.CannotParseException("filename {} cannot parse, because invalid name or file path".format(filename))

        # parsing xml
        xml = etree.parse(filename)

        if xml is None:
            raise excepts.InvalidParamException("parse xml file failed")

        self.xmlroot = xml.getroot()




    def _has_sql_keywords(self, args):
        pattern = r"(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})"
        return re.search(pattern, args) is not None



    
    def _has_valid_chars(self, arg):
        pattern = u"^([\u4e00-\u9fa5]|[0-9a-zA-Z]|\s|-|:|\.|_)+$"
        return re.match(pattern, arg) is not None




    def _sql_prevention(self, value):
        """
        this method will try to prevent sql injection
        """
        if type(value) is not str:
            return False

        if not self._has_valid_chars(value):
            return True

        if self._has_sql_keywords(value):
            return True

        return False



    def _specialize_sql_prevention_for_list(self, value):

        if type(value) is not str:
            return False

        pattern = u"^([\u4e00-\u9fa5]|[0-9a-zA-Z]|\s|-|:|\.|_|,|\|)+$"
        if re.match(pattern, value) is None:
            return True

        pattern = r"(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})"
        m = re.match(pattern, value)
        if m is not None: # trying to replace blank
            for t in m.groups():
                if t is not None: # trying to replace
                    value.replace(t, "")

        return False



    def _obtain_valid_keyval_primary_types(self, xml_attrib: dict, request_params: dict):
        # value from request parameters
        map_val = request_params[xml_attrib["mapping"]]

        if self._sql_prevention(map_val):
            return xml_attrib["mapping"], xml_attrib["default"]
        else:
            return xml_attrib["mapping"], map_val




    def _obtain_valid_keyval_from_list(self, xml_attrib: dict, request_params: dict):

        # value from request parameters
        map_val = request_params[xml_attrib["mapping"]]

        if self._specialize_sql_prevention_for_list(map_val):
            return xml_attrib["mapping"], ""
        else:
            return xml_attrib["mapping"], map_val





    def _obtain_valid_keyval(self, xml_attrib: dict, request_params: dict):
        """
        convert other third parts requests to what we desired
        """
        if xml_attrib["mapping"] in request_params.keys():
                
            if xml_attrib["type"] == "list": 
                return self._obtain_valid_keyval_from_list(xml_attrib, request_params)
            
            else: # primary types
                return self._obtain_valid_keyval_primary_types(xml_attrib, request_params)

        # no key in request to mapping
        return None, None




    def _obtain_valid_keyval_from_dict(self, xmlnode, request_params: dict):

        for sub in xmlnode: # check sql injection
            xml_attrib = sub.attrib

            key, val = self._obtain_valid_keyval(xml_attrib, request_params)

            # update request parameters
            if key is not None:
                request_params[key] = val




    def convert(self, request_params):
        """
        This module mainly used to reduce coupling code, especially transing variables between
        two different platforms or code. At present, the most important application is the network 
        parameter request.

        Args:
        * [request_params], after receiving the data, the incoming string data is roughly converted 
            into a dictionary through some third-party packages. Using custom parsing rule files, 
            convert to the correct data format we need.
            
            see the main function for more details.
        """


        final_result = {}

        for xmlnode in self.xmlroot:

            xml_attrib = xmlnode.attrib

            if xml_attrib["type"] == "value":
                key, val = self._obtain_valid_keyval(xml_attrib, request_params)
                if key is not None:
                    final_result = DictExtern.union(final_result, proc.get_strval_from_param(xml_attrib, key, val))

            elif xml_attrib["type"] == "number":
                key, val = self._obtain_valid_keyval(xml_attrib, request_params)
                if key is not None:
                    final_result = DictExtern.union(final_result, proc.get_numval_from_param(xml_attrib, key, val))

            elif xml_attrib["type"] == "float":
                key, val = self._obtain_valid_keyval(xml_attrib, request_params)
                if key is not None:
                    final_result = DictExtern.union(final_result, proc.get_floatval_from_param(xml_attrib, key, val))

            elif xml_attrib["type"] == "boolean":
                key, val = self._obtain_valid_keyval(xml_attrib, request_params)
                if key is not None:
                    final_result = DictExtern.union(final_result, proc.get_boolval_from_param(xml_attrib, key, val))

            elif xml_attrib["type"] == "list":
                key, val = self._obtain_valid_keyval(xml_attrib, request_params)
                if key is not None:
                    final_result = DictExtern.union(final_result, proc.get_listval_from_param(xml_attrib, key, val))

            elif xml_attrib["type"] == "dictionary":
                self._obtain_valid_keyval_from_dict(xmlnode, request_params)
                final_result = DictExtern.union(final_result, proc.get_dictval_from_param(xmlnode, request_params))

        return final_result




if __name__ == "__main__":

    roughly = {"wkey1":"thus", "wkey2":"", "wkey3":"None", "wkey4":"", "wkey5":"INSERT", 
        "wkey6":"110", "wkey7":"1234|57|214.14|test|测试数据||", "wkey8":"None"}

    """ parsing rule looks like:
        <config>
            <param name="key1" type="value" default="test" mapping="wkey1"/>
            <param name="key2" type="number" default="10" mapping="wkey2"/>
            <param name="key3" type="float" default="10" mapping="wkey3"/>
            <param name="key4" type="dictionary">
                <sub name="sub1" type="number" default="1" mapping="wkey4" />
                <sub name="sub2" type="number" default="2" mapping="wkey5" />
                <sub name="sub3" type="number" default="3" mapping="wkey6" />
            </param>
            <param name="key5" type="list" v_type="number" mapping="wkey7"/>
            <param name="key6" type="boolean" default="true" mapping="wkey8"/>
        </config>
    """

    app = ApplyingXMLRules("rules.xml")
    ret = app.convert(roughly)

    """ finally output will looks like:
        [{'key1': 'thus'}, {'key2': 10}, {'key3': 0.0}, {'key4': {'sub1': 1, 'sub2': 10, 'sub3': 110}}, 
            {'key5': [1, 2, 3, 4]}, {'key6': False}]
        {'key1': 'thus', 'key2': 10, 'key3': 0.0, 'key4': {'sub1': 1, 'sub2': 10, 'sub3': 110}, 'key5': [1, 2, 3, 4], 'key6': False}
    """

    print(ret)