import numpy as np
from scipy.stats import norm, t
from scipy.special import gamma, factorial
import matplotlib.pyplot as plt
from ._distribution import Discrete, Continuous

__all__ = [
    "Bernoulli",
    "Binomial",
    "Beta",
    "Normal",
    "Cauchy",
    "Exponential",
    "Poisson",
    "StudentT",
    "Uniform",
]


class Bernoulli(Discrete):
    """Bernoulli distribution.

    Parameters
    -----
    p: (np.float32, np.float64)
        Probability of success.
    
    Examples
    -----
    >>> from swissroll.distributions import Bernoulli
    >>> dist = Bernoulli(0.3)
    >>> dist.pmf(0.)
    0.7
    >>> print(dist)
    Bernoulli distribution with parameters {'p': 0.3}
    >>> dist.sample(3)
    np.array([1., 0., 1.])
    """

    def __init__(self, p=0.5):
        self.p = p

    def pmf(self, x, p=None):
        if p is not None:
            return p ** x * (1.0 - p) ** (1.0 - x)
        if x not in [0, 1]:
            raise ValueError(
                f"Support for Bernoulli distribution" " is {0, 1}." f" found: {x}."
            )

        return self.p ** x * (1.0 - self.p) ** (1.0 - x)

    def cdf(self, x):
        if x < 0.0:
            return 0.0
        if x < 1.0:
            return 1.0 - self.p
        return 1.0

    def meanvar(self):
        return self.p, self.p * (1.0 - self.p)

    def sample(self, size=10000):
        return np.random.binomial(1.0, self.p, size=size)

    def plot_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=1.0, num=1000)
        for i in theta:
            plt.scatter(i, np.prod(self.pmf(observed, i)), color="r")
        if show:
            plt.show()

    def plot_log_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=1.0, num=1000)
        for i in theta:
            plt.scatter(i, np.sum(np.log(self.pmf(observed, i))), color="r")
        if show:
            plt.show()

    def mle(self, observed):
        return np.mean(observed)


class Binomial(Discrete):
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def pmf(self, x, n=None, p=None):
        if n and p:
            return (
                factorial(n)
                / (factorial(x) * factorial(n - x))
                * (p ** x)
                * ((1.0 - p) ** (n - x))
            )
        return (
            factorial(self.n)
            / (factorial(x) * factorial(self.n - x))
            * (self.p ** x)
            * ((1.0 - self.p) ** (self.n - x))
        )

    def cdf(self, x):
        res = np.zeros_like(x)
        for i, j in enumerate(x):
            res[i] += np.sum(self.pmf(np.arange(0, j, dtype=np.float32)))

        return res

    def meanvar(self):
        return self.n * self.p, self.n * self.p * (1.0 - self.p)

    def sample(self, size=10000):
        return np.random.binomial(self.n, self.p, size=size)

    def plot_likelihood(self, n, observed, show=False):
        theta = np.linspace(start=0.0, stop=1.0, num=1000)
        for i in theta:
            plt.scatter(i, np.prod(self.pmf(observed, n, i)), color="r")
        if show:
            plt.show()

    def plot_log_likelihood(self, n, observed, show=False):
        theta = np.linspace(start=0.0, stop=1.0, num=1000)
        for i in theta:
            plt.scatter(i, np.sum(np.log(self.pmf(observed, n, i))), color="r")
        if show:
            plt.show()

    def mle(self, n, observed):
        return np.mean(observed)


class Poisson(Discrete):
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    def pmf(self, x, lambda_=None):
        if lambda_ is not None:
            return np.exp(-lambda_) * (lambda_ ** x) / factorial(x)
        return np.exp(-self.lambda_) * (self.lambda_ ** x) / factorial(x)

    def cdf(self, x):
        res = np.zeros_like(x)
        for i, j in enumerate(x):
            res[i] += np.sum(self.pmf(np.arange(0, j, dtype=np.float32)))

        return res

    def meanvar(self):
        return self.lambda_, self.lambda_

    def sample(self, size=10000):
        return np.random.poisson(self.lambda_, size=size)

    def plot_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=2 * observed.mean(), num=1000)
        for i in theta:
            plt.scatter(i, np.prod(self.pmf(observed, i)), color="r")
        if show:
            plt.show()

    def plot_log_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=2 * observed.mean(), num=1000)
        for i in theta:
            plt.scatter(i, np.sum(np.log(self.pmf(observed, i))), color="r")
        if show:
            plt.show()

    def mle(self, observed):
        return np.mean(observed)


class Exponential(Continuous):
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    def pdf(self, x, lambda_=None):
        if lambda_ is not None:
            return (x >= 0.0) * lambda_ * np.exp(-lambda_ * x)
        return (x >= 0.0) * self.lambda_ * np.exp(-self.lambda_ * x)

    def cdf(self, x):
        return (x >= 0.0) * (1.0 - np.exp(-self.lambda_ * x))

    def meanvar(self):
        return 1.0 / self.lambda_, 1.0 / (self.lambda_ ** 2)

    def sample(self, size=10000):
        return np.random.exponential(self.lambda_, size=size)

    def plot_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=2.0 / observed.mean(), num=1000)
        for i in theta:
            plt.scatter(i, np.prod(self.pdf(observed, i)), color="r")
        if show:
            plt.show()

    def plot_log_likelihood(self, observed, show=False):
        theta = np.linspace(start=0.0, stop=2.0 / observed.mean(), num=1000)
        for i in theta:
            plt.scatter(i, np.sum(np.log(self.pdf(observed, i))), color="r")
        if show:
            plt.show()

    def mle(self, observed):
        import warnings

        if not np.mean(observed):
            warnings.warn(
                f"mean of the data is zero"
                f" whih is not valid for exponential"
                f"distribution.",
                RuntimeWarning,
            )
        return 1.0 / (np.mean(observed) + 1e-9)


class Normal(Continuous):
    def __init__(self, mu, var):
        self.mu = mu
        self.var = var

    def pdf(self, x, mu=None, var=None):
        if mu and var:
            return (1.0 / np.sqrt(2 * np.pi * var)) * np.exp(-0.5 * (x - mu) ** 2 / var)
        return (1.0 / np.sqrt(2 * np.pi * self.var)) * np.exp(
            -0.5 * (x - self.mu) ** 2 / self.var
        )

    def cdf(self, x):
        return norm.cdf(x, loc=self.mu, scale=self.var)

    def sample(self, size=10000):
        return np.random.normal(self.mu, self.var, size=size)

    def meanvar(self):
        return self.mu, self.var

    def plot_likelihood(self, observed, mu=None, var=None, show=False):
        if mu is None and var is None:
            raise ValueError(
                "at least one parameter must be known" " to plot the likelihood!"
            )
        if mu is None:
            theta = np.linspace(
                start=-2 * observed.mean() - 2,
                stop=2 * observed.mean() + 2,
                num=1000,
                dtype=np.float32,
            )
            for i in theta:
                plt.scatter(i, np.prod(self.pdf(observed, i, var)), color="r")
            if show:
                plt.show()
        elif var is None:
            theta = np.linspace(
                start=-2 * np.var(observed),
                stop=2 * np.var(observed),
                num=1000,
                dtype=np.float32,
            )
            for i in theta:
                plt.scatter(i, np.prod(self.pdf(observed, mu, i)), color="r")

            if show:
                plt.show()

    def plot_log_likelihood(self, observed, mu=None, var=None, show=False):
        if mu is None and var is None:
            raise ValueError(
                "at least one parameter must be known" " to plot the likelihood!"
            )
        if mu is None:
            theta = np.linspace(
                start=-2 * observed.mean() - 2,
                stop=2 * observed.mean() + 2,
                num=1000,
                dtype=np.float32,
            )
            for i in theta:
                plt.scatter(i, np.sum(np.log(self.pdf(observed, i, var))), color="r")
            if show:
                plt.show()
        elif var is None:
            theta = np.linspace(
                start=0.0, stop=2 * np.var(observed), num=1000, dtype=np.float32
            )
            for i in theta:
                plt.scatter(i, np.sum(np.log(self.pdf(observed, mu, i))), color="r")
            if show:
                plt.show()

    def mle(self, observed, mu=None, var=None):
        if mu is None and var is None:
            raise ValueError("at least one parameter must be known" " to find the mle!")

        if mu is None:
            return np.mean(observed)
        elif var is None:
            return np.sum((observed - mu) ** 2) / len(observed)


class Uniform(Continuous):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pdf(self, x):
        return (self.a <= x) * (x <= self.b) / (self.b - self.a)

    def cdf(self, x):
        return np.array(
            list(
                map(
                    lambda i: (i >= self.a) * (i - self.a) / (self.b - self.a)
                    if i <= self.b
                    else 1.0,
                    x,
                )
            )
        )

    def sample(self, size=10000):
        return np.random.uniform(self.a, self.b, size=size)

    def meanvar(self):
        return (self.a + self.b) / 2.0, (self.b - self.a) ** 2 / 2

    def plot_likelihood(self, observed):
        pass

    def plot_log_likelihood(self, observed):
        pass

    def mle(self, observed):
        return np.max(observed)


class Beta(Continuous):
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def pdf(self, x):
        x = np.array(x, dtype=np.float64)
        return (
            gamma(self.alpha + self.beta)
            / (gamma(self.alpha) * gamma(self.beta))
            * x ** (self.alpha - 1)
            * (1 - x) ** (self.beta - 1)
        )

    def cdf(self, x):
        pass


class StudentT(Continuous):
    def __init__(self, dof):
        self.dof = dof

    def pdf(self, x):
        return (
            gamma((self.dof + 1.0) / 2)
            / (np.sqrt(self.dof * np.pi) * gamma(self.dof / 2.0))
            * (1.0 + x ** 2 / self.dof) ** (-(self.dof + 1) / 2)
        )

    def cdf(self, x):
        return t.cdf(x, df=self.dof)

    def sample(self, size=10000):
        return t.rvs(df=self.dof, size=size)

    def plot_likelihood(self, observed):
        pass

    def plot_log_likelihood(self, observed):
        pass

    def mle(self, observed):
        pass


class Cauchy(Continuous):
    def __init__(self, x0, gamma):
        self.x0 = x0
        self.gamma = gamma

    def pdf(self, x):
        return (self.gamma / np.pi) / ((x - self.x0) ** 2 + self.gamma ** 2)

    def cdf(self, x):
        return 0.5 + (1.0 / np.pi) * np.arctan((x - self.x0) / self.gamma)

    def meanvar(self):
        return np.nan, np.nan

    def sample(self):
        pass

    def plot_likelihood(self, observed):
        pass

    def plot_log_likelihood(self, observed):
        pass

    def mle(self, observed):
        pass
