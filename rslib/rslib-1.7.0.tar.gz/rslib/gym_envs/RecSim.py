from . import RecEnvSrc
import numpy as np

class RecSim(object) :
    """ Implements core recommendation simulator"""

    def __init__(self, recEnvSrc :RecEnvSrc, model, modelfile , steps=9):
        # invariant for object life
        self.recEnvSrc        = recEnvSrc
        self.steps            = steps
        self.step             = 0
        self.states           = np.zeros(self.steps)
        self.actions          = np.zeros(self.steps, dtype=int)
        self.probs            = []
        self.gmv              = np.ones(self.steps)
        self.model            = model
        self.model.load_weights(modelfile)
        self.reset()


    def reset(self):
        self.step = 0
        self.actions.fill(-1)
        self.probs = []
        self.states.fill(None)
        self.gmv.fill(0)

    def predict(self, model, feat):
        prob = model.predict(feat)[0][0]
        self.probs.append(prob)
        return prob

    def get_init_info(self):
        return {'reward': 0, 'gmv':self.gmv[self.step], 'actions':self.actions}


    def _step(self, rawstate, action, info):
        """ Given an action and return for prior period, calculates costs, navs,
            etc and returns the reward and a  summary of the day's activity. """

        self.actions[self.step] = action
        info['actions'] = self.actions
        new_rawstate = self.recEnvSrc.get_new_user_rawstate(rawstate, info)

        if self.step < self.steps-1:
            reward = 0
            done = 0
        else:
            reward = 1
            done = 1

        info = {'reward': reward, 'gmv':self.gmv[self.step], 'actions':self.actions}

        self.step += 1

        return new_rawstate, reward, done, info