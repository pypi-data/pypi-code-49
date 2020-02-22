"""
该文件定义了图片显示函数，可以显示图片及其bbox。
然后定义了一个迭代器类，根据.rec和.idx不断生成batch文件。
"""

from matplotlib import colors as mcolors
import matplotlib
import numpy as np
import random
from itertools import zip_longest
import mxnet as mx
from .genRecordIO import get_clsname

# 用于画bbox时的颜色显示
colors = list(mcolors.cnames.values())


def getRecTex(bbox, label=None, bcolor='r', tcolor='w'):
    """
        根据bbox和label返回对应的patches和artist，
        用于后续在matplotlib中画图使用
    :param bbox: numpy，4个浮点值，对应左上角和右下角的xy
    :param label: str，要标注的text
    :param bcolor: str，bbox边框颜色
    :param tcolor: str，文本颜色
    :return:
    """
    rec = matplotlib.patches.Rectangle(
        xy=(bbox[0], bbox[1]), width=bbox[2] - bbox[0], height=bbox[3] - bbox[1],
        fill=False, edgecolor=bcolor, linewidth=3)
    
    if label is not None:
        tex = matplotlib.text.Text(bbox[0], bbox[1], label, color=tcolor,
                               verticalalignment='top', horizontalalignment='left',
                               fontsize=15, bbox=dict(facecolor=bcolor))
    # 如果没有传入label，那么另tex为None即可
    # 后续使用add_artist添加时也没问题
    else:
        tex = None
    return rec, tex



def showBBox(axes, img, bboxes, labels=None):
    """
        在axes上显示img和bbox及其label
    :param axes: 要显示图片的axes
    :param img: 要显示的图片，为numpy.array，要整数
    :param bboxes: 该图片的bbox们，(n, 4)，浮点数，numpy.array
                   为具体的两个点坐标，没有进行归一化的。
    :param labels: (n,) 对应类别的编号
    :return:
    """
    axes.imshow(img)
    h, w, c = img.shape
    if labels is None:
        labels = []
    if bboxes.ndim == 1:
        bboxes = [bboxes]
    for i, (bbox, label) in enumerate(zip_longest(bboxes, labels, fillvalue=None)):
        if label != -1:
            if label is not None:
                text = get_clsname(int(label))
                bcolor = colors[int(label)]
                tcolor = colors[int(label) + 100]
            else:
                text = ''
                bcolor = colors[i%100]
                tcolor = 'w'
 
            RecPatch, TexArt = getRecTex(bbox, text, bcolor=bcolor,
                                         tcolor=tcolor)
            axes.add_patch(RecPatch)
            axes.add_artist(TexArt)

# 值进行了随机裁剪的Augmenter
default_auglist = mx.image.CreateDetAugmenter((3,300,300),
                                              rand_crop=0.5, mean=None, std=None,
                                              min_object_covered=[0.7, 0.9])
# 不光进行了裁剪，还对图片进行了归一化处理
auglist = mx.image.CreateDetAugmenter((3,300,300),
                                      rand_crop=0.5, mean=True, std=True,
                                      min_object_covered=0.95)

auglist_full = mx.image.CreateDetAugmenter((3,300,300),
                rand_crop=0.5, mean=True, std=True,
                min_object_covered=[0.7, 0.9], brightness=0.125,
                contrast=0.125, saturation=0.125)

class DataIter:
    """
        自定义的迭代器类型，根据recordio文件.idx和.rec，来不断生成imgs和labels。
        根据cur和flag指示当前状态。如果当前读完后，到头了，设置flag，但要等到下一次
        读取的时候再抛出stopiteration异常，并复位状态。
    """
    def __init__(self, idx, rec, batch_size, shuffle=False, aug_list=None, ctx=None):
        self.recordio = mx.recordio.MXIndexedRecordIO(idx, rec, 'r')
        self.indexes = self.recordio.keys
        self.num_img = len(self.indexes)
        self.batch_size = batch_size
        self.aug_list = aug_list
        self.ctx = ctx
        self.shuffle = shuffle

        self.rand_indexes = self.indexes.copy()
        self.reset()

    def _sample_from_ind(self, ind, aug_list=None):
        """
        根据ind提取record，并根据aug_list中的Augmenter对图片及标注进行处理
        """
        record = self.recordio.read_idx(ind)
        header, img = mx.recordio.unpack_img(record)
        # 转为RGB，在通道维上倒序即可
        img = img[:, :, ::-1]

        # 提取label信息
        headlen = int(header.label[0])  # 添加信息长度
        labellen = int(header.label[1])  # 每个bbox标注长度
        numbox = int(header.label[2])  # 有多少是有效bbox

        # 各Augmenter需要输入图片是NDArray，label为ndarray
        label = header.label[headlen:].reshape((-1, labellen))
        img = mx.nd.array(img, ctx=self.ctx)

        if aug_list is not None:
            # dtype很重要，不然默认是uint8！！！
            # aug会对图片及其label作出变换
            olabel = np.full(label.shape, -1, dtype='float32')
            # 假label中的多个-1，可能会造成数值上的错误，
            # 所以这边将其过滤出来。
            labeltmp = label[:numbox]
            for aug in aug_list:
                # 有的Augmenter可能会减少标注bbox的数量
                img, labeltmp = aug(img, labeltmp)
            if labeltmp.shape[0] == 0:
                labeltmp = label[:numbox]
            olabel[:labeltmp.shape[0]] = labeltmp
            label = olabel

        label = mx.nd.array(label, ctx=self.ctx)
        return img.transpose((2, 0, 1)), label

    

    def next_sample(self, aug_list=None):
        """
        不断提取下一个图片，如果到头抛出StopIteration异常
        刚到头的时候，设置标志位，但并不抛出。
        设置标志位后，如果还要读取，就抛出。抛前清除状态，为下一次迭代准备。
        """
        if self.flag:
            self.reset()
            raise StopIteration

        img, label = self._sample_from_ind(self.rand_indexes[self.cur],
                                           aug_list=aug_list)
        self.cur += 1
        if self.cur >= self.num_img:
            self.flag = 1

        return img, label

    def next_batch(self):
        labels = []
        imgs = []

        i = 0
        while i < self.batch_size:
            img, label = self.next_sample(aug_list=self.aug_list)
            imgs.append(img)
            labels.append(label)
            i += 1
            # 对于最后一batch，如果数量不足，就不足吧
            if self.cur >= self.num_img:
                break
        # 都是NDArray格式
        return mx.nd.stack(*imgs, axis=0), mx.nd.stack(*labels, axis=0)

    def tell(self):
        return self.cur

    def reset(self):
        self.cur = 0
        self.flag = 0
        if self.shuffle:
            random.shuffle(self.rand_indexes)

    def __next__(self):
        return self.next_batch()

    def __iter__(self):
        return self