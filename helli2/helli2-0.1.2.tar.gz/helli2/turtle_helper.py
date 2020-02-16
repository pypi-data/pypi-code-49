import turtle as t

def islamic_draw(repeat, rotation, pencolor, fillcolor, function, *args):
    t.speed(1)
    t.up()
    t.home()
    t.down()
    t.color(pencolor, fillcolor)
    for i in range(repeat):
        t.begin_fill()
        function(*args)
        t.end_fill()
        t.left(rotation)
    t.color("black", "black")
    t.up()
    t.home()
    t.down()




    
 

