#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.utils import SaveLoad
from sekg.so import SOTagItem


class SOTagItemCollection(SaveLoad):
    def __init__(self):
        self.name2sotag = {}
        self.synonyms2tagname = {}

    def update_synonyms2tagname(self, so_tag_item: SOTagItem):
        if so_tag_item.synonyms:
            for synonym in so_tag_item.synonyms:
                self.synonyms2tagname[synonym] = so_tag_item.tag_name

    def add_so_tag_item(self, so_tag_item: SOTagItem):
        if so_tag_item is None:
            return False
        self.name2sotag[so_tag_item.tag_name] = so_tag_item
        self.update_synonyms2tagname(so_tag_item)
        return True

    def get_so_tag_item(self, tag_name):
        if tag_name in self.name2sotag.keys():
            return self.name2sotag.get(tag_name, None)
        else:
            if tag_name in self.synonyms2tagname:
                return self.name2sotag.get(self.synonyms2tagname[tag_name], None)
        return None

    def sub_collection(self, tag_names):
        subcollection = SOTagItemCollection()
        valid_tag_name = self.get_tag_names()
        for tag_name in tag_names:
            if tag_name in valid_tag_name:
                subcollection.add_so_tag_item(self.get_so_tag_item(tag_name))
        return subcollection

    def size(self):
        return len(set(self.name2sotag.keys()) | set(self.name2sotag.keys()))

    def get_tag_names(self):
        return set(self.name2sotag.keys())

    def get_all_tag_name(self):
        return set(self.name2sotag.keys()) | set(self.name2sotag.keys())
