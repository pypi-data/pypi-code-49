from probability.custom_types import RVMixin
from probability.distributions.mixins.conjugate_mixin import ConjugateMixin


class BetaGeometric(ConjugateMixin):

    def __init__(self, alpha: float, beta: float, n: int):
        """
        :param alpha: Value for the α hyper-parameter of the prior Beta distribution.
        :param beta: Value for the β hyper-parameter of the prior Beta distribution.
        :param n: Number of trials.
        :param m: Number of successes.
        """
        self._alpha: float = alpha
        self._beta: float = beta
        self._n: int = n

        self._reset_distribution()

    def prior(self, **kwargs) -> RVMixin:
        pass

    def likelihood(self, **kwargs) -> RVMixin:
        pass

    def posterior(self, **kwargs) -> RVMixin:
        pass
