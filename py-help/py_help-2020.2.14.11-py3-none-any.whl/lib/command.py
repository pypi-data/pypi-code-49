# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from .CommonLogger import debug, info, warn, error
import time
import sys
import platform


class StringWithExitstatus(str):
    """
    封装shell调用的返回值与返回码
    res = StringWithExitstatus(stdout, stderr, exitstatus)
    print res.exitstatus   # ==> got exitcode
    print res              # ==> got stdout
    print res.err          # ==> got stderr
    """

    def __new__(self, stdout, stderr=None, exitstatus=0):
        """
        str的__new__是在__init__前调用的，然后str在__new__的时候发现参数不对就抛了个异常。
        这么诡异的行为主要是因为str的__new__就返回了个新的实例，而__init__没毛用
        参考: http://www.cnblogs.com/codingmylife/p/3620543.html
        """
        return super(StringWithExitstatus, self).__new__(self, stdout)

    def __init__(self, stdout, stderr=None, exitstatus=0):
        if sys.version_info < (3, 0):
            super(StringWithExitstatus, self).__init__(stdout)
        # out 不推荐使用，直接读对象
        # self.out = stdout
        self.err = stderr
        self.exitstatus = exitstatus

    def dump(self):
        return {
            'stdout': self,
            'stderr': self.err,
            'exitstatus': self.exitstatus
        }


def execute(cmd, blocked=True):
    """
    执行shell命令
    Args:
        cmd: shell命令
        blocked: 是否阻塞
    Returns:
        StringWithExitstatus(out,err,code)
    """
    import time
    code, out, err = 0, None, None
    if 'Windows' in platform.system():
        real_cmd = cmd
    else:
        real_cmd = '. /etc/profile;{cmd}'.format(cmd=cmd)
    time_before = time.time()
    close_fds = True
    if 'Windows' in platform.system():
        close_fds = False
    sh = Popen(real_cmd, shell=isinstance(real_cmd, str),
               bufsize=2048, stdin=PIPE, stdout=PIPE,
               stderr=PIPE, close_fds=close_fds)
    if blocked:
        # 这个必须用 communicate,不能wait,会有deadlock问题
        # https://stackoverflow.com/questions/13832734/difference-between-popen-poll-and-popen-wait
        cmd_out, cmd_err = sh.communicate()
        code = sh.poll()

        if 'Windows' in platform.system():
            encode = 'gb18030'
        else:
            encode = 'utf-8'
        for try_cnt in range(2):
            try:
                if sys.version_info < (3, 0):
                    out = cmd_out.decode(encode).strip()
                    err = cmd_err.decode(encode).strip()
                else:
                    out = str(cmd_out, encode).strip()
                    err = str(cmd_err, encode).strip()
                break
            except UnicodeDecodeError as ex:
                # 翻转一下,可能在windows下搞utf-8,或者在linux下搞gbk
                if 'Windows' in platform.system():
                    encode = 'utf-8'
                else:
                    encode = 'gb18030'
                warn("run decode {ret}".format(ret=ex.reason))
                out = ""
                err = ""
        debug("run return {ext}".format(ext=code))
    time_after = time.time()
    time_spend = round(time_after - time_before, 2)
    debug('exec: {}: ret={}, time_spend={}'.format(cmd, code, time_spend))
    debug('stderr: {}\n stdout: {}'.format(err, out))
    return StringWithExitstatus(out, err, code)


def robust_execute(cmd, retry=5, expect_ret=0, interval=1, blocked=True):
    """高鲁棒性execute接口
    :param cmd: shell命令
    :param retry: 重试次数
    :param expect_ret: 期望返回码
    :param interval: 重试间隔，单位s
    :return:
    """
    res = None
    while retry:
        res = execute(cmd, blocked)
        if res.exitstatus == expect_ret:
            break
        retry -= 1
        warn("执行 {} 返回码为 {}，重试..".format(cmd, res.exitstatus))
        time.sleep(interval)
    return res


def kill_pid(pid):
    if 'Windows' in platform.system():
        execute("taskkill /F /T /PID %s" % pid)
    else:
        execute("kill -9 %s" % pid)


class SshProxy:

    def __init__(self, ip, port, user_name, password):
        import paramiko
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh_client.connect(self.ip, self.port, self.user_name, self.password)
        except Exception as ex:
            error("连接ssh出现异常", ex)
        try:
            transport = paramiko.Transport((self.ip, self.port))
            transport.connect(username=self.user_name, password=self.password)
            self.sftp_client = paramiko.SFTPClient.from_transport(transport)
        except Exception as ex:
            error("连接ftp出现异常", ex)

    def run_cmd(self, cmd):
        debug("运行命令:{}".format(cmd))
        stdin, stdout, stderr = self.ssh_client.exec_command(cmd, timeout=60)
        status = stdout.channel.recv_exit_status()
        stdout_str = str(stdout.read(), 'utf-8')
        stderr_str = str(stderr.read(), 'utf-8')
        debug("命令返回输出:stdout:{},stderr:{}".format(stdout_str, stderr_str))
        return StringWithExitstatus(stdout_str, stderr=stderr_str, exitstatus=status)

    def upload(self, local_path, dst_path):
        return self.sftp_client.put(localpath=local_path, remotepath=dst_path)

    def download(self, local_path, dst_path):
        return self.sftp_client.get(remotepath=dst_path, localpath=local_path)
