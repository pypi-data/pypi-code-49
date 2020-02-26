import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from matplotlib.colors import rgb_to_hsv

class colorAreas:
    
    #Conversion of 1. HEX code to RGB and 2. RGB to HSV
    def convertHEXColours(self,hexColours):
        colour_rgb = []
        colour = []
        for j in hexColours:
            j = j.lstrip('#')
            rgb = list(int(j[i:i+2], 16) for i in (0, 2, 4)) #1. getting RGB values from HEX
            colour_rgb.append(rgb)
            rgbHSV = rgb_to_hsv(rgb)
            rgbHSV = list(map(int, [rgbHSV[0]*360, rgbHSV[1]*100, rgbHSV[2]/2.55])) #2. getting HSV values from RGB
            colour.append(rgbHSV)
        return (colour, colour_rgb)
    
    #Determine the mask and result pixels
    def detectColor(self,colour,img,hsv_img,diff):
        colour[0] /= 2
        colour[1] *= 2.55
        colour[2] *= 2.55
        dark = (colour[0]+diff, colour[1]+diff, colour[2]+diff)
        light = (colour[0]-diff, colour[1]-diff, colour[2]-diff)
        mask = cv.inRange(hsv_img,light,dark)
        result = cv.bitwise_and(img, img, mask=mask)
        return (mask,result)
    
    #Get area of each color
    def getArea(self,hexColours,path,diff):
        img = cv.imread(path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #converting the colorspace from BGR to RGB
        hsv_img = cv.cvtColor(img, cv.COLOR_RGB2HSV) #converting the colorspace from RGB to HSV
        colours, colour_rgb = self.convertHEXColours(hexColours)
        ratio = []
        for i in range(len(colours)):
            mask,result = self.detectColor(colours[i],img,hsv_img,diff) 
            size = mask.shape
            pixels = 100*cv.countNonZero(mask)/(size[0]*size[1]) #ratio of a color = size of masked pixels/ actual size of mask
            ratio.append(pixels)
        return ratio