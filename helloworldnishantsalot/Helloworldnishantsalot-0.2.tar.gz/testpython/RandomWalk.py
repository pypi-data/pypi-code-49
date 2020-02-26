from random import choice

class RandomWalk():
    """A lass to generate random walk """

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.xvalues =[0]
        self.yvalues=[0]

    def fill_walk(self):
        while len(self.xvalues) < self.num_points:
            xdirection = choice([1,-1])
            xdistance = choice([0,1,2,3,4])
            xstep = xdirection * xdistance

            ydirection = choice([1,-1])
            ydistance = choice([0,1,2,3,4])
            ystep = ydirection * ydistance

            if xstep == 0 and ystep == 0:
                continue

            nextx = self.xvalues[-1] + xstep
            nexty = self.yvalues[-1] + ystep

            self.xvalues.append(nextx)
            self.yvalues.append(nexty)
