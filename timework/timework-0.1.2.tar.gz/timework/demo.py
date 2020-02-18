import timework as tw
import logging

r = tw.ResultHandler(5)


@tw.timer(r)
def timer_demo_a():
    i = 0
    while i < 2 ** 23:
        i += 1
    return i


@tw.timer(r, out=print)
def timer_demo_b():
    i = 0
    while i < 2 ** 24:
        i += 1
    return i


@tw.timer(r, out=logging.warning)
def timer_demo_c():
    i = 0
    while i < 2 ** 25:
        i += 1
    return i


@tw.limit(3)
def limit_demo(m):
    i = 0
    while i < 2 ** m:
        i += 1
    return i


@tw.iterative(r, 1)
def iterative_demo_a(max_depth):
    i = 0
    while i < 2 ** max_depth:
        i += 1
    return max_depth, i


timer_demo_a()
timer_demo_b()
timer_demo_c()
print(r.value, end='\n\n')

try:
    s = limit_demo(4)
except Exception as e:
    print(e, end='\n\n')
else:
    print(s)

try:
    s = limit_demo(30)
except Exception as e:
    print(e, end='\n\n')
else:
    print(s)

try:
    r.clear()
    iterative_demo_a(max_depth=10)
except Exception as e:
    print(e)
finally:
    print(r.value, end='\n\n')

try:
    r.clear()
    iterative_demo_a(max_depth=25)
except Exception as e:
    print(e)
finally:
    print(r.value, end='\n\n')
