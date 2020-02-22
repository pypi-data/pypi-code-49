from multidet.model import get_label
from mxnet.gluon.loss import SoftmaxCrossEntropyLoss, HuberLoss
from time import time
import mxnet as mx
from mxnet.gluon import utils as gutils
import logging
import argparse
from multidet import data
from multidet import model
from multidet.utils import get_gpu
from mxnet import nd, gluon


def _as_list(arr):
    """Make sure input is a list of mxnet NDArray"""
    if not isinstance(arr, (list, tuple)):
        return [arr]
    return arr


class SSDMultiBoxLoss(gluon.Block):
    def __init__(self, rho=1.0, lambd=1.0, **kwargs):
        super(SSDMultiBoxLoss, self).__init__(**kwargs)
        self._rho = rho
        self._lambd = lambd
                    # (B,N,c+1), (B,N,4), (B,N),      (B,N,4),    (B,N,4)
    def forward(self, cls_pred, box_pred, cls_target, box_target, box_mask):
        """Compute loss in entire batch across devices."""
        # require results across different devices at this time
        cls_pred, box_pred, cls_target, box_target, box_mask = [_as_list(x) \
            for x in (cls_pred, box_pred, cls_target, box_target, box_mask)]
        # cross device reduction to obtain positive samples in entire batch
        num_pos = []
        for ct in cls_target:
            pos_samples = (ct > 0)
            num_pos.append(pos_samples.sum())
        num_pos_all = sum([p.asscalar() for p in num_pos])

        # compute element-wise cross entropy loss and sort, then perform negative mining
        cls_losses = []
        box_losses = []
        sum_losses = []            #   (B,N,c+1), (B,N,4),  (B,N),      (B,N,4),    (B,N,4)
        for cp, bp, ct, bt, bm in zip(*[cls_pred, box_pred, cls_target, box_target, box_mask]):
            # (B,N,c+1)
            pred = nd.log_softmax(cp, axis=-1)
            # (B,N)
            cls_loss = -nd.pick(pred, ct, axis=-1, keepdims=False)
            # (B,N)
            pos = ct >= 0
            # (B,N)
            cls_loss = nd.where(pos, cls_loss, nd.zeros_like(cls_loss))
            # append (B,)
            cls_losses.append(nd.sum(cls_loss, axis=0, exclude=True) / max(1., num_pos_all))

            # (B,N,4)
            box_loss = nd.abs(bp - bt) * bm
            # (B,N,4)
            box_loss = nd.where(box_loss > self._rho, box_loss - 0.5 * self._rho,
                                (0.5 / self._rho) * nd.square(box_loss))
            # append (B,)
            box_losses.append(nd.sum(box_loss, axis=0, exclude=True) / max(1., num_pos_all))
            
            sum_losses.append(cls_losses[-1] + self._lambd * box_losses[-1])

        return sum_losses, cls_losses, box_losses


def cls_eval(cls_preds, cls_labels, cls_masks):
    a = ((cls_preds.argmax(axis=-1) == cls_labels)*cls_masks).sum().asscalar()
    return a / cls_masks.sum().asscalar()

def bbox_eval(bbox_preds, bbox_labels, bbox_masks):
    a = ((bbox_labels - bbox_preds) * bbox_masks).abs().sum().asscalar()
    return a / bbox_masks.sum().asscalar() * 4

def ssd_train_batch(model, X, y, trainer, loss, batch_size, evals, ctx):
    Xs = gutils.split_and_load(X, ctx_list=ctx)
    ys = gutils.split_and_load(y, ctx_list=ctx)

    with mx.autograd.record():
        cls_preds = []
        box_preds = []
        anchors = []

        # (cls_pred, box_pred, anchor)...
        for xi in Xs:
            cls_pred, box_pred, anchor = model(xi)
            cls_preds.append(cls_pred)
            box_preds.append(box_pred)
            anchors.append(anchor)

        cls_targets = []
        box_targets = []
        box_masks = []
        with mx.autograd.pause():
            # (cls_targets, cls_mask, box_targets, box_masks, num_positive)...
            for anchor, yi, cls_pred in zip(anchors, ys, cls_preds):
                cls_target, box_target, box_mask = get_label(anchor, yi, cls_pred)
                
                cls_targets.append(cls_target)
                box_targets.append(box_target)
                box_masks.append(box_mask)

        sum_loss, cls_loss, box_loss = loss[0](
                    cls_preds, box_preds, cls_targets, box_targets, box_masks)

        # mx.autograd.backward(sum_loss)
    for l in sum_loss:
        l.backward()

    trainer.step(1)
    print(sum_loss)

    # 只统计第一个gpu上的loss
    # [number, number, number]，返回后求和，然后除以批次
    batch_loss =  [cls_loss[0].sum().asscalar(), \
                   box_loss[0].sum().asscalar()]

    # 只统计第一个gpu上的精度
    # [number, number]，返回后求和，然后除以批次
    batch_acc = [evals[0](cls_preds[0], cls_targets[0], \
                          # 过滤掉背景的预测准确率
                          cls_targets[0]>0), \
                 evals[1](box_pred[0], box_targets[0], \
                          box_masks[0])]

    return batch_loss, batch_acc, cls_loss, box_loss

# SoftmaxCrossEntropyLoss的hybrid_forward中，最后会求个平均值：
# return loss.mean(axis=self._batch_axis, exclude=True)
# 这样的话loss就太小了
# 同样，HuberLoss也是如此。

SSDloss = [SSDMultiBoxLoss()]
SSDeval = [cls_eval, bbox_eval]


def model_train(model, train_iter, num_epoch, trainer, batch_size,
                loss, evals, val_iter=None, ctx=None, logger=None):

    ce_metric = mx.metric.Loss('CrossEntropy')
    smoothl1_metric = mx.metric.Loss('SmoothL1')

    for epoch in range(num_epoch):
        cls_loss, offset_loss = 0.0, 0.0
        cls_acc, box_acc = 0.0, 0.0

        ce_metric.reset()
        smoothl1_metric.reset()

        start = time()
        i = 0

        for X, y in train_iter:
            batch_start = time()
            i += 1
            batch_loss, batch_acc, closses, blosses = ssd_train_batch(model, X, y,
                                    trainer, loss, batch_size, evals, ctx)
    
            cls_loss += batch_loss[0]
            offset_loss += batch_loss[1]

            cls_acc += batch_acc[0]
            box_acc += batch_acc[1]
            
            ############################################################
            ce_metric.update(0, [l * batch_size for l in closses])
            smoothl1_metric.update(0, [l * batch_size for l in blosses])
            name1, loss1 = ce_metric.get()
            name2, loss2 = smoothl1_metric.get()

            logger.info('[epoch {}][batch {}], time:{:.1f}s'.format(epoch, i, time()-batch_start))
            logger.info('\tcls acc:{:.3e}, box acc:{:.3e}, {}:{:.4e}, {}:{:.4e}'.
                        format(cls_acc/i, box_acc/i, name1, loss1, name2, loss2))
                                                    # cls_loss/i
            
            
        logger.info('[epoch {}], time:{:.1f}s'.format(epoch, time()-start))
        logger.info('\tcls acc:{:.3e}, box acc:{:.3e}, cls loss:{:.4e}, box loss:{:.4e}'.
                    format(cls_acc/i, box_acc/i, cls_loss/i, offset_loss/i))
        
        logger.info('==========================================================')

        
        model.save_parameters('ssd-params_epoch%d.param'%epoch)

        # for c in ctx:
        #     c.empty_cache()


def parse_args():
    parser = argparse.ArgumentParser(description='Train SSD300.')
    parser.add_argument('idx', help='the path of idx file')
    parser.add_argument('rec', help='the path of rec file')
    parser.add_argument('--pre', dest='pre_params', default=None,
                        help='pretrained weight path')
    parser.add_argument('--base', dest='base_weight', default=None,
                        help='the paht of the weight of vggbase network')
    parser.add_argument('--batch', dest='batch_num', type=int, default=32,
                        help='the data batch number')
    parser.add_argument('--epoch', dest='epoch_num', type=int, default=100,
                        help='the train epoch number')
    parser.add_argument('--lr', dest='lr', type=float, default=1e-3,
                        help='the learning rate')
    parser.add_argument('--wd', dest='wd', type=float, default=0.0005,
                        help='the weight decay')
    parser.add_argument('--momentum', dest='momentum', type=float, default=0.9,
                        help='the momentum for sgd')
    parser.add_argument('--log', dest='log_path', default='./logging.log')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    # data
    train_iter = data.DataIter(args.idx, args.rec, batch_size=args.batch_num,
                               shuffle=True, aug_list=data.auglist_full)
    ctx = get_gpu()

    # model
    ssd = model.get_SSD300()
    ssd.initialize(ctx=ctx)

    if args.pre_params is not None:
        ssd.load_parameters(args.pre_params)

    elif args.base_weight is not None:
        preparams = nd.load(args.base_weight)
        for key in preparams.keys():
            ssd.base_net.collect_params()[key].set_data(preparams[key])

    # trainer
    trainer = gluon.Trainer(ssd.collect_params(), 'sgd', 
                            {'learning_rate':args.lr,
                             'wd':args.wd,
                             'momentum':args.momentum})

    # logger
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(args.log_path)
    logger.addHandler(fh)
    logger.info('Config Done, begin training. training on {!r}'.format(ctx))

    model_train(ssd, train_iter, args.epoch_num, trainer, args.batch_num,
                SSDloss, SSDeval, val_iter=None, ctx=ctx, logger=logger)




