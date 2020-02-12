import inspect


def get_defaults(func):
    args, varargs, keywords, defaults = inspect.getargspec(func)
    return dict(zip(args[-len(defaults):], defaults))

test_name = 1.0           # Pa
BAR = 1.0e5         # Pa
PSI = 6894.76       # Pa
in_h2o = 248.84    # Pa

# Velocity: used to convert values to base units of m/s
KPH = 2.77778e-1    # m/s
MPH = 4.44704e-1    # m/s

# length:
INCHES  = 2.54e-1       # m

totally_new = 200.00

