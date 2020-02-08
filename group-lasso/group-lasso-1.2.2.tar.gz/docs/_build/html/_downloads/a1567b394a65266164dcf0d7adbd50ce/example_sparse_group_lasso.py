"""
A sample script for group lasso regression
"""

from group_lasso import GroupLasso
from group_lasso.utils import extract_ohe_groups
from utils import (
    get_groups_from_group_sizes,
    generate_group_lasso_coefficients,
)
import numpy as np
from scipy import sparse
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt


GroupLasso.LOG_LOSSES = True


if __name__ == "__main__":
    np.random.seed(1)

    num_categories = 20
    min_options = 2
    max_options = 10
    num_datapoints = 10000
    noise_level = 1
    coeff_noise_level = 0.2

    print("Generating data")
    X_cat = np.empty((num_datapoints, num_categories))
    for i in range(num_categories):
        X_cat[:,  i] = np.random.randint(min_options, max_options, num_datapoints)

    ohe = OneHotEncoder()
    X = ohe.fit_transform(X_cat)
    groups = extract_ohe_groups(ohe)
    group_sizes = [np.sum(groups == g) for g in np.unique(groups)]
    group_weights = [np.random.randint(0, 2) for _ in np.unique(groups)]

    intercept = 2

    print("Generating coefficients")
    w = np.concatenate(
        [weight*np.random.standard_normal(group_size) for weight, group_size in zip(group_weights, group_sizes)]
    ).reshape(-1, 1)
    w *= np.random.random((len(w), 1)) > 0.4
    w += np.random.randn(*w.shape) * coeff_noise_level

    print("Generating targets")
    y = X @ w
    y += np.random.randn(*y.shape) * noise_level * y
    y += intercept

    gl = GroupLasso(
        groups=groups,
        n_iter=1000,
        tol=1e-3,
        l1_reg=0,
        group_reg=0.02,
        frobenius_lipschitz=False,
        subsampling_scheme=None,
        fit_intercept=True,
    )
    print("Starting fit")
    gl.fit(X, y)

    for i in range(w.shape[1]):
        plt.figure()
        plt.subplot(211)
        plt.plot(w[:, i], ".", label="True weights")
        plt.plot(gl.coef_[:, i], ".", label="Estimated weights")

        plt.subplot(212)
        plt.plot(w[gl.sparsity_mask, i], ".", label="True weights")
        plt.plot(gl.coef_[gl.sparsity_mask, i], ".", label="Estimated weights")
        plt.legend()

    plt.figure()
    plt.plot([w.min(), w.max()], [gl.coef_.min(), gl.coef_.max()], "gray")
    plt.scatter(w, gl.coef_, s=10)
    plt.ylabel("Learned coefficients")
    plt.xlabel("True coefficients")

    plt.figure()
    plt.plot(gl.losses_)

    print("X shape: {X.shape}".format(X=X))
    print("Transformed X shape: {shape}".format(shape=gl.transform(X).shape))
    print("True intercept: {intercept}".format(intercept=intercept))
    print("Estimated intercept: {intercept}".format(intercept=gl.intercept_))
    plt.show()
