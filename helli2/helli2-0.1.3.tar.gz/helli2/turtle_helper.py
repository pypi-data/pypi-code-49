import turtle as t
import png

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

def create_image(width, height, pixels, name="Untitled"):
    img = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(pixels[i][j][0])
            row.append(pixels[i][j][1])
            row.append(pixels[i][j][2])
        img.append(row)
    with open(name + ".png", mode='wb') as f:    
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
        print("Image Created!")
            




    
 

