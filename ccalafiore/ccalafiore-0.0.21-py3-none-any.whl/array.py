import numpy as np
from ccalafiore.combinations import n_conditions_to_combinations
from glob import glob
import numbers
from math import ceil


def advanced_indexing(indexes_loose):
    def clean_input_of_ix_(indexes_loose):
        n_axes = len(indexes_loose)
        for a in range(n_axes):
            try:
                len(indexes_loose[a])
            except TypeError:
                indexes_loose[a] = np.asarray([indexes_loose[a]], dtype=int)
        return indexes_loose

    indexes_loose = clean_input_of_ix_(indexes_loose)
    indexes = np.ix_(*indexes_loose)
    return indexes


def samples_in_arr1_are_in_arr2(arr1, arr2, axis=0):

    # OLD elements_in_x_are_in_y()

    arr1, arr2 = make_sure_is_iterable(arr1, arr2)

    arr1 = np.array(arr1)
    type_arr1 = arr1.dtype
    if type_arr1 == object:
        arr2 = np.array(list(arr1))

    arr2 = np.array(arr2)
    type_arr2 = arr2.dtype
    if type_arr2 == object:
        arr2 = np.array(list(arr2))

    shape_arr1 = np.array(arr1.shape)
    shape_arr2 = np.array(arr2.shape)

    n_axes_arr1 = len(shape_arr1)
    n_axes_arr2 = len(shape_arr2)
    if n_axes_arr1 != n_axes_arr2:

        if n_axes_arr1 == n_axes_arr2 - 1:

            arr1 = np.expand_dims(arr1, axis=axis)
            shape_arr1 = np.array(arr1.shape)
            n_axes_arr1 = len(shape_arr1)

        else:
            raise Exception('n_axes_arr1 has to be equal to n_axes_arr2\n'
                            'or to n_axes_arr2 - 1.\n'
                            'Now, n_axes_arr1 = {} and n_axes_arr2 = {}.'.format(
                n_axes_arr1, n_axes_arr2))

    axes_arr1_and_arr2 = np.arange(n_axes_arr1)

    if np.all(axis != axes_arr1_and_arr2):
        raise Exception('axis_1 is not in the axes_arr1_and_arr2.\n'
                        'axis_1 has to be equal to either one of the\n'
                        'axes_arr1_and_arr2.\n'
                        'Now, axis_1 = {} and axes_arr1_and_arr2 = {}.\n'
                        'By default, axis_1=0.'.format(
                         axis, axes_arr1_and_arr2))

    n_samples_arr1 = shape_arr1[axis]
    n_samples_arr2 = shape_arr2[axis]

    axes_within_samples = np.argwhere(axes_arr1_and_arr2 != axis)[:, 0]
    # dimensions_within_samples = dimensions_within_samples.astype(int)

    shape_1_sample_arr1 = shape_arr1[axes_within_samples]
    shape_1_sample_arr2 = shape_arr2[axes_within_samples]
    if np.any(shape_1_sample_arr1 != shape_1_sample_arr2):

        raise Exception('shape_1_sample_arr1 has to be equal to shape_1_sample_arr2.\n'
                        'Now,shape_1_sample_arr1 = {} and shape_1_samples_arr2 = {}.'.format(
            shape_1_sample_arr1, shape_1_sample_arr2))

    shape_arr_logical = np.copy(shape_arr2)
    shape_arr_logical = np.insert(shape_arr_logical, axis, shape_arr1[axis], axis=0)
    n_axes_arr_logical = len(shape_arr_logical)
    arr_logical = np.empty(shape_arr_logical, dtype=bool)

    indexes_arr1 = np.full(n_axes_arr1, slice(None))
    indexes_arr_logical = np.full(n_axes_arr_logical, slice(None))

    # indexes_arr1 = np.empty(n_dimensions_arr1, dtype=object)
    # indexes_arr_logical = np.empty(n_dimensions_arr_logical, dtype=object)
    # for i_dimension in range(n_dimensions_arr_logical):
    #     if i_dimension != axis_1:
    #         # indexes_samples_i_window.append(slice(0, n_samples_window))
    #     #     indexes_arr1[i_dimension] = np.arange([0])
    #     # else:
    #         indexes_arr_logical[i_dimension] = np.arange(shape_arr_logical[i_dimension])
    #         if i_dimension < n_dimensions_arr1:
    #             indexes_arr1[i_dimension] = np.arange(shape_arr1[i_dimension])

    for i_sample in range(n_samples_arr1):
        indexes_arr1[axis] = i_sample
        indexes_arr_logical[axis] = i_sample
        arr_logical[tuple(indexes_arr_logical)] = arr1[tuple(indexes_arr1)] == arr2

    elements_of_arr1_in_arr2_logical = np.any(arr_logical, axis=axis + 1)

    return elements_of_arr1_in_arr2_logical


def make_sure_is_iterable(*variables, if_not_iterable_convert_2_type_variable=np.ndarray):
    # list_types_iterable_allowed = [list, tuple, np.ndarray, str]

    # n_types_iterable_allowed = len(list_types_iterable_allowed)
    # if n_types_iterable_allowed == 1:
    #     if_not_iterable_convert_2_type_variable = list_types_iterable_allowed[0]
    # else:
    #     if if_not_iterable_convert_2_type_variable not in list_types_iterable_allowed:
    #         raise Exception(
    #             'if_not_iterable_convert_2_type_variable is not in list_types_iterable_allowed.\n'
    #             'Now, if_not_iterable_convert_2_type_variable = {} and list_types_iterable_allowed = {}.\n'
    #             'By default, make_sure_is_iterable(*variables, list_types_iterable_allowed=[list, tuple, np.ndarray],\n'
    #             'if_not_iterable_convert_2_type_variable=np.ndarray)'.format(
    #                 if_not_iterable_convert_2_type_variable, list_types_iterable_allowed))

    variables = list(variables)
    n_variables = len(variables)

    for i in range(n_variables):

        try:
            len(variables[i])

        except TypeError:

            if if_not_iterable_convert_2_type_variable == str:
                variables[i] = str(variables[i])

            else:
                variables[i] = [variables[i]]

                if if_not_iterable_convert_2_type_variable == list:
                    variables[i] = list(variables[i])

                elif if_not_iterable_convert_2_type_variable == tuple:
                    variables[i] = tuple(variables[i])

                elif if_not_iterable_convert_2_type_variable == np.ndarray:
                    variables[i] = np.array(variables[i])
                else:
                    raise Exception(
                        'if_not_iterable_convert_2_type_variable has to either be equal to np.ndarray, list, tuple or str.\n'
                        'Now, if_not_iterable_convert_2_type_variable = {}.\n'
                        'By default, if_not_iterable_convert_2_type_variable=np.ndarray'.format(
                            if_not_iterable_convert_2_type_variable))

        # type_i_variable = type(variables[i])
        #
        # # if type_i_variable not in list_types_iterable_allowed:
        #     if if_not_iterable_convert_2_type_variable == list:
        #         variables[i] = list([variables[i]])
        #
        #     elif if_not_iterable_convert_2_type_variable == tuple:
        #         variables[i] = tuple([variables[i]])
        #
        #     elif if_not_iterable_convert_2_type_variable == np.ndarray:
        #         variables[i] = np.array([variables[i]])
        #     else:
        #         raise Exception(
        #             'if_not_iterable_convert_2_type_variable has to either be equal to np.ndarray, list or tuple.\n'
        #             'Now, if_not_iterable_convert_2_type_variable = {}.\n'
        #             'By default, if_not_iterable_convert_2_type_variable=np.ndarray'.format(
        #                 if_not_iterable_convert_2_type_variable))

        # elif type_i_variable == np.ndarray:
        #     if variables[i].ndim == 0:
        #         variables[i] = np.array([variables[i]])

    if n_variables == 1:
        return variables[0]
    else:
        return variables


def transfer_n_random_samples_from_arr1_to_arr2(arr1, arr2, n_samples=1, axis=0, replace=False):
    # def transfer_n_random_samples_from_arr1_to_arr2(arr1, arr2, first_n_samples=1, all=False):

    # SPLIT THIS IN TWO FUNCTIONS:
    # 1) transfer_n_random_samples_from_arr1_to_arr2;
    # 2) transfer_n_samples_from_arr1_to_arr2;

    arr1, arr2 = make_sure_is_iterable(arr1, arr2)


    shape_arr1 = np.array(arr1.shape)
    shape_arr2 = np.array(arr2.shape)

    n_dimensions_arr1 = len(shape_arr1)
    n_dimensions_arr2 = len(shape_arr2)
    if n_dimensions_arr1 != n_dimensions_arr2:

        if n_dimensions_arr1 == n_dimensions_arr2 - 1:

            arr1 = np.expand_dims(arr1, axis=axis)
            shape_arr1 = np.array(arr1.shape)
            n_dimensions_arr1 = len(shape_arr1)

        else:
            raise Exception('n_dimensions_arr1 has to be equal to n_dimensions_arr2\n'
                            'or to n_dimensions_arr2 - 1.\n'
                            'Now, n_dimensions_arr1 = {} and n_dimensions_arr2 = {}.'.format(
                n_dimensions_arr1, n_dimensions_arr2))

    dimensions_arr1_and_arr2 = np.arange(n_dimensions_arr1)

    if np.all(axis != dimensions_arr1_and_arr2):
        raise Exception('axis is not in the dimensions_arr1_and_arr2.\n'
                        'axis has to be equal to either one ot the\n'
                        'dimensions_arr1_and_arr2.\n'
                        'Now, axis = {} and dimensions_arr1_and_arr2 = {}.\n'
                        'By default, axis=0.'.format(
            axis, dimensions_arr1_and_arr2))

    n_samples_arr1 = shape_arr1[axis]
    n_samples_arr2 = shape_arr2[axis]
    if n_samples > n_samples_arr1 and replace is False:
        raise Exception('n_samples cannot be greater than n_samples of arr1, when replace=False.\n'
                        'Now, n_samples = {}, n_samples_arr1 = {} and replace = {}.'.format(
            n_samples, n_samples_arr1, replace))


    dimensions_within_samples = np.argwhere(dimensions_arr1_and_arr2 != axis)[:, 0]
    # dimensions_within_samples = dimensions_within_samples.astype(int)

    shape_1_sample_arr1 = shape_arr1[dimensions_within_samples]
    shape_1_sample_arr2 = shape_arr2[dimensions_within_samples]
    if np.any(shape_1_sample_arr1 != shape_1_sample_arr2):

        raise Exception('shape_1_sample_arr1 has to be equal to shape_1_sample_arr2.\n'
                        'Now,shape_1_sample_arr1 = {} and shape_1_samples_arr2 = {}.'.format(
            shape_1_sample_arr1, shape_1_sample_arr2))

    indexes_chosen_samples_in_arr1 = np.random.choice(n_samples_arr1, n_samples, replace=replace)

    indexes = np.empty(n_dimensions_arr1, dtype=object)
    for i_d in range(n_dimensions_arr1):
        if i_d == axis:
            # indexes_samples_i_window.append(slice(0, n_samples_window))
            indexes[i_d] = indexes_chosen_samples_in_arr1
        else:
            indexes[i_d] = np.arange(shape_arr1[i_d])

    # if n_dimensions_arr1 == 1:
    #     chosen_sample_in_arr1 = arr1[np.ix_(indexes)]
    # else:
    chosen_sample_in_arr1 = arr1[np.ix_(*indexes)]

    arr2 = np.append(arr2, chosen_sample_in_arr1)

    arr1 = np.delete(arr1, indexes_chosen_samples_in_arr1, axis=axis)
    # indexes_chosen_sample_in_arr1 = np.argwhere(arr1 == chosen_sample_in_arr1)[0]

    # n_chosen_samples_in_arr1 = len(indexes_chosen_sample_in_arr1)
    # if all:
    #
    # elif n_chosen_samples_in_arr1 <= first_n_samples:
    #     indexes_chosen_sample_in_arr1 = indexes_chosen_sample_in_arr1[np.arange(n_chosen_samples_in_arr1)]
    #
    # elif n_chosen_samples_in_arr1 > first_n_samples:
    #     indexes_chosen_sample_in_arr1 = indexes_chosen_sample_in_arr1[np.arange(first_n_samples)]

    # arr1 = np.delete(arr1, indexes_chosen_sample_in_arr1)

    return arr1, arr2


def shuffle_in_windows(data, n_samples_window=None, n_windows=None, dimension_shuffle=0):

    type_data = type(data)
    if type_data != np.ndarray:
        raise Exception('data must be an numpy array. '
                        'Now, the class of data is {}'.format(type_data))


    dimension_shuffle_is_integer = isinstance(dimension_shuffle, numbers.Integral)
    # The Numeric abstract base classes:
    # numbers.Complex
    # numbers.Real
    # numbers.Integral
    # numbers.Number
    if not dimension_shuffle_is_integer:
        type_dimension_shuffle = type(dimension_shuffle)
        raise Exception('dimension_shuffle must be an integer. '
                        'Now, the class of dimension_shuffle is {}'.format(
            type_dimension_shuffle))

    shape_data = data.shape
    n_samples_data = shape_data[dimension_shuffle]
    n_d_data = len(shape_data)
    if dimension_shuffle > n_d_data:
        raise Exception('shuffle in dimension {} can\'t be done,\n'
                        'because data has {} dimensions and\n'
                        'it doesn\'t have the {}th dimension.\n'
                        'dimension_shuffle has to be an integer in the interval\n'
                        '0 =< dimension_shuffle < n_d_data.\n'
                        'In this case, dimension_shuffle = {} and n_d_data = {}'.format(
            dimension_shuffle, n_d_data, dimension_shuffle, dimension_shuffle, n_d_data))


    n_samples_window_is_integer = isinstance(n_samples_window, numbers.Integral)

    if n_windows is None and not n_samples_window_is_integer:
        type_n_samples_window = type(n_samples_window)
        raise Exception('n_samples_window must be an integer. '
                        'Now, the class of n_samples_window is {}'.format(
            type_n_samples_window))

    n_windows_is_integer = isinstance(n_windows, numbers.Integral)
    if n_samples_window is None and not n_windows_is_integer:
        type_n_windows = type(n_windows)
        raise Exception('n_windows must be an integer. '
                        'Now, the class of n_windows is {}'.format(
            type_n_windows))

    if n_samples_window is None and n_windows is None:
        raise Exception('Both n_samples_window and n_windows are None.'
                        'Define only one of them with an integer.'
                        'One of them has to be None and the other one has to be an integer')

    if n_samples_window is None and n_windows_is_integer:
        n_samples_window = ceil(n_samples_data / n_windows)

    if n_windows is None and n_samples_window_is_integer:
        n_windows = ceil(n_samples_data / n_samples_window)

    if n_samples_window_is_integer and n_windows_is_integer:

        tmp_n_samples_window = ceil(n_samples_data / n_windows)
        tmp_n_windows = ceil(n_samples_data / n_samples_window)

        if tmp_n_samples_window != n_samples_window and tmp_n_windows != n_windows:

            raise Exception('For n_samples_data = {}, n_samples_window = {} and n_windows = {} are not compatible.\n'
                            'If n_samples_window = {}, n_windows has to be {} or None.\n'
                            'If n_windows = {}, n_samples_window has to be {} or None'.format(
                n_samples_data, n_samples_window, n_windows, n_samples_window, tmp_n_windows, n_windows, tmp_n_samples_window))




    if n_samples_window * n_windows > n_samples_data:
        print('Warning: n_samples_window * n_windows > n_samples_data.\n'
              'n_samples_window * n_windows = {} and n_samples_data = {}'.format(
            n_samples_window * n_windows, n_samples_data))

    indexes_samples_i_window = np.empty(n_d_data, dtype=object)
    for i_d in range(n_d_data):
        if i_d == dimension_shuffle:
            # indexes_samples_i_window.append(slice(0, n_samples_window))
            indexes_samples_i_window[i_d] = np.arange(n_samples_window)
        else:
            indexes_samples_i_window[i_d] = np.arange(shape_data[i_d])

    # indexes_samples_i_window = np.array(indexes_samples_i_window)
    # indexes_samples_i_window[dimension_shuffle] = indexes_samples_i_window[dimension_shuffle][indexes_samples_i_window[dimension_shuffle] < n_samples_data]
    # indexes_samples_i_window_tuple = np.ix_(*indexes_samples_i_window)

    tmp_shape_data_shuffle = list(shape_data)
    tmp_shape_data_shuffle[dimension_shuffle] = 0
    dtype_data = data.dtype
    # data_shuffle = np.empty(tmp_shape_data_shuffle, dtype=dtype_data)
    data_shuffle = np.empty(shape_data, dtype=dtype_data)

    for i_window in range(n_windows):

        indexes_samples_i_window[dimension_shuffle] = indexes_samples_i_window[dimension_shuffle][indexes_samples_i_window[dimension_shuffle] < n_samples_data]
        # indexes_samples_i_window = np.arange(n_samples_window * i_window, n_samples_window * (i_window + 1))

        # indexes_samples_i_window = indexes_samples_i_window[indexes_samples_i_window < n_samples_data]
        # index_tuple = tuple(index)
        # index[dimension_shuffle] = start_i_window
        # data = np.arange(6*6*6).reshape(6, 6, 6)
        # i = np.ix_(*[[1, 3], [1, 3, 5], [0, 1, 3, 5]])
        # if n_d_data == 1:
        #     samples_i_window = data[np.ix_(indexes_samples_i_window)]
        # else:
        indexes_samples_i_window_tuple = np.ix_(*indexes_samples_i_window)
            # samples_i_window = data[np.ix_(indexes_samples_i_window_tuple)]
        samples_i_window = data[indexes_samples_i_window_tuple]
            # samples_i_window = np.take(data, indexes_samples_i_window, axis=dimension_shuffle)

        samples_i_window = shuffle_in_any_dimension(samples_i_window, dimension_shuffle=dimension_shuffle)
        # data_shuffle = np.append(data_shuffle, samples_i_window, axis=dimension_shuffle)
        data_shuffle[indexes_samples_i_window_tuple] = samples_i_window

        # indexes_samples_i_window = np.array(indexes_samples_i_window_tuple)
        # indexes_samples_i_window[dimension_shuffle] += n_samples_window
        # indexes_samples_i_window[dimension_shuffle] = indexes_samples_i_window[dimension_shuffle][indexes_samples_i_window[dimension_shuffle] < n_samples_data]
        # indexes_samples_i_window_tuple = tuple(indexes_samples_i_window)

        if i_window < n_windows - 1:
            indexes_samples_i_window[dimension_shuffle] += n_samples_window


    return data_shuffle


def shuffle_in_any_dimension(data, axis=0):

    type_data = type(data)
    if type_data != np.ndarray:
        raise Exception('data must be an numpy array. '
                        'Now, the class of data is {}'.format(type_data))

    dimension_shuffle_is_integer = isinstance(axis, numbers.Integral)
    if not dimension_shuffle_is_integer:
        type_dimension_shuffle = type(axis)
        raise Exception('dimension_shuffle must be an integer. '
                        'Now, the class of dimension_shuffle is {}'.format(
            type_dimension_shuffle))

    shape_data = data.shape
    n_samples = shape_data[axis]
    n_axes = len(shape_data)

    if axis > n_axes:
        raise Exception('shuffle in axis {} can\'t be done,\n'
                        'because data has {} axes and\n'
                        'it doesn\'t have the {}th axis.\n'
                        'axis has to be an integer in the interval\n'
                        '0 =< axis < n_axes.\n'
                        'In this case, axis = {} and n_axes = {}'.format(
            axis, n_axes, axis, axis, n_axes))


    indexes_new = np.empty(n_axes, dtype=object)
    for a in range(n_axes):
        if a == axis:
            # indexes_samples_i_window.append(slice(0, n_samples_window))
            indexes_new[a] = np.random.rand(n_samples).argsort()
        else:
            indexes_new[a] = np.arange(shape_data[a])

    # indexes_new = []
    # for i_d in range(n_d_data):
    #     if i_d == dimension_shuffle:
    #         # indexes_samples_i_window.append(slice(0, n_samples_window))
    #         indexes_new.append(np.random.rand(n_samples).argsort())
    #     else:
    #         indexes_new.append(np.arange(0, shape_data[i_d]))
    #
    # indexes_new = np.array(indexes_new)

    # indexes_new = np.random.rand(n_samples).argsort()
    # data_shuffle = np.take(data, indexes_new, axis=dimension_shuffle, out=data)
    # if n_d_data == 1:
    #     data_shuffle = data[np.ix_(indexes_new)]
    #
    # else:
    data_shuffle = data[advanced_indexing(indexes_new)]

    return data_shuffle


def n_csv_files_to_array(directories_csv_files, names_csv_files_in_directories=False, rows=slice(None), columns=slice(None), data_type=None):

    array = None

    n_axes_directories = len(directories_csv_files)
    n_conditions_directories = np.empty(n_axes_directories, dtype=int)
    for a in range(n_axes_directories):
        n_conditions_directories[a] = len(directories_csv_files[a])

    logical_indexes_conditions = n_conditions_directories > 1

    combinations_directories = n_conditions_to_combinations(n_conditions_directories)
    n_combinations_directories = combinations_directories.shape[0]

    for d in range(n_combinations_directories):

        directory = directories_csv_files[0][combinations_directories[d, 0]]
        for a in range(1, n_axes_directories):

            directory = '/'.join([
                directory,
                directories_csv_files[a][combinations_directories[d, a]]
            ])

        if names_csv_files_in_directories:
            files_per_directory = [directory]
        else:
            files_per_directory = glob('/'.join([directory, '*.csv']))

        n_files_per_directory = len(files_per_directory)

        start_row_f_file = 0
        for f in range(n_files_per_directory):

            array_per_file = np.genfromtxt(files_per_directory[f], delimiter=',', dtype=data_type)[rows, columns]

            if array is None:

                shape_array_per_file = np.asarray(array_per_file.shape, dtype=int)

                shape_array = np.asarray([
                    *n_conditions_directories[logical_indexes_conditions],
                    n_files_per_directory * shape_array_per_file[0],
                    *shape_array_per_file[1:]
                ], dtype=int)

                array = np.empty(shape_array, dtype=data_type)

            end_row_f_file = (f + 1) * shape_array_per_file[0]

            indexes_array = tuple([
                *combinations_directories[d][logical_indexes_conditions],
                slice(start_row_f_file, end_row_f_file)
            ])

            array[indexes_array] = array_per_file
            start_row_f_file = end_row_f_file

    return array


def split(array, n_slices, axis=0):

    shape_array = np.array(array.shape)

    n_dimensions_array = len(shape_array)

    indexes = np.empty(n_dimensions_array, dtype=object)

    for i_d in range(n_dimensions_array):
        if i_d != axis:

            indexes[i_d] = slice(None)

    # indexes_samples_i_window.append(slice(0, n_samples_window))

    n_elements_array = shape_array[axis]

    n_elements_slice = n_elements_array / n_slices

    sliced_array = np.empty(n_slices, dtype=object)

    index_start = 0
    for i_slice in range(n_slices):

        index_stop = int((i_slice + 1) * n_elements_slice)

        indexes[axis] = slice(index_start, index_stop)

        # sliced_array[i_slice] = array[int(i_slice * n_elements_slice): int((i_slice + 1) * n_elements_slice)]
        sliced_array[i_slice] = array[tuple(indexes)]

        index_start = index_stop

    return sliced_array


def pad_array_from_n_samples_target(array, n_samples_target=1, axis=0):

    try:
        len(array)
        array = np.asarray(array)
    except TypeError:
        array = np.asarray([array])

    shape_array = np.asarray(array.shape)
    n_axes = len(shape_array)
    while n_axes <= axis:
        array = np.expand_dims(array, axis=n_axes)
        shape_array = np.asarray(array.shape)
        n_axes = len(shape_array)

    n_samples_true = shape_array[axis]
    while n_samples_true < n_samples_target:
        array = np.append(array, array, axis=axis)
        n_samples_true = array.shape[axis]

    index_array = np.full(n_axes, slice(None))
    index_array[axis] = slice(n_samples_target)
    array = array[tuple(index_array)]

    return array


def pad_arr_1_from_arr_2(arr_1, arr_2, axis=0):

    try:
        len(arr_1)
        arr_1 = np.asarray(arr_1)
    except TypeError:
        arr_1 = np.asarray([arr_1])

    try:
        len(arr_2)
        arr_2 = np.asarray(arr_2)
    except TypeError:
        arr_2 = np.asarray([arr_2])

    shape_arr_1 = np.asarray(arr_1.shape)
    n_axes_1 = len(shape_arr_1)
    shape_arr_2 = np.asarray(arr_2.shape)
    n_axes_2 = len(shape_arr_2)

    if n_axes_1 == n_axes_2 - 1:
        arr_1 = np.expand_dims(arr_1, axis=axis)
        shape_arr_1 = np.asarray(arr_1.shape)
        n_axes_1 = len(shape_arr_1)
    elif n_axes_1 == n_axes_2:
        pass
    else:
        raise Exception('dimensions of arr_1 and arr_2 do not match')

    if np.all(shape_arr_1[np.arange(n_axes_1) != axis] == shape_arr_2[np.arange(n_axes_2) != axis]):
        pass
    else:
        raise Exception('dimensions of arr_1 and arr_2 do not match')

    n_samples_true = shape_arr_1[axis]
    n_samples_target = shape_arr_2[axis]

    while n_samples_true < n_samples_target:
        arr_1 = np.append(arr_1, arr_1, axis=axis)
        n_samples_true = arr_1.shape[axis]

    index_arr_1 = np.full(n_axes_1, slice(None))
    index_arr_1[axis] = slice(n_samples_target)

    arr_1 = arr_1[tuple(index_arr_1)]

    return arr_1
