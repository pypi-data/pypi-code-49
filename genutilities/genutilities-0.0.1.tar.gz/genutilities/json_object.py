import json
import os


class JsonObject:
    def __init__(self, file: str, dict_default: dict = None, saved_destroy: bool = True):
        if os.path.isfile(file):
            with open(file, "r") as f:
                self.dic = json.load(f)
        else:
            if dict_default is None:
                self.dic = {}
            else:
                self.dic = dict_default
        self.file = file
        self.saved_destroy = saved_destroy
    
    def __del__(self):
        if self.saved_destroy:
            self.save()
        
    def __str__(self):
        return json.dumps(self.dic, indent=4)

    def __getitem__(self, key):
        retour = self.get(key, None)
        if retour is None:
            raise KeyError("This key doesn't exist. Use get method to give a default value.")
        return retour

    def __setitem__(self, key, value):
        self.set(key, value)

    def get(self, key: str, default):
        keys = key.split(".")
        value = self.dic
        for i in keys:
            if i == keys[-1]:
                return value.get(i, default)
            else:
                try:
                    value = value[i]
                except KeyError:
                    return default
    
    def set(self, key: str, value):
        keys = key.split(".")
        dic = self.dic
        for i in keys:
            if i == keys[-1]:
                dic[i] = value
            else:
                try:
                    dic = dic[i]
                except KeyError:
                    dic[i] = {}
                    dic = dic[i]

    def __to_xml_list(self, root_name, element_name, liste):
        xml = ["<{}>".format(root_name)]
        for i in liste:
            if isinstance(i, dict):
                for k in self.__to_xml(element_name, element_name, i):
                    xml.append("   "+k)
            elif isinstance(i, list):
                for k in self.__to_xml_list(element_name, element_name, i):
                    xml.append("   "+k)
            else:
                xml.append("   <{0}>{1}</{0}>".format(element_name, i))
        xml.append("</{}>".format(root_name))
        return xml

    def __to_xml(self, root_name, element_name, dic):
        xml = ["<{}>".format(root_name)]
        for k, v in dic.items():
            if isinstance(v, dict):
                for i in self.__to_xml(k, element_name, v):
                    xml.append("   "+i)
            elif isinstance(v, (list, tuple)):
                for i in self.__to_xml_list(k, element_name, v):
                    xml.append("   "+i)
            else:
                xml.append("   <{0}>{1}</{0}>".format(k, str(v)))
        xml.append("</{}>".format(root_name))
        return xml
            
    def to_xml(self, root_name: str = "root", element_name: str = "element"):
        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml.extend(self.__to_xml(root_name, element_name, self.dic))
        return "\n".join(xml)

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.dic, f, indent=4)