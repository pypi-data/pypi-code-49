import datetime
import time
import warnings

from framl.config_cli import ConfigFraml
from framl.config_model import ConfigModel
from google.cloud import firestore
from google.cloud.firestore_v1 import ArrayUnion


class Flags:

    def __init__(self, app_path: str):

        model_conf_ob = ConfigModel(app_path)

        # config params
        self.env = ConfigFraml.get_env()
        self.model_name: str = model_conf_ob.get_model_name()
        self.declared_flags: list = model_conf_ob.get_declared_flags()
        self.refresh_rate: int = model_conf_ob.get_refresh_rate()
        self.fs_client = firestore.Client(project=model_conf_ob.get_gcp_project_id())
        self.fs_doc = self.fs_client.collection(self.model_name).document(self.env)

        # lifecycle
        self.flags: dict = {}
        self.last_reload: int = 0

        # init
        self.load_flags()

    def load_flags(self):

        self.last_reload = int(time.time())
        res = self.fs_doc.get().to_dict()
        if not res or "flags" not in res:
            return {}

        last_flags = res['flags'][-1]
        self._validate_remote_flags(last_flags)
        self.flags = last_flags

    def _validate_remote_flags(self, flags) -> bool:
        for mandatory_flag in self.declared_flags:
            if mandatory_flag not in flags:
                warnings.warn(f'Loaded an undeclared flag from remote: {mandatory_flag}')
                return False

        return True

    def get(self, name: str):
        if int(time.time()) - self.last_reload > self.refresh_rate:
            self.load_flags()

        if name not in self.flags:
            warnings.warn(f"Flag {name} does not exist in {self.env} environment")
            return None

        return self.flags.get(name)

    def set(self, name: str, value) -> None:
        if name not in self.declared_flags:
            raise Exception( f'Flag {name} has not been declared. Please declare it first in config.yaml')

        self.flags[name] = value

    def save(self) -> None:

        flags = {}
        for flag in self.declared_flags:
            value = self.flags[flag]
            flags[flag] = value
        flags["creation_date"] = datetime.datetime.utcnow()
        # if there is no doc for the env we need to create it
        if not self.fs_doc.get().to_dict():
            self.fs_doc.set({u'flags': [flags]}, merge=False)
        else:
             self.fs_doc.update({u'flags': ArrayUnion([flags])})

    def compare_current_with_config(self):
        dec = self.declared_flags
        cur = list(self.flags.keys())
        all_flags = dec + list(set(cur) - set(dec))
        res = []
        for flag in all_flags:
            line = None
            if flag in dec and flag in cur:
                value = self.flags[flag]
                line = [flag,flag, value,' ']
            elif flag in dec:
                line = [flag, '', '', '+']
            elif flag in cur :
                if flag == 'creation_date':
                    continue
                value = self.flags[flag]
                line = ['', flag, value, '-']
            else:
                raise Exception( f'{flag} not supported in {all_flags}')
            if line != None:
                res.append(line)
        return res
