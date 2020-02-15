import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

class Helper:
    def plotshow(self,*args,**kwargs):
        self.plot(*args,**kwargs)
        self.show()
    def plot(self,*args,**kwargs):
        plt.plot(*args,**kwargs)
    def show(self,*args,**kwargs):
        plt.show(*args,**kwargs)
    def save_img(self,img,fp,*args,**kwargs):
        return self.save_pil_img(img,fp,*args,**kwargs)
    def save_pil_img(self,img,fp,*args,**kwargs):
        return self.pil(img).save(fp,*args,**kwargs)
    def save_np_img(self,img,fp,ext='.jpg'):
        return cv2.imencode(ext,self.np(img))[1].tofile(fp)
    def show_img(self, img, *args, **kwargs):
        self.pil(img).show(*args, **kwargs)
    def show_np_img(self,img,title='cv2 img'):
        img=self.np(img)
        cv2.imshow(title,img)
        cv2.waitKey()
    def show_pil_img(self,img,*args,**kwargs):
        self.pil(img).show(*args,**kwargs)
    def pil(self, img):
        if not isinstance(img, Image.Image):
            if len(img.shape) == 3: img = img[:, :, ::-1]
            img = Image.fromarray(np.array(img, dtype=np.uint8))
        return img
    def np(self, img):
        img = np.array(img, dtype=np.float)
        if len(img.shape) == 3: img = img[:, :, ::-1]
        return img
