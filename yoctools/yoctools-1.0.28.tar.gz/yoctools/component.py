# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import sys
import json
import zipfile
import shutil
import threadpool


from .tools import *
from .log import logger
from .package import *
from .gitproject import *


class Component:
    def __init__(self, filename=''):
        self.path = os.path.dirname(filename)
        self.name = os.path.basename(self.path)
        self.type = ''
        self.version = ''
        self.depends = []
        self.description = ''
        self.license = ''
        self.historyVersion = {}
        self.updated = ''
        self.repo_url = ''
        self.repo = None
        self.yoc_version = ''
        self.source_file = []
        self.defconfig = {}
        self.build_config = None
        self.hw_info = None
        self.installs = []
        self.exports = []

        self.depends_on = []  # 该组件被哪个组件依赖

    def loader_json(self, js):
        self.js = js
        self.name = js['name']
        self.depends = js['depends']
        self.description = js['description']
        self.version = js['versions']
        self.license = js['license']
        self.type = js['type']
        # self.repo_url = js['aboutURL']
        # self.repo_url = 'git@gitlab.com:occ-thead/%s.git' % self.name
        # self.repo_url = 'git@github.com:yoc-components/%s.git' % self.name
        self.repo_url = 'https://github.com/yoc-components/%s.git' % self.name

        self.updated = js['updated']

        for ver in js['historyVersion']:
            self.historyVersion[ver['version']] = ver['url']

        if self.type == 'board':
            self.path = os.path.join('boards', self.name)
        elif self.type == 'solution':
            self.path = os.path.join('solutions', self.name)
        else:
            self.path = os.path.join('components', self.name)

    def download(self, yoc_path=''):
        if self.repo_url:
            prj = GitRepo(self.path, self.repo_url)
            # print("%s(%s), clone %s %s ..." % (self.name, self.version, self.repo_url, self.path))
            # print("%s(%s) ..." % (self.name, self.version))
            prj.pull(self.version, None)

        elif self.version in self.historyVersion.keys():
            zip_url = self.historyVersion[self.version]
            filename = http_get(zip_url, os.path.join(yoc_path, '.cache'))
            zipf = zipfile.ZipFile(filename)
            if self.path != '.':
                zipf.extractall('components/')
            else:
                zipf.extractall('.')

    def zip(self, path):
        zipName = os.path.join(
            path, '.cache', self.name + '-' + self.version + '.zip')
        if os.path.exists(zipName):
            os.remove(zipName)
        zip_path(self.path, zipName)

        return zipName

    def show(self, indent=0):
        if os.path.isdir(self.path):
            status = '*'
        else:
            status = ' '

        s1 = self.name + ' (' + self.version + ')'
        size = len(s1)

        text1, text2 = string_strip(self.description, 80)
        print("%s%s %s %s - %s" %
              (' '*indent, status, s1, ' ' * (40 - size), text1))
        while text2:
            text1, text2 = string_strip(text2, 80)
            print(' ' * 46 + text1)

    def info(self, indent=0):
        for f in self.source_file:
            print('%s%s' % (' '*indent, f))

    def load_package(self):
        if self.type:
            return

        filename = os.path.join(self.path, 'package.yaml')

        pack = Package(filename)

        if os.path.basename(self.path) != pack.name:
            logger.warning(
                "component `%s`, but the directory is `%s`." % (pack.name, filename))

        if self.repo:
            self.version = self.repo.active_branch.name

        self.name = pack.name
        self.type = pack.type
        self.description = pack.description
        self.yoc_version = pack.yoc_version
        self.source_file = pack.source_file
        self.build_config = pack.build_config
        self.defconfig = pack.defconfig
        self.installs = pack.install
        self.exports = pack.export
        self.hw_info = pack.hw_info

        self.depends = []
        for d in pack.depends:
            if type(d) == dict:
                for k, _ in d.items():
                    self.depends.append(k)
            else:
                self.depends.append(d)

    def variable_convert(self, varList):
        # include
        incs = []
        for inc in self.build_config.include:
            inc = varList.convert(inc)
            if inc != None:
                path = os.path.join(self.path, inc)
                if not (os.path.isdir(path) and os.path.exists(path)):
                    logger.warning('%s is not exists or not directory.' % path)

            if path not in incs:
                incs.append(path)
        self.build_config.include = incs

        # libpath
        libpaths = []
        for var in self.build_config.libpath:
            var = varList.convert(var)
            if var != None:
                path = os.path.join(self.path, var)
                if not (os.path.isdir(path) and os.path.exists(path)):
                    logger.warning('%s is not exists or not directory.' % path)

            if path not in libpaths:
                libpaths.append(path)
        self.build_config.libpath = libpaths

        # libs
        libs = []
        for lib in self.build_config.libs:
            lib = varList.convert(lib)
            if lib != None and lib not in libs:
                libs.append(lib)
        self.build_config.libs = libs

        # sources
        sources = []
        for s in self.source_file:
            fn = varList.convert(s)
            if fn != None:
                sources.append(fn)
        self.source_file = sources

        if self.hw_info.ld_script:
            ld_script = varList.convert(self.hw_info.ld_script)
            if ld_script:
                self.hw_info.ld_script = os.path.join(self.path, ld_script)

        # install
        installs = []
        for ins in self.installs:
            srcs = []
            for src in ins['source']:
                srcs.append(varList.convert(src))
            installs.append({
                'dest': varList.convert(ins['dest']),
                'source': srcs,
            })
        self.installs = installs

        # export
        exports = []
        for ins in self.exports:
            srcs = []
            for src in ins['source']:
                srcs.append(varList.convert(src))
            exports.append({
                'dest': varList.convert(ins['dest']),
                'source': srcs,
            })
        self.exports = exports

    def install(self, dest):
        for ins in self.installs:
            path = os.path.join(dest, ins['dest'])
            if not os.path.exists(path):
                os.makedirs(path)

            for src in ins['source']:
                src = os.path.join(self.path, src)
                for s in glob.iglob(src):
                    fn = os.path.basename(s)
                    ds = os.path.join(path, fn)
                    # print(ds, s)
                    shutil.copy2(s, ds)

    def export(self):
        for ins in self.exports:
            path = ins['dest']
            if not os.path.exists(path):
                os.makedirs(path)

            for src in ins['source']:
                src = os.path.join(self.path, src)
                for s in glob.iglob(src):
                    fn = os.path.basename(s)
                    ds = os.path.join(path, fn)
                    # print(ds, s)
                    shutil.copy2(s, ds)


class ComponentGroup(list):
    def __init__(self):
        list.__init__([])
        self.components = {}

    def add(self, component):
        not_exists = component.name not in self.components
        if not_exists:
            self.append(component)
            self.components[component.name] = component
        return not_exists

    def get(self, name):
        for c in self:
            if c.name == name:
                return c

    def remove(self, name):
        for c in self:
            if c.name == name:
                del c
                break

    def show(self):
        for c in self:
            c.show()

    def download_all(self):
        def thread_execture(component):
            component.download()

        components = []
        for component in self.components:
            components.append(component)

        task_pool = threadpool.ThreadPool(5)
        requests = threadpool.makeRequests(thread_execture, components)
        for req in requests:
            task_pool.putRequest(req)
        task_pool.wait()

    def get_depend(self, component):
        def _check_depend(component):
            component.load_package()

            for name in component.depends:
                if type(name) == dict:
                    name = name['name']
                c = self.components.get(name)
                if c:
                    if c not in depends:
                        depends.append(c)
                    if component not in c.depends_on:
                        c.depends_on.append(component)
                    _check_depend(c)

        depends = ComponentGroup()

        _check_depend(component)
        return depends


def string_strip(text, size):
    L = 0
    R = ''
    i = 0
    for c in text:
        if c >= '\u4E00' and c <= '\u9FA5':
            # print(c)
            L += 2
        else:
            # print('  ', c)
            L += 1
        R += c
        i += 1
        if L >= size:
            break
    return R, text[i:]


def version_compr(a, b):
    if b[:2] == '>=':
        return a >= b[2:]
    if b[:1] == '>':
        return a > b[1:]
    return a == b
