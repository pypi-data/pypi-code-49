import timework as tw
import logging


@tw.timer(logging.warning)
def timer_demo_a():
    i = 0
    while i < 2 ** 23:
        i += 1
    return i


@tw.timer(print, detail=True)
def timer_demo_b():
    i = 0
    while i < 2 ** 24:
        i += 1
    return i


@tw.timer(timeout=1)
def timer_demo_c():
    i = 0
    while i < 2 ** 25:
        i += 1
    return i


a = timer_demo_a()
b = timer_demo_b()
try:
    c = timer_demo_c()
except tw.TimeError as e:
    print('error:', e.message)
    c = e.result
print(a, b, c)


@tw.limit(3)
def limit_demo(m):
    i = 0
    while i < 2 ** m:
        i += 1
    return i


try:
    s = limit_demo(4)
except tw.TimeError as e:
    print(e)
else:
    print('result:', s)

try:
    s = limit_demo(30)
except tw.TimeError as e:
    print(e)
else:
    print('result:', s)


@tw.iterative(3)
def iterative_demo_a(max_depth):
    i = 0
    while i < 2 ** max_depth:
        i += 1
    return max_depth, i


@tw.iterative(3, history=5, key='depth')
def iterative_demo_b(depth):
    i = 0
    while i < 2 ** depth:
        i += 1
    return depth


try:
    s = iterative_demo_a(max_depth=10)
except tw.TimeError as e:
    print(e.message)
    print(e.result, e.detail)
else:
    print('result:', s)

try:
    s = iterative_demo_a(max_depth=25)
except tw.TimeError as e:
    print(e.message)
    print(e.result, e.detail)
else:
    print('result:', s)

try:
    s = iterative_demo_b(depth=25)
except tw.TimeError as e:
    print(e.message)
    print(e.result, e.detail)
else:
    print('result:', s)
