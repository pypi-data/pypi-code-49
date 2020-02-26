#!/usr/bin/env python

# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import sys
import hashlib
import json
import time
import yaml
import shutil
import re


try:
    from tools import *
    from log import logger
except:
    from yoctools.tools import *
    from yoctools.log import logger


class Driver:
    def __init__(self, tag=''):
        self.name = ''
        self.tag = tag
        self.vendor = ''
        self.ip_id = ''
        self.ip_version = ''
        self.model = ''
        self.files = []
        self.tests = []

    def install(self, src_path, dest_path):
        for f in self.files:
            src = os.path.join(src_path, f.file)
            dest = os.path.join(dest_path, f.dest_file)

            file_copy3(src, dest)

    def add(self, fn):
        self.files.append(fn)

    def show(self, space=0):
        print("%stag: %s, model: %s, vendor: %s" %
              (' ' * space, self.tag, self.model, self.vendor))

        for f in self.files:
            f.show(4 + space)
            # print(' '* (4 + space), f.file)
        print("")


'''
driver file:    tag != '' and model != '' and chip == ''
interface file: tag == '' and model != '' and chip == ''
chip file:      tag == '' and chip != ''
'''
class File:
    def __init__(self, filename):
        self.file = filename
        self.dest_file = filename
        self.brief = ''
        self.version = ''
        self.date = ''
        self.vendor = ''
        self.name = ''
        self.ip_id = ''
        self.model = ''
        self.tag = ''
        self.chip = ''
        self.scan_file()

    def set_value(self, key, text):
        idx = text.find(key)
        if idx >= 0:
            key = key[1:]
            if key in self.__dict__:
                self.__dict__[key] = text[idx + len(key) + 1:].strip()
            return True

    def get_type(self):
        if self.tag == 'HAL':
            return 'HAL_FILE'
        if self.tag == 'CHIP':
            return 'CHIP_FILE'
        if self.tag == '' and self.model == 'model':
            return 'COMMON_FILE'
        if self.tag != '':
            return 'DRV_FILE'

    def scan_file(self):
        contents = ''
        try:
            with open(self.file, 'r') as f:
                contents = f.read()
        except Exception as e:
            # print(filename, str(e))
            pass

        m = re.compile(r"/\*([^\*]|(\*)*[^\*/])*(\*)*\*/", re.M | re.I)

        def parser_text(text):
            self.set_value('@brief',   text) or \
                self.set_value('@version', text) or \
                self.set_value('@date',    text) or \
                self.set_value('@vendor',  text) or \
                self.set_value('@name',    text) or \
                self.set_value('@ip_id',   text) or \
                self.set_value('@tag',     text) or \
                self.set_value('@model',   text) or \
                self.set_value('@chip',    text)

        for v in m.finditer(contents):
            for x in v.group(0).split('\n'):
                parser_text(x)
            if self.tag == '' and self.model != '':
                if self.model == 'common':
                    self.tag = 'BASE'
                else:
                    self.tag = 'HAL'
            if self.tag == '' and self.chip != '':
                self.tag = 'CHIP'
                self.model = 'CHIP'

            if self.tag:
                break

        if not self.tag:
            m = re.finditer(r'\[\/\/\]:\s+#\s+"(.+?)"', contents)
            for i in m:
                parser_text(i.group(1).strip())

    def show(self, space=0):
        print("%stag: %-18s, model: %-10s, vendor: %-8s, chip: %-6s, file: %s" %
              (' '*space, self.tag, self.model, self.vendor, self.chip, self.file))


class Device:
    def __init__(self, conf):
        self.conf = conf
        self.TAG = self.get('TAG', '')
        self.VERSION = self.get('VERSION', '')
        self.ADDRESS = self.get('ADDRESS', 0)
        self.IRQ = self.get('IRQ', -1)
        self.INDEX = self.get('INDEX', 0)

    def get(self, name, default):
        if name in self.conf:
            return self.conf[name]
        return default


class Model:
    def __init__(self, name):
        self.name = name
        self.drivers = {}

    def add(self, dri):
        self.drivers[dri.tag] = dri

    def show(self):
        print(self.name)
        for _, v in self.drivers.items():
            v.show(4)


class CSI:
    def __init__(self, base_path):
        self.devices = []           # 设备列表

        self.csi_path = base_path
        self.all_drivers, self.models = scan_node(base_path)  # 驱动列表

        # print(models)

    def show_drivers(self):
        for _, mod in self.all_drivers.items():
            mod.show()

    def show(self):
        for _, mod in self.models.items():
            mod.show()


class Chip:
    def __init__(self, csi, chip_conf):
        self.chip_name = ''
        self.devices = []           # 设备列表
        self.drivers = {}
        self.drivers_need = {}
        self.models = {}
        self.csi = csi

        self.load(chip_conf)

    def load(self, filename):
        conf = yaml_load(filename)
        if conf:
            self.chip_name = conf['chip']
            for drv in conf['devices']:
                d = Device(drv)
                self.devices.append(d)
                dri = self.csi.all_drivers[d.TAG]
                self.drivers[d.TAG] = dri
                self.models[dri.model] = True

            def CHIP_DRV(name, n):
                drv = Driver(name)
                for f in self.csi.all_drivers[name].files:
                    if n(f):
                        drv.add(f)
                self.drivers[name] = drv

            CHIP_DRV('BASE', lambda f: True)
            CHIP_DRV('DOC', lambda f: f.tag in self.drivers)
            CHIP_DRV('HAL', lambda f: f.tag ==
                     'HAL' and f.model in self.models)
            CHIP_DRV('CHIP', lambda f: f.chip == self.chip_name)

    def install(self, dest_path):
        for _, v in self.drivers.items():
            v.install(self.csi.csi_path, dest_path)
        self.genChip(dest_path)
        save_package(self, os.path.join(dest_path, 'package.yaml'))

    def show(self):
        for _, v in self.drivers.items():
            v.show()

    def genChip(self, dest_path):
        max_irq = 0
        for d in self.devices:
            if d.IRQ > max_irq:
                max_irq = d.IRQ

        devices = []
        for i in range(0, max_irq + 1):
            devices.append('')

        for d in self.devices:
            s = '    {%s, 0x%x, %d}' % (d.TAG, d.ADDRESS, d.INDEX)
            devices[d.IRQ] = s

        fmt = '''
const device_map_t chip_device_config[] = {\n%s};
'''
        text = ''
        for i, s in enumerate(devices):
            if s:
                text += s + ',\n'
            else:
                text += '    {-1, -1, -1},\n'

        text = fmt % text

        write_file(text, os.path.join(dest_path, 'include/soc.h'))


def scan_node(path):
    nodes = []

    # 生成所有 File
    for dirpath, _, filenames in os.walk(path):
        for name in filenames:
            filename = os.path.join(dirpath, name)
            idx = filename.rfind('.')
            if idx >= 0 and filename[idx:] in ['.c', '.h', '.s', '.S', '.md']:
                node = File(filename)
                if node.get_type():
                    node.file = os.path.relpath(node.file, path)
                    if node.tag == 'CHIP':
                        filename = node.file.replace(
                            node.vendor, '').replace(node.chip, '')
                        filename = os.path.relpath(filename, '/')
                        node.dest_file = filename
                    elif node.tag == 'HAL':
                        filename = os.path.basename(node.file)
                        node.dest_file = os.path.join('include', filename)
                    elif node.tag:
                        if node.model == 'doc':
                            node.dest_file = 'docs/' + \
                                os.path.basename(node.file)
                        else:
                            node.dest_file = 'drivers/' + \
                                os.path.basename(node.file)
                    nodes.append(node)

    driver_list = {}
    models = {}
    for f in nodes:
        if f.model == 'doc':
            TAG = 'DOC'
        else:
            TAG = f.tag

        if TAG not in driver_list:
            drv = Driver(TAG)
            drv.name = f.name
            if drv.tag != 'HAL':
                drv.model = f.model
            drv.vendor = f.vendor
            drv.ip_id = f.ip_id
            driver_list[TAG] = drv

            if drv.model in models:
                model = models[drv.model]
                model.add(drv)
            elif drv.model not in ['doc', 'CHIP', 'common', '']:
                model = Model(drv.model)
                models[drv.model] = model
                model.add(drv)
        else:
            drv = driver_list[TAG]
        drv.add(f)

    return driver_list, models


def file_copy3(src, dest):
    try:
        path = os.path.dirname(dest)
        if not os.path.exists(path):
            os.makedirs(path)
        print('install', src)
        shutil.copy2(src, dest)
        return True
    except Exception as e:
        print(str(e))


def save_package(chip, filename):
    fmt = '''
name: chip-%s
description: ''
keywords:
  - base
license: Apache license v2.0

hidden: true

depends:
  - yoc_base

build_config:
  include:
    - include
    - %s/include
  cflag: ''
  cxxflag: ''
  asmflag: ''

source_file:
%s
'''
    fs = ''
    for _, v in chip.drivers.items():
        for f in v.files:
            if f.dest_file[-2:] in ['.c', '.S']:
                fs += '  - ' + f.dest_file + '\n'
    text = fmt % (chip.chip_name, chip.chip_name, fs)
    write_file(text, filename)


def test_chip():
    chip = Chip('../../csi/csi_driver', '../../csi/chip_conf/pangu.yaml')
    chip.show()
    # chip.install('sdk')


def usage():
    print("Usage:")
    print("  csi <command> [options]\n")
    print("Commands:")
    print("  show <csi_path> <chip_config.yaml>               show chip resource tree")
    print("  export <csi_path> <chip_config.yaml> <dest_path> export chip sdk source code")
    print("")

    print("General Options:")
    print("  -h, --help                  Show help.")


def gen_chip_sdk():
    argc = len(sys.argv)
    if argc < 2:
        usage()
        exit(0)

    if sys.argv[1] == 'show':
        if argc == 4:
            csi = CSI(sys.argv[2])
            chip = Chip(csi, sys.argv[3])

            chip.show()
        else:
            usage()
    elif sys.argv[1] == 'export':
        if argc == 5:
            chip = Chip(sys.argv[2], sys.argv[3])
            chip.install(sys.argv[4])
        else:
            usage()


def test_csi(f):
    csi = CSI(f)
    csi.show_drivers()
    print("=============================================")
    csi.show()
    exit(0)
    c = Chip(csi, '../../csi/chip_conf/pangu.yaml')
    print("=============================================")
    c.show()
    exit(0)


if __name__ == "__main__":
    test_csi('../../csi/csi_driver')
    if len(sys.argv) > 2:
        gen_chip_sdk()
    else:
        test_chip()
