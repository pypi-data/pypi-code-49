from numpy import array

from probability.custom_types import RVMixin, Array1d
from probability.distributions.mixins.conjugate_mixin import ConjugateMixin


class DirichletMultinomial(ConjugateMixin):

    def __init__(self, alpha: Array1d, x: Array1d):

        self._alpha = array(alpha)
        self._x = array(x)

    def prior(self, **kwargs) -> RVMixin:
        pass

    def likelihood(self, **kwargs) -> RVMixin:
        pass

    def posterior(self, **kwargs) -> RVMixin:
        pass