import time
from typing import Any, Tuple

from tqdm import tqdm

import draugr
from neodroidagent.agents.torch_agents.model_free.on_policy.evolutionary import EVOAgent
from neodroidagent.entry_points import session_entry_point


class CMAAgent(EVOAgent):

  # region Private

  def __defaults__(self) -> None:
    self._policy = None

  # endregion

  # region Protected

  def __build__(self, env, **kwargs) -> None:
    pass

  def _optimise_wrt(self, error, **kwargs) -> None:
    pass

  def _sample_model(self, state, **kwargs) -> Any:
    pass

  def _train_procedure(self,
                       _environment,
                       rollouts=2000,
                       render=False,
                       render_frequency=100,
                       stat_frequency=10,
                       **kwargs) -> Tuple[Any, Any]:
    training_start_timestamp = time.time()
    E = range(1, rollouts)
    E = tqdm(E, f'Episode: {1}', leave=False, disable=not render)

    stats = draugr.StatisticCollection(stats=('signal', 'duration'))

    for episode_i in E:
      initial_state = _environment.reset()

      if episode_i % stat_frequency == 0:
        draugr.terminal_plot_stats_shared_x(
          stats,
          printer=E.write,
          )

        E.set_description(f'Epi: {episode_i}, Dur: {stats.duration.running_value[-1]:.1f}')

      if render and episode_i % render_frequency == 0:
        signal, dur, *extras = self.rollout(
          initial_state, _environment, render=render
          )
      else:
        signal, dur, *extras = self.rollout(initial_state, _environment)

      stats.duration.append(dur)
      stats.signal.append(signal)

      if self.end_training:
        break

    time_elapsed = time.time() - training_start_timestamp
    end_message = f'Time elapsed: {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s'
    print(f'\n{"-" * 9} {end_message} {"-" * 9}\n')

    return self._policy, stats

  # endregion

  # region Public

  def sample(self, state, *args, **kwargs) -> Any:
    return self._last_connected_environment.action_space.sample()

  def update(self, *args, **kwargs) -> None:
    pass

  def evaluate(self, batch, *args, **kwargs) -> Any:
    pass

  def load(self, *args, **kwargs) -> None:
    pass

  def save(self, *args, **kwargs) -> None:
    pass

  # endregion


# region Test
def cma_test():
  import neodroidagent.configs.agent_test_configs.pg_test_config as C

  C.EnvironmentType = False
  C.ENVIRONMENT_NAME = 'mab'

  session_entry_point(CMAAgent, C)


if __name__ == '__main__':

  cma_test()

# endregion


"""Covariance Matrix Adaptation Evolution Strategy."""
import cma
from dowel import logger, tabular
import numpy as np

from garage.np.algos import BatchPolopt


class CMAES(BatchPolopt):
  """Covariance Matrix Adaptation Evolution Strategy.

  Note:
      The CMA-ES method can hardly learn a successful policy even for
      simple task. It is still maintained here only for consistency with
      original rllab paper.

  Args:
      env_spec (garage.envs.EnvSpec): Environment specification.
      policy (garage.np.policies.Policy): Action policy.
      baseline (garage.np.baselines.Baseline): Baseline for GAE
          (Generalized Advantage Estimation).
      n_samples (int): Number of policies sampled in one epoch.
      discount (float): Environment reward discount.
      max_path_length (int): Maximum length of a single rollout.
      sigma0 (float): Initial std for param distribution.

  """

  def __init__(self,
               env_spec,
               policy,
               baseline,
               n_samples,
               discount=0.99,
               max_path_length=500,
               sigma0=1.):
    super().__init__(policy, baseline, discount, max_path_length,
                     n_samples)
    self.env_spec = env_spec

    self.sigma0 = sigma0

    self._es = None
    self._all_params = None
    self._cur_params = None
    self._all_returns = None

  def _sample_params(self):
    """Return sample parameters.

    Returns:
        np.ndarray: A numpy array of parameter values.

    """
    return self._es.ask()

  def train(self, runner):
    """Initialize variables and start training.

    Args:
        runner (LocalRunner): LocalRunner is passed to give algorithm
            the access to runner.step_epochs(), which provides services
            such as snapshotting and sampler control.

    Returns:
        float: The average return in last epoch cycle.

    """
    init_mean = self.policy.get_param_values()
    self._es = cma.CMAEvolutionStrategy(init_mean, self.sigma0,
                                        {'popsize':self.n_samples})
    self._all_params = self._sample_params()
    self._cur_params = self._all_params[0]
    self.policy.set_param_values(self._cur_params)
    self._all_returns = []

    return super().train(runner)

  def train_once(self, itr, paths):
    """Perform one step of policy optimization given one batch of samples.

    Args:
        itr (int): Iteration number.
        paths (list[dict]): A list of collected paths.

    Returns:
        float: The average return in last epoch cycle.

    """
    paths = self.process_samples(itr, paths)

    epoch = itr // self.n_samples
    i_sample = itr - epoch * self.n_samples

    tabular.record('Epoch', epoch)
    tabular.record('# Sample', i_sample)

    rtn = paths['average_return']
    self._all_returns.append(paths['average_return'])

    if (itr + 1) % self.n_samples == 0:
      avg_rtns = np.array(self._all_returns)
      self._es.tell(self._all_params, -avg_rtns)
      self.policy.set_param_values(self._es.best.get()[0])

      # Clear for next epoch
      rtn = max(self._all_returns)
      self._all_returns.clear()
      self._all_params = self._sample_params()

    self._cur_params = self._all_params[(i_sample + 1) % self.n_samples]
    self.policy.set_param_values(self._cur_params)

    logger.log(tabular)
    return rtn
