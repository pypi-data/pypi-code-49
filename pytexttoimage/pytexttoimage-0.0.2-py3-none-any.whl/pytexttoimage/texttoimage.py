import cv2
import numpy as np


def text_2_image(mark,filename,fontscale,thickness,textcolor):
    #Defining FontFace
    fontface = cv2.FONT_HERSHEY_SIMPLEX

    #Retrieving size of text to perform dynamic resizing of the image
    size = cv2.getTextSize(text=mark,fontFace=fontface,fontScale=fontscale,thickness=thickness)
    #Creating a white blank image
    img = np.ones((size[0][1]+50,size[0][0]+50,3),np.uint8)*255
    img_1 = cv2.putText(img,mark,org=(0,size[0][1]),fontFace=fontface,fontScale=fontscale,thickness=thickness,color=textcolor)

    cv2.imwrite(filename,img_1)




