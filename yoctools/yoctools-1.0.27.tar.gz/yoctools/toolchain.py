# -*- coding:utf-8 -*-
#
# Copyright (C) 2015-2020 Alibaba Group Holding Limited


from __future__ import print_function

import os, stat
import tarfile
import subprocess
import platform

from .tools import *


toolchain_url_64 = "https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420257228264570880/1574927493455/csky-elfabiv2-tools-x86_64-minilibc-20191122.tar.gz"
toolchain_url_32 = "https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420257228264570880/1574927450819/csky-elfabiv2-tools-i386-minilibc-20191122.tar.gz"

rsicv_url_64 = 'https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420262990181302272/1577083328051/riscv64-elf-x86_64-20191111.tar.gz'
rsicv_url_32 = 'https://cop-image-prod.oss-cn-hangzhou.aliyuncs.com/resource/420262990181302272/1577082864564/riscv64-elf-i386-20191111.tar.gz'

all_toolchain_url = {
    'csky-abiv2-elf': [toolchain_url_32, toolchain_url_64],
    'riscv64-unknown-elf': [rsicv_url_32, rsicv_url_64]
}


class ToolchainInstall:
    def __init__(self, path=None):
        if path:
            self.basepath = path
        else:
            self.basepath = home_path('/usr/local/thead/')


        # toolchain_path = os.path.join(self.basepath, 'csky-abiv2-elf')
        # toolchain_bin = os.path.join(toolchain_path, 'bin')
        # files = os.listdir(toolchain_bin)

        # for fil in files:
        #     p = os.path.join(toolchain_bin, fil)
        #     if os.path.isfile(p):
        #         if os.stat(p).st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH) != 0:
        #             try:
        #                 os.symlink(p, os.path.join('/usr/bin', os.path.basename(p)))
        #             except FileExistsError as e:
        #                 pass
        #             except PermissionError:
        #                 print("please use: sudo", ' '.join(sys.argv))
        #                 exit(-1)
        #             except Exception as e:
        #                 pass


    def download(self, arch):
        toolchain_path = os.path.join(self.basepath, arch)

        if os.path.exists(toolchain_path) or arch not in all_toolchain_url:
            return

        architecture = platform.architecture()
        if architecture[0] == '64bit':
            toolchain_url = all_toolchain_url[arch][1]
        else:
            toolchain_url = all_toolchain_url[arch][0]

        tar_path = '/tmp/' + os.path.basename(toolchain_url)
        wget(toolchain_url, tar_path)
        print("")
        with tarfile.open(tar_path, 'r:gz') as tar:
            tar.extractall(toolchain_path)

        os.remove(tar_path)

        toolchain_bin = os.path.join(toolchain_path, 'bin')
        files = os.listdir(toolchain_bin)

        for fil in files:
            p = os.path.join(toolchain_bin, fil)
            if os.path.isfile(p):
                if os.stat(p).st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH) != 0:
                    try:
                        os.symlink(p, os.path.join('/usr/bin', os.path.basename(p)))
                    except FileExistsError:
                        pass
                    except PermissionError:
                        print("please use: sudo", ' '.join(sys.argv))
                        exit(-1)
                    except Exception as e:
                        pass

    def fix_env(self, arch):
        toolchain_path = '$HOME/.thead/%s/bin' % arch
        shell = os.getenv('SHELL')
        shell = os.path.basename(shell)

        if shell == 'zsh':
            rc = home_path('.zshrc')

        elif shell == 'bash':
            rc = home_path('.bashrc')

        with open(rc, 'r') as f:
            contents = f.readlines()

        export_path = ''
        for i in range(len(contents)):
            c = contents[i]
            idx = c.find(' PATH')
            if idx > 0:
                idx = c.find('=')
                if idx >= 0:
                    export_path = c[idx + 1:]

                    if export_path.find(toolchain_path) < 0:
                        export_path = 'export PATH=' + toolchain_path + ':' + export_path
                        contents[i] = export_path

        if not export_path:
            contents.insert(0, 'export PATH=' + toolchain_path + ':$PATH\n\n')

        with open(rc, 'w') as f:
            contents = f.writelines(contents)

    def check_toolchain(self, arch='csky-abiv2-elf'):
        bin_file = self.check_program(arch)
        if bin_file == '':
            self.download(arch)
            # self.fix_env(arch)
            bin_file = self.check_program(arch)
        return bin_file

    def which(self, cmd):
        gcc = subprocess.Popen('which ' + cmd, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines = gcc.stdout.readlines()
        for text in lines:
            text = text.decode().strip()
            info = 'which: no ' + os.path.basename(cmd) + ' in'
            if not text.find(info) >= 0:
                return text
        return ''

    def check_program(self, arch='csky-abiv2-elf'):
        path = self.which(arch + '-gcc')
        if path == '':
            path = home_path('.thead/' + arch + '/bin/' + arch + '-gcc')
            path = self.which(path)
            return path
        else:
            return path
