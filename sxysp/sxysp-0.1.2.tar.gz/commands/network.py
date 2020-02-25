import click
from utils.color import *
import speedtest
import subprocess
import shlex
import utils.string


@click.group()
def network():
    '''网络服务'''
    pass


@network.command()
@click.option('--only-upload', is_flag=True, default=False)
@click.option('--only-download', is_flag=True, default=False)
def test(only_upload, only_download):
    '''测试网络速度'''
    click.echo(info('测速服务由 Speedtest.net 提供'))

    p = subprocess.Popen(shlex.split('spenv/bin/speedtest-cli --bytes'),
                         shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        line = line.strip()
        if line:
            search = [
                '...',
                '(', ')',
                'Retrieving speedtest.net configuration',
                'Testing from ',
                'Retrieving speedtest.net server list',
                'Selecting best server based on ping',
                'Hosted by ',
                'Testing download speed',
                'Download: ',
                'Testing upload speed',
                'Upload: ',
                'Cannot retrieve speedtest configuration',
                'Unable to connect to servers to test latency.'
            ]
            replace = [
                '',
                '（', '）',
                '正在连接测速服务...',
                '待测速服务器为：',
                '正在查询可用测速服务器列表...',
                '正在智能选择延迟最低的测速服务器...',
                '已连接测速服务器：',
                '正在测试下载速度...',
                ';success;下载速度：',
                '正在测试上传速度...',
                ';success;上传速度：',
                ';error;无法连接至测速服务',
                ';error;无法连接到测速服务器'
            ]
            o = utils.string.replace(
                search, replace, line.decode('utf-8'))
            if ';error;' in o:
                o = o.replace(';error;', '')
                click.echo(error(o))
            elif 'ERROR:' in o:
                o = o.replace('ERROR: ', '')
                click.echo(error(o))
            elif ';success;' in o:
                o = o.replace(';success;', '')
                click.echo(success(o))
            else:
                click.echo(info(o))
