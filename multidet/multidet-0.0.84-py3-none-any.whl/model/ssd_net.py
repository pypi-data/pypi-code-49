from .vgg_base import get_VGG16Feature
from .box import BoxGenerator, box_decode, cls_decode
from mxnet.gluon import nn
from mxnet import nd
import mxnet as mx
import time


scales = [[0.1, 0.14], [0.2, 0.27], [0.37, 0.44], 
          [0.54, 0.62], [0.71, 0.79], [0.88, 0.96]]
ratios = [[1,2,0.5], [1,2,3,0.5,1/3], [1,2,3,0.5,1/3], 
          [1,2,3,0.5,1/3], [1,2,0.5], [1,2,0.5]]


class SSD(nn.Block):
    def __init__(self, base_net, scales, ratios, num_cls=20, 
                 init=None, nms_thresh=0.45, nms_topk=400, post_nms=100,**kwargs):
        super(SSD, self).__init__(**kwargs)
        assert len(scales) == len(ratios)
        if init is None:
            self.init = {'weight_initializer': mx.init.Xavier(
                        rnd_type='gaussian', factor_type='out', magnitude=2),
                        'bias_initializer': 'zeros'}
        else:
            self.init = init

        self.base_net = base_net()
        self.scales = list(scales)
        self.ratios = list(ratios)
        self.num_cls = num_cls

        self.nms_thresh = nms_thresh
        self.nms_topk = nms_topk
        self.post_nms = post_nms

        
        # 建立类别预测和偏移预测层
        self.cls_preds = nn.Sequential(prefix='cls_pred_')
        self.box_preds = nn.Sequential(prefix='box_pred_')
        self.anch_gens = []

        for i, (scale, ratio) in enumerate(zip(self.scales, self.ratios)):
            num_box = len(scale) + len(ratio) - 1
            with self.cls_preds.name_scope():
                cls_pred = self._get_pred(num_box, self.num_cls, mode='cls')
            with self.box_preds.name_scope():
                box_pred = self._get_pred(num_box, mode='offset')
            anch_gen = BoxGenerator(scale, ratio)

            self.cls_preds.add(cls_pred)
            self.box_preds.add(box_pred)
            self.anch_gens.append(anch_gen)
        

    def _get_pred(self, num_box, num_cls='', mode='cls', prefix=None):
        """
        根据传入的mode，确定是类别预测层还是偏移预测层。
        """
        assert mode in ('cls', 'offset')
        if mode == 'cls':
            channels = (num_cls + 1) * num_box
        else:
            channels = 4 * num_box
        # 输出层不要有激活函数
        blk = nn.Conv2D(channels, kernel_size=3, strides=1, padding=1, 
                        prefix=prefix, **self.init)
        return blk
        
    def forward(self, x):
        features = self.base_net(x)
        
        cls_preds = []
        offset_preds = []
        dboxes = []
        for f, clsp, boxp, anchg in zip(features, self.cls_preds, self.box_preds, self.anch_gens):
            cls_preds.append(clsp(f).transpose((0,2,3,1)).flatten())
            
            offset_preds.append(boxp(f).transpose((0,2,3,1)).flatten())
            
            dboxes.append(anchg(f))

        # (B, num_box, cls+1)
        cls_preds = nd.concat(*cls_preds, dim=1).reshape((0, -1, self.num_cls+1))
        # (B, num_box*4) -> (B, N, 4)
        box_preds = nd.concat(*offset_preds, dim=1).reshape((0, -1, 4))
        # (1, num_box, 4)
        anchors = nd.concat(*dboxes, dim=1).reshape((1, -1, 4))

        if mx.autograd.is_training():
            return cls_preds, box_preds, anchors

        # (B,N,4)
        boxes = box_decode(box_preds, anchors)
        # (B,N,C) (B,N,C)
        cls_ids, scores = cls_decode(cls_preds)

        results = []
        for i in range(self.num_cls):
            # (B,N,1)
            cls_id = cls_ids.slice_axis(axis=-1, begin=i, end=i+1)
            # (B,N,1)
            score = scores.slice_axis(axis=-1, begin=i, end=i+1)
            # per class results
            # (B,N,6), （类别，分数，左上x，左上y，右下x，右下y）
            per_result = nd.concat(*[cls_id, score, boxes*300], dim=-1)
            results.append(per_result)

        # C x (B,N,6) -> (B,CxN, 6)
        result = nd.concat(*results, dim=1)

        if self.nms_thresh > 0 and self.nms_thresh < 1:
            # (B,CxN,6)
            result = nd.contrib.box_nms(
                result, overlap_thresh=self.nms_thresh, topk=self.nms_topk, valid_thresh=0.01,
                id_index=0, score_index=1, coord_start=2, force_suppress=False)
            if self.post_nms > 0:
                # (B, post_nms, 6)
                result = result.slice_axis(axis=1, begin=0, end=self.post_nms)

        # (B, post_nms, 1)
        ids = nd.slice_axis(result, axis=2, begin=0, end=1)
        # (B, post_nms, 1)
        scores = nd.slice_axis(result, axis=2, begin=1, end=2)
        # (B, post_nms, 4)
        bboxes = nd.slice_axis(result, axis=2, begin=2, end=6)

        return ids, scores, bboxes


def get_SSD300():
    """
    no parameter, just call it
    """
    base_net = get_VGG16Feature
    ssd = SSD(base_net, scales, ratios)
    return ssd