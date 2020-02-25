import click
from utils.color import *


@click.group()
def translate():
    '''翻译服务'''
    pass


@translate.command()
@click.argument('tl', metavar='<target>')
@click.argument('text', metavar='<text>')
@click.argument('sl', metavar='[source]', default='auto')
def baidu(sl, tl, text):
    '''\b
    使用百度翻译进行翻译
    将 <text> 由 <source> 翻译为 <target>
    如 <source> 被省略，则自动识别源语言'''
    import requests
    import json
    import random
    import hashlib
    import sys

    appid = '20180325000139814'
    secret = 'UneRTwnSimKz6CzhaVhR'

    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secret
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate?appid=' + appid + '&q=' + text + '&from=' + sl + '&to=' + tl + '&salt=' + str(
        salt) + '&sign=' + sign
    res = None
    try:
        response = requests.post(url)
        res = json.loads(response.content.decode())
    except requests.RequestException as e:
        click.echo(error('无法发送请求，请检查你的网络连接'))
        click.echo(error(str(e)))
        sys.exit(1)

    error_code_map = {
        52001: '请求超时，请检查网络连接或尝试重新执行',
        52002: '系统错误，请尝试重新执行',
        52003: '服务可能已失效，请联系开发人员确认',
        54000: '缺少必要参数',
        54001: '签名错误，请联系开发人员处理',
        54003: '请求频率过高，请稍后再试',
        54004: '服务可能已失效，请联系开发人员确认',
        54005: '请求频率过高，请稍后再试',
        58000: '未授权的访问源，请联系开发人员处理',
        58002: '服务可能已失效，请联系开发人员确认',
        90107: '服务可能已失效，请联系开发人员确认'
    }

    if 'error_code' in res:
        click.echo(error('%s: %s' % (res['error_code'], res['error_msg'])))
        click.echo(error('%s' % error_code_map[res['error_code']]))
    elif 'trans_result' in res:
        result = res['trans_result'][0]
        click.echo(info('原文：%s' % result['src']))
        click.echo(success('译文：%s' % result['dst']))
    else:
        click.echo(error('无法识别返回值'))
