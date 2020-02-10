def remap_range(value, actual_min, actual_max, new_min, new_max):
    actual_span = actual_max - actual_min
    new_span = new_max - new_min
    value_scaled = float(value - actual_min) / float(actual_span)
    return int(new_min + (value_scaled * new_span))