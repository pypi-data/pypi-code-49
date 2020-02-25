import scalene

def foo():
    x = 1.0
    for i in range(1000):
        for j in range(1000):
            x *= 1.1
    return x

prof = scalene.Scalene
with prof.scalene_profiler():
    foo()

print("WOOT")
