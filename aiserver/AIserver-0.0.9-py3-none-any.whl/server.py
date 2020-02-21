from AIserver import test
sd = test.test()


def left(step):
    s = 10*step
    sd.move(s)
    print("向左转")

