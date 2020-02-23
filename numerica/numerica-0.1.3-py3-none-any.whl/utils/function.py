from functools import partial

def fnx(degree, coefficients, baseExp, x):
  result = 0

  for exp in range(0, degree + 1):
    result += coefficients[exp] * (x ** exp)

  return result ** baseExp

def fnxp(degree, coefficients, baseExp):
  return partial(fnx, degree, coefficients, baseExp)