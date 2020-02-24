from datetime import datetime


_unit_seconds = 'seconds'
_unit_minutes = 'minutes'
_unit_hours = 'hours'

_time_units = {0: _unit_seconds,
               1: _unit_minutes,
               2: _unit_hours,
               }

_reverse_time_units = dict((v, k) for k, v in _time_units.items())

_default_datetime_format = '%Y_%m_%d_%H_%M_%S'  # to add in milliseconds, add %f


def array_of_str_to_array_of_datetime_objects(list_of_string_values,
                                              datetime_format: str =_default_datetime_format,
                                              ):
    """
    Convert a list of string values, back into datetime objects with a specific format; in this case, the string has
    to have been a datetime object that was converted into a string with the datetime_format that is passed in this
    function.

    Main use has previously been when files where timestamped, and when the file names need to be converted back into
    datetime objects in order to do calculations

    :param list_of_string_values:
    :param str, datetime_format: a string to represent the datetime format the string should be converted into; it
        should also have been the format that the strings already are in
    :return:
    """
    array_of_datetime_objects = []
    for value in list_of_string_values:
        datetime_object = datetime.strptime(value, datetime_format)
        array_of_datetime_objects.append(datetime_object)
    return array_of_datetime_objects


def array_of_datetime_objects_to_array_of_relative_datetime_objects(array_of_datetime_objects,
                                                                    units,
                                                                    ):
    """
    Convert an array of datetime objects that are absolute times, and return an array where all the times in the
    array are relative to the first time in the array. The relativity can be in secons, minutes, or hours.

    :param array_of_datetime_objects:
    :param units: one of _unit_seconds, _unit_minutes, or _unit_hours, which are defined in this datetime_utils module
    :return:
    """
    # takes a list of datetime objects, and makes all the values relative to the first object in the list as the
    # 0 points. units must be one of the _time_units types (_unit_seconds, _unit_minutes, or _unit_hours)

    # make an array of timedelta objects where each value is the difference between the actual time relative to
    # the first time point
    array_of_datetime_timedelta = [datetime_value - array_of_datetime_objects[0] for datetime_value in
                                   array_of_datetime_objects]

    # convert the relative timedeltas to floats, where the float number is the number of seconds since the first
    # time point
    array_of_relative_x_in_seconds = [array_of_datetime_timedelta[index].total_seconds() for index
                                      in range(len(array_of_datetime_timedelta))]

    if units == _unit_seconds:
        array_of_relative_datetime_objects = array_of_relative_x_in_seconds
    elif units == _unit_minutes:
        array_of_relative_x_in_minutes = [array_of_relative_x_in_seconds[index] / 60.0 for index in
                                          range(len(array_of_relative_x_in_seconds))]
        array_of_relative_datetime_objects = array_of_relative_x_in_minutes
    elif units == _unit_hours:
        array_of_relative_x_in_hours = [array_of_relative_x_in_seconds[index] / 3600.0 for index in
                                        range(len(array_of_relative_x_in_seconds))]
        array_of_relative_datetime_objects = array_of_relative_x_in_hours

    return array_of_relative_datetime_objects

