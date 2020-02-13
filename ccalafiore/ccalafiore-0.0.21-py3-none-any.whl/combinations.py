import numpy as np
from numbers import *


def n_conditions_to_combinations(
        n_conditions,
        axis_combinations=0,
        n_repetitions_combinations=1,
        dtype=None):

    from ccalafiore.array import pad_array_from_n_samples_target, advanced_indexing

    n_variables = len(n_conditions)
    if n_variables > 0:

        n_conditions = np.asarray(n_conditions, dtype=int)
        conditions = n_conditions_to_conditions(n_conditions)
        n_combinations = np.prod(n_conditions) * n_repetitions_combinations
        if n_combinations < 0:
            n_conditions = n_conditions.astype(np.int64)
            n_combinations = np.prod(n_conditions) * n_repetitions_combinations

        change_dtype = False
        if dtype is None:
            if isinstance(conditions[0][0], str):
                dtype_end = str
                dtype = object
                change_dtype = True
            elif isinstance(conditions[0][0], Integral):
                dtype = int
            elif isinstance(conditions[0][0], Integral):
                dtype = float
            else:
                dtype = type(conditions[0][0])

        # axis_combinations = int(not(bool(axis_variables)))
        axis_variables = int(not(bool(axis_combinations)))
        shape_combinations = np.empty(2, dtype=int)
        shape_combinations[axis_combinations] = n_combinations
        shape_combinations[axis_variables] = n_variables

        combinations = np.empty(shape_combinations, dtype=dtype)

        indexes_combinations =  np.empty(2, dtype=object)
        indexes_combinations[axis_variables] = -1
        indexes_combinations[axis_combinations] = np.arange(n_combinations)
        combinations[advanced_indexing(indexes_combinations)] = np.expand_dims(pad_array_from_n_samples_target(conditions[-1], n_samples_target=n_combinations), axis=axis_variables)
        cumulative_n_combinations = n_conditions[-1]
        for i_variable in range(2, n_variables + 1):
            cumulative_combinations = np.empty(
                cumulative_n_combinations * n_conditions[-i_variable], combinations.dtype)
            for i_condition in range(n_conditions[-i_variable]):
                cumulative_combinations[
                    slice(i_condition * cumulative_n_combinations, (i_condition + 1) * cumulative_n_combinations)] = \
                    conditions[-i_variable][i_condition]

            indexes_combinations[axis_variables] = -i_variable
            combinations[advanced_indexing(indexes_combinations)] = np.expand_dims(pad_array_from_n_samples_target(
                cumulative_combinations, n_samples_target=n_combinations), axis=axis_variables)
            cumulative_n_combinations *= n_conditions[-i_variable]

        if change_dtype:
            combinations = combinations.astype(dtype_end)
    else:
        combinations = []
    return combinations


def conditions_to_combinations(
        conditions,
        axis_combinations=0,
        n_repetitions_combinations=1,
        dtype=None):

    from ccalafiore.array import pad_array_from_n_samples_target, advanced_indexing

    n_variables = len(conditions)
    if n_variables > 0:

        conditions = np.asarray(conditions, dtype=object)
        n_conditions = conditions_to_n_conditions(conditions)
        n_combinations = np.prod(n_conditions) * n_repetitions_combinations
        if n_combinations < 0:
            n_conditions = n_conditions.astype(np.int64)
            n_combinations = np.prod(n_conditions) * n_repetitions_combinations

        change_dtype = False
        if dtype is None:
            if isinstance(conditions[0][0], str):
                dtype_end = str
                dtype = object
                change_dtype = True
            elif isinstance(conditions[0][0], Integral):
                dtype = int
            elif isinstance(conditions[0][0], Integral):
                dtype = float
            else:
                dtype = type(conditions[0][0])

            axis_variables = int(not(bool(axis_combinations)))
            shape_combinations = np.empty(2, dtype=int)
            shape_combinations[axis_combinations] = n_combinations
            shape_combinations[axis_variables] = n_variables

            combinations = np.empty(shape_combinations, dtype=dtype)

            indexes_combinations = np.empty(2, dtype=object)
            indexes_combinations[axis_variables] = -1
            indexes_combinations[axis_combinations] = np.arange(n_combinations)
            combinations[advanced_indexing(indexes_combinations)] = np.expand_dims(
                pad_array_from_n_samples_target(conditions[-1], n_samples_target=n_combinations), axis=axis_variables)
            cumulative_n_combinations = n_conditions[-1]
            for i_variable in range(2, n_variables + 1):
                cumulative_combinations = np.empty(
                    cumulative_n_combinations * n_conditions[-i_variable], combinations.dtype)
                for i_condition in range(n_conditions[-i_variable]):
                    cumulative_combinations[
                        slice(i_condition * cumulative_n_combinations, (i_condition + 1) * cumulative_n_combinations)] = \
                        conditions[-i_variable][i_condition]

                indexes_combinations[axis_variables] = -i_variable
                combinations[advanced_indexing(indexes_combinations)] = np.expand_dims(pad_array_from_n_samples_target(
                    cumulative_combinations, n_samples_target=n_combinations), axis=axis_variables)
                cumulative_n_combinations *= n_conditions[-i_variable]

            if change_dtype:
                combinations = combinations.astype(dtype_end)
        else:
            combinations = []
        return combinations


def make_combinations_of_conditions_as_distributions(conditions_as_distributions, n_repetitions_combinations=1):

    n_variables = len(conditions_as_distributions)
    n_conditions = np.empty(n_variables, dtype=object)

    for i_variable in range(n_variables):

        n_conditions[i_variable] = len(conditions_as_distributions[i_variable])

    combinations_of_conditions = n_conditions_to_combinations(n_conditions)

    n_combinations = len(combinations_of_conditions)

    combinations_of_conditions_as_distributions = np.empty([n_combinations, n_variables], dtype=int)

    for i_variable in range(n_variables):

        for i_condition in range(n_conditions[i_variable]):

            indexes_of_i_condition = np.argwhere(combinations_of_conditions[:, i_variable] == i_condition)

            n_i_condition = len(indexes_of_i_condition)

            combinations_of_conditions_as_distributions[indexes_of_i_condition, i_variable] = \
                np.random.choice(conditions_as_distributions[i_variable][i_condition],
                                 n_i_condition)[:, None]

    return combinations_of_conditions_as_distributions


def trials_to_combinations(
        trials, axis_combinations=0, variables=None,  n_repetitions_combinations=1, dtype=None):

    conditions = trials_to_conditions(trials, axis_combinations=axis_combinations, variables=variables)
    combinations = conditions_to_combinations(
        conditions,
        axis_combinations=axis_combinations,
        n_repetitions_combinations=n_repetitions_combinations,
        dtype=dtype)
    return combinations


def trials_to_conditions(trials, axis_combinations=0, variables=None):

    from ccalafiore.array import advanced_indexing

    axis_variables = int(not(bool(axis_combinations)))
    if variables is None:
        n_variables = trials.shape[axis_variables]
        variables = np.arange(n_variables)
    else:
        try:
            n_variables = len(variables)
        except TypeError:
            variables = np.asarray([variables], dtype=int)
            n_variables = len(variables)

    conditions = np.empty(n_variables, dtype=object)

    indexes_trials_adv = np.empty(2, dtype=object)
    indexes_trials_adv[axis_combinations] = np.arange(trials.shape[axis_combinations])

    indexes_trials_slice = np.full(2, 0, dtype=object)
    indexes_trials_slice[axis_combinations] = slice(None)
    indexes_trials_slice = tuple(indexes_trials_slice)

    for i_variable in range(n_variables):

        indexes_trials_adv[axis_variables] = variables[i_variable]
        trials_variables_i = trials[advanced_indexing(indexes_trials_adv)]
        trials_variables_i = trials_variables_i[indexes_trials_slice]

        conditions[i_variable] = np.unique(trials_variables_i)

    return conditions


def trials_to_n_conditions(trials, axis_combinations=0, variables=None):
    conditions = trials_to_conditions(trials, axis_combinations=axis_combinations, variables=variables)
    n_conditions = conditions_to_n_conditions(conditions)
    # n_variables = len(conditions)
    # n_conditions = np.empty(n_variables, dtype=int)
    # for i_variable in range(n_variables):
    #     n_conditions[i_variable] = len(conditions[i_variable])
    return n_conditions


def n_conditions_to_conditions(n_conditions):
    n_variables = len(n_conditions)
    conditions = np.empty(n_variables, dtype=object)
    for i_variable in range(n_variables):
        conditions[i_variable] = np.arange(n_conditions[i_variable])
    return conditions


def conditions_to_n_conditions(conditions):
    n_variables = len(conditions)
    n_conditions = np.empty(n_variables, dtype=int)
    for i_variable in range(n_variables):
        n_conditions[i_variable] = len(conditions[i_variable])
    return n_conditions
