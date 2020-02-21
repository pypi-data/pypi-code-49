from PIL import Image
import datetime
import numpy as np
import os

def instagrid(input_file,output_folder='INSTA',human_readable=False):
    img = Image.open(input_file)
    try :
        os.mkdir(output_folder)
    except FileExistsError:
        pass
    W,H = img.size
    WW = np.linspace(0,W,4,dtype=int)
    Hcut = H/(W//3)
    Hceil = np.ceil(Hcut)
    Hfloor = np.floor(Hcut)
    Hround = np.round(Hcut)
    Hgap = (W//3*Hceil - H)//2
    #Ceil : Adding extra black layer to cover the top
    HH = np.linspace(-Hgap,W//3*Hceil-Hgap,Hceil+1,dtype=int)
    imgnum = 0
    for i in range(len(HH)-1):
        for j in range(len(WW)-1):
            tmpim = img.crop((WW[j],HH[i],WW[j+1],HH[i+1]))
            if human_readable==False:
                tmpim.save(output_folder+'/'+str(i)+str(j)+'.png')
            else:
                tmpim.save(output_folder+'/'+str(i+1)+str(j+1)+'.png')
            
    return(output_folder)
