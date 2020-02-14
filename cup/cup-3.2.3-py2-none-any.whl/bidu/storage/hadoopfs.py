#!/usr/bin/env python
# -*- coding: utf-8 -*
# #############################################################
#
#  Copyright (c) Baidu.com, Inc. All Rights Reserved
#
# #############################################################
"""
:authors:
    yangruiying yangruiying @yangruiying01
"""
from __future__ import print_function
import os
import signal
import shlex
import subprocess
import threading
import warnings

# pylint: disable=R0904
class HdfsCmd(object):
    """
    执行hdfs命令的类，举例ls操作用法如下：
    其中timeout代表命令超时时间， 传入None代表一直等待直到超时.
    返回一个dict, 包含'stdout' 'stderr' 'returncode' 三个key:
    returncode == 0 代表执行成功, returncode 999代表执行超时.
    其他命令类比ls

    ::
        from cup.bidu.storage import hadoopfs
        fsshell = hadoopfs.HdfsCmd(hadoophome)
        # timeout为NONE表示一直运行直到fsshell命令返回
        fsshell.ls('/dir1', timeout=NONE)
        # timeout>=0, 等待固定时间，如超时未结束terminate fsshell命令
        fsshell.ls('/dir1', timeout=30)
    """

    def __init__(self, hadoophome=None):
        """
        :param hadoophome:
            如果不传，表示使用默认环境变量HADOOP_HOME
            传入则使用hadoophome。如
            /home/yangruiying/hadoop-client/hadoop/bin/

        :raise:
            如果hadoophome不存在或者不是个目录，会raise TypeError
        """
        if hadoophome is None:
            self._hadoophome = os.getenv("HADOOP_HOME")
        else:
            self._hadoophome = hadoophome
            if not os.path.isdir(self._hadoophome):
                raise TypeError('hadoophome should be a direcotry')
        self._subpro = None
        self._subpro_data = None

    def run(self, cmd, path, timeout):
        """
        参见类说明。

        :param cmd:
            fsshel命令

        :param path
            fsshell操作除命令部分，如可选参数，路径等

        :param timeout:
            fsshell命令执行等待时间， None为无限等待。 timeout>=0等待具体时间，
            超时terminate.

        :return:
            一个dict, 包含'stdout' 'stderr' 'returncode' 三个key:

            returncode == 0 代表执行成功, returncode 999代表执行超时

            {
                'stdout' : 'Success',
                'stderr' : None,
                'returncode' : 0
            }

        E.g.

        执行ls， 超时时间为10s, 超过10s会kill掉该fsshell进程，
        然后返回returncode 999
        ::
            from cup.bidu.storage import hadoopfs
            fsshell = hadoopfs.HdfsCmd(
                '/home/yangruiying/hadoop-client/hadoop/bin/'
            )
            print(fsshell.ls('/yry', timeout=10))
        """

        def _signal_handle():
            signal.signal(signal.SIGPIPE, signal.SIG_DFL)

        def _target(cmd):
            hadoopcmd = self._hadoophome + cmd + " " + path
            self._subpro = subprocess.Popen(
                shlex.split(hadoopcmd), shell=False, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=_signal_handle
            )
            self._subpro_data = self._subpro.communicate()

        ret = {
            'stdout': None,
            'stderr': None,
            'returncode': 0
        }
        cmdthd = threading.Thread(target=_target, args=(cmd, ))
        cmdthd.start()
        cmdthd.join(timeout)
        if cmdthd.isAlive() is True:
            str_warn = (
                'fsshell "%s"execution timout:%d. To kill it' % (cmd, timeout)
            )
            warnings.warn(str_warn, RuntimeWarning)
            self._subpro.terminate()
            ret['returncode'] = 999
            ret['stderr'] = str_warn
        else:
            ret['returncode'] = self._subpro.returncode
            assert type(self._subpro_data) == tuple, \
                'self._subpro_data should be a tuple'
            ret['stdout'] = self._subpro_data[0]
            ret['stderr'] = self._subpro_data[1]
        return ret

    def ls(self, path, timeout):
        """
        如果是文件，则按照如下格式返回文件信息：
        文件名 <副本数> 文件大小 修改日期 修改时间 权限 用户ID 组ID
        如果是目录，则返回它直接子文件的一个列表，就像在Unix中一样。目录返回列表的信息如下：
        目录名 <dir> 修改日期 修改时间 权限 用户ID 组ID
        """
        ret = self.run('hadoop fs -ls', path, timeout)
        return ret

    def lsr(self, path, timeout):
        """
        ls命令的递归版本
        """
        ret = self.run('hadoop fs -lsr', path, timeout)
        return ret

    def du(self, path, timeout):
        """
        显示目录中所有文件的大小，或者当只指定一个文件时，显示此文件的大小
        """
        ret = self.run('hadoop fs -du', path, timeout)
        return ret

    def dus(self, path, timeout):
        """
        显示文件的大小
        """
        ret = self.run('hadoop fs -dus', path, timeout)
        return ret

    def count(self, path, timeout):
        """
        查看文件占用配额
        """
        ret = self.run('hadoop fs -count', path, timeout)
        return ret

    def mv(self, path, timeout):
        """
        将文件从源路径移动到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录。不允许在不同的文件系统间移动文件
        """
        ret = self.run('hadoop fs -mv', path, timeout)
        return ret

    def cp(self, path, timeout):
        """
        将文件从源路径复制到目标路径。这个命令允许有多个源路径，此时目标路径必须是一个目录
        """
        ret = self.run('hadoop fs -cp', path, timeout)
        return ret

    def ln(self, path, timeout):
        """
        链接，同linux
        """
        ret = self.run('hadoop fs -ln', path, timeout)
        return ret

    def rm(self, path, timeout):
        """
        删除指定的文件。只删除非空目录和文件
            """
        ret = self.run('hadoop fs -rm', path, timeout)
        return ret

    def rmr(self, path, timeout):
        """
        delete的递归版本
            """
        ret = self.run('hadoop fs -rmr', path, timeout)
        return ret

    def expunge(self, path, timeout):
        """
        清空回收站
            """
        ret = self.run('hadoop fs -expunge', path, timeout)
        return ret

    def put(self, path, timeout):
        """
        从本地文件系统中复制单个或多个源路径到目标文件系统
            """
        ret = self.run('hadoop fs -put', path, timeout)
        return ret

    def copy_fromlocal(self, path, timeout):
        """
        除了限定源路径是一个本地文件外，和put命令相似
            """
        ret = self.run('hadoop fs -copyFromLocal', path, timeout)
        return ret

    def move_fromlocal(self, path, timeout):
        """
        输出一个”not implemented“信息
            """
        ret = self.run('hadoop fs -moveFromLocal', path, timeout)
        return ret

    def get(self, path, timeout):
        """
        复制文件到本地文件系统。可用-ignorecrc选项复制CRC校验失败的文件。使用-crc选项复制文件以及CRC信息
            """
        ret = self.run('hadoop fs -get', path, timeout)
        return ret

    def getmerge(self, path, timeout):
        """
        接受一个源目录和一个目标文件作为输入，并且将源目录中所有的文件连接成本地目标文件
            """
        ret = self.run('hadoop fs -getmerge', path, timeout)
        return ret

    def cat(self, path, timeout):
        """
        使用方法：hadoop fs -cat URI [URI …]
        将路径指定文件的内容输出到stdout
            """
        ret = self.run('hadoop fs -cat', path, timeout)
        return ret

    def text(self, path, timeout):
        """
        将源文件输出为文本格式。允许的格式是zip和TextRecordInputStream
            """
        ret = self.run('hadoop fs -text', path, timeout)
        return ret

    def copy_tolocal(self, path, timeout):
        """
        除了限定目标路径是一个本地文件外，和get命令类似
            """
        ret = self.run('hadoop fs -copyToLocal', path, timeout)
        return ret

    def copy_seqfile_tolocal(self, path, timeout):
        """
        get SeqFile到本地
            """
        ret = self.run('hadoop fs -copySeqFileToLocal', path, timeout)
        return ret

    def move_tolocal(self, path, timeout):
        """
        Option '-moveToLocal' is not implemented yet
        """
        ret = self.run('hadoop fs -moveToLocal', path, timeout)
        return ret

    def mkdir(self, path, timeout):
        """
        接受路径指定的uri作为参数，创建这些目录
            """
        ret = self.run('hadoop fs -mkdir', path, timeout)
        return ret

    def setrep(self, path, timeout):
        """
        改变一个文件的副本系数。-R选项用于递归改变目录下所有文件的副本系数
            """
        ret = self.run('hadoop fs -setrep', path, timeout)
        return ret

    def setacl(self, path, timeout):
        """
        对目录设置权限控制
            """
        ret = self.run('hadoop fs -setAcl', path, timeout)
        return ret

    def getacl(self, path, timeout):
        """
        查看目录权限控制
        """
        ret = self.run('hadoop fs -getAcl', path, timeout)
        return ret

    def removeacl(self, path, timeout):
        """
        移除权限控制
        """
        ret = self.run('hadoop fs -removeAcl', path, timeout)
        return ret

    def touchz(self, path, timeout):
        """
        创建一个0字节的空文件
        """
        ret = self.run('hadoop fs -touchz', path, timeout)
        return ret

    def test(self, path, timeout):
        """
        检查文件或者目录
        """
        ret = self.run('hadoop fs -test', path, timeout)
        return ret

    def stat(self, path, timeout):
        """
        返回指定路径的统计信息
        """
        ret = self.run('hadoop fs -stat', path, timeout)
        return ret

    def tail(self, path, timeout):
        """
        将文件尾部1K字节的内容输出到stdout
        """
        ret = self.run('hadoop fs -tail', path, timeout)
        return ret

    def chown(self, path, timeout):
        """
        改变文件的拥有者。使用-R将使改变在目录结构下递归进行。命令的使用者必须是超级用户
        """
        ret = self.run('hadoop fs -chown', path, timeout)
        return ret

    def chmod(self, path, timeout):
        """
        改变文件的权限。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户
        """
        ret = self.run('hadoop fs -chmod', path, timeout)
        return ret

    def chgrp(self, path, timeout):
        """
        改变文件所属的组。使用-R将使改变在目录结构下递归进行。命令的使用者必须是文件的所有者或者超级用户
            """
        ret = self.run('hadoop fs -chgrp', path, timeout)
        return ret

    def help(self, path, timeout):
        """
        帮助文档
        """
        ret = self.run('hadoop fs -help', path, timeout)
        return ret

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
