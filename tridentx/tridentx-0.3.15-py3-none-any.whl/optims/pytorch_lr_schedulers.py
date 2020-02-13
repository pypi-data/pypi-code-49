import math
import warnings
import torch
from torch import nn
from torch._six import inf
from torch.optim.lr_scheduler import _LRScheduler,CosineAnnealingLR,LambdaLR
from torch.optim.optimizer import  Optimizer
import numpy as np
from ..backend.common import get_function,get_class,snake2camel
from ..backend.pytorch_backend import to_numpy

from ..callbacks.AdjustLRCallbacks import AdjustLRCallbackBase
__all__ = ['warmup_lr_scheduler','adjust_learning_rate','reduce_lr_on_plateau','cyclic_scheduler','get_lr_scheduler']


def warmup_lr_scheduler(func):
    def wrapper(*args, **kwargs):
        x = args[0]
        w = args[1]
        if x.ndim == 3:
            w = np.flipud(w)
            w = np.transpose(w, (1, 2, 0))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 2, 1))
        elif x.ndim == 4:
            w = np.fliplr(np.flipud(w))
            w = np.transpose(w, (2, 3, 0, 1))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 3, 1, 2))
        else:
            w = np.flip(np.fliplr(np.flipud(w)), axis=2)
            w = np.transpose(w, (3, 4, 0, 1, 2))
            if kwargs['data_format'] == 'channels_last':
                x = np.transpose(x, (0, 4, 1, 2, 3))
        dilation_rate = kwargs.pop('dilation_rate', 1)
        if isinstance(dilation_rate, int):
            dilation_rate = (dilation_rate,) * (x.ndim - 2)
        for (i, d) in enumerate(dilation_rate):
            if d > 1:
                for j in range(w.shape[2 + i] - 1):
                    w = np.insert(w, 2 * j + 1, 0, axis=2 + i)
        y = func(x, w, **kwargs)
        if kwargs['data_format'] == 'channels_last':
            if y.ndim == 3:
                y = np.transpose(y, (0, 2, 1))
            elif y.ndim == 4:
                y = np.transpose(y, (0, 2, 3, 1))
            else:
                y = np.transpose(y, (0, 2, 3, 4, 1))
        return y
    return wrapper



def adjust_learning_rate(optimizer,base_lr=0.001, current_epoch=0,num_epochs=3, power=0.8,warmup=5,verbose=True):
    """Sets the learning rate: milestone is a list/tuple"""

    # def lr_poly(base_lr, iter, max_iter, power):
    #     return base_lr * ((1 - float(iter) / max_iter) ** (power))
    def lr_poly(base_lr, iter, max_iter, power):
        return base_lr * pow(power,max(float(iter)-1,0))
    if current_epoch<warmup:
        lr=1e-5*(current_epoch+1)
    else:
        lr = lr_poly(base_lr, current_epoch, num_epochs, power)
    if verbose==True:
        print('learning rate : {0:.4e}'.format(lr))
    #optimizer.param_groups[0]['lr'] = lr
    optimizer.adjust_learning_rate(lr,True)

    return lr



class ReduceLROnPlateau(AdjustLRCallbackBase):
    """Reduce learning rate when a metric has stopped improving.
    Models often benefit from reducing the learning rate by a factor
    of 2-10 once learning stagnates. This callback monitors a
    quantity and if no improvement is seen for a 'patience' number
    of epochs, the learning rate is reduced.
    # Example
    ```python
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                                  patience=5, min_lr=0.001)
    model.fit(X_train, Y_train, callbacks=[reduce_lr])
    ```
    # Arguments
        monitor: quantity to be monitored.
        factor: factor by which the learning rate will
            be reduced. new_lr = lr * factor
        patience: number of epochs that produced the monitored
            quantity with no improvement after which training will
            be stopped.
            Validation quantities may not be produced for every
            epoch, if the validation frequency
            (`model.fit(validation_freq=5)`) is greater than one.
        verbose: int. 0: quiet, 1: update messages.
        mode: one of {auto, min, max}. In `min` mode,
            lr will be reduced when the quantity
            monitored has stopped decreasing; in `max`
            mode it will be reduced when the quantity
            monitored has stopped increasing; in `auto`
            mode, the direction is automatically inferred
            from the name of the monitored quantity.
        min_delta: threshold for measuring the new optimum,
            to only focus on significant changes.
        cooldown: number of epochs to wait before resuming
            normal operation after lr has been reduced.
        min_lr: lower bound on the learning rate.
    """

    def __init__(self, monitor='total_losses', factor=0.1, patience=10,
                 verbose=0, mode='auto', min_delta=1e-4, cooldown=0, min_lr=0,
                 **kwargs):
        super(ReduceLROnPlateau, self).__init__()

        self.monitor = monitor
        if factor >= 1.0:
            raise ValueError('ReduceLROnPlateau '
                             'does not support a factor >= 1.0.')
        if 'epsilon' in kwargs:
            min_delta = kwargs.pop('epsilon')
            warnings.warn('`epsilon` argument is deprecated and '
                          'will be removed, use `min_delta` instead.')
        self.factor = factor
        self.min_lr = min_lr
        self.min_delta = min_delta
        self.patience = patience
        self.verbose = verbose
        self.cooldown = cooldown
        self.cooldown_counter = 0  # Cooldown counter.
        self.wait = 0
        self.best = 0
        self.mode = mode
        self.monitor_op = None
        self._reset()

    def _reset(self):
        """Resets wait counter and cooldown counter.
        """
        if self.mode not in ['auto', 'min', 'max']:
            warnings.warn('Learning Rate Plateau Reducing mode %s is unknown, '
                          'fallback to auto mode.' % (self.mode),
                          RuntimeWarning)
            self.mode = 'auto'
        if (self.mode == 'min' or
           (self.mode == 'auto' and 'acc' not in self.monitor)):
            self.monitor_op = lambda a, b: np.less(a, b - self.min_delta)
            self.best = np.Inf
        else:
            self.monitor_op = lambda a, b: np.greater(a, b + self.min_delta)
            self.best = -np.Inf
        self.cooldown_counter = 0
        self.wait = 0

    def on_train_begin(self, training_context):
        self._reset()

    def on_epoch_end(self, training_context):
        training_context['current_lr']=training_context['optimizer'].lr
        current =to_numpy(training_context['losses'].get(self.monitor,training_context['metrics'].get(self.monitor,training_context['losses']['total_losses']))).mean()
        if current is None:
            warnings.warn(
                'Reduce LR on plateau conditioned on metric `%s` '
                'which is not available. Available metrics are: %s' %
                (self.monitor, ','.join(training_context['metrics'].keys_list)), RuntimeWarning
            )

        else:
            if self.in_cooldown():
                self.cooldown_counter -= 1
                self.wait = 0

            if self.monitor_op(current, self.best):
                self.best = current
                self.wait = 0
            elif not self.in_cooldown():
                self.wait += 1
                print(self.wait )
                if self.wait >= self.patience:
                    old_lr = float(training_context['optimizer'].lr)
                    if old_lr > self.min_lr:
                        new_lr = old_lr * self.factor
                        new_lr = max(new_lr, self.min_lr)
                        training_context['optimizer'].adjust_learning_rate(new_lr,True)

                        if self.verbose > 0:
                            print('\nEpoch %05d: ReduceLROnPlateau reducing '
                                  'learning rate to %s.' % (training_context['current_epoch'] + 1, new_lr))
                        self.cooldown_counter = self.cooldown
                        self.wait = 0

    def on_batch_end(self, training_context):
        if training_context['current_batch']>0 and training_context['current_batch']%200==0:
            training_context['current_lr']=training_context['optimizer'].lr
            current =to_numpy(training_context['losses'].get(self.monitor,training_context['metrics'].get(self.monitor,training_context['losses']['total_losses']))).mean()
            if current is None:
                warnings.warn(
                    'Reduce LR on plateau conditioned on metric `%s` '
                    'which is not available. Available metrics are: %s' %
                    (self.monitor, ','.join(training_context['metrics'].keys_list)), RuntimeWarning
                )

            else:
                if self.in_cooldown():
                    self.cooldown_counter -= 1
                    self.wait = 0

                if self.monitor_op(current, self.best):
                    self.best = current
                    self.wait = 0
                elif not self.in_cooldown():
                    self.wait += 1
                    print(self.wait )
                    if self.wait >= self.patience:
                        old_lr = float(training_context['optimizer'].lr)
                        if old_lr > self.min_lr:
                            new_lr = old_lr * self.factor
                            new_lr = max(new_lr, self.min_lr)
                            training_context['optimizer'].adjust_learning_rate(new_lr,True)

                            if self.verbose > 0:
                                print('\nEpoch %05d: ReduceLROnPlateau reducing '
                                      'learning rate to %s.' % (training_context['current_epoch'] + 1, new_lr))
                            self.cooldown_counter = self.cooldown
                            self.wait = 0


    def in_cooldown(self):
        return self.cooldown_counter > 0

def reduce_lr_on_plateau(monitor='total_loss',base_lr=0.001 ,verbose=True, mode='min', factor=0.5, patience=5, threshold=1e-4, threshold_mode='rel', cooldown=0, min_lr=1e-8, eps=1e-9):
   return ReduceLROnPlateau(monitor=monitor,mode=mode,factor=factor,patience=patience,verbose=int(verbose),min_delta=threshold,threshold_mode=threshold_mode,cooldown=cooldown,min_lr=min_lr)

def cosine_annealing_lr(optimizer,base_lr=0.001 ,total_epoch=100,  eta_min=0, last_epoch=-1):
    return CosineAnnealingLR(optimizer,total_epoch, eta_min, last_epoch=last_epoch)


def cyclic_scheduler(optimizer,base_lr=0.001, current_epoch=0,current_batch=0,total_epoch=100,total_batch=100,verbose=True,min_lr_factor=0.05, max_lr=1.0 ):
    half_epochs = total_epoch // 2
    decay_epochs = total_epoch * 0.05
    lr_grow = np.linspace(min_lr_factor, max_lr, half_epochs)
    lr_down = np.linspace(max_lr, min_lr_factor, half_epochs - decay_epochs)
    lr_decay = np.linspace(min_lr_factor, min_lr_factor * 0.01, decay_epochs)
    learning_rates = np.concatenate((lr_grow, lr_down, lr_decay)) / max_lr
   # lrs=[base_lr * learning_rates[last_epoch] for base_lr in base_lrs]




def get_lr_scheduler(lr_scheduler_name):
    if lr_scheduler_name is None:
        return None
    lr_scheduler_modules = ['trident.optims.pytorch_lr_schedulers','torch.optim']
    lr_scheduler_fn=None
    if isinstance(lr_scheduler_name,str):
        if lr_scheduler_name in __all__:
            lr_scheduler_fn=get_function(lr_scheduler_name,lr_scheduler_modules)
    else:
        try:
            lr_scheduler_fn = get_function(lr_scheduler_name, lr_scheduler_modules)
        except Exception :
            lr_scheduler_fn = get_function(snake2camel(lr_scheduler_name), lr_scheduler_modules)
    return lr_scheduler_fn





