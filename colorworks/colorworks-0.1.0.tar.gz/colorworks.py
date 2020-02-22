import sys
import turtle
import tkinter
shell = sys.stdout.shell
t = turtle.Turtle

ColorRed = [255, 0, 0, '#FF0000']
ColorGreen = [0, 255, 0, '#00FF00']
ColorBlue = [0, 0, 255, '#0000FF']
ColorWhite = [255, 255, 255, '#FFFFFF']
ColorForest = [255, 255, 0, '#FFFF00']
ColorMint = [0, 255, 255, '#00FFFF']
ColorMagenta = [255, 0, 255, '#FF00FF']
ColorIndigoViolet = [122, 20, 133, '#7A1485']
ColorSky = [89, 89, 255, '#5959ff']
ColorYellow = [255, 255, 102 , '#FFFF66']


class print():
    def purple(Str):
        shell.write(Str+'\n', 'BUILTIN')
        return None

    def black(Str):
        shell.write(Str+'\n', 'SYNC')
        return None

    def green(Str):
        shell.write(Str+'\n', 'STRING')
        return None

    def brown(Str):
        shell.write(Str+'\n', 'console')
        return None
    
    def red(Str):
        shell.write(Str+'\n', 'COMMENT')
        return None

    def blue(Str):
        shell.write(Str+'\n', 'stdout')
        return None

    def errorcolor(Str):
        shell.write(Str+'\n', 'stderr')
        return None

    def orange(Str):
        shell.write(Str+'\n', 'KEYWORD')
        return None
