root = 48  # C3

major_pattern = [2, 2, 1, 2, 2, 2, 1]
minor_pattern = [2, 1, 2, 2, 1, 2, 2]


def generate_scale(transpose=0, minor=False):
    scale = [root + transpose]
    step_pattern = minor_pattern if minor else major_pattern

    # Get us a few octaves of range
    for _ in range(3):
        for interval in step_pattern:
            scale.append(scale[-1] + interval)

    return scale
