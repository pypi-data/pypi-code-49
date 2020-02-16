import queue as _queue
import threading as _threading


class PipeClose:
    pass


class Pipe:
    def __init__(
        self,
        queue_in: _queue.Queue,
        queue_out: _queue.Queue,
        *,
        forward_close_to_output=False,
        with_queue=False,
    ) -> None:
        self._queue_in = queue_in
        self._queue_out = queue_out
        self._forward_close = forward_close_to_output
        self._with_queue = with_queue
        self.thread = _threading.Thread(
            target=self._pipe,
            args=(self._queue_in, self._queue_out, forward_close_to_output, with_queue),
        )
        self.thread.start()

    def _pipe(
        self,
        queue_in: _queue.Queue,
        queue_out: _queue.Queue,
        forward_close: bool,
        with_queue: bool,
    ) -> None:
        while True:
            mes_in = queue_in.get()
            if not forward_close and isinstance(mes_in, PipeClose):
                return
            if with_queue:
                queue_out.put((queue_in, mes_in))
            else:
                queue_out.put(mes_in)
            if isinstance(mes_in, PipeClose):
                return

    def stop(self) -> None:
        self._queue_in.put(PipeClose())
