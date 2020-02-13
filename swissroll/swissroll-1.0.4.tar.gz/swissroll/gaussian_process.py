import numpy as np

__all__ = ["GPRegressor"]


def rbf_kernel(x1, x2, sigma, landmark):
    """Evaluate the rbf kernel

    Parameters
    -----
    x1: matrix of shape `(n_samples, n_features)`

    x2: vector of size `(n_features)`

    sigma: scalar

    landmark: scalar

    Returns
    -----
    rbf: vector of size `(n_samples)`
    """
    x2 = x2.reshape(1, -1)
    if x1.shape[1] != x2.shape[1]:
        raise ValueError(
            f"shapes of x1 and x2 are inconsistent => "
            f"{x1.shape[1]} != {x2.shape[1]}"
        )
    s = sigma
    l = landmark
    return s ** 2.0 * np.exp(
        -0.5 * np.linalg.norm(x1 - x2, axis=-1) ** 2.0 / (l ** 2.0)
    )


def normalize(xs):
    """Center the data to match the standard scale

    Parameters
    -----
    xs: matrix of shape `(n_samples, n_features)`

    Returns
    -----
    norm_xs: matrix of shape `(n_samples, n_features)`
    """
    return (xs - np.mean(xs)) / np.std(xs)


class GPRegressor:
    """Gaussian Process Regressor

    Parameters
    -----
    k_sigma: scalar
        standard deviation of RBF kernel

    k_landmark: scalar
        landmark of the RBF kernel
    """

    def __init__(self, k_sigma, k_landmark):
        self.k_sigma = k_sigma
        self.k_landmark = k_landmark
        self.__fitted = False

    def fit(self, xs, ys, verbose=False):
        """Fit the regressor on your dataset

        Parameters
        -----
        xs: matrix of shape `(n_samples, n_features)`
            training data to be fitted

        ys: vector of size `(n_samples)`
            target values

        verbose: bool, optional
            if `True`, prints the results after calculation
        """
        self.n_samples = xs.shape[0]
        self.n_features = xs.shape[1]
        self._x = xs
        self._y = ys

        self.mus = np.zeros_like(ys.reshape(-1, 1))
        self.sigmas = np.zeros((self.n_samples, self.n_samples))
        for i in range(self.n_samples):
            self.sigmas[i, :] = rbf_kernel(xs, xs[i], self.k_sigma, self.k_landmark)

        if verbose:
            print(self.mus)
            print(self.sigmas)
            print(self.mus.shape)
            print(self.sigmas.shape)

        self.__fitted = True

    def predict(self, xs, predict_uncertainties=False):
        """Predict on the new datapoint

        Parameters
        -----
        x: matrix of shape `(n_new_samples, n_features)`
            new datapoints for which the target is to be predicted

        predict_uncertainties: bool, optional
            if `True`, return the covarience matrix with predicted target values

        Returns
        -----
        pos_mus: vector of size `(n_new_samples)`
            predicted target values
        
        pos_sigmas: (if `predict_uncertainties=True`) matrix of shape (n_new_samples, n_new_samples)
            covarience matrix of the predicted targets
        """
        if not self.__fitted:
            raise TypeError(f"no dataset fitted! First call the `fit` method")
        if xs.shape[1] != self.n_features:
            raise ValueError(
                f"inconsistent input to method `predict` "
                f"{xs.shape[1]} != {self.n_features}"
            )

        k = np.zeros((xs.shape[0], self.n_samples))
        for i in range(xs.shape[0]):
            k[i, :] = rbf_kernel(self._x, xs[i], self.k_sigma, self.k_landmark)

        # pos_mus = (self.n_new_samples, 1)
        pos_mus = k @ np.linalg.inv(self.sigmas) @ self._y

        if predict_uncertainties:
            # pos_sigmas = (n_new_samples, n_new_samples)
            pos_sigmas = self.k_sigma ** 2.0 - k @ np.linalg.inv(self.sigmas) @ k.T
            return pos_mus, pos_sigmas

        return pos_mus
