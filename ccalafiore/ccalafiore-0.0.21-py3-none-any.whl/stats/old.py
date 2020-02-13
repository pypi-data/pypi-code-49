import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing
# from scipy.stats import t
# from scipy.stats.stats import _ttest_finish
# from ccalafiore.combinations import n_conditions_to_combinations


def format_scores_for_paired_t_test(scores_raw, axis_independent_variable=-2, dtype=None):

    shape_scores_raw = np.asarray(scores_raw.shape)
    n_axes_scores_raw = len(shape_scores_raw)
    axis_independent_variable_raw = axis_independent_variable % n_axes_scores_raw

    scores_raw = np.expand_dims(scores_raw, axis=axis_independent_variable_raw)
    scores_raw = np.expand_dims(scores_raw, axis=axis_independent_variable_raw)
    axis_independent_variable_raw += 2

    n_conditions_iv_per_comparisons = 2

    shape_scores_raw = np.asarray(scores_raw.shape)
    n_axes_scores_raw = len(shape_scores_raw)
    n_conditions_iv = shape_scores_raw[axis_independent_variable_raw]

    axes_scores = np.arange(n_axes_scores_raw)
    axes_non_independent_variables_scores_raw = axes_scores[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_scores, axis_independent_variable_raw))]

    index_0_raw = np.empty(n_axes_scores_raw, dtype=object)
    index_0_formatted = np.copy(index_0_raw)

    for a in axes_non_independent_variables_scores_raw:
        index_0_raw[a] = np.arange(shape_scores_raw[a])
    index_1_raw = np.copy(index_0_raw)

    axes_independent_variable_formatted = np.asarray([
        axis_independent_variable_raw - 2,
        axis_independent_variable_raw - 1,
        axis_independent_variable_raw], dtype=int)

    axes_non_independent_variable_formatted = axes_scores[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_scores, axes_independent_variable_formatted))]

    index_0_formatted[axes_non_independent_variable_formatted] = index_0_raw[axes_non_independent_variable_formatted]
    index_0_formatted[axes_independent_variable_formatted[0]] = np.arange(2)
    index_1_formatted = np.copy(index_0_formatted)

    shape_scores_formatted = np.copy(shape_scores_raw)
    shape_scores_formatted[axes_independent_variable_formatted[0]] = n_conditions_iv_per_comparisons
    shape_scores_formatted[axes_independent_variable_formatted[1:]] = n_conditions_iv

    if dtype is None:
        dtype = scores_raw.dtype
    # scores_formatted = np.full(shape_scores_formatted, 0, dtype=dtype)
    scores_formatted = np.empty(shape_scores_formatted, dtype=dtype)

    for i_condition_0 in range(n_conditions_iv):

        index_0_raw[axis_independent_variable_raw] = i_condition_0
        index_0_raw_adv = advanced_indexing(index_0_raw)

        index_0_formatted[axes_independent_variable_formatted[1]] = i_condition_0
        index_1_formatted[axes_independent_variable_formatted[2]] = i_condition_0

        for i_condition_1 in range(i_condition_0, n_conditions_iv):

            scores_raw_0 = scores_raw[index_0_raw_adv]

            index_0_formatted[axes_independent_variable_formatted[2]] = i_condition_1
            index_0_formatted_adv = advanced_indexing(index_0_formatted)

            if i_condition_0 == i_condition_1:

                scores_formatted[index_0_formatted_adv] = np.append(
                    scores_raw_0, scores_raw_0, axis=axes_independent_variable_formatted[0])

            else:
                index_1_raw[axis_independent_variable_raw] = i_condition_1
                index_1_raw_adv = advanced_indexing(index_1_raw)

                scores_raw_1 = scores_raw[index_1_raw_adv]

                index_1_formatted[axes_independent_variable_formatted[1]] = i_condition_1
                index_1_formatted_adv = advanced_indexing(index_1_formatted)

                scores_formatted[index_0_formatted_adv] = np.append(
                    scores_raw_0, scores_raw_1, axis=axes_independent_variable_formatted[0])

                scores_formatted[index_1_formatted_adv] = np.append(
                    scores_raw_1, scores_raw_0, axis=axes_independent_variable_formatted[0])

    return scores_formatted


def scores_to_diff_of_scores(scores, axis_independent_variable=-2, dtype=None):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    axis_independent_variable %= n_axes_scores

    scores = np.expand_dims(scores, axis=axis_independent_variable + 1)
    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    n_conditions_iv = shape_scores[axis_independent_variable]

    axes_scores = np.arange(n_axes_scores)
    axes_non_independent_variables_scores = axes_scores[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_scores, axis_independent_variable))]

    index_1 = np.empty(n_axes_scores, dtype=object)
    index_diff_1 = np.copy(index_1)

    for a in axes_non_independent_variables_scores:
        index_1[a] = np.arange(shape_scores[a])
    index_2 = np.copy(index_1)

    independent_variables_diff = np.asarray([axis_independent_variable, axis_independent_variable + 1], dtype=int)
    axes_non_independent_variables_diff = axes_scores[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_scores, independent_variables_diff))]

    index_diff_1[axes_non_independent_variables_diff] = index_1[axes_non_independent_variables_diff]
    index_diff_2 = np.copy(index_diff_1)

    shape_diff = np.copy(shape_scores)
    shape_diff[independent_variables_diff] = n_conditions_iv
    if dtype is None:
        dtype = scores.dtype
    diff_of_scores = np.full(shape_diff, 0, dtype=dtype)

    for i_condition_1 in range(n_conditions_iv - 1):

        index_1[axis_independent_variable] = i_condition_1
        index_1_adv = advanced_indexing(index_1)
        index_diff_1[independent_variables_diff[0]] = i_condition_1
        index_diff_2[independent_variables_diff[1]] = i_condition_1

        for i_condition_2 in range(i_condition_1 + 1, n_conditions_iv):

            index_2[axis_independent_variable] = i_condition_2
            index_2_adv = advanced_indexing(index_2)

            index_diff_1[independent_variables_diff[1]] = i_condition_2
            index_diff_1_adv = advanced_indexing(index_diff_1)

            index_diff_2[independent_variables_diff[0]] = i_condition_2
            index_diff_2_adv = advanced_indexing(index_diff_2)

            diff_of_scores_1_2 = scores[index_1_adv] - scores[index_2_adv]
            diff_of_scores[index_diff_1_adv] = diff_of_scores_1_2
            diff_of_scores[index_diff_2_adv] = -diff_of_scores_1_2 + 0

    return diff_of_scores


