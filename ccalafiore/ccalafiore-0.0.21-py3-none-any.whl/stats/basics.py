import numpy as np
from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing
from scipy.stats import t
# from scipy.stats.stats import _ttest_finish
from ccalafiore.combinations import n_conditions_to_combinations


def scores_to_diff_of_scores(scores, axis, delta=1, stride=1, keepdims=False):

    shape_scores = np.asarray(scores.shape)
    n_axes_scores = shape_scores.size
    if axis < 0:
        axis += n_axes_scores

    n_conditions = shape_scores[axis]
    index_0 = np.empty(n_axes_scores, dtype=object)
    index_0[:] = slice(None)
    index_1 = np.copy(index_0)

    index_diff = np.copy(index_0)
    index_diff[axis] = 0

    n_differences = int((n_conditions - delta) // stride)
    shape_diff_of_scores = shape_scores
    shape_diff_of_scores[axis] = n_differences
    diff_of_scores = np.empty(shape_diff_of_scores, dtype=scores.dtype)

    for i in range(0, n_conditions - delta, stride):
        index_0[axis] = i
        index_1[axis] = i + delta
        diff_of_scores[tuple(index_diff)] = scores[tuple(index_0)] - scores[tuple(index_1)]
        index_diff[axis] += 1

    if not keepdims and (diff_of_scores.shape[axis] == 1):
        diff_of_scores = np.squeeze(diff_of_scores, axis=axis)

    return diff_of_scores


def scores_to_n_samples(scores, axis_samples, keepdims=False):

    if scores.dtype == object:

        shape_object_scores = np.asarray(scores.shape)
        n_axes_object_scores = shape_object_scores.size
        axes_object_scores = np.arange(n_axes_object_scores)

        indexes_object = np.empty(n_axes_object_scores, dtype=object)
        indexes_object[:] = 0
        shape_scores = np.asarray(scores[tuple(indexes_object)].shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        if keepdims:
            shape_scores_tmp = shape_scores
            shape_scores_tmp[axis_samples] = 1
        else:
            shape_scores_tmp = shape_scores[np.arange(n_axes_scores) != axis_samples]

        shape_n_samples = np.append(shape_object_scores, shape_scores_tmp)
        n_samples = np.empty(shape_n_samples, dtype=int)

        n_axes_n_samples = shape_n_samples.size
        indexes_n_samples = np.empty(n_axes_n_samples,dtype=object)
        indexes_n_samples[:] = slice(None)

        indexes_object = n_conditions_to_combinations(shape_object_scores)
        for indexes_object_i in indexes_object:

            indexes_n_samples[axes_object_scores] = indexes_object_i
            indexes_n_samples_tuple = tuple(indexes_n_samples)
            indexes_object_i_tuple = tuple(indexes_object_i)

            n_samples[indexes_n_samples_tuple] = np.sum(np.logical_not(np.isnan(
                scores[indexes_object_i_tuple])), axis=axis_samples, keepdims=keepdims)

    else:
        shape_scores = np.asarray(scores.shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=keepdims)

    return n_samples


def scores_to_df_of_variance_and_paired_t(scores, axis_samples, keepdims=False):

    n_samples = scores_to_n_samples(scores, axis_samples=axis_samples, keepdims=keepdims)
    df = n_samples - 1

    return n_samples


def scores_to_means(scores, axes, keepdims=False):

    axes_means = axes

    if scores.dtype == object:

        shape_object_scores = np.asarray(scores.shape)
        n_axes_object_scores = shape_object_scores.size
        axes_object_scores = np.arange(n_axes_object_scores)

        indexes_object = np.empty(n_axes_object_scores, dtype=object)
        indexes_object[:] = 0
        shape_scores = np.asarray(scores[tuple(indexes_object)].shape, dtype=int)
        n_axes_scores = shape_scores.size
        try:
            len(axes_means)
            # n_axes_means = len(axes_means)
            axes_means = np.asarray(axes_means, dtype=int)
            axes_means[axes_means < 0] += n_axes_scores
            # check point 1
            if np.sum(axes_means[0] == axes_means) > 1:
                raise ValueError('axes cannot contain repeated values')
            axes_means = np.sort(axes_means)[::-1]
        except TypeError:
            if axes_means < 0:
                axes_means += n_axes_scores
            axes_means = np.asarray([axes_means], dtype=int)
            # n_axes_means = 1

        if keepdims:
            shape_scores_tmp = shape_scores
            shape_scores_tmp[axes_means] = 1
        else:
            axes_scores = np.arange(n_axes_scores)
            shape_scores_tmp = shape_scores[np.logical_not(samples_in_arr1_are_in_arr2(
                axes_scores, axes_means))]

        shape_means = np.append(shape_object_scores, shape_scores_tmp)
        means = np.empty(shape_means, dtype=float)

        n_axes_means = shape_means.size
        indexes_means = np.empty(n_axes_means, dtype=object)
        indexes_means[:] = slice(None)

        indexes_object = n_conditions_to_combinations(shape_object_scores)
        for indexes_object_i in indexes_object:

            indexes_means[axes_object_scores] = indexes_object_i
            indexes_means_tuple_i = tuple(indexes_means)
            indexes_object_tuple_i = tuple(indexes_object_i)

            scores_tmp_i = scores[indexes_object_tuple_i]
            for a in axes_means:
                n_samples = np.sum(np.logical_not(np.isnan(scores_tmp_i)), axis=a, keepdims=keepdims)
                sum_of_scores = np.nansum(scores_tmp_i, axis=a, keepdims=keepdims)
                scores_tmp_i = sum_of_scores / n_samples

            means[indexes_means_tuple_i] = scores_tmp_i

    else:

        shape_scores = np.asarray(scores.shape, dtype=int)
        n_axes_scores = shape_scores.size

        try:
            len(axes_means)
            # n_axes_means = len(axes_means)
            axes_means = np.asarray(axes_means, dtype=int)
            axes_means[axes_means < 0] += n_axes_scores
            # check point 1
            if np.sum(axes_means[0] == axes_means) > 1:
                raise ValueError('axes cannot contain repeated values')
            axes_means = np.sort(axes_means)[::-1]
        except TypeError:
            if axes_means < 0:
                axes_means += n_axes_scores
            axes_means = np.asarray([axes_means], dtype=int)
            # n_axes_means = 1
        scores_tmp = scores
        for a in axes_means:
            sum_of_scores = np.nansum(scores_tmp, axis=a, keepdims=keepdims)
            n_samples = np.sum(np.logical_not(np.isnan(scores_tmp)), axis=a, keepdims=keepdims)
            scores_tmp = sum_of_scores / n_samples
        means = scores_tmp

    return means


def scores_to_variances(scores, axis_samples, keepdims=False):

    if scores.dtype == object:

        shape_object_scores = np.asarray(scores.shape)
        n_axes_object_scores = shape_object_scores.size
        axes_object_scores = np.arange(n_axes_object_scores)

        indexes_object = np.empty(n_axes_object_scores,dtype=object)
        indexes_object[:] = 0
        shape_scores = np.asarray(scores[tuple(indexes_object)].shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        if keepdims:
            shape_scores_tmp = shape_scores
            shape_scores_tmp[axis_samples] = 1
        else:
            shape_scores_tmp = shape_scores[np.arange(n_axes_scores) != axis_samples]

        shape_variances = np.append(shape_object_scores, shape_scores_tmp)
        variances = np.empty(shape_variances, dtype=float)

        n_axes_variances = shape_variances.size
        indexes_variances = np.empty(n_axes_variances,dtype=object)
        indexes_variances[:] = slice(None)

        indexes_object = n_conditions_to_combinations(shape_object_scores)
        for indexes_object_i in indexes_object:

            indexes_variances[axes_object_scores] = indexes_object_i
            indexes_variances_tuple = tuple(indexes_variances)
            indexes_object_i_tuple = tuple(indexes_object_i)

            n_samples = np.sum(np.logical_not(np.isnan(
                scores[indexes_object_i_tuple])), axis=axis_samples, keepdims=True)
            sum_of_scores = np.nansum(scores[indexes_object_i_tuple], axis=axis_samples, keepdims=True)
            means = sum_of_scores / n_samples

            sum_of_squared_distances = np.nansum(
                (scores[indexes_object_i_tuple] - means) ** 2,
                axis=axis_samples, keepdims=keepdims)

            if not keepdims:
                n_samples = np.squeeze(n_samples, axis=axis_samples)
            df = n_samples - 1

            variances[indexes_variances_tuple] = sum_of_squared_distances / df

    else:

        shape_scores = np.asarray(scores.shape)
        n_axes_scores = shape_scores.size
        if axis_samples < 0:
            axis_samples += n_axes_scores

        n_samples = np.sum(np.logical_not(np.isnan(scores)), axis=axis_samples, keepdims=True)
        means = np.nansum(scores, axis=axis_samples, keepdims=True) / n_samples
        sum_of_squared_distances = np.nansum((scores - means) ** 2, axis=axis_samples, keepdims=keepdims)
        if not keepdims:
            n_samples = np.squeeze(n_samples, axis=axis_samples)
        df = n_samples - 1
        variances = sum_of_squared_distances / df

    return variances


def scores_to_standard_deviations(scores, axis_samples, keepdims=False):

    variances = scores_to_variances(scores, axis_samples, keepdims=keepdims)
    standard_deviations = np.sqrt(variances)

    return standard_deviations


def scores_to_standard_errors(scores, axis_samples, keepdims=False):

    # shape_scores = np.asarray(scores.shape)
    # n_axes_scores = shape_scores.size
    # if axis_samples < 0:
    #     axis_samples += n_axes_scores

    n_samples = scores_to_n_samples(scores, axis_samples, keepdims=keepdims)
    variances = scores_to_variances(scores, axis_samples, keepdims=keepdims)
    std_error = np.sqrt(variances / n_samples)

    return std_error


def scores_to_confidence_intervals(
        scores, axis_samples, alpha=0.05, tails='2', keepdims=False):

    confidence = 1 - alpha

    # shape_scores = np.asarray(scores.shape)
    # n_axes_scores = shape_scores.size
    # if axis_samples < 0:
    #     axis_samples += n_axes_scores

    std_err = scores_to_standard_errors(scores, axis_samples, keepdims=keepdims)
    df = scores_to_df_of_variance_and_paired_t(scores, axis_samples, keepdims=keepdims)

    shape_df = np.asarray(df.shape)
    indexs_df = n_conditions_to_combinations(shape_df)
    t_critical = np.empty(shape_df, dtype=float)

    for indexs_df_i in indexs_df:

        indexs_df_i_tuple = tuple(indexs_df_i)

        if tails == '2':
            t_critical[indexs_df_i_tuple] = t.ppf((1 + confidence) / 2., df[indexs_df_i_tuple])

        elif tails == '1l':
            t_critical[indexs_df_i_tuple] = -t.ppf(confidence, df[indexs_df_i_tuple])
        elif tails == '1r':
            t_critical[indexs_df_i_tuple] = t.ppf(confidence, df[indexs_df_i_tuple])

    h = std_err * t_critical

    return h
