# -*- coding: utf-8 -*-


def read_content(file_path):
    fp = open(file_path)
    content = fp.readlines()
    fp.close()
    return content
