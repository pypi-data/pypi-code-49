import turtle as t

def islamic_draw(rotation, repeat, pencolor, fillcolor, function, *args):
    t.speed(-1)
    t.home()
    t.color(pencolor, fillcolor)
    for i in range(repeat):
        function(*args)        
        t.left(rotation)
    t.color("black, "black")
    t.home()


    
