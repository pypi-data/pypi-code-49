# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import sys
try:
    import SCons.Script as SCons
except:
    import scons
    for path in scons.__path__:
        sys.path.append(path)
        import SCons.Script as SCons

from .log import logger
from .toolchain import *


class Builder(object):
    def __init__(self, solution):
        self.toolchain_path = ''
        self.PREFIX = 'csky-abiv2-elf'
        self.SIZE = lambda: self.PREFIX + '-size'
        self.OBJDUMP = lambda: self.PREFIX + '-objdump'
        self.OBJCOPY = lambda: self.PREFIX + '-objcopy'
        self.STRIP = lambda: self.PREFIX + '-strip'
        self.AS = lambda: self.PREFIX + '-gcc'
        self.CC = lambda: self.PREFIX + '-gcc'
        self.CXX = lambda: self.PREFIX + '-g++'
        self.AR = lambda: self.PREFIX + '-ar'
        self.LINK = lambda: self.PREFIX + '-g++'

        self.solution = solution

        self.env = SCons.Environment(tools=['default', 'objcopy', 'objdump', 'product'],
                                     toolpath=[os.path.dirname(
                                         __file__) + '/site_tools'],
                                     AS=self.AS(),
                                     CC=self.CC(),
                                     CXX=self.CXX(),
                                     AR=self.AR(),
                                     LINK=self.CXX(),
                                     OBJCOPY=self.OBJCOPY(),
                                     OBJDUMP=self.OBJDUMP(),
                                     ARFLAGS='-rc',
                                     )

        # self.env.Decider('timestamp-newer')
        self.env.Decider('make')
        # self.env.Decider('MD5')

        self.env.PrependENVPath('TERM', "xterm-256color")
        self.env.PrependENVPath('PATH', os.getenv('PATH'))

        if SCons.GetOption('verbose'):
            self.env.Replace(
                ARCOMSTR='AR $TARGET',
                ASCOMSTR='AS $TARGET',
                ASPPCOMSTR='AS $TARGET',
                CCCOMSTR='CC $TARGET',
                CXXCOMSTR='CXX $TARGET',
                # LINKCOMSTR = 'LINK $TARGET',
                INSTALLSTR='INSTALL $TARGET',
                # BINCOMSTR="Generating $TARGET",
            )

        self.set_cpu(self.solution.cpu_name)
        if self.solution.LINKFLAGS:
            linkflags = self.solution.LINKFLAGS
        else:
            linkflags = ['-lm', '-Wl,-ckmap="yoc.map"',
                         '-Wl,-zmax-page-size=1024']
        self.env.AppendUnique(
            ASFLAGS=self.solution.ASFLAGS,
            CCFLAGS=self.solution.CCFLAGS,
            CXXFLAGS=self.solution.CXXFLAGS,
            LINKFLAGS=linkflags,
        )

    def set_cpu(self, cpu):
        flags = ['-MP', '-MMD', '-g', '-Os', '-Wno-main']
        self.CPU = cpu.lower()
        if self.CPU in ['ck801', 'ck802', 'ck803', 'ck805', 'ck803f', 'ck803ef', 'ck803efr1', 'ck804ef', 'ck805f', 'ck805ef']:
            self.PREFIX = 'csky-abiv2-elf'
            flags.append('-mcpu=' + self.CPU)
            if 'f' in self.CPU:
                flags.append('-mhard-float')
            if self.CPU == 'ck803ef':
                flags.append('-mhigh-registers')
                flags.append('-mdsp')
        elif self.CPU in ['rv32emc']:
            self.PREFIX = 'riscv64-unknown-elf'
            flags.append('-march=' + self.CPU)
            flags.append('-mabi=ilp32e')
        else:
            logger.error(
                'error cpu `%s`, please make sure your cpu mode' % self.CPU)
            exit(0)

        self.env.AppendUnique(
            ASFLAGS=flags, CCFLAGS=flags,
            CXXFLAGS=flags, LINKFLAGS=flags
        )

    def clone_component(self, component):
        def var_convert(defs):
            if type(defs) == dict:
                vars = {}
                for k, v in defs.items():
                    if type(v) == str:
                        vars[k] = '\\"' + v + '\\"'
                    else:
                        vars[k] = v
                return vars
            else:
                return defs

        env = self.env.Clone()

        if component.build_config.cflag:
            env.AppendUnique(CCFLAGS=component.build_config.cflag.split())
            env.AppendUnique(CCFLAGS=component.build_config.cflag.split())
        if component.build_config.cxxflag:
            env.AppendUnique(CPPFLAGS=component.build_config.cxxflag.split())
        if component.build_config.asmflag:
            env.AppendUnique(ASFLAGS=component.build_config.asmflag.split())

        env.AppendUnique(CPPPATH=component.build_config.internal_include)
        env.AppendUnique(CPPPATH=self.solution.global_includes)
        env.AppendUnique(CPPDEFINES=var_convert(self.solution.defines))
        env.AppendUnique(CPPDEFINES=var_convert(component.build_config.define))

        if self.toolchain_path == '':
            tool = ToolchainInstall()
            path = tool.check_toolchain(self.PREFIX)
            if path:
                self.toolchain_path = os.path.dirname(path)
        if self.toolchain_path:
            env.PrependENVPath('PATH', self.toolchain_path)
        else:
            print("not found toolchain, please check it.")
            exit(-1)

        return env

    def build_component(self, component):
        env = self.clone_component(component)

        sources = []
        for fn in component.source_file:
            f_list = env.Glob(fn)
            if f_list:
                for f in f_list:
                    if f not in sources:
                        sources.append(f)

        if component.type == 'solution':
            linkflags = ' -Wl,--whole-archive -l' + \
                ' -l'.join(self.solution.libs) + ' -Wl,--no-whole-archive'
            linkflags += ' -nostartfiles -Wl,--gc-sections'
            linkflags += ' -T ' + self.solution.ld_script
            cname = 'yoc'  # component.name
            env.AppendUnique(LINKFLAGS=linkflags.split())
            env.AppendUnique(LIBPATH=self.solution.libpath)
            job = env.Program(target=cname + '.elf', source=sources)

            env.Decider(config_file_decider)
            env.Depends(job, self.solution.depend_libs)
            env.Default(job)
        else:
            job = env.StaticLibrary(os.path.join(
                self.solution.lib_path, component.name), sources)

            env.Default(job)

    def build_image(self, path):
        component = self.solution.solution_component
        env = self.clone_component(component)

        if path and not os.path.exists(path):
            os.makedirs(path)
        source_name = os.path.join('out', component.name, 'yoc.elf')
        job1 = env.Binary(source=source_name,
                          target=os.path.join(path, 'prim'))
        job2 = env.Dump(source=source_name, target='yoc.asm')
        job3 = env.Zip(source='generated/data/config.yaml',
                       target="generated/images.zip", PATH='generated/data')
        job4 = env.Hex(source='generated/images.zip', PATH='generated')
        env.Default(job1)
        env.Default(job2)
        env.Default(job3)
        env.Default(job4)


def config_file_decider(dependency, target, prev_ni, repo_node=None):
    # print(dependency, prev_ni)
    if not prev_ni:
        return True
    if dependency.get_timestamp() != prev_ni.timestamp:
        return True

    return False
