import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import random
from torch.autograd import Variable
import numpy as np
from math import *
from torch.nn.modules.loss import  _Loss, _WeightedLoss
from torch.nn import init
from torch.nn import _reduction as _Reduction
from ..backend.common import *
from ..backend.pytorch_backend import *
from ..backend.pytorch_ops import *

_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
_session=get_session()

__all__ = ['MSELoss','CrossEntropyLoss','F1ScoreLoss', 'make_onehot', 'MS_SSIM', 'CrossEntropyLabelSmooth', 'mixup_criterion', 'DiceLoss', 'FocalLoss', 'SoftIoULoss', 'CenterLoss', 'TripletLoss', 'LovaszSoftmax','PerceptionLoss','EdgeLoss','TransformInvariantLoss','get_loss']

class CrossEntropyLoss(nn.CrossEntropyLoss):
    def __init__(self, weight=1, ignore_index=-100, reduction='mean',name='CrossEntropyLoss'):
        super().__init__()
        self.name=name
        self.ignore_index=ignore_index
        self.reduction=reduction
        self.reduce=True
        self.size_average=True






class MSELoss(nn.MSELoss):
    def __init__(self,  reduction='mean', name='MSELoss'):
        super(MSELoss, self).__init__(reduction)
        self.name=name
        self.reduction = reduction






def make_onehot(labels, classes):
    one_hot_shape=list(labels.size())
    one_hot_shape.insert(1,classes)
    one_hot = torch.zeros(tuple(one_hot_shape)).to(_device)
    target = one_hot.scatter_(1, labels.unsqueeze(1).data, 1)
    return target

def gaussian(window_size, sigma):
    gauss = torch.Tensor([exp(-(x - window_size//2)**2/float(2*sigma**2)) for x in range(window_size)])
    return gauss/gauss.sum()

def create_window(window_size, sigma, channel):
    _1D_window = gaussian(window_size, sigma).unsqueeze(1)
    _2D_window = _1D_window.mm(_1D_window.t()).float().unsqueeze(0).unsqueeze(0)
    window = Variable(_2D_window.expand(channel, 1, window_size, window_size).contiguous())
    return window

class MS_SSIM(_Loss):
    def __init__(self, reduction='mean', max_val = 255):
        super(MS_SSIM, self).__init__()
        self.reduction = reduction
        self.channel = 3
        self.max_val = max_val
    def _ssim(self, img1, img2, size_average = True):
        _, c, w, h = img1.size()
        window_size = min(w, h, 11)
        sigma = 1.5 * window_size / 11
        window = create_window(window_size, sigma, self.channel).to(_device)
        mu1 = F.conv2d(img1, window, padding = window_size//2, groups = self.channel)
        mu2 = F.conv2d(img2, window, padding = window_size//2, groups = self.channel)

        mu1_sq = mu1.pow(2)
        mu2_sq = mu2.pow(2)
        mu1_mu2 = mu1*mu2

        sigma1_sq = F.conv2d(img1*img1, window, padding = window_size//2, groups = self.channel) - mu1_sq
        sigma2_sq = F.conv2d(img2*img2, window, padding = window_size//2, groups = self.channel) - mu2_sq
        sigma12 = F.conv2d(img1*img2, window, padding = window_size//2, groups = self.channel) - mu1_mu2

        C1 = (0.01*self.max_val)**2
        C2 = (0.03*self.max_val)**2
        V1 = 2.0 * sigma12 + C2
        V2 = sigma1_sq + sigma2_sq + C2
        ssim_map = ((2*mu1_mu2 + C1)*V1)/((mu1_sq + mu2_sq + C1)*V2)
        mcs_map = V1 / V2
        if self.reduction=='mean':
            return ssim_map.mean(), mcs_map.mean()
        else:
            return ssim_map.sum(), mcs_map.sum()

    def ms_ssim(self, img1, img2, levels=5):

        weight = Variable(torch.Tensor([0.0448, 0.2856, 0.3001, 0.2363, 0.1333]).cuda())

        msssim = Variable(torch.Tensor(levels,).to(_device))
        mcs = Variable(torch.Tensor(levels,).to(_device))
        for i in range(levels):
            ssim_map, mcs_map = self._ssim(img1, img2)
            msssim[i] = ssim_map
            mcs[i] = mcs_map
            filtered_im1 = F.avg_pool2d(img1, kernel_size=2, stride=2)
            filtered_im2 = F.avg_pool2d(img2, kernel_size=2, stride=2)
            img1 = filtered_im1
            img2 = filtered_im2
        value = (torch.prod(mcs[0:levels-1]**weight[0:levels-1])* (msssim[levels-1]**weight[levels-1]))
        return value

    def forward(self, img1, img2):
        return self.ms_ssim(img1, img2)

class CrossEntropyLabelSmooth(_Loss):
    def __init__(self, num_classes,reduction='mean' ):
        super(CrossEntropyLabelSmooth, self).__init__()
        self.num_classes = num_classes
        self.logsoftmax = nn.LogSoftmax(dim=1)

    def forward(self, inputs, targets):
        log_probs = self.logsoftmax(inputs)
        targets = torch.zeros_like(log_probs).scatter_(1, targets.unsqueeze(1), 1)

        smooth = np.random.choice(np.arange(0, 0.12, 0.01))
        targets = (1 - smooth) * targets + smooth / self.num_classes
        loss = (-targets * log_probs).mean(0).sum()
        return loss





def mixup_criterion(y_a, y_b, lam):
    return lambda criterion, pred: lam * criterion(pred, y_a) + (1 - lam) * criterion(pred, y_b)



class DiceLoss(nn.Module):
    def __init__(self, smooth=1., ignore_index=0):
        super(DiceLoss, self).__init__()
        self.ignore_index = ignore_index
        self.smooth = smooth
    def forward(self, output, target):
        if self.ignore_index not in range(target.min(), target.max()):
            if (target == self.ignore_index).sum() > 0:
                target[target == self.ignore_index] = target.min()
        target = make_onehot(target.unsqueeze(dim=1), classes=output.size()[1])
        output = F.softmax(output, dim=1)
        output_flat = output.contiguous().view(-1)
        target_flat = target.contiguous().view(-1)
        intersection = (output_flat * target_flat).sum()
        loss = 1 - ((2. * intersection + self.smooth) / (output_flat.sum() + target_flat.sum() + self.smooth))
        return loss



def focal_loss_with_logits(
    input: torch.Tensor,
    target: torch.Tensor,
    gamma=2.0,
    alpha = 0.25,
    reduction="mean",
    normalized=False,
    threshold = None,
) -> torch.Tensor:
    """Compute binary focal loss between target and output logits.

    See :class:`~pytorch_toolbelt.losses.FocalLoss` for details.

    Args:
        input: Tensor of arbitrary shape
        target: Tensor of the same shape as input
        reduction (string, optional): Specifies the reduction to apply to the output:
            'none' | 'mean' | 'sum' | 'batchwise_mean'. 'none': no reduction will be applied,
            'mean': the sum of the output will be divided by the number of
            elements in the output, 'sum': the output will be summed. Note: :attr:`size_average`
            and :attr:`reduce` are in the process of being deprecated, and in the meantime,
            specifying either of those two args will override :attr:`reduction`.
            'batchwise_mean' computes mean loss per sample in batch. Default: 'mean'
        normalized (bool): Compute normalized focal loss (https://arxiv.org/pdf/1909.07829.pdf).
        threshold (float, optional): Compute reduced focal loss (https://arxiv.org/abs/1903.01347).
    References::

        https://github.com/open-mmlab/mmdetection/blob/master/mmdet/core/loss/losses.py
    """
    target = target.type(input.type())

    logpt = -F.binary_cross_entropy_with_logits(input, target, reduction="none")
    pt = torch.exp(logpt)

    # compute the loss
    if threshold is None:
        focal_term = (1 - pt).pow(gamma)
    else:
        focal_term = ((1.0 - pt) / threshold).pow(gamma)
        focal_term[pt < threshold] = 1

    loss = -focal_term * logpt

    if alpha is not None:
        loss = loss * (alpha * target + (1 - alpha) * (1 - target))

    if normalized:
        norm_factor = focal_term.sum()
        loss = loss / norm_factor

    if reduction == "mean":
        loss = loss.mean()
    if reduction == "sum":
        loss = loss.sum()
    if reduction == "batchwise_mean":
        loss = loss.sum(0)
    return loss






class FocalLoss(_Loss):
    def __init__(self, alpha=0.5, gamma=2, ignore_index=None ,reduction="mean",reduced=False):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.ignore_index = ignore_index
        self.reduction=reduction
        self.reduced=reduced

    def forward(self, input, target):

        num_classes = input.size(1)
        if target.dtype == torch.int64:
            target_tensor =make_onehot(target, num_classes)
        loss = 0

        # Filter anchors with -1 label from loss computation
        if self.ignore_index is not None:
            not_ignored = target != self.ignore_index

        for cls in range(num_classes):
            cls_target = (target == cls).long()
            cls_input = input[:, cls, ...]

            if self.ignore_index is not None:
                cls_target = cls_target[not_ignored]
                cls_input = cls_input[not_ignored]

            loss =loss+ focal_loss_with_logits(
                cls_input, cls_target, gamma=self.gamma, alpha=self.alpha,reduction=self.reduction
            )
        return loss.sum()

class SoftIoULoss(_Loss):
    def __init__(self, n_classes,reduction="mean",reduced=False):
        super(SoftIoULoss, self).__init__()
        self.n_classes = n_classes
        self.reduction = reduction
        self.reduced = reduced

    def forward(self, input, target):
        # logit => N x Classes x H x W
        # target => N x H x W

        N = len(input)

        pred = F.softmax(input, dim=1)
        target_onehot = make_onehot(target, self.n_classes)

        # Numerator Product
        inter = pred * target_onehot
        # Sum over all pixels N x C x H x W => N x C
        inter = inter.view(N, self.n_classes, -1).sum(2)

        # Denominator
        union = pred + target_onehot - (pred * target_onehot)
        # Sum over all pixels N x C x H x W => N x C
        union = union.view(N, self.n_classes, -1).sum(2)

        loss = inter / (union + 1e-16)

        # Return average loss over classes and batch
        return -loss.mean()

def _lovasz_grad(gt_sorted):
    """
    Computes gradient of the Lovasz extension w.r.t sorted errors
    See Alg. 1 in paper
    """
    p = len(gt_sorted)
    gts = gt_sorted.sum()
    intersection = gts - gt_sorted.float().cumsum(0)
    union = gts + (1 - gt_sorted).float().cumsum(0)
    jaccard = 1. - intersection / union
    if p > 1:  # cover 1-pixel case
        jaccard[1:p] = jaccard[1:p] - jaccard[0:-1]
    return jaccard


class LovaszSoftmax(_Loss):
    def __init__(self, reduction="mean",reduced=False):
        super(LovaszSoftmax, self).__init__()
        self.reduction = reduction
        self.reduced = reduced
        self.num_classes=None

    def prob_flatten(self, input, target):
        assert input.dim() in [4, 5]
        num_class = input.size(1)
        if input.dim() == 4:
            input = input.permute(0, 2, 3, 1).contiguous()
            input_flatten = input.view(-1, num_class)
        elif input.dim() == 5:
            input = input.permute(0, 2, 3, 4, 1).contiguous()
            input_flatten = input.view(-1, num_class)
        target_flatten = target.view(-1)
        return input_flatten, target_flatten

    def lovasz_softmax_flat(self, inputs, targets):
        num_classes = inputs.size(1)
        losses = []
        for c in range(num_classes):
            target_c = (targets == c).float()
            if num_classes == 1:
                input_c = inputs[:, 0]
            else:
                input_c = inputs[:, c]
            loss_c = (torch.autograd.Variable(target_c) - input_c).abs()
            loss_c_sorted, loss_index = torch.sort(loss_c, 0, descending=True)
            target_c_sorted = target_c[loss_index]
            losses.append(torch.dot(loss_c_sorted, torch.autograd.Variable(_lovasz_grad(target_c_sorted))))
        losses = torch.stack(losses)

        if self.reduction == 'none':
            loss = losses
        elif self.reduction == 'sum':
            loss = losses.sum()
        else:
            loss = losses.mean()
        return loss

    def flatten_binary_scores(self,scores, labels, ignore=None):
        """
        Flattens predictions in the batch (binary case)
        Remove labels equal to 'ignore'
        """
        scores = scores.view(-1)
        labels = labels.view(-1)
        if ignore is None:
            return scores, labels
        valid = (labels != ignore)
        vscores = scores[valid]
        vlabels = labels[valid]
        return vscores, vlabels
    def lovasz_hinge(self,logits, labels, per_image=True, ignore=None):
        """
        Binary Lovasz hinge loss
          logits: [B, H, W] Variable, logits at each pixel (between -\infty and +\infty)
          labels: [B, H, W] Tensor, binary ground truth masks (0 or 1)
          per_image: compute the loss per image instead of per batch
          ignore: void class id
        """
        if per_image:
            loss = (self.lovasz_hinge_flat(*self.flatten_binary_scores(log.unsqueeze(0), lab.unsqueeze(0), ignore))
                 for log, lab in zip(logits, labels)).mean()
        else:
            loss = self.lovasz_hinge_flat(*self.flatten_binary_scores(logits, labels, ignore))
        return loss

    def lovasz_hinge_flat(self,logits, labels):
        """
        Binary Lovasz hinge loss
          logits: [P] Variable, logits at each prediction (between -\infty and +\infty)
          labels: [P] Tensor, binary ground truth labels (0 or 1)
          ignore: label to ignore
        """
        if len(labels) == 0:
            # only void pixels, the gradients should be 0
            return logits.sum() * 0.
        signs = 2. * labels.float() - 1.
        errors = (1. - logits * torch.tensor(signs,requires_grad=True))
        errors_sorted, perm = torch.sort(errors, dim=0, descending=True)
        perm = perm.data
        gt_sorted = labels[perm]
        grad = _lovasz_grad(gt_sorted)
        loss = torch.dot(F.relu(errors_sorted), Variable(grad))
        return loss

    def forward(self, inputs, targets):
        # print(inputs.shape, targets.shape) # (batch size, class_num, x,y,z), (batch size, 1, x,y,z)
        self.num_classes=inputs.size(1)
        inputs, targets = self.prob_flatten(inputs, targets)

        # print(inputs.shape, targets.shape)

        losses = self.lovasz_softmax_flat(inputs, targets) if self.num_classes>2 else self.lovasz_hinge_flat(inputs, targets)
        return losses

class TripletLoss(_Loss):
    """Triplet loss with hard positive/negative mining.
    Reference:
        Hermans et al. In Defense of the Triplet Loss for Person Re-Identification. arXiv:1703.07737.
    Imported from `<https://github.com/Cysu/open-reid/blob/master/reid/loss/triplet.py>`_.

    Args:
        margin (float, optional): margin for triplet. Default is 0.3.
    """

    def __init__(self, global_feat, labels,margin=0.3,reduction="mean",reduced=False):
        super(TripletLoss, self).__init__()
        self.reduction = reduction
        self.reduced = reduced
        self.margin = margin
        self.ranking_loss = nn.MarginRankingLoss(margin=margin,reduction=reduction)

    def forward(self, inputs, targets):
        """
        Args:
            inputs (torch.Tensor): feature matrix with shape (batch_size, feat_dim).
            targets (torch.LongTensor): ground truth labels with shape (num_classes).
        """
        n = inputs.size(0)
        # Compute pairwise distance, replace by the official when merged
        dist = torch.pow(inputs, 2).sum(dim=1, keepdim=True).expand(n, n)
        dist = dist + dist.t()
        dist.addmm_(1, -2, inputs, inputs.t())
        dist = dist.clamp(min=1e-12).sqrt()  # for numerical stability
        # For each anchor, find the hardest positive and negative
        mask = targets.expand(n, n).eq(targets.expand(n, n).t())
        dist_ap, dist_an = [], []
        for i in range(n):
            dist_ap.append(dist[i][mask[i]].max().unsqueeze(0))
            dist_an.append(dist[i][mask[i] == 0].min().unsqueeze(0))
        dist_ap = torch.cat(dist_ap)
        dist_an = torch.cat(dist_an)
        # Compute ranking hinge loss
        y = torch.ones_like(dist_an)
        if self.reduction=='mean':
            return  self.ranking_loss(dist_an, dist_ap, y).mean()
        else:
            return  self.ranking_loss(dist_an, dist_ap, y).sum()



class CenterLoss(_Loss):
    """Center loss.
    Reference:
    Wen et al. A Discriminative Feature Learning Approach for Deep Face Recognition. ECCV 2016.

    Args:
        num_classes (int): number of classes.
        feat_dim (int): feature dimension.
    """
    def __init__(self, num_classes=751, feat_dim=2048, reduction="mean",reduced=False):
        super(CenterLoss, self).__init__()
        self.reduction = reduction
        self.reduced = reduced
        self.num_classes = num_classes
        self.feat_dim = feat_dim
        self.centers = nn.Parameter(torch.randn(self.num_classes, self.feat_dim))
        init.kaiming_uniform_(self.centers,a=sqrt(5))
        self.to(_device)

    def forward(self, x, labels):
        """
        Args:
            x: feature matrix with shape (batch_size, feat_dim).
            labels: ground truth labels with shape (num_classes).

        """
        assert x.size(0) == labels.size(0), "features.size(0) is not equal to labels.size(0)"
        batch_size = x.size(0)
        distmat = torch.pow(x, 2).sum(dim=1, keepdim=True).expand(batch_size, self.num_classes) +  torch.pow(self.centers, 2).sum(dim=1, keepdim=True).expand(self.num_classes, batch_size).t()
        distmat.addmm_(1, -2, x,self.centers.t())
        classes = torch.arange(self.num_classes).long().to(_device)

        labels = labels.unsqueeze(1).expand(batch_size, self.num_classes)
        mask = labels.eq(classes.expand(batch_size, self.num_classes))
        dist = []
        for i in range(batch_size):
            value = distmat[i][mask[i]]
            value = value.clamp(min=1e-8, max=1e+5)  # for numerical stability
            dist.append(value)
        dist = torch.cat(dist)
        if self.reduction=='mean':
            return  dist.mean()/self.num_classes
        else:
            return  dist.sum()/self.num_classes


class StyleLoss(nn.Module):
    def __init__(self):
        super(StyleLoss, self).__init__()
        self.to(_device)
    def forward(self,output, target):
        target.detach()
        img_size=list(output.size())
        G = gram_matrix(output)
        Gt = gram_matrix(target)
        return F.mse_loss(G, Gt).div((img_size[1] * img_size[2] * img_size[3]))

class PerceptionLoss(_Loss):
    def __init__(self, reduction="mean",reduced=False):
        super(PerceptionLoss, self).__init__()
        self.vgg_model = torchvision.models.vgg16(pretrained=True)
        self.vgg_model.eval()
        self.vgg_layers = self.vgg_model.features
        self.layer_name_mapping = {'3': "conv1_2", '8': "conv2_2", '15': "conv3_3", '22': "conv4_3"}
        self.reduction = reduction
        self.reduced = reduced
        self.styleloss=StyleLoss()
        self.to(_device)
    def forward(self,output, target):
        loss = 0
        target.detach()
        vgg_output=self.vgg_model.features(output)
        vgg_target=self.vgg_model.features(target)

        # for name, module in self.vgg_layers._modules.items():
        #     if name in self.layer_name_mapping:
        #         loss =loss+ self.styleloss(module(output),module(target)).mean()
        return self.styleloss(vgg_output,vgg_target).sum()



class EdgeLoss(_Loss):
    def __init__(self, reduction="mean"):
        super(EdgeLoss, self).__init__()

        self.reduction = reduction

        self.styleloss=StyleLoss()
        self.to(_device)
    def first_order(self,x,axis=2):
        h,w = x.size(2), x.size(3)
        if axis == 2:
            return (x[:, :,:h - 1, :w - 1] - x[:, :, 1:, :w - 1]).abs()
        elif axis == 3:
            return (x[:,:, :h - 1, :w - 1] - x[:, :, :h - 1, 1:]).abs()
        else:
            return None
    def forward(self,output, target):
        loss = MSELoss(reduction=self.reduction)(self.first_order(output,2),self.first_order(target,2))\
        +MSELoss(reduction=self.reduction)(self.first_order(output,3),self.first_order(target,3))
        return loss



class TransformInvariantLoss(nn.Module):
    def __init__(self, loss:_Loss, embedded_func:Layer):
        super(TransformInvariantLoss, self).__init__()
        self.loss=MSELoss(reduction='mean')
        self.coverage = 110
        self.rotation_range = 20
        self.zoom_range = 0.1
        self.shift_range = 0.02
        self.random_flip = 0.3
        self.embedded_func=embedded_func
        self.to(_device)
    def forward(self,input:torch.Tensor, target:torch.Tensor):
        angle= torch.tensor(np.random.uniform(-self.rotation_range, self.rotation_range,target.size(0))*np.pi/180).float().to(input.device)
        scale=torch.tensor(np.random.uniform(1 - self.zoom_range, 1 + self.zoom_range,target.size(0))).float().to(input.device)
        height,width= target.size()[-2:]
        center_tensor =  torch.tensor([(width-1)/2,(height-1)/2]).expand(target.shape[0], -1).float().to(input.device)
        mat = get_rotation_matrix2d(center_tensor, angle, scale).float().to(input.device)
        rotated_target=warp_affine(target,mat,target.size()[2:]).float().to(input.device)

        embedded_output=self.embedded_func(input)
        embedded_target = self.embedded_func(rotated_target)
        return self.loss(embedded_output, embedded_target)


class GPLoss(nn.Module):
    def __init__(self, discriminator, l=10):
        super(GPLoss, self).__init__()
        self.discriminator = discriminator
        self.l = l

    def forward(self, real_data, fake_data):
        alpha = real_data.new_empty((real_data.size(0), 1, 1, 1)).uniform_(0, 1)
        alpha = alpha.expand_as(real_data)
        interpolates = alpha * real_data + ((1 - alpha) * fake_data)

        interpolates = torch.tensor(interpolates, requires_grad=True)
        disc_interpolates = self.discriminator(interpolates)
        gradients = torch.autograd.grad(outputs=disc_interpolates, inputs=interpolates,
                                  grad_outputs=real_data.new_ones(disc_interpolates.size()), create_graph=True,
                                  retain_graph=True, only_inputs=True)[0]
        gradients = gradients.view(gradients.size(0), -1)
        gradients_norm = torch.sqrt(torch.sum(gradients ** 2, dim=1) + 1e-12)
        gradient_penalty = ((gradients_norm - 1) ** 2).mean() * self.l


class F1ScoreLoss(_Loss):
    def __init__(self, reduction='mean' ):
        super(F1ScoreLoss, self).__init__()


    def forward(self, inputs, targets):
        assert targets.ndim == 1
        assert inputs.ndim == 1 or inputs.ndim == 2

        if inputs.ndim == 2:
            inputs = inputs.argmax(dim=1)

        tp = (targets * inputs).sum().to(torch.float32)
        tn = ((1 - targets) * (1 - inputs)).sum().to(torch.float32)
        fp = ((1 - targets) * inputs).sum().to(torch.float32)
        fn = (targets * (1 - inputs)).sum().to(torch.float32)

        precision = tp / (tp + fp + 1e-8)
        recall = tp / (tp + fn + 1e-8)

        f1 = 2 * (precision * recall) / (precision + recall + 1e-8)
        f1.requires_grad =True
        return f1



def get_loss(loss_name):
    if loss_name is None:
        return None
    loss_modules = ['trident.optims.pytorch_losses']
    if loss_name in __all__:
        loss_fn = get_class(loss_name, loss_modules)
    else:
        try:
            loss_fn = get_class(camel2snake(loss_name), loss_modules)
        except Exception :
            loss_fn = get_class(loss_name,loss_modules)
    return loss_fn



