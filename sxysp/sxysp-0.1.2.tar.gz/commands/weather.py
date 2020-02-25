import click
from utils.color import *
import requests
from vendor.geoip import getGeoInfo, getCityCode, getLocalIP
from utils.input import select


@click.group()
def weather():
    '''天气查询服务'''
    pass


@weather.command('check', short_help='查询当前位置的天气')
def check():
    '''\b
    查询当前位置的天气
    支持 国家气象局 和 魅族天气 两种天气信息源'''
    click.echo(info('正在获取您的地理位置...'))
    geo_info = getGeoInfo(getLocalIP())
    province = geo_info.subdivisions[0].names['zh-CN']
    city = geo_info.city.names['zh-CN']
    city = str(city).replace('市', '')
    click.echo(info('正在查询城市代码...'))
    code = getCityCode(province, city)
    click.echo(success('当前位置：%s省 %s市 [%s]' % (province, city, code)))
    provider = select('请选择天气信息源：', {'gov': '国家气象局', 'meizu': '魅族天气'})
    if provider == 'meizu':
        checkByMeiZu(code)
    if provider == 'gov':
        checkByGov(code)


def checkByGov(code):
    click.echo(info('正在查询当地天气...'))
    r = requests.get('http://www.weather.com.cn/data/sk/%s.html' % code)
    r.encoding = 'utf-8'

    data = r.json()['weatherinfo']
    click.echo(success('温度：%s 摄氏度' % data['temp']))
    click.echo(success('相对湿度: %s' % data['SD']))
    click.echo(success('风向：%s' % data['WD']))
    click.echo(success('风速：%s' % data['WS']))
    click.echo(success('大气压强：%s' % data['AP']))
    click.echo(info('最后更新于 %s' % data['time']))
    if data['isRadar'] == '1':
        click.echo(info('以上信息由 %s 雷达站收集获得' % data['Radar']))


def checkByMeiZu(code):
    r = requests.get(
        'https://aider.meizu.com/app/weather/listWeather?cityIds=%s' % code)
    data = r.json()

    if data['code'] == '200':
        data = data['value'][0]
        click.pause(info('请按任意键以展示实时天气'))
        click.clear()
        click.echo(info('= 实时天气 ='))
        click.echo(success('天气：%s' % data['realtime']['weather']))
        click.echo(success('温度：%s 摄氏度' % data['realtime']['temp']))
        click.echo(success('相对湿度: %s' % data['realtime']['sD']))
        click.echo(success('风向：%s' % data['realtime']['wD']))
        click.echo(success('风速：%s' % data['realtime']['wS']))
        click.pause(info('请按任意键以展示空气指数'))
        click.clear()
        click.echo(info('= 空气指数 ='))
        click.echo(success('空气质量指数：%s [%s]' % (
            data['pm25']['aqi'], data['pm25']['quality'])))
        click.echo(success('PM2.5含量：%s' % data['pm25']['pm25']))
        click.echo(success('PM1.0含量：%s' % data['pm25']['pm10']))
        click.echo(info('空气质量在 %d 个城市中排名第 %d' %
                        (data['pm25']['citycount'], data['pm25']['cityrank'])))
        click.pause(info('请按任意键以展示生活建议'))
        click.clear()
        click.echo(info('= 生活建议 ='))
        for suggest in data['indexes']:
            click.echo(success('%s：%s' % (suggest['name'], suggest['level'])))
            click.echo(success('建议：%s' % suggest['content']))
        click.echo(info('以上信息由 魅族天气 提供'))
