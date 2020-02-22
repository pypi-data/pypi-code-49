"""
本文件中的函数用于操作box。
包含计算两box的iou，根据特征图生存anchor box，
根据iou得到匹配结果，根据匹配结果进行负采样，
anchor box的类别及偏移标注。

谨记，这些函数都是基于numpy的。
"""

import numpy as np
from collections import abc
import numbers
import time

class ctime():
    def __init__(self, prefix=''):
        self.prefix = prefix
    def __enter__(self, prefix=''):
        self.begin = time.time()
    def __exit__(self, *args):
        print(self.prefix, ': %.4f'%(time.time()-self.begin))


def getnp(data):
    """
        用于将scales和ratios转为numpy.array
    """
    if data is None:
        data = np.array([1.], dtype='float')
    elif isinstance(data, numbers.Real):
        data = np.array([data], dtype='float')
    elif isinstance(data, abc.Sequence):
        data = np.array(data, dtype='float')
        assert len(data.shape) == 1
    return data


def getwh(scales, ratios, fw, fh, srmode):
    """
        根据scales和ratios，以及特征图的宽高生成
        box的宽和高。srmode用于指定scales和ratios的组合形式。
        特征图上每个cell具有的box形状一致，所以这里就生成这些形状的宽高。
    输入：
        scales: 为处理好的一维numpy.array
        ratios: 为处理好的一维numpy.array
        fw: 特征图宽度
        fh: 特征图高度
        srmode: 
            'few': 只生成scales[0]和ratios以及scales[1:]和ratios[0]的box尺寸
            'many': 生成scales和所有ratios组合的box尺寸
    输出：
        width: 所有高度，为一维numpy.array形式
        height: 对应的宽度，为一维numpy.array形式
    """
    if srmode == 'few':
        # box的尺寸数量
        num = scales.size + ratios.size - 1
        # 用于存入各尺寸对应的宽高
        width = np.zeros((num,))
        height = np.zeros((num,))
        
        # 先将ratios中的值开方，以待后续使用
        sqt_ratios = np.sqrt(ratios)
        # 先是scales[0]与所有ratio搭配
        width[:ratios.size] = scales[0] * sqt_ratios
        height[:ratios.size] = width[:ratios.size] / ratios
        
        # 然后是scales[1:]与ratios[0]搭配
        width[ratios.size:] = scales[1:] * sqt_ratios[0]
        height[ratios.size:] = width[ratios.size:] / ratios[0]
    else:
        # 先是scales[0]与ratios，然后是scales[1]与ratios.....
            # np.repeat是对每个元素进行重复
            # ratios.size个scales[0], ratios.size个scales[1],
            # ratios.size个scales[2], ratios.size个scales[2],......
        rscales = np.repeat(scales.reshape((-1,1)), ratios.size, axis=1).flatten()
            # np。tile是将数组作为整体重复
            # scales.size个ratios
        rratios = np.tile(ratios, scales.size)
        
        # 就是按元素乘除
        width = rscales * np.sqrt(rratios)
        height = width / rratios
        
    # 将归一化的结果放大到特征图尺寸，
    # 后面再加上各个cell的中心点，得到所有像素点的box坐标
    width = width * fw
    height = height * fh
    
    return width, height


def getDefaultBoxes(fmap, scales=None, ratios=None, 
                    offset=None, norm=None, clip=False, 
                    srmode='few', omode='flatten'):
    """
        在输入特征图fmap上生成default boxes。
    输入：
        fmap:输入特征图，形状(n, c, h, w)，只要有shape方法获取形状即可
        scales: 列表，默认为[1.]
        ratios: 列表，默认为[1.]
        srmode: 'few'或'many'，'few'只生成len(scales)+len(ratios)-1个，
              'many'生成len(scales)*len(ratios)个
              
        offset: 两元素列表，分别为xy偏移。默认为[0.5, 0.5]
        norm: 两元素列表，分别为宽高归一化的分母。默认为fmap的宽高。
        omod: 输出形状，'flatten'则输出(1, 总box数, 4)，
                       'stack'则输出(1, h, w, 每点box数, 4)
                       (左上角x, 左上角y, 右下角x, 右下角y)
        clip: 是否对超出边界的坐标进行截取
    """
    assert omode in ('flatten', 'stack')
    assert srmode in ('few', 'many')
    n, c, fh, fw = fmap.shape
    
    scales = scales if type(scales).__name__ == 'ndarray' else getnp(scales)
    ratios = ratios if type(ratios).__name__ == 'ndarray' else getnp(ratios)
        
    width, height = getwh(scales, ratios, fw, fh, srmode)
    
    nbox_per_pixel = width.size
    # 得到各个cel的xy坐标
    xcenter, ycenter = np.meshgrid(np.arange(fw), np.arange(fh))
    xycenters = np.stack((xcenter, ycenter), axis=2)
    # 在第三维上tile，是为了后面
    xycenters = np.tile(xycenters, [1, 1, nbox_per_pixel*2])
    

    # left-up and right-down points offset，相对于中心点的偏移
    lu_rd_offset = np.stack((width, height, width, height), axis=1) *\
                   np.array([-1, -1 , 1, 1]) / 2
    lu_rd_offset = lu_rd_offset.flatten()
    
    # (h, w, nbox_per_pixel, 2, 2)
    lu_rd_points = (xycenters + lu_rd_offset).reshape((fh, fw, nbox_per_pixel, 2, 2))
    # points get done
    
    if offset is None:
        offset = np.array([0.5, 0.5])
    else:
        offset = np.array(offset)
    assert offset.size <= 2
    
    if norm is None:
        norm = np.array([fw, fh])
    else:
        norm = np.array(norm)
    assert norm.size <= 2
    
    # 加上偏移，再归一化
    lu_rd_points = (lu_rd_points + offset) / norm
    
    if clip:
        np.clip(lu_rd_points, 0., 1., out=lu_rd_points)
    
    if omode == 'flatten':
        # 左上x、左上y、右下x、右下y、...、repeat
        lu_rd_points = lu_rd_points.reshape((1, -1, 4))
    else:
        lu_rd_points = lu_rd_points.reshape((1, fh, fw, nbox_per_pixel, 4))
    
    return lu_rd_points


def calIOU(anchor, gt):
    """
        计算二者的IoU
    输入：    
        anchor形状-(N,4)或(4,)或(1,N,4)
        gt形状-(B,M,4)或(M,4)或(4,)
    输出：
        形状(B,N,M)    
    """
    assert len(anchor.shape) in (1,2,3)
    assert len(gt.shape) in (1,2,3)
    
    anchor = anchor.reshape((-1,4))
    if len(gt.shape) < 3:
        gt = gt.reshape((1,1,4)) if len(gt.shape) == 1 else np.expand_dims(gt, axis=0)
    # to (N,1,4)
    # 扩展维数，为后续的broadcast做准备
    anchor = np.expand_dims(anchor, axis=1)
    # to (B,1,M,4)
    gt = np.expand_dims(gt, axis=1)
    
    # (B,N,M,2)
    # maximum和minimum都会做broadcast，然后Element-wise比较
    with ctime('iou max_min'):
        max_tl = np.maximum(np.take(anchor, [0,1], axis=-1), np.take(gt, [0,1], axis=-1))
        min_br = np.minimum(np.take(anchor, [2,3], axis=-1), np.take(gt, [2,3], axis=-1))
    
    # (B,N,M)
    with ctime('iou prod1'):
        area = np.prod(min_br-max_tl, axis=-1)
    # x,y 必须整体小于才表示有intersection
    with ctime('iou inter'):
        i = np.where((max_tl < min_br).all(axis=-1), area, np.zeros_like(area))
    
    # (N,1)
    anchor_area = np.prod(anchor[:,:,2:]-anchor[:,:,:2], axis=-1)
    # (B,1,M)
    gt_area = np.prod(gt[:,:,:,2:]-gt[:,:,:,:2], axis=-1)
    # (B,N,M)
    total_area = anchor_area + gt_area - i
    iou = i / total_area
    
    return iou


def getUniqueMatch(iou, min_threshold=1e-12):
    """
        iou shape:(N,M)，需要在batch中for一下。
    """
    N, M = iou.shape
    iouf = iou.flatten()
    
    argmax = np.argsort(iouf)[::-1]
    argrow, argcol = np.divmod(argmax, M)

    uniquel = set()
    uniquer = set()
    match = np.ones((N,)) * -1
    i = 0
    while True:
        if argcol[i] not in uniquel and argrow[i] not in uniquer:
            uniquel.add(argcol[i])
            uniquer.add(argrow[i])
            if iou[argrow[i], argcol[i]] > min_threshold:
                match[argrow[i]] = argcol[i]
        if len(uniquel) == M or len(uniquer) == N:
            break
        i += 1
    return match.reshape((1,-1))


def match(iou, threshould=0.5, share_max=False):
    """
    input:
        iou: (B,N,M)
    output:
        result: (B,N)
    """
    B, N, M = iou.shape
    
    if share_max:
        result = np.argmax(iou, axis=-1)
        result = np.where(np.max(iou, axis=-1) > threshould, result, np.ones_like(result)*-1)
    else:
        # 论文第一步
        # [(1,N), ..., ]
        match = [getUniqueMatch(i) for i in iou]
        # (B,N)
        result = np.concatenate(match, axis=0)
        # (B,N)
        # 论文第二步
        argmax_row = np.argmax(iou, axis=-1)
        max_row = np.max(iou, axis=-1)
        argmax_row = np.where(max_row > threshould, argmax_row, np.ones_like(argmax_row)*-1)
        # 只有对于第一步中未匹配到的，进行分配
        result = np.where(result > -0.5, result, argmax_row)
        
    return result


def sample(match, cls_pred, iou, ratio=3, min_sample=0, threshold=0.5, do=True):
    """
    输入：
        match: 匹配结果，(B,N)
        cls_pred: 网络对box的类别预测，(B,N,cls+1),
                  网络的输出是NDArray类型，如果转为ndarray很耗时，
                  所以这里使用NDArray处理。
        iou: (B,N,M)
        ratio: negative:positive
        min_sample: the least number of negative
        threshold: if the negative has iou greater than this value,
                   we treat is as ignore sample. Do not treat is as negative.
        do: whether to do subsample
    输出：
        (B,N)-[-1,0,1]
            -1: negative, 0: ignore, 1:positive
    """
    if do is False:
        ones = np.ones_like(match)
        sample = np.where(match > -0.5, ones, ones*-1)
        return sample
    sample = np.zeros_like(match)
    # 先确定负框数量
    # (B,)
    num_pos = np.sum(match > -0.5, axis=-1)
    requre_neg = ratio * num_pos
    # (B,N) 值为1的表示可被采样的负框，0表示已经忽略了的负框及正框
    neg_mask = np.where(match < -0.5, np.max(iou, axis=-1) < threshold, sample)
    # 过滤掉IoU大的负框之后，最多有多少负框
    max_neg = neg_mask.sum(axis=-1)
    # 最终的负框数量，(B,)
    num_neg = np.minimum(max_neg, np.maximum(requre_neg, min_sample)).astype('int')
   
    # 得到各框的背景loss
    # (B,N)
    neg_prob = np.take(cls_pred, 0, axis=-1)
    # (B,N,1)
    max_value = np.max(cls_pred, axis=-1)
    # 就是log softmax，提高数值稳定性，(B,N)
    score = max_value - neg_prob + np.log(
                                   np.sum(
                                   np.exp(cls_pred-max_value[:,:,np.newaxis]), axis=-1))
    # 将正框和已经忽略的负框的分数置为0
    score = np.where(neg_mask, score, np.zeros_like(score))
    # (B,N)，np.argsort只能是升序排列
    argmax = np.argsort(score, axis=-1)[:,::-1]
    # (B,N)，正类置1
    sample[match>-0.5] = 1
    
    # 负类置-1
    for i, num in enumerate(num_neg):
        sample[i, argmax[i,:num]] = -1
    
    return sample


def np_pick(data, pick_array, axis=-1): 
    """
    在data的特定维中，提取出pick_array指定索引的元素。
    如data=
    array([[[ 0,  1,  2],
            [ 3,  4,  5]],

           [[ 6,  7,  8],
            [ 9, 10, 11]]])
    pick_array=
    array([[2, 0],
           [1, 2]])    
    axis = -1
    那么结果为：
    array([[ 2,  3],
           [ 7, 11]])  
           
    pick_array=
    array([[0, 1, 0],
           [1, 0, 1]])    
    axis = 1
    那么结果为：
    array([[ 0, 4, 2],
           [ 9, 7, 11]])    
           
    pick_array=
    array([[0, 1, 0],
           [1, 0, 1]])    
    axis = 0
    那么结果为：
    array([[ 0, 7, 2],
           [ 9, 4, 11]])   
    如果data的shape为(x,y,z,h,q)，在第2维中pick元素。那么pick_array的shape必须为(x,y,h,q)                             
    输入：
        - data：要被pick的array。至少有两维
        - pick_array：根据这个进行pick。
            如果data.shape==(B,N,M)，
            要pick最后一维，那么pick_array.shape==(B,N)
            如果要pick第一维，pick_array.shape==(B,M)
            如果要pick第0维，pick_array.shape==(N,M)
    输出：
        pick结果，与pick_array形状相同        
    """
    pick_array = pick_array.astype('int')
    data_shape = list(data.shape) 
    pick_array_shape = list(pick_array.shape)
    data_shape.pop(axis)  # 在指定维pick，就是对指定维降维，结果中便没有该维度了。
                          # 后面在索引时，对该维度的索引使用的就是pick_array。
                          # 所以，pick_array的维度需要与data_shape.pop(axis)之后的相同
    assert data_shape == pick_array_shape
    
    grid = np.indices(data_shape) 
    grid = grid.tolist() # 按grid的第0维展开，tolist即可
    if axis != -1:
        grid.insert(axis, pick_array) 
    elif axis == -1 or axis == len(data_shape) + 1:
        grid.append(pick_array)
    grid = tuple(grid)
    return data[grid]


def label_box_cls(match, sample, gt_cls, ignore_label=-1):
    """
    input:
        match-(B,N)
        sample-(B,N)
        gt_cls-(B,M)
        ignore_label-set the value of the ignored sample's label
    output:
        label_cls-(B,N), value is [0, cls]
        label_mask-(B,N), value is 0 or 1
    """
    B, N = match.shape
    B, M = gt_cls.shape
    # (B,N,M)
    gt_cls = np.broadcast_to(gt_cls[:,np.newaxis,:], (B,N,M))
    # (B,N)
    label_cls = np_pick(gt_cls, match, axis=-1) + 1
    label_cls = np.where(sample > 0.5, label_cls, np.ones_like(label_cls)*ignore_label)
    label_cls = np.where(sample < -0.5, np.zeros_like(label_cls), label_cls)
    # (B,N)
    label_mask = (label_cls > -0.5).astype('int')
    return label_cls, label_mask


def corner_to_center(box, split=False, eps=1e-12):
    """
    input:
        box-(B,N,4) or (N,4)
    output:
        (B,N,4) or (N,4) - split == False
        4x(B,N,1) or 4x(N,1) - split == True
    """
    shape = box.shape
    assert len(shape) in (2,3) and shape[-1] == 4
    # (B,N,1) or (N,1)
    xmin, ymin, xmax, ymax = np.split(box, 4, axis=-1)
    width = xmax - xmin
    height = ymax - ymin
    cx = xmin + width / 2
    cy = ymin + height / 2
    # 如果存在无效的gt bbox，那么width和height便为0，后续标注时
    # 会出现runtimewarning，所以这里加个eps
    width = np.where(width==0, np.full(width.shape, eps), width)
    height = np.where(height==0, np.full(height.shape, eps), height)
    result = [cx, cy, width, height]
    if split:
        return result
    else:
        return np.concatenate(result, axis=-1)


def label_offset(anchors, bbox, match, sample, 
                 means=(0,0,0,0), stds=(0.1,0.1,0.2,0.2), flatten=True):
    """
    input:
        anchors - (N,4)
        bbox - (B,M,4)
        match - (B,N)
        sample - (B,N)
    output:
        offset_mask - (B,N,4) or (B,N*4)
        anchor_offset - (B,N,4) or (B,N*4)
    """
    anchors = anchors.reshape((-1,4))
    N, _ = anchors.shape
    B, M, _ = bbox.shape
    # 4x(N,1)，转为center模式并拆开
    anchor_x, anchor_y, anchor_w, anchor_h = corner_to_center(anchors, split=True)
    
    # (B,M,4) -> (B,N,M,4)，为下面pick准备
    bbox = np.broadcast_to(bbox[:,np.newaxis,:,:], (B,N,M,4))
    # sample, (B,N,M,4) -> 4x(B,N,M) -> 4x(B,N) -> (B,N,4)
    # 取dbox分配到的gt的框
    bbox = np.stack([np_pick(np.take(bbox, p, axis=-1), match) for p in range(4)], axis=-1)
    # (B,N,4) -> 4x(B,N,1)，转为center模式并拆开
    bbox_x, bbox_y, bbox_w, bbox_h = corner_to_center(bbox, split=True)
    
    # (B,N,1)，标注过程
    offset_x = ((bbox_x - anchor_x) / anchor_w - means[0]) / stds[0]
    offset_y = ((bbox_y - anchor_y) / anchor_h - means[1]) / stds[1]
    offset_w = (np.log(bbox_w/anchor_w) - means[2]) / stds[2]
    offset_h = (np.log(bbox_h/anchor_h) - means[3]) / stds[3]
    # 4x(B,N,1) -> (B,N,4)，合并
    offset = np.concatenate((offset_x, offset_y, offset_w, offset_h), axis=-1)
    # (B,N) -> (B,N,4)
    # sample中为0和-1的都mask掉，因为localization loss只考虑正框
    sample = np.broadcast_to(sample[:,:,np.newaxis], (B,N,4)) > 0.5
    
    # (B,N,4)，将忽略的dbox和背景的dbox offset掩掉
    anchor_offset = np.where(sample, offset, np.zeros_like(offset))
    # 得到对应的掩码，后续训练使用
    anchor_mask = np.where(sample, np.ones_like(offset), np.zeros_like(offset))
    
    if flatten:
        anchor_offset = anchor_offset.reshape((B,-1))
        anchor_mask = anchor_mask.reshape((B,-1))
        
    return anchor_mask, anchor_offset



def get_label(anchor, gt_label_offset, cls_pred, match_threshould=0.5):
    gt = gt_label_offset[:,:,1:]
    gt_cls = gt_label_offset[:,:,0]
    cls_pred = cls_pred.asnumpy() 
    # anchor-(1,N,4), gt-(B,M,4)
    # iou-(B,N,M)
    iou = calIOU(anchor, gt)
    # iou-(B,N,M)
    # mat-(B,N)
    mat = match(iou, threshould=match_threshould, share_max=False)
    # mat-(B,N), cls_pred-(B,N,C+1), iou-(B,N,M)
    # samp-(B,N)
    samp = sample(mat, cls_pred, iou, ratio=3, min_sample=0, threshold=0.5, do=True)
    # mat-(B,N), samp-(B,N), gt_cls-(B,M)
    # label_cls-(B,N), label_mask-(B,N)
    label_cls, label_mask = label_box_cls(mat, samp, gt_cls, ignore_label=-1)
    # anchor-(1,N,4), gt-(B,M,4), mat-(B,N), samp-(B,N)
    # anchor_mask-(B,N*4), anchor_offset-(B,N*4)
    anchor_mask, anchor_offset = label_offset(anchor, gt, mat, samp)

    return label_cls, label_mask, anchor_offset, anchor_mask
