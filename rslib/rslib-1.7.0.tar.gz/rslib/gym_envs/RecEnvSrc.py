from rslib.core.FeatureUtil import FeatureUtil
from numpy import random

class RecEnvSrc(object):
    '''
    file-based implementation of a RecommnedEnv's data source.

    Pulls data from file, preps for use by RecommnedEnv and then
    acts as data provider for each new episode.
    '''


    def __init__(self, config, statefile, actionfile):
        self.state_dict={}
        self.action_dict={}
        self.FeatureUtil = FeatureUtil(config)
        self.fs = open(statefile,'r')
        self.fs.readline()
        self.fa = open(actionfile,'r')
        self.fa.readline()
        self.rawstate_cache(self.fs, 10000)
        self.action_cache(self.fa)

    def rawstate_cache(self, f, num):
        for i in range(num):
            tmp = f.readline()
            role_id = tmp.split('@')[0]
            if len(role_id)>1:
                self.state_dict[role_id] = tmp

    def action_cache(self, f):
        for tmp in f.read().split('\n'):
            item_id = tmp.split('@')[0]
            itemfeat = '@'.join(tmp.split('@')[1:])
            self.action_dict[item_id] = itemfeat
        f.close()

    def get_item_price(self, item_id):
        return float(self.action_dict[str(item_id)].split('@')[0])

    def get_item_feat(self, item_id):
        return self.action_dict[str(item_id)].split('@')[1]

    def get_user_rawstate(self, role_id):
        rawstate = self.state_dict[str(role_id)]
        return rawstate

    def get_user_state(self, role_id):
        rawstate = self.get_user_rawstate(str(role_id))
        feature = self.rawstate_to_state(rawstate)
        return feature

    def get_random_user(self):
        return random.choice(list(self.state_dict.keys()))

    def get_random_user_rawstate(self):
        rawstate = self.get_user_rawstate(self.get_random_user())
        return rawstate

    def get_random_user_state(self):
        rawstate = self.get_random_user_rawstate()
        feature = self.rawstate_to_state(rawstate)
        return feature

    def rawstate_to_state(self, state):
        feature = self.FeatureUtil.feature_extraction(data=[state], predict=True)
        return feature

    def get_new_user_rawstate(self, rawstate, info):
        assert type(rawstate) == type('')
        return rawstate

    def get_new_user_state(self, rawstate, info):
        new_rawstate = self.get_new_user_rawstate(rawstate, info)
        feature = self.rawstate_to_state(new_rawstate)
        return feature

    def reset(self):
        self.state_dict = {}
        self.rawstate_cache(self.fs, 10000)