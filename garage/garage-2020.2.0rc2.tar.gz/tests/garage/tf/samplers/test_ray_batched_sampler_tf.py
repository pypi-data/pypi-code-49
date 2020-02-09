"""
Test whether tensorflow session is properly created and destroyed.

Other features of ray sampler are tested in
tests/garage/sampler/test_ray_sampler.py

"""

from unittest.mock import Mock

import ray

from garage.envs.grid_world_env import GridWorldEnv
from garage.np.policies import ScriptedPolicy
from garage.sampler import RaySampler, WorkerFactory
from garage.tf.envs import TfEnv


class TestRaySamplerTF():
    """
    Uses mock policy for 4x4 gridworldenv
    '4x4': [
        'SFFF',
        'FHFH',
        'FFFH',
        'HFFG'
    ]
    0: left
    1: down
    2: right
    3: up
    -1: no move
    'S' : starting point
    'F' or '.': free space
    'W' or 'x': wall
    'H' or 'o': hole (terminates episode)
    'G' : goal
    [2,2,1,0,3,1,1,1,2,2,1,1,1,2,2,1]
    """

    def setup_method(self):
        ray.init(local_mode=True, ignore_reinit_error=True)

        self.env = TfEnv(GridWorldEnv(desc='4x4'))
        self.policy = ScriptedPolicy(
            scripted_actions=[2, 2, 1, 0, 3, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1])
        self.algo = Mock(env_spec=self.env.spec,
                         policy=self.policy,
                         max_path_length=16)

    def teardown_method(self):
        self.env.close()

    def test_ray_batch_sampler(self):
        workers = WorkerFactory(seed=100,
                                max_path_length=self.algo.max_path_length)
        sampler1 = RaySampler(workers, self.policy, self.env)
        sampler1.start_worker()
        sampler1.shutdown_worker()
