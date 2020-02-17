"""
"""
import numpy as np


def extract_ohe_groups(onehot_encoder):
    """Extract a vector with group indices from a scikit-learn OneHotEncoder

    Arguments
    ---------
    onehot_encoder : sklearn.preprocessing.OneHotEncoder

    Returns
    -------
    np.ndarray
        A group-vector that can be used with the group lasso regularised
        linear models.
    """
    if not hasattr(onehot_encoder, "categories_"):
        raise ValueError(
            "Cannot extract group labels from an unfitted OneHotEncoder instance."
        )

    categories = onehot_encoder.categories_
    return np.concatenate(
        [
            group * np.ones_like(category)
            for group, category in enumerate(categories)
        ]
    )


def _get_reg_values(reg_min, reg_max, n_values, logarithmic, reg_values):
    if reg_values is not None:
        return reg_values

    reg_min, reg_max = min(reg_min, reg_max), max(reg_min, reg_max)
    if logarithmic and reg_min != 0:
        reg_sequence_generator = np.logspace
        reg_min = np.log(reg_min)
        reg_max = np.log(reg_max)
    elif logarithmic:
        raise ValueError(
            "Cannot have minimum regularisation equal to 0 with logarithmic scale."
        )
    else:
        reg_sequence_generator = np.linspace

    return reg_sequence_generator(reg_max, reg_min, n_values)


def regularisation_group_selection(
    estimator,
    X,
    y,
    group_reg_min=1e-5,
    group_reg_max=1,
    n_values=100,
    logarithmic=True,
    group_reg_values=None,
):
    """Train an estimator many times with different regularisation to select groups.
    """
    group_reg_values = _get_reg_values(
        group_reg_min, group_reg_max, n_values, logarithmic, group_reg_values
    )
    estimator.warm_start = True
    groups = {}
    masks = {}
    for group_reg in group_reg_values:
        estimator.group_reg = group_reg
        estimator.fit(X, y)
        groups[group_reg] = estimator.chosen_groups_
        masks[group_reg] = estimator.sparsity_mask_

    return groups


