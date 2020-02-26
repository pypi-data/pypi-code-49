from threading import Thread


class Hi(Thread):

    def __init__(self, threadID, name, counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        for i in range(0, 10):
            print('Hi')


if __name__ == '__main__':
    print('Nishant')
    t1 = Hi(1,'t1', 10)
    t1.start()
    t1.join()
    print('bye')
