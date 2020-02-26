# -*- coding:utf-8 -*-


import os
import re
import string
from src.analysis.analysis_base import AnalysisBase


class BathroomSSC(AnalysisBase):
    """
        Description:
            preprocess str, drop punction and prefix-suffix
    """

    def __init__(self, dict_map, config):
        self.exclude_set = []
        self.prefix_list = []
        self.suffix_list = []
        self.prefix_pattern = None
        if 'punction' in config['use_dict_name']:
            self.exclude_set = dict_map['punction']
        if 'prefix' in config['use_dict_name']:
            self.prefix_list = dict_map['prefix']
            self.prefix_pattern = re.compile(
                r"^{}".format("|".join(self.prefix_list)))
        if 'suffix' in config['use_dict_name']:
            self.suffix_list = config['use_dict_name']

    def drop_endpunc(self, text):
        while text:
            if text[-1] in self.exclude_set:
                text = text[:-1]
            else:
                break
        return text

    def remove_suffix(self, text):
        if isinstance(text, str):
            if len(text) > 0:
                start = len(text)
                if text[-1] in self.suffix_list:
                    text = text[:-1]
                if start > len(text):
                    return self.remove_suffix(text)
                else:
                    return text
            else:
                return text
        else:
            return text

    def clean(self, text):
        text_clean = text.strip()
        if self.exclude_set:
            text_clean = self.drop_endpunc(text_clean.lower().replace("\n", ""))
        if self.prefix_pattern:
            text_clean = re.sub(self.prefix_pattern, '', text_clean)
        if self. suffix_list:
            text_clean = self.remove_suffix(text_clean)
        return text_clean

    def process(self, text):
        return self.clean(text)
