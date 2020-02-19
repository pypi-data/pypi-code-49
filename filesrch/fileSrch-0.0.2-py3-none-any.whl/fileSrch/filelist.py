#!/usr/bin/python3
import os
import fnmatch

def files(path,pattern):
    files = []
    for root, dirs, fs in os.walk(path):
        if fs:
            for f in fs:
                if fnmatch.fnmatch(f, pattern):
                    files.append(os.path.join(root,f))
    return files