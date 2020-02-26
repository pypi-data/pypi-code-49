import matplotlib.pyplot as plt

from testpython.RandomWalk import RandomWalk

for i in range(1, 2):
    rw = RandomWalk()
    rw.fill_walk()
    pointnumbers = list(range(rw.num_points))
    # print(pointnumbers)
    plt.scatter(rw.xvalues, rw.yvalues, c=pointnumbers,
                cmap=plt.cm.Blues, s=15)
    plt.show()
