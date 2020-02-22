"""
本文件中的函数用于操作box。
包含计算两box的iou，根据特征图生存anchor box，
根据iou得到匹配结果，根据匹配结果进行负采样，
anchor box的类别及偏移标注。

谨记，这些函数的输入输出类型都是mxnet.NDArray的。
"""

import time
from mxnet import nd

class ctime():
    def __init__(self, prefix=''):
        print('\n')
        self.prefix = prefix
    def __enter__(self, prefix=''):
        self.begin = time.time()
    def __exit__(self, *args):
        print(self.prefix, ': %.4f'%(time.time()-self.begin))



def getwh(scales, ratios, fw, fh, srmode, ctx=None):
    """
        根据scales和ratios，以及特征图的宽高生成
        box的宽和高。srmode用于指定scales和ratios的组合形式。
        特征图上每个cell具有的box形状一致，所以这里就生成这些形状的宽高。
    输入：
        scales: 为处理好的一维NDArray
        ratios: 为处理好的一维NDArray
        fw: 特征图宽度
        fh: 特征图高度
        srmode: 
            'few': 只生成scales[0]和ratios以及scales[1:]和ratios[0]的box尺寸
            'many': 生成scales和所有ratios组合的box尺寸
    输出：
        width: 所有高度，为一维NDArray形式
        height: 对应的宽度，为一维NDArray形式
    """
    if srmode == 'few':
        # box的尺寸数量
        num = scales.size + ratios.size - 1
        # 用于存入各尺寸对应的宽高
        width = nd.zeros((num,), ctx=ctx)
        height = nd.zeros((num,), ctx=ctx)
        
        # 先将ratios中的值开方，以待后续使用
        sqt_ratios = nd.sqrt(ratios)

        # 先是ratios[0]与所有scale搭配
        width[:scales.size] = scales * sqt_ratios[0]
        height[:scales.size] = scales / sqt_ratios[0]
        # 然后是scales[0]与ratios[1:]搭配
        width[scales.size:] = scales[0] * sqt_ratios[1:]
        height[scales.size:] = scales[0] / sqt_ratios[1:]


    else:
        # 先是scales[0]与ratios，然后是scales[1]与ratios.....
        # nd.repeat是对每个元素进行重复
        # ratios.size个scales[0], ratios.size个scales[1],
        # ratios.size个scales[2], ratios.size个scales[2],......
        rscales = nd.repeat(scales, ratios.size)
        # nd.tile是将数组作为整体重复
        # scales.size个ratios
        rratios = nd.tile(ratios, scales.size)
        
        # 就是按元素乘除
        width = rscales * nd.sqrt(rratios)
        height = width / rratios
        
    # 将归一化的结果放大到特征图尺寸，
    # 后面再加上各个cell的中心点，得到所有像素点的box坐标
    width = width * fw
    height = height * fh
    
    return width, height


def getDefaultBoxes(fmap, scales, ratios, 
                    offset, norm, clip=False, 
                    srmode='few', omode='flatten'):
    """
        在输入特征图fmap上生成default boxes。
    输入：
        fmap:输入特征图，形状(n, c, h, w)，需要时NDArray
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
    ctx = fmap.context
    
    width, height = getwh(scales, ratios, fw, fh, srmode, ctx=ctx)
    
    nbox_per_pixel = width.size
    # 得到各个cel的xy坐标
    # (fh, fw)
    xcenter = nd.repeat(nd.arange(fw, ctx=ctx).reshape((1,-1)), fh, axis=0)
    ycenter = nd.repeat(nd.arange(fh, ctx=ctx).reshape((-1,1)), fw, axis=1)
    # (fh, fw, 2)
    xycenters = nd.stack(xcenter, ycenter, axis=2)
    # 在第三维上tile，是为了后面
    # (fh, fw, 4*nbox_per_pixel)
    xycenters = nd.tile(xycenters, [1, 1, nbox_per_pixel*2])
    

    # left-up and right-down points offset，相对于中心点的偏移
    # [nbox_per_pixel,4]
    lu_rd_offset = nd.stack(width*-0.5, height*-0.5, width*0.5, height*0.5, axis=1)

    # [4*nbox_per_pixel,]
    lu_rd_offset = lu_rd_offset.reshape((-1,))
    
    # (h, w, nbox_per_pixel, 2, 2)
    lu_rd_points = (xycenters + lu_rd_offset).reshape((fh, fw, nbox_per_pixel, 2, 2))
    # points get done!!!
    
    
    # 加上偏移，再归一化
    lu_rd_points = (lu_rd_points + offset) / norm
    
    if clip:
        nd.clip(lu_rd_points, a_min=0., a_max=1., out=lu_rd_points)
    
    if omode == 'flatten':
        # 左上x、左上y、右下x、右下y、...、repeat
        lu_rd_points = lu_rd_points.reshape((1, -1, 4))
    else:
        lu_rd_points = lu_rd_points.reshape((1, fh, fw, nbox_per_pixel, 4))
    
    return lu_rd_points


class BoxGenerator:
    """
    在SSD类中使用，用于生成并保存特定特征图上生成的default box
    """
    def __init__(self, scale=(1,), ratio=(1,), offset=(0.5,0.5), norm=None, clip=False, 
                 srmode='few', omode='flatten'):
        self.scale = nd.array(scale)
        self.ratio = nd.array(ratio)
        self.offset = nd.array(offset)
        self.norm = nd.array(norm) if norm is not None else None
        self.clip = clip
        self.srmode = srmode
        self.omode = omode
        self.box = None
    
    def __call__(self, feature):
        if self.box is not None:
            return self.box
        else:
            ctx = feature.context

            shape = feature.shape
            if self.norm is None:
                self.norm = nd.array(shape[-2:], ctx=ctx)
            self.scale = self.scale.as_in_context(ctx)
            self.ratio = self.ratio.as_in_context(ctx)
            self.offset = self.offset.as_in_context(ctx)

            self.box = getDefaultBoxes(feature, 
                        self.scale, self.ratio,
                        self.offset, self.norm, self.clip,
                        self.srmode, self.omode)
            return self.box



def calIOU(anchor, gt):
    """
        计算二者的IoU
    输入：    
        anchor形状-(N,4)或(4,)或(1,N,4)
        gt形状-(B,M,4)或(M,4)或(4,)
    输出：
        形状(B,N,M)    
    """
    anchor = anchor.as_in_context(gt.context)
    assert len(anchor.shape) in (1,2,3)
    assert len(gt.shape) in (1,2,3)
    
    anchor = anchor.reshape((-1,4))
    if len(gt.shape) < 3:
        gt = gt.reshape((1,1,4)) if len(gt.shape) == 1 else nd.expand_dims(gt, axis=0)
    # (N,4) to (N,1,4)
    # 扩展维数，为后续的broadcast做准备
    anchor = nd.expand_dims(anchor, axis=1)
    # (B,M,4) to (B,1,M,4)
    gt = nd.expand_dims(gt, axis=1)
    
    # (B,N,M,2)
    # maximum和minimum都会做broadcast，然后Element-wise比较
    max_tl = nd.maximum(anchor[:,:,:2], gt[:,:,:,:2])
    min_br = nd.minimum(anchor[:,:,2:], gt[:,:,:,2:])
    
    # (B,N,M)
    area = nd.prod(min_br-max_tl, axis=-1)
    # x,y 必须整体小于才表示有intersection
    # 当都小于时，才说明有相交
    # (B,N,M)
    i = nd.where((max_tl >= min_br).sum(axis=-1), nd.zeros_like(area), area)
    
    # (N,1)
    anchor_area = nd.prod(anchor[:,:,2:]-anchor[:,:,:2], axis=-1)
    # (B,1,M)
    gt_area = nd.prod(gt[:,:,:,2:]-gt[:,:,:,:2], axis=-1)
    # (B,N,M)
    total_area = anchor_area + gt_area - i
    iou = i / total_area
    
    return iou


def getUniqueMatch(iou, ctx=None, min_threshold=1e-12):
    """
        iou shape:(N,M)，需要在batch中for一下。
    """
    N, M = iou.shape
    iouf = iou.reshape((-1,))
    
    argmax = nd.argsort(iouf, is_ascend=False)
    argrow = nd.floor(nd.divide(argmax, M))
    argcol = nd.modulo(argmax, M)

    uniquel = set()
    uniquer = set()
    match = nd.ones((N,), ctx=ctx) * -1
    i = 0
    while True:
        if argcol[i].asscalar() not in uniquel and argrow[i].asscalar() not in uniquer:
            uniquel.add(argcol[i].asscalar())
            uniquer.add(argrow[i].asscalar())
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
    ctx = iou.context
    
    if share_max:
        result = nd.argmax(iou, axis=-1)
        result = nd.where(nd.max(iou, axis=-1) > threshould, result, nd.ones_like(result)*-1)
    else:
        # 论文第一步
        # [(1,N), ..., ]
        # match = [getUniqueMatch(i, ctx=ctx) for i in iou]
        # (B,N)
        # result = nd.concat(*match, dim=0)
        
        # 这个threshold一定不能太大，不然如果有的框特别偏，与所有的default box
        # 的iou的特别小，那么该gt的框就不会匹配到任何default box。
        # 会使训练的时候loss出现nan。因为除以0了。
        # 这个是bipartite matching，
        match = nd.contrib.bipartite_matching(iou, threshold=1e-12,
                                                 is_ascend=False)
        
        result = match[0]
        # 该匹配完之后，可能会存在一种情况，假如dbox_i以及与gt_j匹配了，
        # 但对于未匹配到的dbox_k，其与gt_j的IoU就比dbox_i的小一点或近似相等。
        # 但该IoU可能也小于threshold，所以在第二步中也匹配不到。
        # 所以在这里添加上
        # (B, N, 1)
        row_max = nd.max(iou, axis=-1, keepdims=True)
        # (B, N)
        row_argmax = nd.argmax(iou, axis=-1)
        # (B, 1, M)
        col_max = nd.max(iou, axis=-2, keepdims=True)
        # (B, N, M)
        mask = nd.greater_equal(row_max+1e-12, col_max)
        # (B, N)
        mask = nd.pick(mask, row_argmax, axis=-1)
        mask = nd.where(mask, row_argmax, nd.ones_like(row_argmax)*-1)

        result = nd.where(result < 0, mask, result)


        # (B,N)
        # 论文第二步
        argmax_row = nd.argmax(iou, axis=-1)
        max_row = nd.max(iou, axis=-1)
        argmax_row = nd.where(max_row > threshould, argmax_row, nd.ones_like(argmax_row)*-1)
        # 只有对于第一步中未匹配到的，进行分配
        result = nd.where(result > -0.5, result, argmax_row)
        
    return result


def sample(match, cls_pred, iou, ratio=3, min_sample=0, threshold=0.3, do=True):
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
        ones = nd.ones_like(match)
        sample = nd.where(match > -0.5, ones, ones*-1)
        return sample
    sample = nd.zeros_like(match)
    # 先确定负框数量
    # (B,)
    num_pos = nd.sum(match > -0.5, axis=-1)
    requre_neg = ratio * num_pos
    # (B,N) 值为1的表示可被采样的负框，0表示已经忽略了的负框及正框
    neg_mask = nd.where(match < -0.5, nd.max(iou, axis=-1) < threshold, nd.zeros_like(match))
    # 过滤掉IoU大的负框之后，最多有多少负框
    max_neg = neg_mask.sum(axis=-1)
    # 最终的负框数量，(B,)
    num_neg = nd.minimum(max_neg, nd.maximum(requre_neg, min_sample)).astype('int')
   
    #########################My###############################
    # # 得到各框的背景loss
    # # (B,N)
    # neg_prob = cls_pred[:,:,0]
    # # (B,N,1)
    # max_value = nd.max(cls_pred, axis=-1, keepdims=True)

    # # 就是log softmax，提高数值稳定性，(B,N)
    # score = max_value[:,:,0] - neg_prob + nd.log(
    #                                nd.sum(
    #                                nd.exp(cls_pred-max_value), axis=-1))

    ############################################################


    positive = cls_pred[:,:,1:]
    background = cls_pred[:,:,0:1].reshape((0, -1))
    maxval = positive.max(axis=2)
    esum = nd.exp(cls_pred - maxval.reshape((0, 0, 1))).sum(axis=2)
    score = -nd.log(nd.exp(background - maxval) / esum)


    # 将正框和已经忽略的负框的分数置为-1
    score = nd.where(neg_mask, score, nd.ones_like(score)*-1)
    # (B,N)，降序排序
    argmax = nd.argsort(score, axis=-1, is_ascend=False)
    
    # 负类置-1
    for i, num in enumerate(num_neg):
        indices = argmax[i, :num.asscalar()]
        sample[i, indices] = -1

    # (B,N)，正类置1
    sample = nd.where(match > -0.5, nd.ones_like(sample), sample)

    return sample


def label_box_cls(match, sample, gt_cls, ignore_label=-1):
    """
    input:
        match-(B,N)
        sample-(B,N)
        gt_cls-(B,M)
        ignore_label-set the value of the ignored sample's label
    output:
        label_cls-(B,N), value is [0, cls] or -1
    """
    B, N = match.shape
    B, M = gt_cls.shape
    # (B,N,M)
    gt_cls = gt_cls.reshape((B,1,M))
    gt_cls = nd.broadcast_to(gt_cls, (B,N,M))
    # (B,N)
    label_cls = nd.pick(gt_cls, match, axis=-1) + 1
    label_cls = nd.where(sample > 0.5, label_cls, nd.ones_like(label_cls)*ignore_label)
    label_cls = nd.where(sample < -0.5, nd.zeros_like(label_cls), label_cls)
    
    return label_cls


def corner_to_center(box, split=False, eps=1e-12):
    """
    input:
        box-(B,N,4) or (N,4)
    output:
        (B,N,4) or (N,4) - split == False
        4x(B,N,1) or 4x(N,1) - split == True
    """
    ctx = box.context
    shape = box.shape
    assert len(shape) in (2,3) and shape[-1] == 4
    # (B,N,1) or (N,1)
    xmin, ymin, xmax, ymax = nd.split(box, 4, axis=-1)
    width = xmax - xmin
    height = ymax - ymin
    cx = xmin + width / 2
    cy = ymin + height / 2
    # 如果存在无效的gt bbox，那么width和height便为0，后续标注时
    # 会出现runtimewarning，所以这里加个eps
    width = nd.where(width==0, nd.full(width.shape, eps, ctx=ctx), width)
    height = nd.where(height==0, nd.full(height.shape, eps, ctx=ctx), height)
    result = [cx, cy, width, height]
    if split:
        return result
    else:
        return nd.concat(*result, dim=-1)


def label_offset(anchors, bbox, match, sample, 
                 means=(0,0,0,0), stds=(0.1,0.1,0.2,0.2), flatten=False):
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
    bbox = bbox.reshape((B,1,M,4))
    bbox = nd.broadcast_to(bbox, (B,N,M,4))
    # sample, (B,N,M,4) -> 4x(B,N,M) -> 4x(B,N) -> (B,N,4)
    # 取dbox分配到的gt的框
    bbox = nd.stack(*[nd.pick(bbox[:,:,:,p], match) for p in range(4)], axis=-1)
    # (B,N,4) -> 4x(B,N,1)，转为center模式并拆开
    bbox_x, bbox_y, bbox_w, bbox_h = corner_to_center(bbox, split=True)
    
    # (B,N,1)，标注过程
    offset_x = ((bbox_x - anchor_x) / anchor_w - means[0]) / stds[0]
    offset_y = ((bbox_y - anchor_y) / anchor_h - means[1]) / stds[1]
    offset_w = (nd.log(bbox_w/anchor_w) - means[2]) / stds[2]
    offset_h = (nd.log(bbox_h/anchor_h) - means[3]) / stds[3]
    # 4x(B,N,1) -> (B,N,4)，合并
    offset = nd.concat(*(offset_x, offset_y, offset_w, offset_h), dim=-1)
    # (B,N) -> (B,N,4)
    # sample中为0和-1的都mask掉，因为localization loss只考虑正框
    sample = sample.reshape((B,N,1))
    sample = nd.broadcast_to(sample, (B,N,4)) > 0.5
    
    # (B,N,4)，将忽略的dbox和背景的dbox offset掩掉
    anchor_offset = nd.where(sample, offset, nd.zeros_like(offset))
    # 得到对应的掩码，后续训练使用
    anchor_mask = nd.where(sample, nd.ones_like(offset), nd.zeros_like(offset))
    
    if flatten:
        anchor_offset = anchor_offset.reshape((B,-1))
        anchor_mask = anchor_mask.reshape((B,-1))
        
    return anchor_offset, anchor_mask


def box_decode(box_preds, anchors, means=(0,0,0,0), stds=(0.1,0.1,0.2,0.2)):
    """
    对预测的anchor偏移进行解码，得到修正后的anchor坐标
    坐标形式为(左上x, 左上y, 右下x, 右下y)
    输入：
        box_preds: (B,N,4)
        anchors: (1,N,4)
    输出：
        decode: (B,N,4)
    """
    # first, convert anchors to center format
    # 4x(1,N,1), [cx, cy, width, height]
    a = corner_to_center(anchors, split=True)
    # (B,N,4) -> 4x(B,N,1)
    p = nd.split(box_preds, 4, axis=-1)
    # (B,N,1)
    x = (p[0] * stds[0] + means[0]) * a[2] + a[0]
    y = (p[1] * stds[1] + means[0]) * a[3] + a[1]
    # (B,N,1)
    w = nd.exp(p[2] * stds[2] + means[2]) * a[2] / 2
    h = nd.exp(p[3] * stds[3] + means[3]) * a[3] / 2
    # (B,N,4)
    return nd.concat(x-w, y-h, x+w, y+h, dim=-1)


def cls_decode(cls_pred, axis=-1, thresh=0.01):
    """
    根据网络对每一个anchor的各类别预测，输出分数大于thresh的所有类别的分数和类别号。
    小于thresh的类别标记为-1，分数为0.
    输入：
        num_cls：包含背景的类别总数
        cls_pred：(B,N,C+1)，网络类别预测输出
        axis：各类别的预测维度
        thresh: softmax之后的分数阈值，分数低于该值的输出类别标为-1，分数标为0
    输出：
        cls_id：（B,N,C)，不包含背景的类别编号，从0开始，-1表示为该类别分数小于thresh
        scores：（B,N,C)，对应的各类别的分数，0表示该类别的分数小于thresh
    """
    # 先对预测转为softmax分数
    cls_pred = nd.softmax(cls_pred, axis=axis)
    # (B,N,C) 除背景外的类别分数
    fore_score = nd.slice_axis(cls_pred, axis=axis, begin=1, end=None)
    B, N, C = fore_score.shape
    # (B,N,C)
    cls_id = nd.tile(nd.arange(C).reshape((1,1,C)), (B,N,1))
    mask = fore_score > thresh

    cls_id = nd.where(mask, cls_id, nd.ones_like(cls_id) * -1)
    scores = nd.where(mask, fore_score, nd.zeros_like(fore_score))
    return cls_id, scores


def get_label(anchor, gt_label_offset, cls_pred, match_threshould=0.5,
              do_samp=True):
    gt = gt_label_offset[:,:,1:]
    gt_cls = gt_label_offset[:,:,0]
    # anchor-(1,N,4), gt-(B,M,4)
    # iou-(B,N,M)
    iou = calIOU(anchor, gt)
    # iou-(B,N,M)
    # mat-(B,N)
    mat = match(iou, threshould=match_threshould, share_max=False)
    # mat-(B,N), cls_pred-(B,N,C+1), iou-(B,N,M)
    # samp-(B,N)
    samp = sample(mat, cls_pred, iou, ratio=3, min_sample=0, threshold=0.3, do=do_samp)
    # mat-(B,N), samp-(B,N), gt_cls-(B,M)
    # label_cls-(B,N), label_mask-(B,N)
    label_cls = label_box_cls(mat, samp, gt_cls, ignore_label=-1)
    # anchor-(1,N,4), gt-(B,M,4), mat-(B,N), samp-(B,N)
    # anchor_mask-(B,N,4), anchor_offset-(B,N,4)
    anchor_offset, anchor_mask = label_offset(anchor, gt, mat, samp, flatten=False)

    return label_cls, anchor_offset, anchor_mask
