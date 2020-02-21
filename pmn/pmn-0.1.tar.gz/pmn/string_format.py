def left_fit(string: str, fit_size: int):
    return string.ljust(fit_size)[:fit_size]


def right_fit(string: str, fit_size: int):
    return string.rjust(fit_size)[-fit_size:]
