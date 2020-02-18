import modelx as mx

def t_arg(t):
    pass

m = mx.new_model("DynModel")
s1 = m.new_space('SpaceA', formula=t_arg)
s2 = s1.new_space('SpaceB')

@mx.defcells
def foo(x):
    return x

# m.new_space('SpaceB', refs={'RefSpaceA': m.SpaceA(0)})
# s1[1].foo[2] = 3

ds1 = s1[1].SpaceB
