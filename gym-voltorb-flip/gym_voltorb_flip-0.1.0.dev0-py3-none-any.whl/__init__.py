from gym.envs.registration import register

__version__ = "0.1.0-dev"

register(id="VoltorbFlip-v0", entry_point="gym_voltorb_flip.envs:VoltorbFlipEnv")
