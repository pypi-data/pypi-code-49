# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import shutil
import pickle

from .tools import *
from .component import *
from .occ import *
from .log import logger
from .solution import *


class Configure:
    def __init__(self):
        self.yoc_version = 'v7.2'
        self.lastUpdateTime = 0
        self.gitlab_token = ''
        self.github_token = ''
        self.username = ''
        self.password = ''
        self.occ_host = 'occ.t-head.cn'
        self.init = False

        self.yoc_path = current_pwd()
        if not self.yoc_path:
            self.yoc_path = '/'
        tmp_path = self.yoc_path
        while tmp_path != '/':
            f = os.path.join(tmp_path, '.yoc')
            if os.path.exists(f):
                self.yoc_path = tmp_path
                conf = yaml_load(f)
                if conf:
                    self.init = True
                    for k, v in conf.items():
                        if v:
                            self.__dict__[k] = v
                break
            tmp_path = os.path.dirname(tmp_path)

    def save(self):
        yoc_file = os.path.join(self.yoc_path, '.yoc')
        with open(yoc_file, 'w') as f:
            for k, v in self.__dict__.items():
                if k not in ['yoc_path', 'init']:
                    f.write("{}: {}\n".format(k, v))
        self.init = True

    def search_pacakge_yaml(self, subpath=[]):
        paths = []
        if subpath:
            for sub in subpath:
                p = os.path.join(self.yoc_path, sub)
                if os.path.exists(p):
                    paths.append(p)
        else:
            paths.append(self.yoc_path)

        package_list = []

        while paths:
            path = paths[0]
            filename = os.path.join(path, 'package.yaml')
            if os.path.isfile(filename):
                package_list.append(filename)
            else:
                files = os.listdir(path)
                for file in files:
                    p = os.path.join(path, file)
                    if os.path.isdir(p):
                        paths.append(p)
            del paths[0]
        return package_list


class YoC:
    def __init__(self):
        self.occ = None
        self.occ_components = None
        self.yoc_version = 'v7.2'
        self.conf = Configure()
        self.yoc_path = self.conf.yoc_path

        try:
            compenent_db = os.path.join(self.yoc_path, '.components.db')
            with open(compenent_db, "rb") as f:
                self.occ_components = pickle.load(f)
                if len(self.occ_components) == 0:
                    self.occ_components = None
        except:
            self.occ_components = None

        if self.occ_components:
            self.conf.lastUpdateTime = 0

        # scanning yoc all components
        self.components = ComponentGroup()
        package_yamls = self.conf.search_pacakge_yaml(
            ['boards', 'components', 'solutions'])
        for filename in package_yamls:
            pack = Component(filename)

            if pack.version == '':
                pack.version = self.yoc_version

            if not self.components.add(pack):
                pre_component = self.components.get(pack.name)
                logger.error('component `%s` is multiple (%s : %s)' %
                             (pack.name, pre_component.path, pack.path))
                exit(0)

    def check_depend(self, component):
        def _check_depend(component):
            component.load_package()

            for name in component.depends:
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

    def getSolution(self):
        for component in self.components:
            if component.path == current_pwd():
                components = self.components.get_depend(component)
                components.append(component)
                solution = Solution(components)

                return solution

    def download_component(self, name, update=True):
        if self.components.get(name) == None:
            if update:
                self.occ_update()

            component = self.occ_components.get(name)
            if component:
                depends = self.occ_components.get_depend(component)
                depends.add(component)

                return depends

    def remove_component(self, name):
        component = self.components.get(name)
        if component:
            if not component.depends_on:                     # 如果没有组件依赖它
                for dep in component.depends:
                    p = self.components.get(dep)
                    if p:
                        if name in p.depends_on:
                            del p.depends_on[name]
                        self.remove_component(dep)

                shutil.rmtree(component.path)
                self.components.remove(component)
                return True
            else:
                logger.info("remove fail, %s depends on:" % component.name)
                for dep in component.depends_on:
                    logger.info('  ' + dep.name)
                return False

    def upload(self, name):
        component = self.components.get(name)
        if component:
            if not os.path.isdir(os.path.join(component.path, '.git')):
                if self.occ == None:
                    self.occ = OCC(self.conf)
                self.occ.login()
                zip_file = component.zip(self.yoc_path)
                if self.occ.upload(component.version, component.type, zip_file) == 0:
                    print("component upload success: " + component.name)
                else:
                    print("component upload fail: " + component.name)
                # self.save_version()

    def uploadall(self):
        if self.occ == None:
            self.occ = self.occ = OCC(self.conf)
        self.occ.login()
        for component in self.components:
            zip_file = component.zip(self.yoc_path)
            # self.occ.upload(version_inc(component.version, 1), component.type, zip_file)
            if self.occ.upload(component.version, component.type, zip_file) == 0:
                print("component upload success: " + component.name)
            else:
                print("component upload fail: " + component.name)

    def update(self):
        for component in self.components:
            component.download(self.yoc_path)

    def occ_update(self):
        if self.occ == None:
            self.occ = self.occ = OCC(self.conf)
            components, time = self.occ.yocComponentList(
                '614193542956318720', self.conf.lastUpdateTime)
            if components:
                self.occ_components = components
                self.conf.lastUpdateTime = time
                for component in self.occ_components:
                    component.path = os.path.join(
                        self.yoc_path, component.path)

                with open(os.path.join(self.yoc_path, '.components.db'), "wb") as f:
                    pickle.dump(self.occ_components, f)
                    self.conf.save()

    def list(self):
        for component in self.components:
            component.load_package()
            component.show()
            # repo.create_project(component.name, component.path, component.version)
            # if component.depends:
            #     print('  ', 'depends:')
            #     for v in component.depends:
            #         print('    -', v)
            # if component.depends_on:
            #     print('  ', 'depends_on:')
            #     for p in component.depends_on:
            #         print('    -', p.name)
