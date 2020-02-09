from . import VecEnvWrapper
from agnes.common.running_mean_std import RunningMeanStd, _BaseMeanStd
import numpy as np


class VecNormalize(VecEnvWrapper):
    """
    A vectorized wrapper that normalizes the observations
    and returns from an environment.
    """

    def __init__(self, venv, ob=True, ret=True, clipob=10., cliprew=10., gamma=0.99, epsilon=1e-8, rew_shape=(),
                 normalizer: _BaseMeanStd.__class__ = RunningMeanStd):
        VecEnvWrapper.__init__(self, venv)
        self.ob_rms = normalizer(shape=self.observation_space.shape, epsilon=epsilon) if ob else None
        self.ret_rms = normalizer(shape=rew_shape, epsilon=epsilon) if ret else None
        self.clipob = clipob
        self.cliprew = cliprew
        self.ret = np.zeros((self.num_envs,) + rew_shape)
        self.gamma = gamma
        self.epsilon = epsilon
        self.rew_shape = rew_shape

    def step_wait(self):
        obs, rews, news, infos = self.venv.step_wait()
        self.ret = self.ret * self.gamma + rews
        obs = self._obfilt(obs)
        if self.ret_rms:
            self.ret_rms.update(self.ret)
            rews = np.clip(rews / np.sqrt(self.ret_rms.var + self.epsilon), -self.cliprew, self.cliprew)
        self.ret[news] = 0.
        return obs, rews, news, infos

    def _obfilt(self, obs):
        if self.ob_rms:
            self.ob_rms.update(obs)
            obs = np.clip((obs - self.ob_rms.mean) / np.sqrt(self.ob_rms.var + self.epsilon), -self.clipob, self.clipob)
            return obs
        else:
            return obs

    def reset(self):
        self.ret = np.zeros((self.num_envs,) + self.rew_shape)
        obs = self.venv.reset()
        return self._obfilt(obs)
