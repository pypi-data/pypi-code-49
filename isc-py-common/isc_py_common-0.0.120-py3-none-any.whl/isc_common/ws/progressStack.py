import json

import websocket


class WebSocketExt(websocket.WebSocket):
    def sendEx(self, message):
        if not isinstance(message, dict):
            raise Exception(f'Message must be a dict.')
        self.send(payload=json.dumps(message))


class WebSocketAppExt(websocket.WebSocketApp):
    # def __init__(self,
    #              url,
    #              header=None,
    #              on_open=None,
    #              on_message=None,
    #              on_error=None,
    #              on_close=None,
    #              on_ping=None,
    #              on_pong=None,
    #              on_cont_message=None,
    #              keep_running=True,
    #              get_mask_key=None,
    #              cookie=None,
    #              subprotocols=None,
    #              on_data=None):
    #     super().__init__(
    #         url=url,
    #         header=header,
    #         on_open=on_open,
    #         on_message=on_message,
    #         on_error=on_error,
    #         on_close=on_close,
    #         on_ping=on_ping,
    #         on_pong=on_pong,
    #         on_cont_message=on_cont_message,
    #         keep_running=keep_running,
    #         get_mask_key=get_mask_key,
    #         cookie=cookie,
    #         subprotocols=subprotocols,
    #         on_data=on_data
    #     )

    def _send(self, message):
        if not isinstance(message, dict):
            raise Exception(f'Message must be a dict.')
        self.send(data=json.dumps(message))

    def show(self, title, id, label_contents=None, cntAll=0, caption=None):
        self._send(dict(
            caption=caption,
            cntAll=cntAll,
            labelContents=label_contents,
            progressBarId=id,
            title=title,
            type='show_progress',
        ))

    def setContentsLabel(self, labelContents, id):
        self._send(dict(type='set_contents_label', labelContents=labelContents, progressBarId=id))

    def setTitleProgress(self, title, id):
        self._send(dict(type='set_title_progress', title=title, progressBarId=id))

    def setPercentsDone(self, percent, id):
        self._send(dict(type='set_percent_done_progress', percent=percent, progressBarId=id))

    def setCntDone(self, cnt, id):
        self._send(dict(type='set_cnt_done_progress', cnt=cnt, progressBarId=id))

    def closed(self, id):
        self._send(dict(type='close_progress', progressBarId=id))


class ProgressStack:
    host = None
    port = None
    channel = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

        if not self.host:
            raise Exception(f'Not specified a host.')

        if not self.port:
            raise Exception(f'Not specified a port.')

        if not self.channel:
            raise Exception(f'Not specified a channel.')

        self.url = f'ws://{self.host}:{self.port}/ws/{self.channel}/'

    def _send(self, message):
        if not isinstance(message, dict):
            raise Exception(f'Message must be a dict.')

        self.ws = websocket.create_connection(url=self.url, class_=WebSocketExt)
        self.ws.sendEx(message)
        self.ws.close()

    def show(self, title, id, label_contents=None, cntAll=0, caption=None):
        self._send(dict(
            caption=caption,
            cntAll=cntAll,
            labelContents=label_contents,
            progressBarId=id,
            title=title,
            type='show_progress',
        ))

    def close(self, id):
        self._send(dict(type='close_progress', progressBarId=id))

    def setContentsLabel(self, labelContents, id):
        self._send(dict(type='set_contents_label', labelContents=labelContents, progressBarId=id))

    def setTitleProgress(self, title, id):
        self._send(dict(type='set_title_progress', title=title, progressBarId=id))

    def setPercentsDone(self, percent, id):
        self._send(dict(type='set_percent_done_progress', percent=percent, progressBarId=id))

    def setCntDone(self, cnt, id):
        self._send(dict(type='set_cnt_done_progress', cnt=cnt, progressBarId=id))

    def sendInfo(self, message):
        self._send(dict(type='info', message=message))

    def sendWarn(self, message):
        self._send(dict(type='warn', message=message))


class ProgressSerialStack:
    host = None
    port = None
    channel = None

    def __init__(self, func, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v() if callable(v) else v)

        if not self.host:
            raise Exception(f'Not specified a host.')

        if not self.port:
            raise Exception(f'Not specified a port.')

        if not self.channel:
            raise Exception(f'Not specified a channel.')

        url = f'ws://{self.host}:{self.port}/ws/{self.channel}/'

        def on_open(ws):
            try:
                import thread
            except ImportError:
                import _thread as thread

            def run(*args, **kwargs):
                try:
                    func(ws, **kwargs)
                    ws.close()
                except:
                    ws.close()

            thread.start_new_thread(run, (), kwargs)

        ws = WebSocketAppExt(url)
        ws.on_open = on_open
        ws.run_forever()
