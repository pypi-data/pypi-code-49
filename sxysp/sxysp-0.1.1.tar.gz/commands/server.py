import click
from utils.color import *
from utils.config import config, set_config
import sys
import utils.input as input
import utils.validate as validator
import subprocess
import os


@click.group()
@click.pass_context
def server(ctx):
    '''管理 Minecraft 服务器'''
    ctx.ensure_object(dict)
    ctx.obj['status_map'] = {
        'stopped': '已停止',
        'stopping': '停止中',
        'starting': '启动中',
        'running': '运行中'
    }
    ctx.obj['status'] = 'stopped'
    ctx.obj['process'] = None
    ctx.obj['mcdir'] = '/data/mcserver'


@server.command()
@click.pass_context
def status(ctx, silent=False):
    '''获取服务器状态'''

    ctx.invoke(sync_status, True)

    if not silent:
        status_text = ctx.obj['status_map'].get(ctx.obj['status'])
        click.echo(info('当前服务器状态为 %s' % status_text))

    return ctx.obj['status']


@server.command('change-status', short_help='设定服务器状态')
@click.argument('target', metavar='<status>')
@click.pass_context
def change_status(ctx, target):
    '''\b
    将服务器状态设定为 <status>
    服务器实际状态不会变更，仅作用于内部识别区'''
    if target in ctx.obj['status_map']:
        ctx.obj['status'] = target
        status_text = ctx.obj['status_map'].get(ctx.obj['status'])
        click.echo(success('服务器状态已切换至 %s' % status_text))
        ctx.invoke(status)
    else:
        click.echo(warn('未知的目标状态'))


@server.command('sync-status', short_help='同步服务器状态')
@click.pass_context
def sync_status(ctx, silent=False):
    '''自动同步服务器状态'''

    output = os.popen('screen -ls').read()

    if '.smcserver' in output:
        if not silent:
            click.echo(info('已检测到服务器进程'))
        ctx.obj['status'] = 'running'
    else:
        if not silent:
            click.echo(info('服务器进程不存在'))
        ctx.obj['status'] = 'stopped'


@server.command()
def setup():
    '''配置服务器'''

    if config('server.setup'):
        click.echo(warn('您已经配置过一次服务器了，继续配置将会重置配置'))
        click.confirm(info('是否继续进行配置？'), False, abort=True)

    jar_file = input.ask('服务端（JAR）文件路径', rule='ext|jar')
    set_config('server.jar_file', jar_file)

    max_ram = input.ask('服务端最大运行内存（MB）', 2048, rule='int')
    set_config('server.max_ram', max_ram)


@server.command()
@click.argument('command', metavar='<command>')
@click.pass_context
def exec(ctx, command):
    '''在服务器中执行命令'''
    rstatus = ctx.invoke(status, True)
    if rstatus == 'running':
        os.system('screen -S smcserver -X stuff "{}\015"'.format(command))
    else:
        click.echo(error('服务器进程不存在'))


@server.command()
@click.pass_context
def start(ctx):
    '''启动服务器'''

    if not config('server.setup'):
        click.echo(warn('请先配置服务器管理系统'))
        click.confirm(info('是否现在进行配置？'), True, True)
        ctx.invoke(setup)

    rstatus = ctx.invoke(status, True)
    if rstatus == 'stopped':
        os.chdir(ctx.obj['mcdir'])
        os.system(
            'screen -dmS smcserver java -Xms1G -Xmx2G -jar minecraft_server.1.12.2.jar nogui')
        click.echo(success('服务器已启动'))
    else:
        click.echo(error('服务器进程已存在'))


@server.command()
@click.pass_context
def stop(ctx):
    rstatus = ctx.invoke(status, True)
    if rstatus == 'running':
        ctx.invoke(exec, 'stop')
        click.echo(success('服务器已停止'))
    else:
        click.echo(error('服务器进程不存在'))


@server.command()
@click.pass_context
def web(ctx):
    '''启动 WEB 服务（前台执行）'''
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import json

    host = ('localhost', 8888)

    class Resquest(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'status': ctx.invoke(status, True)}
            self.wfile.write(json.dumps(data).encode())

    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
