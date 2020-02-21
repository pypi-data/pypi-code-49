from functools import partial
from operator import mul


def rev(s):
    return ''.join(reversed(s))


def oper(f, x, y):
    return f(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return oper(mul, x, y)
    # return x * y


def div(x, y):
    return x / y


def just(t, n):
    return str(t).rjust(n)


print(rev('Hello World'))

end = 13
for m, f in [(m, partial(mult, m)) for m in range(1, end)]:
    for n in range(1, end):
        print(f'{just(m, 2)} * {just(n, 2)} = {just(f(n), 3)}')


