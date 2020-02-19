"""
   This is the color increase command that matches the turtle drawing command.
   颜色增加与颜色设定命令,用来在海龟画图中做颜色渐变。
   作者:李兴球 2020/2/20更新
   本程序定义了四个函数，coloradd是用来增加颜色的，参数为RGB的255三元组颜色和一个小数。
   colorset是把一个整数转换成rgb三元色值。
   brightset命令用来设置RGB的255三元组颜色的亮度。
   saturationset命令用来设置RGB的255三元组颜色的饱和度。

"""
__version = 0.25
__author__ = "lixingqiu"
__blog__ = "www.lixingqiu.com"

import colorsys

def coloradd(color,dh):
    """color：three tuple color value，example：(255,255,0)，
       dh：0-1.0       
       此函数把颜色转换成hls模式,对色度h进行增加色度dh的操作
       然后转换回去,dh是小于1的浮点数。
       return three tuple color
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        h =  h + dh
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        return int(r*255),int(g*255),int(b*255)
    else:
        return color
addcolor = coloradd   # define alias name 定义别名

def colorset(color):
    """color：a integer from 1 to 360
       turn a integer to three tuple color value
       把一个整数转换成三元颜色值,返回三元组。
    """
    color = color % 360
    color = color / 360.0    
    r,g,b = colorsys.hsv_to_rgb(color,1.0,1.0)
    
    return int(r*255),int(g*255),int(b*255)
    
setcolor = colorset    # define alias name 定义别名

def brightset(color,light):
    """亮度设置函数
       color:这是RGB255三元组
       light:这是一个小数
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        r,g,b = colorsys.hls_to_rgb(h,light,s)
        r = min(int(r * 255),255)
        g = min(int(g * 255),255)
        b = min(int(b *255),255)
        return max(0,r),max(0,g),max(0,b)
    else:
        return color
lightset = brightset
setbright = brightset

def saturationset(color,baohedu):
    """亮度设置函数
       color:这是RGB255三元组
       baohedu:这是一个小数
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        r,g,b = colorsys.hls_to_rgb(h,l,baohedu)
        r = min(int(r * 255),255)
        g = min(int(g * 255),255)
        b = min(int(b *255),255)
        return max(0,r),max(0,g),max(0,b)
    else:
        return color
baoheduset = saturationset
satuset = saturationset
setbaohedu = saturationset

if __name__ == "__main__":

    import turtle

    ft = ("",12,"normal")
    screen = turtle.getscreen()    
    screen.colormode(255)
    screen.delay(0)
    screen.bgcolor('black')
    screen.title("draw lollipop 画棒棒糖")
    
    c  = (255,0,0)                # RGB红色
    turtle.ht()                   # 隐藏海龟
    turtle.penup()                # 抬起笔来
    turtle.goto(0,100)            # 定位坐标
    turtle.pendown()              # 落下画笔
    for i in range(300):          # 迭代变量
        turtle.width(i/10)        # 画笔笔宽
        turtle.fd(i/10)           # 海龟前进
        turtle.rt(10)             # 海龟右转
        c = coloradd(c,0.01)      # 颜色增加
        turtle.pencolor(c)        # 画笔颜色
        
    turtle.penup()                # 抬起笔来
    turtle.goto(0,100)            # 定位坐标
    turtle.setheading(-90)        # 方向向下
    turtle.color("brown")         # 画笔颜色
    turtle.pendown()              # 落下笔来
    turtle.fd(280)                # 前进300
    turtle.penup()                # 抬起笔来
    turtle.color("gray")          # 画笔颜色
    turtle.write("www.lixingqiu.com",align='center',font=ft)
    
    # 亮度设置
    turtle.goto(-300,-200)
    turtle.write("lightset test (亮度测试)",font=ft)
    turtle.goto(-300,-230)
    c = (255,0,0)
    turtle.setheading(0)
    turtle.pendown()
    for x in range(200):
        ys = lightset(c,x/200)
        turtle.color(ys)
        turtle.fd(3)
    turtle.penup()
    
    # 饱和度设置
    turtle.goto(-300,-280)
    turtle.write("saturation test (饱和度测试)",font=ft)
    turtle.goto(-300,-300)
    c = (255,0,0)
    turtle.setheading(0)
    turtle.pendown()
    for x in range(200):
        ys = saturationset(c,x/200)
        turtle.color(ys)
        turtle.fd(3)

    screen.mainloop()


print("import successful,email: 406273900@qq.com, wechat:scratch8")
