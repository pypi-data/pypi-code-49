# -*- coding: UTF-8 -*
from __future__ import print_function
from xiot import App, MQTTDTU, __version__
import time

try:
    from queue import Queue, Empty
except ImportError:  # python < 3.0
    from Queue import Queue, Empty
from threading import Thread


class ReadTimeoutException(Exception):
    pass


class Pipe(object):
    """A wrapper around a pipe opened for reading"""

    def __init__(self, pipe):
        self.pipe = pipe
        self.queue = Queue()
        self._runing = True
        self.thread = Thread(target=self._loop)
        self.thread.start()

    def readline(self, timeout=None):
        "A non blocking readline function with a timeout"
        try:
            return self.queue.get(True, timeout)
        except Empty:
            raise ReadTimeoutException()

    def _loop(self):
        try:
            while self._runing:
                line = self.pipe.readline()
                self.queue.put(line)
        except (ValueError, IOError):  # pipe was closed
            pass

    def close(self):
        self._runing = False
        self.pipe.close()


class ShellDTU(MQTTDTU):
    def __init__(self, shell):
        self.shell = shell
        return MQTTDTU.__init__(self, app=self.shell.app, dtu_id=self.shell.gw_id, mqtt_host=self.shell.mqtt_host, mqtt_port=self.shell.mqtt_port)

    def on_action(self, dev_id, action, value=None):
        self.shell.on_action(dev_id, action, value)

    def on_notify(self, dev_id, data):
        self.shell.on_notify(dev_id, data)


class Runner(object):
    running = True

    def __init__(self, name=None):
        if not name:
            name = self.__class__.__name__
        self.name = name

    def get_attributes(self):
        pass

    def get_actions(self):
        pass

    def get_charts(self):
        pass

    def get_name(self):
        return self.name

    def __get_type_of_value(self, v):
        return 'float' if isinstance(v, float) else \
            'int' if isinstance(v, int) else \
                'bool' if isinstance(v, bool) else \
                    'text' if isinstance(v, type('')) or isinstance(v, type(u'')) else ''

    def get_define(self):
        attributes = self.get_attributes() or []
        for atd in attributes:
            if 'type' not in atd:
                v = atd['value']
                atd['type'] = self.__get_type_of_value(v)
            if 'name' not in atd:
                atd['name'] = atd['attr_id']
        define = {
            'name': self.get_name(),
            'attributes': attributes or [],
            'charts': self.get_charts() or [],
            'actions': self.get_actions() or [],
        }
        return {
            k: v for k, v in define.items() if v != None
        }

    def on_action(self, dtu, dev_id, action, value=None):
        pass

    def start_thread(self, target, args=()):
        th = Thread(target=target, args=args)
        th.setDaemon(True)
        th.start()
        return th

    def stop(self):
        self.running = False

    def get_time(self):
        return 10


class Shel(object):
    def __init__(self, servurl, appid, appkey, mqtturi, gateway, device, runner, name=None, interval=30):
        try:
            import urlparse as parse
        except:
            from urllib import parse
        res = parse.urlparse(mqtturi)
        if res.scheme != 'mqtt':
            raise Exception(u'Unsupported URI: %s' % mqtturi)
        self.app = App(servurl, appid, appkey)
        self.gw_id = gateway
        self.dev_id = device
        self.mqtt_host = res.hostname
        self.mqtt_port = int(res.port or 1883)
        self.runner = runner
        self.name = name
        interval = int(interval)
        if interval <= 0:
            interval = 30
        self.interval = interval
        self.running = False

    def new_dtu(self):
        dtu = ShellDTU(self)
        return dtu

    def __shell_run__(self):
        while True:
            dtu = None
            while self.running:
                try:
                    dtu = self.new_dtu()
                    self.dtu = dtu
                    define = self.runner.get_define()
                    attrs = define.get('attributes') or []
                    attrs += [
                        {'attr_id': 'version', 'name': '版本', 'value': __version__},
                        {'attr_id': 'type', 'name': '类型', 'value': 'shell'},
                        {'attr_id': 'code', 'name': '代码', 'value': self.dev_id},
                    ]
                    if self.name:
                        define['name'] = self.name
                    define['attributes'] = attrs
                    print('registering %s ...' % define['name'])
                    self.app.doApi('register', {'dtu_id': self.dtu.dtu_id, 'dev_id': self.dev_id, 'define': define})
                    time.sleep(1)
                    print('running...')
                    lastdata = {}

                    def update():
                        if not lastdata:
                            vals = attrs
                        else:
                            vals = self.runner.get_attributes()
                        if not vals:
                            return
                        nd = {
                            d['attr_id']: d['value'] for d in vals if d['value'] != lastdata.get(d['attr_id'])
                        }
                        if nd:
                            # print('update', nd)
                            dtu.updateValues(self.dev_id, nd)
                        lastdata.update(nd)

                    while self.running:
                        update()
                        ct = self.interval
                        while ct > 0 and self.running:
                            time.sleep(1)
                            ct -= 1
                except:
                    import traceback
                    traceback.print_exc()
            if dtu:
                dtu.sendEvent(self.dev_id, 'normal', u'主动断开连接')
                dtu.updateValues(self.dev_id, {'status': 'disconnected'})
                time.sleep(3)
                dtu.stop()
                self.dtu = None
        self.running = False

    def start_thread(self, target, args=()):
        th = Thread(target=target, args=args)
        th.setDaemon(True)
        th.start()
        return th

    def start(self):
        if self.running:
            return
        self.running = True
        self.start_thread(self.__shell_run__)

    def stop(self):
        self.running = False
        self.runner.stop()

    def on_notify(self, dev_id, data):
        '''通知'''
        # print('shell on_notify', dev_id, data)
        pass

    def on_action(self, dev_id, action, value):
        if dev_id == self.dev_id:
            self.runner.on_action(self.dtu, dev_id, action, value)


class CommandRunner(Runner):
    def __init__(self, name=None, commands=[]):
        Runner.__init__(self, name)
        cmdmap = {}
        cmds = []
        for arg in commands or []:
            if not arg:
                continue
            if isinstance(arg, dict):
                cmdd = arg
            else:
                if '=' not in arg:
                    print('error command: %s' % arg)
                    exit(-1)
                ix = arg.index('=')
                act_id = arg[0:ix]
                cmdd = {
                    'act_id': act_id,
                    'cmd': arg[ix + 1:]
                }
            cmdmap[cmdd['act_id']] = cmdd
            cmds.append(cmdd)
        self.cmdmap = cmdmap
        self.commands = cmds

    def get_actions(self):
        return [
            {
                "name": d.get('name', d['act_id']),
                "act_id": d['act_id'],
                "type": "button",
            } for d in self.commands
        ]

    def on_action(self, dtu, dev_id, action, value=None):
        if action in self.cmdmap:
            self.run_cmd_action(dtu, dev_id, action, self.cmdmap[action], value)
        else:
            print('unknown acction', action)

    def run_cmd_action(self, dtu, dev_id, action, cmdd, value=None):
        import subprocess, os, uuid
        cmd = cmdd['cmd']
        if cmdd.get('shell'):
            args = cmd
        else:
            args = cmd.split(' ')
        sid = str(uuid.uuid4())
        needret = cmdd.get('return', False)

        def run():
            print(action, args)
            dtu.sendEvent(dev_id, 'warning', 'start %s' % action)
            try:
                # subprocess.call()
                p = subprocess.Popen(cmd, shell=cmdd.get('shell'), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=os.getcwd(), bufsize=1)
                pipe = Pipe(p.stdout)
                last = time.time()
                outs = []

                def notify(finish=False):
                    if needret:
                        return
                    text = ''.join(outs)
                    dtu.sendNotify(dev_id, {'type': 'result', 'text': text, 'value': value, 'finish': finish, 'sid': sid})
                    # print(text)
                    del outs[:]

                while self.running:
                    notify()
                    try:
                        out = pipe.readline(1)
                        if not out:
                            break
                        outs.append(out.decode('utf-8'))
                    except ReadTimeoutException as e:
                        # import traceback
                        # traceback.print_exc()
                        pass
                    timeoff = (time.time() - last)
                    if timeoff > 2 and outs or timeoff > 5:
                        last = time.time()
                        notify()
                notify(True)

                try:
                    pipe.close()
                except:
                    pass
                if needret and outs:
                    dtu.sendEvent(dev_id, 'normal', ''.join(outs))
                    time.sleep(.5)
                dtu.sendEvent(dev_id, 'success', 'finish %s' % action)
            except Exception as e:
                import traceback
                traceback.print_exc()
                dtu.sendEvent(dev_id, 'error', str(e))

        self.start_thread(run)


class SysInfoRunner(CommandRunner):
    def __init__(self, name=None, commands=None, monitor=True):
        self.monitor = monitor
        return CommandRunner.__init__(self, name=name, commands=commands)

    def get_attributes(self):
        if self.monitor:
            import psutil, datetime
            return [
                {
                    'attr_id': 'now',
                    'value': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'name': '时间',
                    'unit': ''
                },
                {
                    'attr_id': 'cpu',
                    'value': psutil.cpu_percent(),
                    'name': 'CPU',
                    'unit': '%'
                },
                {
                    'attr_id': 'mem',
                    'value': psutil.virtual_memory().percent,
                    'name': '内存',
                    'unit': '%'
                },
                {
                    'attr_id': 'disk',
                    'value': psutil.disk_usage('/').percent,
                    'name': '磁盘',
                    'unit': '%'
                }
            ]

    def get_charts(self):
        if self.monitor:
            return [
                {
                    "name": "系统信息",
                    "type": "timeline",
                    "size": "large",
                    "fields": "cpu,mem,disk",
                },
            ]


def sys_exit(code):
    try:
        exit(code)
    except:
        pass


if __name__ == '__main__':
    import argparse, json

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-s', '--server', help='The Server URL', type=str, required=False)
    parser.add_argument('-m', '--mqtt', help='The MQTT Uri, Example: mqtt://username:password@xxx.com:1883', type=str, required=False)
    parser.add_argument('-a', '--appid', help='The xiot appid', type=str, required=False)
    parser.add_argument('-k', '--appkey', help='The xiot appkey', type=str, required=False)
    parser.add_argument('-g', '--gateway', help='The Gateway ID', type=str, required=False)
    parser.add_argument('-d', '--device', help='The Device ID', type=str, required=False)
    parser.add_argument('-n', '--name', help='The Device Name', type=str, required=False)
    parser.add_argument('-i', '--interval', help='The Update Interval(seconds)', default=0, type=int, required=False)
    parser.add_argument('-c', '--command', action='append', type=str, help='The Command, Example: list="echo hi"')
    parser.add_argument('--config', type=str, help='The Config File/URI, Example: define.yaml')
    parser.add_argument('--runner', type=str, help='The Define JSON String')
    args = parser.parse_args()
    if args.runner:
        args.runner = json.loads(args.runner)
    if args.config:
        # define
        import os, socket

        rawargs = args.__dict__  # {k: v for k, v in args.__dict__.items()}
        uri = args.config
        if '://' in uri:
            import requests

            print('fetching config...')
            txt = requests.get(uri).text
        else:
            import io, os

            if not os.path.exists(uri):
                raise Exception('define file not exists: %s' % uri)
            txt = io.open(uri, encoding='utf8').read()
        cxt = {'pid': os.getpid(), 'hostname': socket.gethostname()}
        for k, v in cxt.items():
            if not v:
                continue
            txt = txt.replace('${%s}' % k, str(v))
        if '.yaml' in uri:
            import yaml

            newargs = yaml.safe_load(txt)
        elif '.json' in uri:
            newargs = json.loads(txt)
        else:
            raise Exception(u'unknow define type: %s' % uri)
        for k, v in newargs.items():
            if not rawargs.get(k):
                rawargs[k] = v
    sh = None

    try:
        import socket

        runner_clz_map = {
            c.__name__: c for c in [CommandRunner, SysInfoRunner]
        }
        if args.runner:
            runner_clz = runner_clz_map.get(args.runner['class'])
            runner_args = args.runner.get('args', {})
        elif args.command:
            runner_clz = CommandRunner
            runner_args = {'commands': args.command}
        # print(runner_clz, runner_args)
        runner = runner_clz(**runner_args)
        sh = Shel(servurl=args.server, appid=args.appid, appkey=args.appkey, mqtturi=args.mqtt, gateway=args.gateway, device=args.device, runner=runner, name=args.name, interval=int(args.interval))
        sh.start()
        while sh.running:
            time.sleep(1)
            # print('sleepping...')
    except KeyboardInterrupt:
        if sh:
            print('exit...')
            sh.stop()
            time.sleep(3)
        sys_exit(0)
