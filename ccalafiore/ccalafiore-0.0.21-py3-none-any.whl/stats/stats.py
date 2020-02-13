import numpy as np
from ccalafiore.array import pad_arr_1_from_arr_2, samples_in_arr1_are_in_arr2, advanced_indexing
from scipy.stats import t, sem
from scipy.stats.stats import _ttest_finish
from ccalafiore.combinations import n_conditions_to_combinations


def scores_to_df_for_unpaired_t_test(
        scores, axis_samples=-1, axis_independent_variables=-2, keepdims=False):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    axis_samples %= n_axes_scores
    axis_independent_variables_scores = axis_independent_variables % n_axes_scores

    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    variances = scores_to_variances(scores, axis_samples=axis_samples, keepdims=keepdims)
    if not(keepdims):
        axis_independent_variables_n_samples = axis_independent_variables_scores - (
                axis_independent_variables_scores > axis_samples)
    else:
        axis_independent_variables_n_samples = axis_independent_variables_scores

    n_samples = np.expand_dims(n_samples, axis=axis_independent_variables_n_samples + 1)
    variances = np.expand_dims(variances, axis=axis_independent_variables_n_samples + 1)
    shape_n_samples = np.asarray(n_samples.shape)
    n_axes_n_samples = len(shape_n_samples)
    n_conditions_iv = shape_n_samples[axis_independent_variables_n_samples]

    axes_n_samples = np.arange(n_axes_n_samples)
    axes_non_independent_variables_n_samples = axes_n_samples[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_n_samples, axis_independent_variables_n_samples))]

    index_n_samples_1 = np.empty(n_axes_n_samples, dtype=object)
    index_df_1 = np.copy(index_n_samples_1)

    for a in axes_non_independent_variables_n_samples:
        index_n_samples_1[a] = np.arange(shape_n_samples[a])
    index_n_samples_2 = np.copy(index_n_samples_1)

    axis_independent_variables_df = np.asarray(
        [axis_independent_variables_n_samples, axis_independent_variables_n_samples + 1], dtype=int)
    axes_non_independent_variables_df = axes_n_samples[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_n_samples, axis_independent_variables_df))]

    index_df_1[axes_non_independent_variables_df] = index_n_samples_1[axes_non_independent_variables_df]
    index_df_2 = np.copy(index_df_1)

    shape_df = np.copy(shape_n_samples)
    shape_df[axis_independent_variables_df] = n_conditions_iv

    df = np.full(shape_df, 0, dtype=int)

    for i_condition_1 in range(n_conditions_iv):

        index_n_samples_1[axis_independent_variables_n_samples] = i_condition_1
        index_n_samples_1_adv = advanced_indexing(index_n_samples_1)
        index_df_1[axis_independent_variables_df[0]] = i_condition_1
        index_df_2[axis_independent_variables_df[1]] = i_condition_1

        for i_condition_2 in range(i_condition_1, n_conditions_iv):

            index_n_samples_2[axis_independent_variables_n_samples] = i_condition_2
            index_n_samples_2_adv = advanced_indexing(index_n_samples_2)

            index_df_1[axis_independent_variables_df[1]] = i_condition_2
            index_df_1_adv = advanced_indexing(index_df_1)

            variances_1 = variances[index_n_samples_1_adv]
            variances_2 = variances[index_n_samples_2_adv]

            n_samples_1 = n_samples[index_n_samples_1_adv]
            n_samples_2 = n_samples[index_n_samples_2_adv]

            df_1_2 = (((variances_1 / n_samples_1) + (variances_2 / n_samples_2))**2) / (
                (((variances_1 / n_samples_1)**2) / (n_samples_1 - 1)) +
                (((variances_2 / n_samples_2)**2) / (n_samples_2 - 1)))
            # df_1_2 = np.maximum(
            #     n_samples[index_n_samples_1_adv], n_samples[index_n_samples_2_adv])

            df[index_df_1_adv] = df_1_2

            if i_condition_1 < i_condition_2:
                index_df_2[axis_independent_variables_df[0]] = i_condition_2
                index_df_2_adv = advanced_indexing(index_df_2)
                df[index_df_2_adv] = df_1_2

    return df


def scores_to_unpaired_t_test_denominator(
        scores, axis_samples=-1, axis_independent_variables=-2, keepdims=False, dtype=None):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = len(shape_scores)
    axis_samples %= n_axes_scores
    axis_independent_variables %= n_axes_scores

    n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)
    variances = scores_to_variances(scores, axis_samples=axis_samples, keepdims=keepdims)

    if not(keepdims):
        axis_independent_variables -= (axis_independent_variables > axis_samples)
    n_samples = np.expand_dims(n_samples, axis=axis_independent_variables + 1)
    variances = np.expand_dims(variances, axis=axis_independent_variables + 1)
    shape_variances = np.asarray(variances.shape)
    n_axes_variances = len(shape_variances)
    n_conditions_iv = shape_variances[axis_independent_variables]

    axes_variances = np.arange(n_axes_variances)
    axes_non_independent_variables_variances = axes_variances[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_variances, axis_independent_variables))]

    index_1 = np.empty(n_axes_variances, dtype=object)
    index_denominator_1 = np.copy(index_1)

    for a in axes_non_independent_variables_variances:
        index_1[a] = np.arange(shape_variances[a])
    index_2 = np.copy(index_1)

    independent_variables_denominator = np.asarray([axis_independent_variables, axis_independent_variables + 1], dtype=int)
    axes_non_independent_variables_denominator = axes_variances[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_variances, independent_variables_denominator))]

    index_denominator_1[axes_non_independent_variables_denominator] = index_1[axes_non_independent_variables_denominator]
    index_denominator_2 = np.copy(index_denominator_1)

    shape_denominator = np.copy(shape_variances)
    shape_denominator[independent_variables_denominator] = n_conditions_iv
    if dtype is None:
        dtype = variances.dtype
    denominator = np.full(shape_denominator, 0, dtype=dtype)

    for i_condition_1 in range(n_conditions_iv - 1):

        index_1[axis_independent_variables] = i_condition_1
        index_1_adv = advanced_indexing(index_1)
        index_denominator_1[independent_variables_denominator[0]] = i_condition_1
        index_denominator_2[independent_variables_denominator[1]] = i_condition_1

        for i_condition_2 in range(i_condition_1 + 1, n_conditions_iv):

            index_2[axis_independent_variables] = i_condition_2
            index_2_adv = advanced_indexing(index_2)

            index_denominator_1[independent_variables_denominator[1]] = i_condition_2
            index_denominator_1_adv = advanced_indexing(index_denominator_1)

            index_denominator_2[independent_variables_denominator[0]] = i_condition_2
            index_denominator_2_adv = advanced_indexing(index_denominator_2)

            denominator_1_2 = np.sqrt(
                (variances[index_1_adv] / n_samples[index_1_adv]) +
                (variances[index_2_adv] / n_samples[index_2_adv])
            )

            denominator[index_denominator_1_adv] = denominator_1_2
            denominator[index_denominator_2_adv] = denominator_1_2

    return denominator


def scores_to_unpaired_t_test(
        scores, axis_samples=-1, axis_independent_variables=-2, alpha=0.05, tails='2', keepdims=False):

    np.seterr(divide='ignore', invalid='ignore')

    confidence = 1 - alpha

    shape_scores = scores.shape
    n_axes = len(shape_scores)
    axis_samples %= n_axes
    axis_independent_variables %= n_axes

    means_of_scores = scores_to_means(scores, axis_samples=axis_samples, keepdims=keepdims)

    denominator = scores_to_unpaired_t_test_denominator(
        scores, axis_samples=axis_samples, axis_independent_variables=axis_independent_variables)

    df = scores_to_df_for_unpaired_t_test(
        scores, axis_samples=axis_samples, axis_independent_variables=axis_independent_variables,
        keepdims=keepdims)

    if not(keepdims):
        axis_independent_variables -= (axis_independent_variables > axis_samples)

    diff_of_means = scores_to_diff_of_scores(means_of_scores, axis_independent_variables=axis_independent_variables)

    t_values = diff_of_means / denominator
    np.nan_to_num(t_values, copy=False, nan=0.0)

    shape_df = df.shape
    n_df = df.size

    t_critical = np.empty(shape_df, dtype=float)
    p_values = np.empty(shape_df, dtype=float)

    indexs_df = n_conditions_to_combinations(shape_df)
    for i in range(n_df):

        if tails == '2':
            t_critical[tuple(indexs_df[i])] = t.ppf((1 + confidence) / 2., df[tuple(indexs_df[i])])
            p_values[tuple(indexs_df[i])] = (1.0 - t.cdf(abs(t_values[tuple(indexs_df[i])]), df[tuple(indexs_df[i])])) * 2
        elif tails == '1l':
            t_critical[tuple(indexs_df[i])] = -t.ppf(confidence, df[tuple(indexs_df[i])])
            p_values[tuple(indexs_df[i])] = t.cdf(t_values[tuple(indexs_df[i])], df[tuple(indexs_df[i])])
        elif tails == '1r':
            t_critical[tuple(indexs_df[i])] = t.ppf(confidence, df[tuple(indexs_df[i])])
            p_values[tuple(indexs_df[i])] = 1.0 - t.cdf(t_values[tuple(indexs_df[i])], df[tuple(indexs_df[i])])

    return t_values, df, t_critical, p_values


# def height_of_t_confidence_interval(data, confidence=0.95):
#     a = 1.0 * np.array(data)
#     n = len(a)
#     m, se = np.mean(a), stats.sem(a)
#     h = se * stats.t.ppf((1 + confidence) / 2., n-1)
#     return h
