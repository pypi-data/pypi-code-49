import threading, time
from typing import Union, List
from framl.config_model import ConfigModel
from framl.wrappers.pubsub import Pubsub


class Logger:

    MESSAGE_VERSION = 1

    def __init__(self, app_path: str):
        model_conf_ob = ConfigModel(app_path)

        self._model_name = model_conf_ob.get_model_name()
        self._model_version = model_conf_ob.get_model_version()
        self._logs_buffer: List[dict] = []
        self.pubsub = Pubsub()

    def add(self, prediction_id: str, model_input: dict, model_output: dict):
        full_log = {
            "prediction_id":   prediction_id,
            "message_version": self.MESSAGE_VERSION,
            "prediction_time": int(time.time()),
            "metadata":        {
                "model_name":    self._model_name,
                "model_version": self._model_version,
            },
            "input":           {**model_input},
            "output":          {**model_output}
        }
        # self._logs_buffer.append(full_log)
        self.pubsub.publish_message(full_log)

    # def start_daemon(self):
    #     thread = threading.Thread(target=self.__timer)
    #     thread.start()
    #
    # def __timer(self):
    #     while True:
    #         time.sleep(1)
    #         print(self._logs_buffer)
    #         self._logs_buffer = []
