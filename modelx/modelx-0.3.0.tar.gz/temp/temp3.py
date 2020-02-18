import modelx as mx


"""
    Sub <------------------- Base1
     |                        |
    Child <--------- Base2  Child
     |                |       |
    GChild <--Base3  GChild  GChild
               |      |       |
              foo    foo     foo
"""
m = mx.new_model()
m.new_space("Sub").new_space("Child").new_space("GChild")
m.new_space("Base1").new_space("Child").new_space("GChild").new_cells(
    "foo", formula=lambda: "Under Base1")
m.new_space("Base2").new_space("GChild").new_cells(
    "foo", formula=lambda: "Under Base2")
m.new_space("Base3").new_cells(
    "foo", formula=lambda: "Under Base3")

m.Sub.Child.GChild.add_bases(m.Base3)
m.Sub.Child.add_bases(m.Base2)
m.Sub.add_bases(m.Base1)
