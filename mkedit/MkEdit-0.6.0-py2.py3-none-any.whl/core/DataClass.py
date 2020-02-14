#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class FileInfo:
    def __init__(self, fileName: str = "", filePath: str = "", data: List = None):
        self.fileName = fileName
        self.filePath = filePath
        self.data = data


class WorkdirInfo:
    def __init__(self, dirPath: str = ""):
        self.dirPath = dirPath


class CreateDirInfo:
    def __init__(self, dirPath: str = ""):
        self.dirPath = dirPath


class CreateFileInfo:
    def __init__(self, dirPath: str = ""):
        self.dirPath = dirPath