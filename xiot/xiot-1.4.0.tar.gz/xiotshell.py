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
        self.shell.on_action(self, dev_id, action, value)

    def on_notify(self, dev_id, data):
        self.shell.on_notify(dev_id, data)


class Shel(object):
    def __init__(self, servurl, appid, appkey, mqtturi, gateway, device, cmdmap):
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
        self.cmdmap = cmdmap
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
                    dtu.updateValues(self.dev_id, {'code': self.dev_id, 'version': __version__, 'type': 'shell'})

                    while self.running:

                        ct = 10
                        while ct > 0 and self.running:
                            time.sleep(1)
                            ct -= 1
                        # print('ping')
                        # print(dtu.client.publish('ping', {'dev_id': self.dev_id}))
                except:
                    import traceback
                    traceback.print_exc()
            if dtu:
                dtu.sendEvent(self.dev_id, 'normal', u'主动断开连接')
                dtu.updateValues(self.dev_id, {'status': 'disconnected'})
                time.sleep(3)
                dtu.stop()
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

    def on_notify(self, dev_id, data):
        '''通知'''
        # print('shell on_notify', dev_id, data)
        pass

    def on_action(self, dtu, dev_id, action, value=None):
        if dev_id != self.dev_id:
            return
        if action in self.cmdmap:
            self.run_cmd_action(dtu, action, self.cmdmap[action], value)
        else:
            print('unknown acction', action)

    def run_cmd_action(self, dtu, action, cmd, value=None):
        import subprocess, os, uuid
        args = cmd.split(' ')
        sid = str(uuid.uuid4())

        def run():
            print(action, args)
            p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=os.getcwd(), bufsize=1)
            pipe = Pipe(p.stdout)
            last = time.time()
            outs = []

            def notify(finish=False):
                text = ''.join(outs)
                dtu.sendNotify(self.dev_id, {'type': 'result', 'text': text, 'finish': finish, 'sid': sid})
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
            dtu.sendEvent(self.dev_id, 'normal', action)

        self.start_thread(run)


def sys_exit(code):
    try:
        exit(code)
    except:
        pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-s', '--server', help='The Server URL', type=str, required=True)
    parser.add_argument('-m', '--mqtt', help='The MQTT Uri, Example: mqtt://username:password@xxx.com:1883', type=str, required=True)
    parser.add_argument('-a', '--appid', help='The xiot appid', type=str, required=True)
    parser.add_argument('-k', '--appkey', help='The xiot appkey', type=str, required=True)
    parser.add_argument('-g', '--gateway', help='The Gateway ID', type=str, required=True)
    parser.add_argument('-d', '--device', help='The Device ID', type=str, required=True)
    parser.add_argument('-c', '--command', action='append', type=str, help='The Command, Example: list="ls -l"')
    args = parser.parse_args()

    # print(args)

    # servurl, mqtt_host = ('https://xiot.inruan.com/', 'xiot.inruan.com')

    cmdmap = {}
    for arg in args.command:
        if '=' not in arg:
            print('error command: %s' % arg)
            exit(-1)
        ix = arg.index('=')
        key = arg[0:ix]
        cmd = arg[ix + 1:]
        cmdmap[key] = cmd  # .split(' ')
    sh = None

    try:
        sh = Shel(servurl=args.server, appid=args.appid, appkey=args.appkey, mqtturi=args.mqtt, gateway=args.gateway, device=args.device, cmdmap=cmdmap)
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
