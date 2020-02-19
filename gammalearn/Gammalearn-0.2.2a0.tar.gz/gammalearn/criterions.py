import logging

import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F


def cross_entropy_loss(output, target, weight):
    return F.cross_entropy(output, target.long(), weight)


def cross_entropy_loss_nn(output, target):
    return nn.CrossEntropyLoss()(output, target.long())


def nll_nn(output, target):
    return nn.NLLLoss()(output, target.long())


def angular_separation_loss(reduce='mean'):

    def loss_function(output, target):
        """
        Compute the mean angular separation loss between 2 directions
        Parameters
        ----------
        output (Tensor) : output of the net for direction regression
        target (Tensor) : labels for direction regression

        Returns
        -------
        Loss
        """
        logger = logging.getLogger('angular separation loss')
        logger.debug('output size : {}'.format(output.size()))
        # logger.debug('direction regression : {}'.format(output))
        # logger.debug('direction target : {}'.format(target))
        try:
            assert output.size() == target.size()
        except AssertionError as err:
            logger.exception('Output and target shapes must be the same but are {} and {}'.format(output.size(),
                                                                                                  target.size()))
            raise err

        alt1 = output[:, 0]
        try:
            assert alt1.data.nelement() > 0
        except AssertionError as err:
            logger.exception('reconstructed alt must have at least 1 element but have {}'.format(alt1.data.nelement()))
            raise err
        try:
            assert not np.isnan(np.sum(alt1.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('alt1 has NaN value(s) : {}'.format(alt1.data))
            raise err
        logger.debug('mean on {} elements'.format(alt1.data.nelement()))

        az1 = output[:, 1]
        try:
            assert not np.isnan(np.sum(az1.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('az1 has NaN value(s) : {}'.format(az1.data))
            raise err

        alt2 = target[:, 0]
        try:
            assert not np.isnan(np.sum(alt2.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('alt2 has NaN value(s) : {}'.format(alt2.data))
            raise err

        az2 = target[:, 1]
        try:
            assert not np.isnan(np.sum(az2.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('az2 has NaN value(s) : {}'.format(az2.data))
            raise err
        loss_cos = (torch.mul(torch.mul(alt1.cos(), alt2.cos()), (az1 - az2).cos()) + torch.mul(alt1.sin(), alt2.sin()))

        try:
            assert not np.isnan(np.sum(loss_cos.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('loss_cos has NaN value(s) : {}'.format(loss_cos.data))
            raise err
        # the loss_coss needs to be < 1 for the gradient not to be inf
        loss = loss_cos.clamp(min=-0.999999, max=0.999999).acos()
        if reduce == 'mean':
            loss = loss.sum() / alt1.data.nelement()
        elif reduce == 'sum':
            loss = loss.sum()
        try:
            assert not np.isnan(np.sum(loss.data.cpu().numpy()))
        except AssertionError as err:
            logger.exception('loss has NaN value(s) : {}'.format(loss.data))
            raise err

        return loss
    return loss_function


# From https://github.com/kornia/kornia/blob/master/kornia/losses/focal.py
def one_hot(labels, num_classes, device=None, dtype=None, eps=1e-6):
    r"""Converts an integer label 2D tensor to a one-hot 3D tensor.
    Args:
        labels (torch.Tensor) : tensor with labels of shape :math:`(N, H, W)`,
                                where N is batch siz. Each value is an integer
                                representing correct classification.
        num_classes (int): number of classes in labels.
        device (Optional[torch.device]): the desired device of returned tensor.
         Default: if None, uses the current device for the default tensor type
         (see torch.set_default_tensor_type()). device will be the CPU for CPU
         tensor types and the current CUDA device for CUDA tensor types.
        dtype (Optional[torch.dtype]): the desired data type of returned
         tensor. Default: if None, infers data type from values.
    Returns:
        torch.Tensor: the labels in one hot tensor.
    """
    if not torch.is_tensor(labels):
        raise TypeError("Input labels type is not a torch.Tensor. Got {}"
                        .format(type(labels)))
    if not len(labels.shape) == 1:
        raise ValueError("Invalid depth shape, we expect B. Got: {}"
                         .format(labels.shape))
    if not labels.dtype == torch.int64:
        raise ValueError(
            "labels must be of the same dtype torch.int64. Got: {}" .format(
                labels.dtype))
    if num_classes < 1:
        raise ValueError("The number of classes must be bigger than one."
                         " Got: {}".format(num_classes))
    batch_size = labels.shape[0]
    one_hot = torch.zeros(batch_size, num_classes,
                          device=device, dtype=dtype)
    return one_hot.scatter_(1, labels.unsqueeze(1), 1.0) + eps


def focal_loss(input, target, gamma=2.0, reduction='none'):
    r"""Function that computes Focal loss.
    See :class:`~kornia.losses.FocalLoss` for details.
    """
    if not torch.is_tensor(input):
        raise TypeError("Input type is not a torch.Tensor. Got {}"
                        .format(type(input)))

    if not len(input.shape) == 2:
        raise ValueError("Invalid input shape, we expect BxC. Got: {}"
                         .format(input.shape))

    if not input.device == target.device:
        raise ValueError(
            "input and target must be in the same device. Got: {}" .format(
                input.device, target.device))

    # network outputs logsoftmax.

    # create the labels one hot tensor
    target_one_hot = one_hot(target, num_classes=input.shape[1], device=input.device, dtype=input.dtype)

    # compute the actual focal loss
    weight = torch.pow(-torch.exp(input) + 1., gamma)

    focal = - weight * input
    loss_tmp = torch.sum(target_one_hot * focal, dim=1)

    if reduction == 'none':
        loss = loss_tmp
    elif reduction == 'mean':
        loss = torch.mean(loss_tmp)
    elif reduction == 'sum':
        loss = torch.sum(loss_tmp)
    else:
        raise NotImplementedError("Invalid reduction mode: {}"
                                  .format(reduction))
    return loss


class FocalLoss(nn.Module):
    r"""Criterion that computes Focal loss.
    According to [1], the Focal loss is computed as follows:
    .. math::
        \text{FL}(p_t) = -\alpha_t (1 - p_t)^{\gamma} \, \text{log}(p_t)
    where:
       - :math:`p_t` is the model's estimated probability for each class.
    Arguments:
        alpha (float): Weighting factor :math:`\alpha \in [0, 1]`.
        gamma (float): Focusing parameter :math:`\gamma >= 0`.
        reduction (str, optional): Specifies the reduction to apply to the
         output: ‘none’ | ‘mean’ | ‘sum’. ‘none’: no reduction will be applied,
         ‘mean’: the sum of the output will be divided by the number of elements
         in the output, ‘sum’: the output will be summed. Default: ‘none’.
    Shape:
        - Input: :math:`(N, C, H, W)` where C = number of classes.
        - Target: :math:`(N, H, W)` where each value is
          :math:`0 ≤ targets[i] ≤ C−1`.
    Examples:
        >>> N = 5  # num_classes
        >>> args = {"alpha": 0.5, "gamma": 2.0, "reduction": 'mean'}
        >>> loss = kornia.losses.FocalLoss(*args)
        >>> input = torch.randn(1, N, 3, 5, requires_grad=True)
        >>> target = torch.empty(1, 3, 5, dtype=torch.long).random_(N)
        >>> output = loss(input, target)
        >>> output.backward()
    References:
        [1] https://arxiv.org/abs/1708.02002
    """

    def __init__(self, alpha=0.5, gamma=2.0, reduction='mean') -> None:
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, input, target):
        return focal_loss(input, target.long(), self.gamma, self.reduction)


def compute_mt_loss(targets, conditional=False):
    """
    Create the function to compute the loss in case of simple regression experiment
    Parameters
    ----------
    criterions (dict): The loss dictionary defining for every objectives of the experiment the loss function and its weight

    Returns
    -------
    The function to compute the loss
    """

    def compute_loss(output, labels):
        """
        Compute the loss of the batch
        Parameters
        ----------
        output: result of the forward pass of a mini-batch in the network
        labels: mini-batch of labels

        Returns
        -------
        The Loss tensor, and the loss data of each objective
        """
        loss = []
        loss_data = []
        condition = torch.ones(output.shape[0])
        if conditional:
            i = 0
            for k, v in targets.items():
                label_shape = v['label_shape'] if 'label_shape' in v else v['output_shape']
                if k == 'class':
                    condition = labels[:, i:i+label_shape]
                    break
                i += label_shape
        i_o = 0
        i_l = 0
        for k, v in targets.items():
            output_shape = v['output_shape']
            label_shape = v['label_shape'] if 'label_shape' in v else output_shape
            out = output[:, i_o:i_o + output_shape]
            lab = labels[:, i_l:i_l + label_shape]
            lab = lab.squeeze() if lab.ndim == 2 and lab.shape[-1] == 1 and k == 'class' else lab
            l = v['loss'](out, lab)
            if k != 'class':
                if conditional:
                    assert l.shape[0] == condition.shape[0], 'loss should not be reduced for condition on particle type' \
                                                             'but got {} and {}'.format(l.shape, condition.shape)
                    if l.dim() > 1:
                        cond = [condition for _ in range(l.shape[1])]
                        cond = torch.cat(cond, dim=1)
                    else:
                        cond = condition
                    l = (l * cond).sum() / cond.sum() if cond.sum() > 0 else torch.tensor(0)
                else:
                    l = l.mean()
            loss_data.append(l.item())
            i_l += label_shape
            i_o += output_shape
            loss.append(l * v['loss_weight'])

        return loss, loss_data

    return compute_loss


class MultilossBalancing(nn.Module):
    """
    Create the function to compute the loss in case of multi regression experiment with homoscedastic uncertainty
    loss balancing. See the paper https://arxiv.org/abs/1705.07115
    Parameters
    ----------
    criterions (dict): The loss dictionary defining for every objectives of the experiment the loss function and its
    initial log_var

    Returns
    -------
    The function to compute the loss
    """
    def __init__(self, targets, conditional=False):
        super(MultilossBalancing, self).__init__()
        self.logger = logging.getLogger(__name__ + 'MultilossBalancing')
        self.targets = targets
        self.conditional = conditional
        if self.conditional:
            assert 'class' in self.targets, 'The conditional loss is defined based on particle type'
        self.log_vars = nn.Parameter(torch.rand(len(self.targets.keys())))
        self.logger.debug('log vars : {}'.format(self.log_vars))

        with torch.no_grad():
            for i, key in enumerate(self.targets.keys()):
                self.log_vars[i] = self.targets[key]['loss_weight']
        self.logger.debug('log vars : {}'.format(self.log_vars))

    def forward(self, output, labels):
        """
        Compute the loss of the batch
        Parameters
        ----------
        output: result of the forward pass of a mini-batch in the network
        labels: mini-batch of labels

        Returns
        -------
        The Loss tensor, and the loss data of each objective
        """
        loss = []
        loss_data = []
        condition = torch.ones(output.shape[0])
        if self.conditional:
            i = 0
            for k, v in self.targets.items():
                label_shape = v['label_shape'] if 'label_shape' in v else v['output_shape']
                if k == 'class':
                    condition = labels[:, i:i + label_shape]
                    break
                i += label_shape
        i_o = 0
        i_l = 0
        for i, (k, v) in enumerate(self.targets.items()):
            precision = torch.exp(- self.log_vars[i])
            output_shape = v['output_shape']
            label_shape = v['label_shape'] if 'label_shape' in v else output_shape
            out = output[:, i_o:i_o + output_shape]
            lab = labels[:, i_l:i_l + label_shape]
            lab = lab.squeeze() if lab.ndim == 2 and lab.shape[-1] == 1 and k == 'class' else lab
            l = v['loss'](out, lab)
            if k != 'class':
                if self.conditional:
                    assert l.shape[0] == condition.shape[0], 'loss should not be reduced for condition on particle type' \
                                                       'but got {} and {}'.format(l.shape, condition.shape)
                    if l.dim() > 1:
                        cond = [condition for _ in range(l.shape[1])]
                        cond = torch.cat(cond, dim=1)
                    else:
                        cond = condition

                    l = (l * cond).sum() / cond.sum() if cond.sum() > 0 else torch.tensor(0)
                else:
                    l = l.mean()
            loss_data.append(l.item())
            i_l += label_shape
            i_o += output_shape
            l = precision * l + self.log_vars[i]
            loss.append(l)

        return loss, loss_data


class GradNormBalancing(nn.Module):
    """
    Compute the loss in case of multi regression experiment
    Parameters
    ----------
    criterions (dict): The loss dictionary defining for every objectives of the experiment the loss function and its
    initial log_var

    Returns
    -------
    The function to compute the loss
    """
    def __init__(self, targets, conditional=False, last_common_layer=None, alpha=0):
        super(GradNormBalancing, self).__init__()

        assert last_common_layer is not None, 'The last common layer must be provided'

        self.targets = targets
        self.conditional = conditional
        self.task_number = len(self.targets)
        self.last_common_layer = last_common_layer
        self.alpha = alpha
        self.weights = nn.Parameter(torch.ones(self.task_number))
        self.initial_losses = torch.zeros(self.task_number)
        self.t0 = True

    def forward(self, output, labels):
        """
        Compute the loss of the batch
        Parameters
        ----------
        output: result of the forward pass of a mini-batch in the network
        labels: mini-batch of labels

        Returns
        -------
        The Loss tensor, and the loss data of each objective
        """
        losses = []
        condition = torch.ones(output.shape[0])
        if self.conditional:
            i = 0
            for k, v in self.targets.items():
                label_shape = v['label_shape'] if 'label_shape' in v else v['output_shape']
                if k == 'class':
                    condition = labels[:, i:i + label_shape]
                    break
                i += label_shape
        i_o = 0
        i_l = 0
        for i, (k, v) in enumerate(self.targets.items()):
            output_shape = v['output_shape']
            label_shape = v['label_shape'] if 'label_shape' in v else output_shape
            out = output[:, i_o:i_o + output_shape]
            lab = labels[:, i_l:i_l + label_shape]
            lab = lab.squeeze() if lab.ndim == 2 and lab.shape[-1] == 1 and k == 'class' else lab
            l = v['loss'](out, lab)
            if k != 'class':
                if self.conditional:
                    assert l.shape[0] == condition.shape[0], 'loss should not be reduced for condition on particle type' \
                                                             'but got {} and {}'.format(l.shape, condition.shape)
                    if l.dim() > 1:
                        cond = [condition for _ in range(l.shape[1])]
                        cond = torch.cat(cond, dim=1)
                    else:
                        cond = condition
                    l = (l * cond).sum() / cond.sum() if cond.sum() > 0 else torch.tensor(0)
                else:
                    l = l.mean()
            i_l += label_shape
            i_o += output_shape
            if self.t0:
                self.initial_losses[i] = l.item()
            losses.append(l)
        self.t0 = False

        return torch.stack(losses), [l.item() for l in losses]

