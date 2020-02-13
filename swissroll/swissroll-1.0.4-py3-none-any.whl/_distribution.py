from abc import ABCMeta, abstractmethod


class Distribution:
    """Abstract base class for all the distributions.

    Parameters
    -------
    **kwargs:
              Keyword arguments, if any.
    
    Attributes
    -------
    get_params: `callable`
                Get a copy of parameters of the distribution.
    
    set_params: `callable`
                Update the parameters of the distribution.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_params(self):
        """Get a clone of paramters of the distribution"""
        return self.__dict__.copy()

    def set_params(self, **kwargs):
        """Update the parameters of the distribution"""
        self.__init__(**kwargs)

    def __repr__(self):
        """Returns the memory address of the distribution"""
        return f"<{self.__class__.__name__} at {id(self)}>"

    def __str__(self):
        """Pretty print the distribution and its parameters"""
        message = (
            f"{self.__class__.__name__} distribution with"
            f" parameters {self.__dict__}."
        )

        return message

    def __getstate__(self):
        """Makes the class and subclasses serailizable."""
        return self.__dict__.copy()

    def __setstate__(self, state):
        """Makes the class and subclasses serializable."""
        self.__dict__.update(state)

    @property
    def _short_str(self):
        """A short string of the parameters of the distribution"""
        params = self.get_params()
        msg = ", ".join(f"{name}={val}" for name, val in params.items())
        return msg


class Continuous(Distribution, metaclass=ABCMeta):
    """Abstract base class for continuous distributions."""

    @abstractmethod
    def pdf(self, x, *args, **kwargs):
        """Evaluate the Probability Density Function of a distribution."""
        pass

    @abstractmethod
    def cdf(self, x, *args, **kwargs):
        """Cumulative Distribution Function"""
        pass

    @abstractmethod
    def plot_likelihood(self, *args, **kwargs):
        """Plot the likelihood function.
        NOTE: Use with caution! It may not work
        for a large sample size. Instead, use the 
        alternative `plot_log_likelihood`.
        """
        pass

    @abstractmethod
    def plot_log_likelihood(self, observed, *args, **kwargs):
        """Plot the log-likelihood"""
        pass

    @abstractmethod
    def mle(self, observed, *args, **kwargs):
        """Maximum Likelihood Estimation"""
        pass


class Discrete(Distribution, metaclass=ABCMeta):
    """Abstract base class for Discrete distributions."""

    @abstractmethod
    def pmf(self, x, *args, **kwargs):
        """Evaluate the Probability Mass Function of the distribution"""
        pass

    @abstractmethod
    def cdf(self, x, *args, **kwargs):
        """Evaluate Cumulative Distribution function of the distribution"""
        pass

    @abstractmethod
    def plot_likelihood(self, *args, **kwargs):
        """Plot the likelihood function.
        NOTE: Use with caution! It may not work
        for a large sample size. Instead, use the 
        alternative `plot_log_likelihood`.
        """
        pass

    @abstractmethod
    def plot_log_likelihood(self, observed, *args, **kwargs):
        """Plot the log-likelihood"""
        pass

    @abstractmethod
    def mle(self, observed, *args, **kwargs):
        """Compute Maximum Likelihood Estimation of paramters
        of the distribution."""
        pass
