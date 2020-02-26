# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import re

from .log import logger
from .tools import *
from .package import *
from .component import *


class Variables:
    def __init__(self):
        self.vars = {}
        pass

    def set(self, k, v, lower=False):
        self.vars[k] = v
        if lower:
            self.vars[k.lower()] = v.lower()

    def get(self, var):
        if var in self.vars:
            return self.vars[var]

    def convert(self, var):
        v = var.split('?')
        if len(v) > 1:
            x = re.search('<(.+?)>', v[1], re.M | re.I)
            if x:
                x = self.get(x.group(1))
                if x not in ['y', 'yes', 't', 'true', '1']:
                    return None
                var = v[0].strip()

        x = re.findall('<(.+?)>', var)
        for key in x:
            value = self.get(key)
            if value != None:
                var = var.replace('<'+key+'>', self.vars[key])
            else:
                print('not found variable:', var)

        return var

    def items(self):
        return self.vars.items()


class Solution:
    def __init__(self, components):
        self.variables = Variables()
        self.solution_component = None       # 当前 solution 组件
        self.board_component = None          # 当前开发板组件
        self.chip_component = None           # 当前芯片组件
        self.components = components         # 使用到的组件
        self.global_includes = []
        self.libs = []
        self.libpath = []
        self.depend_libs = []
        self.defines = {}
        self.ASFLAGS = []
        self.CCFLAGS = []
        self.CXXFLAGS = []
        self.LINKFLAGS = []
        self.ld_script = ''
        self.cpu_name = ''

        # find current solution & board component
        for component in self.components:
            if component.path == current_pwd() and component.type == 'solution':
                self.solution_component = component
                self.board_component = self.components.get(
                    self.solution_component.hw_info.board_name)
                if self.board_component:
                    self.chip_component = self.components.get(
                        self.board_component.hw_info.chip_name)
                break

        if not self.solution_component:
            logger.error(
                'No define solution component, please set a solution component')
            exit(-1)

        if not self.board_component:
            for name in self.solution_component.depends:
                component = self.components.get(name)
                if component:
                    if component.type == 'board':
                        self.board_component = component
                        break
                else:
                    print("`%s` not found, please install it: yoc install %s" %
                          (name, name))
                    exit(-1)
            if not self.board_component:
                logger.warning(
                    'No define board component, please set a board component')
            else:
                self.solution_component.hw_info.board_name = self.board_component.name

        if not self.chip_component:
            for name in self.solution_component.depends:
                component = self.components.get(name)
                if component.type == 'chip':
                    self.chip_component = component
                    break
            if not self.chip_component:
                logger.warning(
                    'No define chip component, please set a chip component')
            else:
                self.solution_component.hw_info.chip_name = self.chip_component.name

        def cpu_set_variable(cpu, arch):
            self.cpu_name = cpu
            self.variables.set('CPU', cpu.upper(), True)
            if cpu.lower() == 'rv32emc':
                self.variables.set('cpu_num', 'rv32')
                self.variables.set('arch', 'RISCV', True)
            # elif cpu.lower() == 'ck803ef':
            #     self.variables.set('cpu_num', '803ef')
            #     self.variables.set('ARCH', 'CSKY', True)
            else:
                self.variables.set('cpu_num', cpu_id(cpu))
                self.variables.set('ARCH', 'CSKY', True)

        for component in self.components:
            # defines
            for k, v in component.defconfig.items():
                self.variables.set(k, v)
                self.defines[k] = v

        solution_hw_info = HardwareInfo({})
        for component in [self.chip_component, self.board_component, self.solution_component]:
            if component:
                solution_hw_info.merge(component.hw_info)

                for c in component.build_config.cflag.split():
                    self.CCFLAGS.append(c)
                for c in component.build_config.asmflag.split():
                    self.ASFLAGS.append(c)
                for c in component.build_config.cxxflag.split():
                    self.CXXFLAGS.append(c)
                for c in component.build_config.ldflag.split():
                    self.LINKFLAGS.append(c)

        # 根据 cpu_id 加载配置
        if solution_hw_info.cpu_id in solution_hw_info.cpu_list:
            for k, v in solution_hw_info.cpu_list[solution_hw_info.cpu_id].items():
                solution_hw_info.__dict__[k] = v

        # soution 的hw_info 优先
        solution_hw_info.merge(self.solution_component.hw_info)
        for k, v in self.solution_component.hw_info.__dict__.items():
            if v:
                solution_hw_info.__dict__[k] = v

        if solution_hw_info.cpu_name == '':
            logger.error("not found cpu_id, please set cpu_id")
            exit(-1)

        if solution_hw_info.cpu_name:
            cpu_set_variable(solution_hw_info.cpu_name,
                             solution_hw_info.arch_name)

        if solution_hw_info.cpu_id:
            self.variables.set(solution_hw_info.cpu_id.upper(), 1)

        if solution_hw_info.vendor_name:
            self.variables.set(
                'VENDOR', solution_hw_info.vendor_name.upper(), True)

        if solution_hw_info.chip_name:
            self.variables.set(
                'CHIP', solution_hw_info.chip_name.upper(), True)

        if solution_hw_info.board_name:
            self.variables.set(
                'BOARD', solution_hw_info.board_name.upper(), True)

        if self.chip_component:
            self.variables.set('CHIP_PATH', self.chip_component.path)

        if self.board_component:
            self.variables.set('BOARD_PATH', self.board_component.path)

        self.variables.set('SOLUTION_PATH', self.solution_component.path)
        self.yoc_path = os.path.join(self.solution_component.path, 'yoc_sdk')
        self.lib_path = os.path.join(self.yoc_path, 'lib')
        self.libpath.append(self.lib_path)

        # save_yoc_config(self.defines, os.path.join(self.solution_component.path, 'include/yoc_config.h'))
        # save_csi_config(self.defines, os.path.join(self.solution_component.path, 'include/csi_config.h'))
        self.global_includes.append(os.path.join(
            self.solution_component.path, 'include'))

        for component in self.components:
            if len(component.source_file) > 0 and component.type != 'solution' and component.name not in self.libs:
                self.libs.append(component.name)
                self.depend_libs.append(os.path.join(
                    self.lib_path, 'lib' + component.name + '.a'))

            component.variable_convert(self.variables)

            # include
            for path in component.build_config.include:
                if path not in self.global_includes:
                    self.global_includes.append(path)

            # libpath
            for path in component.build_config.libpath:
                if path not in self.libpath:
                    self.libpath.append(path)

            # libs
            for lib in component.build_config.libs:
                if lib not in self.libs:
                    self.libs.append(lib)

        if self.solution_component.hw_info.ld_script:
            self.ld_script = self.solution_component.hw_info.ld_script
        elif self.board_component and self.board_component.hw_info.ld_script:
            self.ld_script = self.board_component.hw_info.ld_script
        elif self.chip_component and self.chip_component.hw_info.ld_script:
            self.ld_script = self.chip_component.hw_info.ld_script
        else:
            logger.error("not found LD script file, please set ld_script")
            exit(-1)

    def install(self):
        for component in self.components:
            component.install(self.yoc_path)
        save_yoc_config(self.defines, os.path.join(
            self.solution_component.path, 'include/yoc_config.h'))
        save_csi_config(self.defines, os.path.join(
            self.solution_component.path, 'include/csi_config.h'))

    def show(self):
        print("[component]")
        for c in self.components:
            c.show(4)

        if self.solution_component:
            print("solution: " + self.solution_component.name)
        if self.board_component:
            print("board   : " + self.board_component.name)
        if self.chip_component:
            print("chip    : " + self.chip_component.name)

        print("[libs]")
        for v in self.libs:
            print('    ' + v)

        print("[libpath]")
        for v in self.libpath:
            print('    ' + v)

        print("[global_includes]")
        for v in self.global_includes:
            print('    ' + v)

        print("[defines]")
        for k, v in self.defines.items():
            print('    ', k, '=', v)

        print("[variables]")
        for k, v in self.variables.items():
            print('    %s = %s' % (k, v))

        print("ASFLAGS  :" + ' '.join(self.ASFLAGS))
        print("CCFLAGS  :" + ' '.join(self.CCFLAGS))
        print("CXXFLAGS :" + ' '.join(self.CXXFLAGS))
        print("LINKFLAGS:" + ' '.join(self.LINKFLAGS))


def cpu_id(s):
    s += 'z'
    ids = ''
    for c in s:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            ids += c
        elif ids:
            return ids
