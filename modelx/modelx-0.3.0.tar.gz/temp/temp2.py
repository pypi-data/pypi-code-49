from modelx import *

m, s1 = new_model(), new_space('s1')

def t_arg(t):
    pass

s2 = m.new_space(name='s2', formula=t_arg)

s2(0)
s2.a = 1

print(s2(0).a)