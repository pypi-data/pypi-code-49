from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

import cv2


class IndexGUI(object):
    ref_dump_path = None

    def __init__(self, file_path):
        self.pxpy = np.array(np.loadtxt(file_path, dtype=str, delimiter=',')[1:, :], dtype=float)
        self.source_index = 0

        self.root = tk.Tk()
        self.root.title('Index Finder')

        # distances related
        self.distances = None
        self.dis_image = None

        # index label
        o = tk.Label(self.root, text="Index:", width=10)
        o.grid(row=1, column=0)

        # index
        variable = tk.IntVar(0)
        l = tk.Entry(self.root, textvariable=variable)
        l.grid(row=1, column=1)
        scale = tk.Scale(self.root, orient=tk.HORIZONTAL, length=300,
                              from_=0, to=len(self.pxpy)-1, resolution=1, variable=variable, command=self.update_index)
        scale.grid(row=1, column=2, columnspan=2, padx=10)
        l.bind('<Return>', self.update_index)

        self.scale = scale
        self.index_var = variable

        # distance label
        o = tk.Label(self.root, text="distance:", width=10)
        o.grid(row=2, column=0)

        # distance vald
        variable = tk.DoubleVar(0)
        l = tk.Label(self.root, textvariable=variable)
        l.grid(row=2, column=1)
        self.distance_var = variable

        # save ref button
        variable = tk.DoubleVar(0)
        o = tk.Button(self.root, text='Save As Ref', command=self.save_trace_as_ref)
        o.grid(row=2, column=2)

        # Graph
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)

        frame = ttk.Frame(self.root)
        frame.grid(row=3, column=0, columnspan=4)

        canvas = FigureCanvasTkAgg(f, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = canvas
        self.axis = a
        self.axis.plot(self.pxpy[:, 0], self.pxpy[:, 1], 'ob', markersize=1)

        # image component
        self.img_canvas = None
        self.img_axis = None
        self.row_var = None
        self.column_var = None

        # set general config
        self.root.grid_rowconfigure(1, minsize=100)

        # draw plot with initial settings
        self.update_ui()

    def init_image_component(self):
        # row variable
        l = tk.Label(self.root, text='Row: ')
        l.grid(row=1, column=4)
        variable = tk.IntVar(0)
        l = tk.Label(self.root, textvariable=variable)
        l.grid(row=1, column=5)
        self.row_var = variable

        # col variable
        l = tk.Label(self.root, text='Column: ')
        l.grid(row=1, column=6)
        variable = tk.IntVar(0)
        l = tk.Label(self.root, textvariable=variable)
        l.grid(row=1, column=7)
        self.column_var = variable

        # Image plot
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)

        frame = ttk.Frame(self.root)
        frame.grid(row=3, column=4, columnspan=4)

        canvas = FigureCanvasTkAgg(f, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.img_canvas = canvas
        self.img_axis = a

    def update_index(self, event):
        self.update_ui()

    def calc_distance(self, trace, ref, offset):
        sig = trace - ref
        d_i = np.argmax(trace - ref)

        if sig[d_i] > 100:
            d = (d_i - offset) * self.lr.sample_distance
        else:
            d = 0
            d_i = offset

        return d_i, d, sig

    def build_distances_image(self):
        distances = np.empty(len(self.traces))
        for i, t in enumerate(self.traces):
            _, d, _ = self.calc_distance(t, self.ref, self.source_index.start)
            distances[i] = d

        if self.distance_low_thr:
            distances[distances < self.distance_low_thr] = 0
        distances[distances < 0] = 0

        self.distances = distances
        dis_image = self.lr.get_2d_image(distances)
        self.dis_image = np.stack((dis_image,)*3, -1)

    def save_trace_as_ref(self):
        index = self.index_var.get()
        self.ref = self.pxpy[index, :]
        np.save(IndexGUI.ref_dump_path, self.ref)
        self.build_distances_image()
        self.update_ui()

    def update_ui(self):
        index = self.index_var.get()
        trace = self.pxpy[index, :]
        ind = np.arange(len(trace))

        # update plot
        self.axis.clear()
        self.axis.plot(self.pxpy[:, 0], self.pxpy[:, 1], 'ob', markersize=1)
        self.axis.plot(self.pxpy[index, 0], self.pxpy[index, 1], 'or')

        # self.axis.set_xlim(-max(angles), max(angles))
        # self.axis.set_ylim(-max(angles), max(angles))
        self.canvas.draw()

        # update image
        # if self.is_image:
        #     # update row, column labels
        #     r, c = self.lr.img_index_to_r_c(self.index_var.get())
        #     self.row_var.set(r)
        #     self.column_var.set(c)
        #
        #     # update image
        #     # max_ = np.max(self.dis_image)
        #     # img = np.array(self.dis_image / max_ * 255, np.uint8)
        #     # cv2.circle(img, (c, r), 4, color=(255, 0, 0), thickness=2)
        #     self.img_axis.clear()
        #     self.img_axis.imshow(self.dis_image[:, :, 0], cmap='gray')
        #
        #     self.img_canvas.draw()

