# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import sys
import time
import hashlib
import zipfile
import codecs

try:
    from urlparse import urlparse
    import urllib
    import httplib as http
    urlretrieve = urllib.urlretrieve
except:
    from urllib.parse import urlparse
    import urllib.request
    import http.client as http
    urlretrieve = urllib.request.urlretrieve


try:
    import yaml
except:
    print("\n\nNot found pyyaml, please install: \nsudo pip install pyyaml")
    sys.exit(0)


def yaml_load(filename):
    try:
        with codecs.open(filename) as fh:
            text = fh.read()
            return yaml.safe_load(text)
    except Exception as e:
        print(e)
        exit(-1)


def current_pwd():
    return os.getcwd()


def home_path(path=''):
    return os.path.join(os.path.expanduser('~'), path)


def http2git(url):
    conn = urlparse(url)
    url = 'git@' + conn.netloc + ':' + conn.path[1:]
    return url


def MD5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


def http_get(url, path):
    conn = urlparse(url)

    if conn.scheme == "https":
        connection = http.HTTPSConnection(conn.netloc)
    else:
        connection = http.HTTPConnection(conn.netloc)

    connection.request('GET', conn.path)
    response = connection.getresponse()

    filename = os.path.join(path, os.path.basename(conn.path))

    try:
        with open(filename, 'wb') as f:
            f.write(response.read())
    except:
        pass

    return filename


def wget(url, out_file):
    start_time = time.time()

    def barProcess(blocknum, blocksize, totalsize):
        speed = (blocknum * blocksize) / (time.time() - start_time)
        # speed_str = " Speed: %.2f" % speed
        speed_str = " Speed: %sB/S         " % format_size(speed)
        recv_size = blocknum * blocksize

        # 设置下载进度条
        f = sys.stdout
        pervent = recv_size / totalsize
        percent_str = "%.2f%%" % (pervent * 100)
        n = round(pervent * 50)
        s = ('#' * n).ljust(50, '-')
        f.write(percent_str.ljust(8, ' ') + '[' + s + ']' + speed_str)
        f.flush()
        f.write('\r')

    def format_size(bytes):
        bytes = float(bytes)
        kb = bytes / 1024
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%.3fG" % (G)
            else:
                return "%.3fM" % (M)
        else:
            return "%.3fK" % (kb)

    return urlretrieve(url, out_file, barProcess)


def dfs_get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            dfs_get_zip_file(input_path + '/' + file, result)
        else:
            result.append(input_path + '/' + file)


def version_inc(v, x):
    l = len(v)
    num_start = -1
    for i in range(l - 1, -1, -1):
        if num_start == -1:
            if v[i:i + 1].isdigit():
                num_start = i + 1
        else:
            if not v[i:i + 1].isdigit():
                s = v[i + 1:num_start]
                v2 = v.replace(s, str(int(s) + x))
                return v2

    return v + '-0'


def zip_path(input_path, zipName):
    if os.path.isdir(input_path):
        base = os.path.dirname(zipName)
        try:
            os.makedirs(base)
        except:
            pass
        predir = input_path.rsplit('/', 1)[0]
        f = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
        filelists = []
        dfs_get_zip_file(input_path, filelists)
        for file in filelists:
            suffix = os.path.splitext(file)[-1]
            if suffix != '.d' and suffix != '.o':
                f.write(file, file.split(predir)[1])
        f.close()


def write_file(text, filename):
    contents = None

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except:
        pass

    if text == contents:
        return
    try:
        p = os.path.dirname(filename)
        try:
            os.makedirs(p)
        except:
            pass

        with open(filename, 'w') as f:
            f.write(text)
    except:
        print("Generate %s file failed." % filename)


def genSConcript(path):
    file_name = os.path.join(path, 'SConscript')
    text = '''Import('defconfig')\ndefconfig.library_yaml()\n'''
    write_file(text, file_name)
    return file_name


def genSConstruct(components, path):
    text = """#! /bin/env python

from yoctools.make import Make

defconfig = Make()

Export('defconfig')

defconfig.build_components()
defconfig.program()
"""

    comp_list = ''
    for component in components:
        if component != '.':
            comp_list += '    "' + component.name + '",\n'

    text = text % comp_list

    script_file = os.path.join(path, 'SConstruct')
    write_file(text, script_file)


def genMakefile(path):
    text = """CPRE := @
ifeq ($(V),1)
CPRE :=
endif


.PHONY:startup
startup: all

all:
	$(CPRE) scons -j4
	@echo YoC SDK Done


.PHONY:clean
clean:
	$(CPRE) rm yoc_sdk -rf
	$(CPRE) scons -c
	$(CPRE) find . -name "*.[od]" -delete

%:
	$(CPRE) scons --component="$@" -j4
"""

    script_file = os.path.join(path, 'Makefile')
    write_file(text, script_file)


def save_yoc_config(defines, filename):
    contents = ""

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except:
        pass

    text = '''/* don't edit, auto generated by tools/toolchain.py */\n
#ifndef __YOC_CONFIG_H__
#define __YOC_CONFIG_H__
#ifndef CONFIG_CPU\n\n'''
    for k, v in defines.items():
        if v in ['y', 'Y']:
            text += '#define %s 1\n' % k
        elif v in ['n', 'N']:
            text += '// #define %s 1\n' % k
        elif type(v) == int:
            text += '#define %s %d\n' % (k, v)
        else:
            text += '#define %s "%s"\n' % (k, v)

    text += '\n#endif\n#endif\n'

    if text == contents:
        return False

    write_file(text, filename)


def save_csi_config(defines, filename):
    text = '''/* don't edit, auto generated by tools/toolchain.py */

#ifndef __CSI_CONFIG_H__
#define __CSI_CONFIG_H__

#include <yoc_config.h>

#endif

'''

    write_file(text, filename)
