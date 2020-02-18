import modelx as mx

m, s = mx.new_model(), mx.new_space()

s.formula = lambda i: {"refs": {"x": "dynspace ref"}}

# s.x = "space ref"
m.x = "model ref"
s.x = "space ref"
# s.x = "space ref2"
