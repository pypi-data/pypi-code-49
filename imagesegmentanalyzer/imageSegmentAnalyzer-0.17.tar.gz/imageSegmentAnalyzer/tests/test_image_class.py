from unittest import TestCase
import numpy as np
import matplotlib.pyplot as plt
from imageSegmentAnalyzer.image import Image
import rawpy
from skimage.color import rgb2hsv,rgb2grey


class TestImage(TestCase):
    def setUp(self):
        self.img = rawpy.imread("TestImg3.NEF")
        self.I = Image(image=self.img, name="Test")

        self.I.select_points(name="column14", shape="rectangle", rows=33, columns=8, addPoints=False,
                          p=[[1265.4519217793313, 235.97145579854194],
                                  [1228.3420703378579, 2345.7487165855196],
                                  [1730.970515697517, 251.79981742008587]])
        """
        self.I.select_points(name="column2A", shape="rectangle", rows=17, columns=2,
                          points=[[2012.4414514832285, 265.57813164320805],
                                  [2032.0545832184525, 1290.2104755026899],
                                  [2078.476218574243, 269.5308789522611]])
        self.I.select_points(name="column2A-2", shape="rectangle", rows=16, columns=2, row_start=17,
                          points=[[2039.657558968272, 1356.3186423398915],
                                  [2075.22399675894, 2351.0048873519872],
                                  [2102.556143498964, 1356.5185741323305]])
        self.I.select_points(name="column2A-3", shape="rectangle", rows=16, columns=3, column_start=6,
                          points=[[2302.8045925848346, 226.38600492249816],
                                  [2298.2437565036416, 1181.9267624869933],
                                  [2438.896012253875, 222.18587138667925]])
        self.I.select_points(name="column2A-4", shape="rectangle", rows=17, columns=3, column_start=6, row_start=16,
                          points=[[2345.8230453756773, 1298.5127766969872],
                                  [2394.469136127031, 2356.5652505389344],
                                  [2479.5997949419, 1286.3512540091488]])
        self.I.select_points(name="column3A-1", shape="rectangle", rows=16, columns=8,
                          points=[[2704.4808583495346, 217.02330914372243],
                                  [2661.269156383273, 1183.2633254448685],
                                  [3160.768157795752, 240.3484007324065]])
        self.I.select_points(name="column3A-2", shape="rectangle", rows=17, columns=8, row_start=17,
                          points=[[2693.7062825416538, 1350.3552183645627],
                                  [2769.1363062055766, 2414.4163033246928],
                                  [3156.958156953698, 1316.043469802245]])
        self.I.select_points(name="column2A-5", shape="rectangle", rows=5, columns=2, column_start=3,
                          points=[[2128.0050665060744, 253.4208813364067],
                                  [2133.3350308965228, 506.6701874738177],
                                  [2189.5529822999583, 252.06305770842175],
                                  ])
        self.I.select_points(name="column2A-6", shape="rectangle", rows=10, columns=2, column_start=3, row_start=6,
                          points=[[2135.413715845436, 637.4292676957775],
                                  [2138.4352109813117, 1216.1210724123266],
                                  [2194.0525104067583, 631.896343004993]
                                  ])
        self.I.select_points(name="column2A-7", shape="rectangle", rows=17, columns=2, column_start=3, row_start=17,
                          points=[[2139.447036029427, 1281.2176072456111],
                                  [2198.0958330235862, 2332.2525430471483],
                                  [2207.035931452093, 1279.5800744544233]])
        self.I.select_points(name="column2A-8", shape="rectangle", rows=2, columns=2, column_start=3, row_start=6,
                          points=[[2165.231031345811, 592.5303135444244],
                                  [2226.2426070125466, 590.9051541111032],
                                  [2162.588707852786, 617.7224703865124]])"""
    def test_select_points1(self):
        self.I.select_points(name="column1A", shape="rectangle", rows=33, columns=8)
        self.I.select_points(name="column2A", shape="rectangle", rows=33, columns=8)
        self.I.select_points(name="column2A", shape="rectangle", rows=33, columns=8)
        self.I.show()
        plt.show()

    def test_plot_intensities(self):
        self.I.plot_intensities(type="smart_max")

    def test_init_image(self):
        self.assertIsInstance(self.I, Image)

    def test_process_image(self):
        self.I.process_image()
        self.assertIsInstance(self.I.processed_image, np.ndarray)


    def test_select_points(self):
        self.I.show()
        plt.show()
        self.I.set_references(black=0.0, white=.75)
        self.I.get_values(pixels=(30, 30), type="smart_max")

    def test_segment_images(self):
        self.I.select_points(name="column1A", shape="rectangle", rows=8, columns=33)
        self.I.select_points(name="column2A", shape="rectangle", rows=8, columns=33)
        self.I.show()
        plt.show()
        seg = self.I.get_segmented()
        k = seg.values()
        print(seg)
        plt.imshow(seg['column1A'])
        plt.show()

    def test_getValues_images(self):
        self.I.select_points(name="column1A", shape="rectangle", rows=33, columns=8)
        self.I.show()
        plt.show()
        self.I.get_values()