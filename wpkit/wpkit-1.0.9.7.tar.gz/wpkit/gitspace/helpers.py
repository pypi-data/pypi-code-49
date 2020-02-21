
from .StoreItem import *
from .utils import generate_hash



_BRANCH_DICT='branch_dict'
_FAKE2TRUE='fake2true'
_TRUE2FAKE='true2fake'
USER_HOME=os.path.expanduser('~')
STORE_HOME=USER_HOME+'/.store'
BRANCH_DICTS_DIR=STORE_HOME+'/BranchDicts'


class BranchDict_dev(StoreFolder):
    def __init__(self,path,remote_location=None,remote_branch=None):
        # path=USER_HOME+'/.store'
        remote_branch=remote_branch or _BRANCH_DICT
        super().__init__(path,remote_location,remote_branch)
        self._init_branch_dict()
    def _init_branch_dict(self):
        '''
        Make sure we have local branch dict same with remote one.
        '''
        self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        self._read_remote_branch_list(pull=True)
        self._pull_else_push_self()
        # self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        if self.is_empty():
            self.openFiledict(_FAKE2TRUE)
            self.openFiledict(_TRUE2FAKE)
            self._push_self()
        # print("bd:", self._read_fake2true_dict())
    def _sync_dict(self):
        return self._try_pull_remote()
    def _concat_fakes(self,parent,fake):
        return parent+StoreFolder.delimiter+fake
    def _generate_hash(self,fake):
        import hashlib
        m=hashlib.md5()
        def gen():
            m.update(fake.encode('utf-8'))
            return m.hexdigest()[:10]
        while True:
            true=gen()
            if not true in self.trues():
                return true

    def _update_branch_dict(self,fake,true):
        self._try_pull_remote()
        fake2true=self._read_fake2true_dict()
        true2fake=self._read_true2fake_dict()
        fake2true[fake]=true
        true2fake[true]=fake
        self._push_self()
    def true(self,fake):
        if fake in self.fakes():
            return self.fake2true(fake)
        else:
            true=self._generate_hash(fake)
            self.set(fake,true)
            return true
    def _read_fake2true_dict(self):
        return self.openFiledict(_FAKE2TRUE)
    def _read_true2fake_dict(self):
        return self.openFiledict(_TRUE2FAKE)
    def fake2true(self,fake):
        return self._read_fake2true_dict()[fake]
    def true2fake(self,true):
        return self._read_true2fake_dict()[true]
    def trues(self):
        return self._read_true2fake_dict().keys()
    def fakes(self):
        return self._read_fake2true_dict().keys()
    def set(self,fake,true):
        return self._update_branch_dict(fake,true)
class BranchDict(StoreFolder):
    def __init__(self,path,remote_location=None,remote_branch=None):
        remote_branch=remote_branch or _BRANCH_DICT
        super().__init__(path,remote_location,remote_branch)
        self._init_branch_dict()
    def _init_branch_dict(self):
        '''
        Make sure we have local branch dict same with remote one.
        '''
        self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        self._read_remote_branch_list(pull=True)
        self._pull_else_push_self()
        # self._try_pull_remote()
        # print("bd:", self._read_fake2true_dict())
        if self.is_empty():
            self.openFiledict(_FAKE2TRUE)
            self.openFiledict(_TRUE2FAKE)
            self._push_self()
        # print("bd:", self._read_fake2true_dict())
    def _sync_dict(self):
        return self._try_pull_remote()
    def _concat_fakes(self,parent,fake):
        return parent+StoreFolder.delimiter+fake
    def _generate_hash(self,fake):
        import hashlib
        m=hashlib.md5()
        def gen():
            m.update(fake.encode('utf-8'))
            return m.hexdigest()[:10]
        while True:
            true=gen()
            if not true in self.trues():
                return true

    def _update_branch_dict(self,fake,true):
        self._try_pull_remote()
        fake2true=self._read_fake2true_dict()
        true2fake=self._read_true2fake_dict()
        fake2true[fake]=true
        true2fake[true]=fake
        self._push_self()
    def true(self,fake):
        if fake in self.fakes():
            return self.fake2true(fake)
        else:
            true=self._generate_hash(fake)
            self.set(fake,true)
            return true
    def _read_fake2true_dict(self):
        return self.openFiledict(_FAKE2TRUE)
    def _read_true2fake_dict(self):
        return self.openFiledict(_TRUE2FAKE)
    def fake2true(self,fake):
        return self._read_fake2true_dict()[fake]
    def true2fake(self,true):
        return self._read_true2fake_dict()[true]
    def trues(self):
        return self._read_true2fake_dict().keys()
    def fakes(self):
        return self._read_fake2true_dict().keys()
    def set(self,fake,true):
        return self._update_branch_dict(fake,true)
