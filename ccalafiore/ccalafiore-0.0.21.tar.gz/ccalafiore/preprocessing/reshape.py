import numpy as np
from ccalafiore.combinations import n_conditions_to_combinations, conditions_to_combinations
from ccalafiore.array import samples_in_arr1_are_in_arr2


def merge_axes(
        array_input,
        axes_removing_input,
        axis_samples_input,
        dtype=None):

    # Input requirements:
    # 1) axes_removing_input cannot contain same values;
    # 2) variables_inserting_table_output cannot contain same values;
    # 3) shapes of axes_removing_input and variables_inserting_table_output must be equal
    # 4) axes_removing_input[a] != axis_samples_input != axis_variables_table_input

    # Import requirements:
    # 1) import numpy as np
    # 2) from ccalafiore.combinations import n_conditions_to_combinations
    # 3) from ccalafiore.array import samples_in_arr1_are_in_arr2
    # 4) from ccalafiore.array import advanced_indexing

    # from ccalafiore.array import samples_in_arr1_are_in_arr2, advanced_indexing

    # format axes_removing_input
    try:
        n_axes_removing_input = len(axes_removing_input)
        axes_removing_input = np.asarray(axes_removing_input, dtype=int)
    except TypeError:
        axes_removing_input = np.asarray([axes_removing_input], dtype=int)
        n_axes_removing_input = len(axes_removing_input)

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = len(shape_array_input)

    if axis_samples_input < 0:
        axis_samples_input += n_axes_array_input
    axes_removing_input[axes_removing_input < 0] += n_axes_array_input

    # check point 1
    if np.sum(axes_removing_input[0] == axes_removing_input) > 1:
        raise Exception('axes_removing_input cannot contain repeated values')

    # check point 4
    if np.sum(axes_removing_input == axis_samples_input) > 0:
        raise Exception('axes_removing_input[a] != axis_samples_input')

    axes_array_input = np.arange(n_axes_array_input)
    axes_other_array_input = axes_array_input[np.logical_not(samples_in_arr1_are_in_arr2(
        axes_array_input, np.append(axis_samples_input, axes_removing_input)))]

    # axes_other_array_input_inverted = axes_other_array_input[::-1]
    # n_axes_other_array_input = len(axes_other_array_input)

    axis_samples_output = axis_samples_input - np.sum(axes_removing_input < axis_samples_input)

    n_axes_array_output = n_axes_array_input - n_axes_removing_input
    axes_array_output = np.arange(n_axes_array_output)
    axes_other_output = axes_array_output[axes_array_output != axis_samples_output]

    shape_array_output = np.empty(n_axes_array_output, dtype=object)
    n_conditions_in_axes_removing_input = shape_array_input[axes_removing_input]
    shape_array_output[axis_samples_output] = (
            shape_array_input[axis_samples_input] * np.prod(n_conditions_in_axes_removing_input))
    shape_array_output[axes_other_output] = shape_array_input[axes_other_array_input]

    if dtype is None:
        dtype = array_input.dtype
    array_output = np.empty(shape_array_output, dtype=dtype)

    combinations_axes_removing_input = n_conditions_to_combinations(n_conditions_in_axes_removing_input)
    n_combinations_axes_removing_input = combinations_axes_removing_input.shape[0]

    indexes_combinations_removing_input = np.empty(2, dtype=object)
    indexes_combinations_removing_input[:] = slice(None)

    indexes_combinations_removing_output = np.empty(2, dtype=object)
    indexes_combinations_removing_output[:] = slice(None)

    axes_removing_input_inverted = np.sort(axes_removing_input)[::-1]

    # index_input = np.full(n_axes_array_input, slice(None), dtype=object)
    indexes_input = np.empty(n_axes_array_input, dtype=object)
    indexes_input[:] = slice(None)

    index_array_output = np.empty(n_axes_array_output, dtype=object)
    index_array_output[:] = slice(None)

    length_axis_flattering_input = shape_array_input[axis_samples_input]

    start_index_axis_samples_output = 0
    for c in range(n_combinations_axes_removing_input):

        stop_index_axis_samples_output = (c + 1) * length_axis_flattering_input
        index_array_output[axis_samples_output] = slice(
            start_index_axis_samples_output, stop_index_axis_samples_output)
        start_index_axis_samples_output = stop_index_axis_samples_output

        indexes_combinations_removing_input[0] = c
        indexes_input[axes_removing_input] = (
            combinations_axes_removing_input[tuple(indexes_combinations_removing_input)])

        array_output[tuple(index_array_output)] = array_input[tuple(indexes_input)]

    return array_output


def merge_neighbouring_conditions(array_input, axis_1, axis_2, m=3, s=None):
    # axis_1 is (are) the axis (axes) that contains (contain) the merging conditions. it can be
    #        an integer or a list of integers. In case of list of integers, the list cannot contain repeated values.
    # axis_2 is the axis that contains the merging samples of a set of n neighbouring conditions in axis_1.
    #        it is always an integer.
    # m is (are) the number(s) of the merging conditions in axis_1. it is an integer is axis_1 is an integer or
    #        a list of integers if axis_1 is a list of integers. In case of list of int, its size has to be the
    #        same as the size of the axis_1.

    shape_array_input = np.asarray(array_input.shape)
    n_axes_array_input = shape_array_input.size

    # format axes_2
    if axis_2 < 0:
        axis_2 += n_axes_array_input

    # format axes_1
    try:
        n_axis_1 = len(axis_1)
        axis_1 = np.asarray(axis_1, dtype=int)
        axis_1[axis_1 < 0] += n_axes_array_input
        # check point 1
        if np.sum(axis_1[0] == axis_1) > 1:
            raise ValueError('axis_1 cannot contain repeated values')
    except TypeError:
        if axis_1 < 0:
            axis_1 += n_axes_array_input
        axis_1 = np.asarray([axis_1], dtype=int)
        n_axis_1 = 1

    # format m
    try:
        n_m = len(m)
        if n_m == n_axis_1:
            m = np.asarray(m, dtype=int)
        elif n_m == 1:
            m_tmp = m[0]
            m = np.empty(n_axis_1, dtype=int)
            m[:] = m_tmp
            n_s = n_axis_1
        else:
            # check point 3
            raise ValueError('sizes of axis_1 and m must be equal')
    except TypeError:
        m_tmp = m
        m = np.empty(n_axis_1, dtype=int)
        m[:] = m_tmp
        n_m = n_axis_1

    # format s
    if s is None:
        s = m
    else:
        try:
            n_s = len(s)
            if n_s == n_axis_1:
                s = np.asarray(s, dtype=int)
                for a in range(n_axis_1):
                    if s[a] is None:
                        s[a] = m[a]
            elif n_s == 1:
                s_tmp = s[0]
                if s_tmp is None:
                    s = m
                else:
                    s = np.empty(n_axis_1, dtype=int)
                    s[:] = s_tmp
                n_s = n_axis_1
            else:
                # check point 3
                raise ValueError('sizes of axis_1 and s must be equal')
        except TypeError:
            s_tmp = s
            s = np.empty(n_axis_1, dtype=int)
            s[:] = s_tmp
            n_s = n_axis_1

    r_1 = m // 2
    r_0 = r_1
    m_even = (m % 2) == 0
    if any(m_even):
        r_0[m_even] -= 1

    n_conditions_input = shape_array_input[axis_1]
    n_samples_per_condition_input = shape_array_input[axis_2]

    n_conditions_output = ((n_conditions_input - m) // s) + 1
    n_samples_per_m_conditions_output = n_samples_per_condition_input * np.prod(m)

    shape_array_output = shape_array_input
    shape_array_output[axis_1] = n_conditions_output
    shape_array_output[axis_2] = n_samples_per_m_conditions_output
    array_output = np.empty(shape_array_output, dtype=array_input.dtype)

    index_input = np.empty(n_axes_array_input, dtype=object)
    index_input[:] = slice(None)
    index_output = np.copy(index_input)

    center = np.empty(n_axis_1, dtype=object)
    for a in range(n_axis_1):
        center[a] = np.arange(r_0[a], n_conditions_input[a] - r_1[a], s[a])
    combinations_centers = conditions_to_combinations(center)
    n_combinations_centers = combinations_centers.shape[0]

    combinations_merged_conditions_output = n_conditions_to_combinations(n_conditions_output)
    for i in range(n_combinations_centers):
        for a in range(n_axis_1):
            index_input[axis_1[a]] = slice(combinations_centers[i, a] - r_0[a], combinations_centers[i, a] + r_1[a] + 1)
        index_output[axis_1] = combinations_merged_conditions_output[i]

        array_output[tuple(index_output)] = merge_axes(array_input[tuple(index_input)], axis_1, axis_2)

    return array_output
