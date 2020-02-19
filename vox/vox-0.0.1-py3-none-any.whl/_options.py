import nox._options


def get_options():
    return nox._options.options.parse_args()
