#!/usr/bin/env python

import os
import struct

from array import array
import png
from tqdm import tqdm


def read(dataset="train", path="."):
    if dataset is "train":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "test":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'train' or 'test'")

    flbl = open(fname_lbl, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = array("b", flbl.read())
    flbl.close()

    fimg = open(fname_img, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = array("B", fimg.read())
    fimg.close()

    return lbl, img, size, rows, cols


def write_dataset(labels, data, size, rows, cols, output_path, dataset):
    output_dir = os.path.join(output_path, dataset)
    # create output directories
    output_dirs = [os.path.join(output_dir, str(i)) for i in range(10)]
    for dir in output_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)

    txt_path = os.path.join(output_path, dataset + ".txt")

    # erase .txt file if it exists
    open(txt_path, "w").close()

    # write data
    i = 0
    for label in tqdm(labels):
        output_filename = os.path.join(output_dirs[label], str(i) + ".png")
        with open(output_filename, "wb") as h:
            w = png.Writer(cols, rows, greyscale=True)
            data_i = [data[(i*rows*cols + j*cols): (i*rows*cols + (j+1)*cols)] for j in range(rows)]
            w.write(h, data_i)
        with open(txt_path, "a") as f:
            f.write(output_filename + "\n")
        i += 1


def raw_to_png(raw_dir, png_dir):
    raw_dir = os.path.abspath(raw_dir)
    png_dir = os.path.abspath(png_dir)

    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

    for dataset in ["train", "test"]:
        print("Writing {} dataset".format(dataset))
        labels, data, size, rows, cols = read(dataset, raw_dir)
        write_dataset(labels, data, size, rows, cols, png_dir, dataset)
