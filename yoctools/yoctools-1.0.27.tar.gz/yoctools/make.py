# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


import os
import sys

from .tools import *
from .log import logger
from .yoc import YoC
from .builder import *

try:
    import SCons.Script as SCons
except:
    import scons
    for path in scons.__path__:
        sys.path.append(path)
        import SCons.Script as SCons


SCons.AddOption('--verbose', dest='verbose', default=True,
                action='store_false',
                help='verbose command line output')


class Make(object):
    def __init__(self):
        self.yoc = YoC()
        solution = self.yoc.getSolution()
        if solution:
            self.build_env = Builder(solution)

    def library_yaml(self):
        package_file = self.build_env.env.GetBuildPath('package.yaml')
        conf = yaml_load(package_file)
        if conf and 'name' in conf:
            component = self.yoc.components.get(conf['name'])
            self.build_env.build_component(component)
            component.export()

    def build_component(self, component):
        new_file = False
        file_name = os.path.join(component.path, 'SConscript')
        if not os.path.exists(file_name):
            file_name = genSConcript(component.path)
            new_file = True
        if os.path.isfile(file_name):
            SCons.SConscript(file_name, exports={"env": self.build_env.env.Clone(
            )}, variant_dir='out/' + component.name, duplicate=0)
            if new_file:
                os.remove(file_name)

    def build_components(self, components=None):
        if components != None:
            for c in components:
                component = self.yoc.components.get(c)
                if component:
                    self.build_component(component)
        else:
            for component in self.build_env.solution.components:
                self.build_component(component)

    def build_image(self, path):
        self.build_env.build_image(path)

    def install(self):
        self.build_env.install()
