from datetime import datetime
from math import pi, sin, cos, tan

from testpython.inheritance import Mammal

print("hello world")
print('Nishant')
price = 10
rating = 4.9
name = 'nishant'
print(price)
is_published = False
birthyear = 1990
print(birthyear)
print(datetime.now().year)
print("age " + (str(datetime.now().year - birthyear)))

name='john smith'
age = 20
is_new = True
# name = input("What is your name? ")
print(f'Hi {name} {len(name)}')




mammals = []
for i in range(0, 10):
    m = Mammal()
    m.mtype = 'Donkey' + str(i)
    mammals.append(m)
# print(m.mtype for m in mammals.__iter__())

temperatures = [10,20,30]

converted = list(map(lambda x: (float(9)/5)*x + 32, temperatures))
print(converted)

def map_functions(x, functions):
    res = []
    for fucn in functions:
        res.append(fucn(x))
    return res
fof = (sin, cos, tan)
print(map_functions(pi, fof))

