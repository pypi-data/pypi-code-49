import os
import math
import logging
import numpy as np
from rasterbox.utilities import Misc
from rasterbox.Image import Image
from rasterbox.Target import Target

class Rasterbox(object):
    logging.basicConfig(filename="rasterbox.log",level=logging.INFO)
    def __init__(self, src, images_path, targets_path, target_dict):
        logging.info("Init Rasterbox")
        self.src = src
        self.targets = target_dict
        self.__build(images_path, targets_path)

    def __build(self, images_path, targets_path):
        images_path = os.path.join(self.src, '%s' % images_path)
        targets_path = os.path.join(self.src, '%s' % targets_path)

        logging.info("Images Path " + images_path)
        logging.info("Targets Path " + targets_path)

        if images_path == None or targets_path == None:
            logging.error("Image or target path could not be located")
            raise FileNotFoundError("Couldn't locate images path or targets path")

        image_bins = self.__build_binaries(images_path)
        target_bins = self.__build_binaries(targets_path)

        if image_bins == None:
            logging.error("There is a problem with the path to binary images")
            raise Exception(images_path + " returns None object")
        if target_bins == None:
            logging.error("There is a problem with the path to binary targets")
            raise Exception(targets_path + " returns None object")

        self.__build_images(image_bins)
        self.__build_targets(target_bins)
        self.__build_combined_satellites()
        self.__build_onehot()


    def __build_images(self, bins):
        for idx, bin in enumerate(bins):
            if 'S2' in bin:
                self.S2 = Image(bins[idx])
                logging.info("Sentinel 2 built")

            elif 'L8' in bin:
                self.L8 = Image(bins[idx])
                logging.info("Landsat 8 built")

            else:
                Misc.err("Do not recognize file ", bin)


    def __build_targets(self, bins):
        self.Target = dict()

        for _, bin in enumerate(bins):
            self.Target.update({
                target:Target(target, bin, self.targets)
                for target in self.targets if target in bin.lower()
            })
        logging.info("Targets built")


    def __build_binaries(self,path):
        logging.info("Building binaries " + path)
        try:
            for root, dirs, files in os.walk(path, topdown=False):
                bin_files = [
                    os.path.join(path, '%s' % file)
                    for file in files if '.hdr' not in file
                ]
                if bin_files == None:
                    raise FileNotFoundError()
                return bin_files
        except:
            Misc.err("Error building headers and binaries for %s" % path)


    def __build_combined_satellites(self):
        self.Combined = Image(nparray=np.append(self.S2._Data, self.L8._Data, axis=0))


    def __build_onehot(self):
        tmp = np.zeros((self.S2.lines * self.S2.samples, len(self.Target.keys())))
        for idx, target in enumerate(self.Target.keys()):
            tmp[:,idx] = self.Target[target].Binary
        self.Onehot = Image(nparray=tmp)


    def onehot_inconsistencies():
        pass
