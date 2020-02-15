import math


def cnpk(k, n):
    k = int(k)
    n = int(n)
    res = 1
    for u in range(n, n - k, -1):
        res *= u
    res //= math.factorial(k)
    return res


def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    y, x, gcd = exgcd(b, a % b)
    return x, y - (a // b) * x, gcd


def is_less(a, b, can_be_equal):
    if a < b:
        return True
    return can_be_equal and a == b


def addition(a, b, c):
    a = 0 if a is None else a
    return a + b * c
