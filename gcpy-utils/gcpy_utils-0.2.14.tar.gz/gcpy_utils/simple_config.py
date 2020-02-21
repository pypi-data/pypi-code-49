# coding:utf-8
# write  by  zhou
from six.moves import configparser
import os

environ = None
try:
    with open(os.path.expanduser("~/.environ"), "r") as f:
        environ = f.read().strip()
        assert environ
except:
    raise Exception("no ~/.environ found! you must create one!")

_ = configparser.ConfigParser()
_flag = None


def parse_config(config_dir):
    '''
    :param config_dir: 配置文件的目录
    :return: 返回一个dict
    '''
    config_dir = os.path.abspath(config_dir)
    global _flag
    if not _flag:
        _.read(os.path.join(config_dir, "%s.ini" % environ))
        buff = dict()
        for s in _.sections():
            buff[s] = {}
            for info in _.items(s):
                buff[s][info[0]] = info[1]
        _flag = buff
    return _flag
