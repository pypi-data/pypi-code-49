"""
本文件中的函数用于对pascal voc数据集中的目标检测部分，生成mxnet的RecordIO文件。
主要调用getRecordIO函数，从指定文件中，读取图片名，然后根据该名，去JPEGImages目录
以及Annotations目录中，读取图片及其bbox的类别坐标。
将所有图片的信息，打包成.rec和.idx文件。
"""

import xml.etree.ElementTree as ET
import mxnet as mx
from tqdm import tqdm


obj_cls = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
           'bus', 'car', 'cat', 'chair', 'cow',
           'diningtable', 'dog', 'horse', 'motorbike', 'person',
           'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']


def get_path(voc_root):
    """
    根据voc根目录，得到多个文件及目录位置
    """
    pathes = {}
    pathes['voc_root'] = voc_root
    pathes['xml_root'] = voc_root + 'Annotations/'
    pathes['train_path'] = voc_root + 'ImageSets/Main/train.txt'
    pathes['val_path'] = voc_root + 'ImageSets/Main/val.txt'
    pathes['tv_path'] = voc_root + 'ImageSets/Main/trainval.txt'
    pathes['img_root'] = voc_root + 'JPEGImages/'
    return pathes


def get_cls(name):
    """
    将类别名称转为编号
    :param name: xml文件中object类别名称
    :return: 类别编号
    """
    return obj_cls.index(name)


def get_clsname(cls):
    """
    将类别编号转为名称
    :param cls: 编号
    :return: 名称
    """
    return obj_cls[cls]


def get_objs(xmlfile):
    """
        从xml文件中，得到各object的Element以及图片的宽高
    output:
        - 包含所有objcet的Element的列表
        - 图片的宽高，用于后续对bbox的坐标归一化
    """
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    # 一定要使用find，不要硬编码，否则会出现读取错误的情况
    size = root.find('size')
    w = size.find('width').text
    h = size.find('height').text

    return root.findall('object'), int(w), int(h)


def get_clspos(obj, w, h):
    """
    从object的Element中，得到bbox类别以及归一化了的坐标
    """
    name = obj.find('name')
    cls = get_cls(name.text)
    bndbox = obj.find('bndbox')

    xmin = float(bndbox.find('xmin').text) / w
    ymin = float(bndbox.find('ymin').text) / h
    xmax = float(bndbox.find('xmax').text) / w
    ymax = float(bndbox.find('ymax').text) / h
    assert xmin <= 1.0 and ymin <= 1.0 and xmax <= 1.0 and ymax <= 1.0, \
        'xmin %.2f, ymin %.2f, xmax %.2f, ymax %.2f' % (xmin, ymin, xmax, ymax)

    return [cls, xmin, ymin, xmax, ymax]


def get_label(xmlfile, pad=False, maxboxes=None, paddata=-1):
    """
    从xml文件中，得到这张图片所有物体的bbox以及类别
    [cls, xmin, ymin, xmax, ymax]
    pad用于指定是否添加[-1, -1, -1, -1, -1]
    maxNboxes指明数据集中图片最多有多少box
    """
    objs, w, h = get_objs(xmlfile)

    result = []
    try:
        for obj in objs:
            # 全拉成一维，因为recordio unpack的时候也不保留维度信息
            # 所以这边弄成两维的也没用
            result.extend(get_clspos(obj, w, h))
    except AssertionError:
        print(xmlfile)
        raise ValueError

    objs_num = len(objs)
    assert objs_num > 0
    # 为使后续可以将图片及其label打包成一个batch
    # 需要所有图片具有相同的ground truth box个数
    # 不足的，在这里进行添加
    if pad:
        paddata = [paddata] * 5
        result.extend(paddata * (maxboxes - objs_num))

    # 3指的是头长，也就是[3, 5, objs_num]这个长度
    # 5指的是该ground box的label长度，这里的5就是get_clspos返回数据长度
    # objs_num指定的是，label中有多少是有效的box坐标，后续对图片进行裁剪时要用到
    result = [3, 5, objs_num] + result  # 符合mxnet对物体检查RecordIO raw data的格式

    return result  # 这里不需要转化为numpy.array格式，后面pack时会自动转


def get_MaxNBox(file_path, xml_root):
    """
        遍历数据集，得到数据集中图片的最多bbox数
    输入
        - xml_root:  xml文件根目录
        - file_path: 文件路径，其中每行保存数据集中所有xml文件名（无后缀）
    输出
        - 图片包含的最多bbox数量
        - 对应的xml文件

    maxbox, _ = get_MaxNBox(train_path, xml_root)
    """
    num = 0
    file = ''
    with open(file_path, 'r', encoding='utf8') as fp:
        for line in fp:
            xmlfile = xml_root + line.strip() + '.xml'
            objs, *_ = get_objs(xmlfile)
            if len(objs) > num:
                num = len(objs)
                file = xmlfile

    return num, file


def getXJpath(file, xroot, jroot):
    """
        生成器函数，从file中取出文件名，得到对应的xml文件路径和jpg文件路径
    """
    fp = open(file, 'r', encoding='utf8')
    for line in fp:
        xpath = xroot + line.strip() + '.xml'
        jpath = jroot + line.strip() + '.jpg'
        yield xpath, jpath
    fp.close()


def get_img(impath, resize=None):
    """从图片路径读取图片，并resize"""
    # 记住，读入的图片是BGR格式的
    img = mx.image.imread(impath) 
    if resize is not None:
        img = mx.image.imresize(img, *resize)
    return img


def packLabelImg(label, img, quality=95):
    """打包label和image，返回打包好的record"""
    header = mx.recordio.IRHeader(0, label, id(label), 0)
    packio = mx.recordio.pack_img(header, img, quality=quality)
    return packio


# 主要调用该函数生成recordio文件
# 但要先调用get_MaxNBox函数获得数据集中图片最多bbox数量
def getRecordIO(filepath, maxbox, rec_name='voc', path='./',
                pad=True, resize=None, quality=95, voc_root='./'):
    """

    :param filepath: 保存训练或测试图片名的文件位置
    :param maxbox: 图片中的最多锚框数量
    :param rec_name: recordio文件名称
    :param path: recordio文件保存路径
    :param pad: 是补全图片标注，使数量一致
    :param resize: 对图片进行resize
    :param quality: pack图片时的编码质量
    :return:

    getRecordIO(tv_path, maxbox, rec_name='tvVOC', resize=(480,480))
    """
    rec_path = path + rec_name + '.rec'
    idx_path = path + rec_name + '.idx'

    recordio = mx.recordio.MXIndexedRecordIO(idx_path, rec_path, 'w')
    getpath = getXJpath(filepath, xroot=get_path(voc_root)['xml_root'],
                        jroot=get_path(voc_root)['img_root'])

    for i, (xml, jpg) in tqdm(enumerate(getpath)):
        img = get_img(jpg, resize=resize)
        label = get_label(xml, pad=pad,
                          maxboxes=maxbox, paddata=-1)

        packio = packLabelImg(label, img, quality)
        recordio.write_idx(i, packio)

    recordio.close()


