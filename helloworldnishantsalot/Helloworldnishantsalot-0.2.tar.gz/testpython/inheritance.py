import math
import os
import random
import re
import sys

from typing import Type


class Mammal:
    n = "name"

    def __init__(self, mtype=''):
        self.mtype = mtype
        print(self.mtype)

    def walk(self):
        print("walk")
        print(self.mtype)


class Dog(Mammal):
    def walk(self):
        print("dog walk")





class Cat:
    x = 'nishant'
    def annoying(self):

        print(Cat.x)
        print("annoying")

    def walk(self):
        print("cat walk")


def met(m: Type[str]):
    m.walk()


if __name__ == '__main__':
    met(Cat())
    n = -29
    n = abs(n)
    m = Mammal('Donkey')
    c = Cat()
    c.annoying()
    # m.walk()
    # list = list()
    # for i in range(0,10):
    #     m = Mammal(i)
    #     list.append(m)
    #
    # listmamal = tuple(list)
    # list[1].mtype = "horse"
    # listmamal[0].mtype = "horse"
    # print(listmamal[0].mtype)
    # print(listmamal[1].mtype)

    # if n % 2 == 0:
    #     print("Not Weird")
    # else:
    #     print("Weird")
