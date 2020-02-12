import os
import sys
import tkinter
import matplotlib
import platform

if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
    matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from IPython import display
import inspect
import time
import uuid
import time
import platform
import copy
from functools import partial
import numpy as np
from ..backend.common import to_list, addindent, get_time_suffix, format_time, get_terminal_size, get_session, \
    snake2camel, PrintException, unpack_singleton, enforce_singleton, OrderedDict
from ..data.data_provider import *
from ..callbacks import *
from ..callbacks.visualization_callbacks import *
from ..misc.ipython_utils import *
from ..misc.visualization_utils import tile_rgb_images, loss_metric_curve

__all__ = ['progress_bar', 'OptimizerMixin', 'ModelBase', 'TrainingPlan']

_session = get_session()
_backend = _session.backend
if _backend == 'pytorch':
    import torch
    import torch.nn as nn
    from ..backend.pytorch_backend import *
elif _backend == 'tensorflow':
    import tensorflow as tf
    from ..backend.tensorflow_backend import *
elif _backend == 'cntk':
    import cntk as C
    from cntk.learners import *
    from ..backend.cntk_backend import *

_, term_width = get_terminal_size()
term_width = int(term_width)
TOTAL_BAR_LENGTH = 65.
last_time = time.time()
begin_time = last_time


class OptimizerMixin(object):
    # def __init__(self, parameters,lr=0.01,**kwargs):
    #     if _backend == 'pytorch':
    #         kwargs['lr']=lr
    #         self.base_lr=lr
    #         super(parameters,kwargs)
    #     elif _backend == 'tensorflow':
    #         super().set_value(self.lr, lr)
    #         kwargs['learning_rate '] = lr
    #         super(kwargs)
    #         self.parameters=parameters
    #     elif _backend == 'cntk':
    #         kwargs['lr'] = lr
    #         self.base_lr = lr
    #         super(parameters, **kwargs)
    #     self.optimizer=super()

    def adjust_learning_rate(self, new_lr, verbose=True):
        if _backend in ['cntk', 'pytorch']:
            old_lr = self.param_groups[0]['lr']
            if old_lr != new_lr:
                self.param_groups[0]['lr'] = new_lr
                if verbose:
                    print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr, new_lr))
        elif _backend == 'tensorflow':
            old_lr = self.lr
            if old_lr != new_lr:
                if hasattr(self, '_set_hyper'):
                    if hasattr(self, '_optimizer'):
                        self._optimizer._set_hyper('learning_rate', new_lr)
                    else:
                        self._set_hyper('learning_rate', new_lr)
                elif hasattr(self, 'set_value'):
                    self.lr.set_value(new_lr)
                if verbose:
                    print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr, new_lr))

        # elif _backend=='cntk':  #     old_lr = super(OptimizerMixin, self).learning_rate()  #     if old_lr!= new_lr:  #         super(OptimizerMixin, self).reset_learning_rate(new_lr)  #         if verbose:  #             print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr,new_lr))

    @property
    def default_setting(self):
        if _backend == 'pytorch':
            return self.defaults
        elif _backend == 'tensorflow':
            return self.__dict__
        elif _backend == 'cntk':
            return self.__dict__

    @default_setting.setter
    def default_setting(self, value):
        if _backend == 'pytorch':
            self.defaults = value
        elif _backend == 'tensorflow':
            self.__dict__.update(value)
        elif _backend == 'cntk':
            self.__dict__.update(value)

    @property
    def parameters(self):
        if _backend == 'pytorch':
            return self.param_groups['params']
        elif _backend == 'tensorflow':
            return self.get_weights()
        elif _backend == 'cntk':
            return self.param_groups['params']

    @parameters.setter
    def parameters(self, params):
        if _backend == 'pytorch':
            self.param_groups = [{'params': list(params)}]
        elif _backend == 'tensorflow':
            self.set_weights(params)

    @property
    def lr(self):
        if _backend in ['cntk', 'pytorch']:
            return self.param_groups[0]['lr']
        elif _backend == 'tensorflow':
            if hasattr(self, '_optimizer'):
                return self._optimizer._get_hyper('learning_rate').numpy()
            else:
                return self._get_hyper('learning_rate').numpy()  # elif _backend == 'cntk':  #     self.learning_rate()

    @lr.setter
    def lr(self, value: float):
        if self.lr != value:
            old_lr = self.lr
            new_lr = value
            if _backend in ['cntk', 'pytorch']:
                self.param_groups[0]['lr'] = new_lr
            elif _backend == 'tensorflow':
                if hasattr(self, '_optimizer'):
                    self._optimizer._set_hyper('learning_rate', new_lr)
                else:
                    self._set_hyper('learning_rate', new_lr)
            # elif _backend == 'cntk':
            #     old_lr = super(OptimizerMixin, self).learning_rate()
            #     if old_lr != new_lr:
            #         super(OptimizerMixin, self).reset_learning_rate(new_lr)
            print('learning rate changed! ( form {0:.3e} to {1:.3e})'.format(old_lr, new_lr))

    @property
    def base_lr(self):
        return self._base_lr

    @base_lr.setter
    def base_lr(self, value):
        self._base_lr = value

    def get_gradients(self, loss, params=None):
        if _backend == 'pytorch':
            return loss.grad
        elif _backend == 'tensorflow':
            return self.get_gradients(loss, params)
        elif _backend == 'cntk':
            pass

    def updates(self, closure, training_context):

        if _backend == 'pytorch':
            try:
                if callable(closure):
                    loss = closure()
                    loss.backward()
            except Exception as e:
                PrintException()
        elif _backend == 'tensorflow':
            if callable(closure):
                loss = closure()
            self.get_updates(loss, training_context['current_model'].trainable_)
        elif _backend == 'cntk':
            pass

        for callback in training_context['callbacks']:
            callback.on_optimization_step_end(training_context)

    def before_batch_train(self):
        if _backend == 'pytorch':
            self.zero_grad()
        else:
            pass


class ModelBase(object):
    def __init__(self, inputs=None, output=None, input_shape=None, name='', **kwargs):
        self.inputs = OrderedDict()
        self.targets = OrderedDict()
        self.model = None
        self.name = name
        self.optimizer = None
        self.lr_scheduler = None
        self._losses = OrderedDict()
        self._metrics = OrderedDict()
        self.loss_weights = OrderedDict()

        self._output_regs = OrderedDict()
        self._model_regs = OrderedDict()
        self._constraints = OrderedDict()
        self.base_lr = None
        self.warmup = 0
        self.sample_collect_history = []

        self.epoch_loss_history = OrderedDict()
        self.epoch_loss_history['total_losses'] = []
        self.epoch_metric_history = OrderedDict()
        self.weights_history = []
        self.gradients_history = []
        self.input_history = []
        self.target_history = []
        self.callbacks = []
        self.training_context = {'losses': OrderedDict(),  # loss_wrapper
                                 'metrics': OrderedDict(),  # loss_wrapper
                                 'grads_state': OrderedDict(),  # loss_wrapper
                                 'tmp_losses': OrderedDict(),  # loss_wrapper
                                 'tmp_metrics': OrderedDict(),  # loss_wrapper
                                 'grads': None, 'optimizer': None,  # optimizer
                                 'stop_training': False,  # stop training
                                 'total_epoch': -1,  # current_epoch
                                 'total_batch': -1,  # current_batch
                                 'current_epoch': -1,  # current_epoch
                                 'current_batch': -1,  # current_batch
                                 'current_model': None,  # current model
                                 'current_input': None,  # current input
                                 'current_target': None,  # current target
                                 'current_output': None,  # current output
                                 'current_loss': None,  # current loss
                                 'best_metric': None,  # current loss
                                 'best_model': None,  # current model
                                 'loss_history': None, 'metric_history': None, 'base_lr': self.base_lr,  # current loss
                                 'current_lr': None,  # current loss
                                 'save_path': None, 'is_collect_data': True, 'callbacks': self.callbacks,
                                 'stop_update': False, 'retain_graph': False}
        self.training_context['losses']['total_losses'] = []

        self._initial_graph(inputs, output, input_shape)

    @property
    def batch_metric_history(self):
        return self.training_context['metrics']

    @batch_metric_history.setter
    def batch_metric_history(self, value):
        self.training_context['metrics'] = value

    @property
    def batch_loss_history(self):
        return self.training_context['losses']

    @batch_loss_history.setter
    def batch_loss_history(self, value):
        self.training_context['losses'] = value

    @property
    def losses(self):
        return self._losses

    @property
    def metrics(self):
        return self._metrics

    def _initial_graph(self, inputs=None, output=None, input_shape=None):
        pass

    def complie(self, optimizer, losses=None, metrics=None, loss_weights=None, sample_weight_mode=None,
                weighted_metrics=None, target_tensors=None):
        raise NotImplementedError

    def __call__(self, *input, **kwargs):
        return self.model(*input, **kwargs)

    def with_optimizer(self, optimizer, **kwargs):
        return self

    def with_loss(self, loss, loss_weight=1, output_idx=0, name='', **kwargs):
        return self

    def with_metric(self, metric, output_idx=0, name='', **kwargs):
        return self

    def with_regularizer(self, reg, **kwargs):
        return self

    def with_constraint(self, constraint, **kwargs):
        return self

    def with_model_save_path(self, save_path, **kwargs):
        return self

    def with_callbacks(self, *callbacks):
        if len(self.callbacks) == 0:
            self.callbacks = to_list(callbacks)
        else:
            self.callbacks.extend(callbacks)
        self.training_context['callbacks'] = self.callbacks
        return self

    def with_learning_rate_scheduler(self, lr_schedule, warmup=0, **kwargs):
        return self

    def reset_training_context(self):
        self.training_context = {'losses': OrderedDict(),  # loss_wrapper
                                 'metrics': OrderedDict(),  # loss_wrapper
                                 'grads_state': OrderedDict(),  # loss_wrapper
                                 'tmp_losses': OrderedDict(),  # loss_wrapper
                                 'tmp_metrics': OrderedDict(),  # loss_wrapper
                                 'grads': None, 'optimizer': None,  # optimizer
                                 'stop_training': False,  # stop training
                                 'total_epoch': -1,  # current_epoch
                                 'total_batch': -1,  # current_batch
                                 'current_epoch': -1,  # current_epoch
                                 'current_batch': -1,  # current_batch
                                 'current_model': self.model,  # current model
                                 'current_input': None,  # current input
                                 'current_target': None,  # current target
                                 'current_output': None,  # current output
                                 'current_loss': None,  # current loss
                                 'best_metric': None,  # current loss
                                 'best_model': None,  # current model
                                 'loss_history': None, 'metric_history': None, 'base_lr': self.base_lr,  # current loss
                                 'current_lr': None,  # current loss
                                 'save_path': None, 'callbacks': self.callbacks, 'stop_update': False,
                                 'retain_graph': False}

    def adjust_learning_rate(self, lr):
        raise NotImplementedError

    def do_on_training_start(self):
        # set model as training state
        # zero grad
        pass

    def do_on_training_end(self):
        # set model as training state
        # zero grad
        pass

    def do_on_epoch_start(self):
        # set model as training state
        # zero grad
        pass

    def do_on_epoch_end(self):
        # set model as training state
        # zero grad
        pass

    def do_on_batch_start(self):
        # set model as training state
        # zero grad
        pass

    def do_on_batch_end(self):
        # set model as training state
        # zero grad
        pass

    def do_on_data_received(self, train_data, test_data):
        input = None
        target = None
        test_input = None
        test_target = None
        if 'data_feed' in self.training_context and len(self.training_context['data_feed']) > 0:
            data_feed = self.training_context['data_feed']
            input = to_tensor(train_data[data_feed.get('input')]) if data_feed.get('input') >= 0 else None
            target = to_tensor(train_data[data_feed.get('target')]) if data_feed.get('target') >= 0 else None
            if test_data is None:
                test_data = train_data
            test_input = to_tensor(test_data[data_feed.get('input')]) if data_feed.get('input') >= 0 else None
            test_target = to_tensor(test_data[data_feed.get('target')]) if data_feed.get('target') >= 0 else None

        else:
            data_feed = OrderedDict()
            data_feed['input'] = -1
            data_feed['target'] = -1
            inshapes = self.inputs.value_list
            outshapes = self.targets.value_list

            if train_data is not None:
                if len(train_data) == 1:
                    input = to_tensor(train_data[0])
                    target = to_tensor(train_data[0].copy())
                    data_feed['input'] = 0
                    data_feed['target'] = 0
                else:
                    for i in range(len(train_data)):
                        data = train_data[i]
                        data_shape = list(data.shape[1:])
                        if data_shape == inshapes[0]:
                            data_feed['input'] = i if data_feed['input'] < 0 else data_feed['input']
                            input = to_tensor(train_data[i])
                        elif data_shape == outshapes[0]:
                            data_feed['target'] = i if data_feed['target'] < 0 else data_feed['target']
                            target = to_tensor(train_data[i])
                        elif data.dtype in (np.int64, np.int32) and (data_shape == outshapes[0][:-1]):
                            data_feed['target'] = i if data_feed['target'] < 0 else data_feed['target']
                            target = to_tensor(train_data[i])
                        elif list(data.shape) == inshapes[0]:
                            data_feed['input'] = i if data_feed['input'] < 0 else data_feed['input']
                            input = to_tensor(train_data[i])
            self.training_context['data_feed'] = data_feed
            if test_data is None:
                test_data = train_data
            test_input = to_tensor(test_data[data_feed.get('input')]) if data_feed.get('input') >= 0 else None
            test_target = to_tensor(test_data[data_feed.get('target')]) if data_feed.get('target') >= 0 else None
        self.training_context['current_input'] = input
        self.training_context['current_target'] = target
        return input, target, test_input, test_target

    def do_preparation_for_loss(self):
        pass

    def do_post_loss_calculation(self):
        pass

    def do_pre_optimization_step(self):
        # set model as training state
        # zero grad
        pass

    def do_gradient_update(self, log_gradients=False, keep_gradients_history=False):
        pass

    def do_post_gradient_update(self):
        pass

    def do_on_metrics_evaluation_start(self):
        pass

    def do_on_metrics_evaluation_end(self):
        pass

    def do_on_progress_start(self):
        # set model as training state
        # zero grad
        pass

    def do_on_progress_end(self):
        # set model as training state
        # zero grad
        pass

    def log_gradient(self, grads=None, keep_gradients_history=False):
        raise NotImplementedError

    def log_weight(self, weghts=None, keep_weghts_history=False):
        raise NotImplementedError

    def merge_grads(self, old_grads, new_grades):
        raise NotImplementedError

    def save_model(self, file_path, ):
        raise NotImplementedError

    def save_onnx(self, file_path):
        raise NotImplementedError

    def save_weights(self, file_path):
        raise NotImplementedError

    def load_model(self, file_path, ):
        raise NotImplementedError

    def print_batch_progress(self, print_batch_progress_frequency):
        slice_cnt = sum(self.sample_collect_history[-1 * print_batch_progress_frequency:])

        progress_bar(self.training_context['current_batch'], self.training_context['total_batch'],
                     'Loss: {0:<8.3f}| {1} | learning rate: {2:<10.3e}| epoch: {3}'.format(
                         np.array(self.batch_loss_history['total_losses'][-1 * slice_cnt:]).mean(), ','.join(
                             ['{0}: {1:<8.3%}'.format(k, np.array(v[-1 * slice_cnt:]).mean()) for k, v in
                              self.batch_metric_history.items()]), self.training_context['current_lr'],
                         self.training_context['current_epoch']), name=self.name)

    def print_epoch_progress(self, print_epoch_progress_frequency):
        progress_bar(self.training_context['current_epoch'], self.training_context['total_epoch'],
                     'Loss: {0:<8.3f}| {1} | learning rate: {2:<10.3e}'.format(
                         np.array(self.epoch_loss_history['total_losses']).mean(), ','.join(
                             ['{0}: {1:<8.3%}'.format(k, np.array(v).mean()) for k, v in
                              self.epoch_metric_history.items()]), self.training_context['current_lr']), name=self.name)

    def plot_loss_metric_curve(self, unit='batch'):
        if unit == 'batch':
            loss_metric_curve(self.batch_loss_history, self.batch_metric_history, self.sample_collect_history,
                              max_iteration=None, calculate_base=unit, save_path=None, imshow=True)
        elif unit == 'epoch':
            loss_metric_curve(self.epoch_loss_history, self.epoch_metric_history, self.sample_collect_history,
                              max_iteration=None, calculate_base=unit, save_path=None, imshow=True)
        else:
            raise ValueError('unit should be batch or epoch.')

    def train_model(self, train_data, test_data, current_epoch, current_batch, total_epoch, total_batch,
                    is_collect_data=True, is_print_batch_progress=True, is_print_epoch_progress=True,
                    is_print_batch_gradients=True, log_gradients=False, log_weights=False, accumulate_grads=False):
        try:
            self.training_context['current_epoch'] = current_epoch
            self.training_context['current_batch'] = current_batch
            self.training_context['total_epoch'] = total_epoch
            self.training_context['total_batch'] = total_batch
            self.training_context['is_collect_data'] = is_collect_data
            self.training_context['log_gradients'] = log_gradients
            self.training_context['log_weights'] = log_weights
            self.training_context['current_model'] = self.model
            self.training_context['current_lr'] = self.optimizer.lr

            self.sample_collect_history.append(1 if is_collect_data else 0)

            if self.training_context['current_batch'] == 0:
                if self.training_context['current_epoch'] == 0:
                    self.do_on_training_start()
                self.training_context['print_batch_progress_frequency'] = 1
                self.training_context['print_epoch_progress_frequency'] = 1
                self.training_context['losses'] = OrderedDict()
                self.training_context['losses']['total_losses'] = []
                self.training_context['metrics'] = OrderedDict()
                self.training_context['grads_state'] = OrderedDict()
                self.training_context['grads_state']['first_layer'] = []
                self.training_context['grads_state']['last_layer'] = []

                self.training_context['tmp_losses'] = OrderedDict()
                self.training_context['tmp_losses'] = []
                self.training_context['tmp_metrics'] = OrderedDict()
                self.do_on_epoch_start()
                for callback in self.callbacks:
                    callback.on_epoch_start(self.training_context)

            self.do_on_batch_start()

            input, target, test_input, test_target = self.do_on_data_received(train_data, test_data)

            self.training_context['current_input'] = input
            self.training_context['current_target'] = target
            self.training_context['current_model'] = self.model
            for callback in self.callbacks:
                callback.on_data_received(self.training_context)
            input = self.training_context['current_input']
            target = self.training_context['current_target']

            if accumulate_grads == False:
                self.training_context['current_loss'] = 0
                self.do_preparation_for_loss()
                self.training_context['current_model'] = self.model
                self.training_context['optimizer'] = self.optimizer

            output = self.model(input)
            # confirm singleton
            # output=unpack_singleton(output)
            self.training_context['current_model'] = self.model
            self.training_context['current_output'] = output

            # losss
            for k, v in self._losses.items():
                if k not in self.training_context['losses']:
                    self.training_context['losses'][k] = []
                loss_weight = 1
                if k in self.loss_weights:
                    loss_weight = self.loss_weights[k]
                this_loss = v.forward(output, target) if hasattr(v, 'forward') else v(output, target)
                self.training_context['current_loss'] = self.training_context['current_loss'] + this_loss * loss_weight

                if is_collect_data:
                    self.training_context['losses'][k].append(float(to_numpy(this_loss) * loss_weight))

            self.do_post_loss_calculation()
            for callback in self.callbacks:
                callback.post_loss_calculation(self.training_context)

            if accumulate_grads == False:
                # regularizer
                for k, v in self._output_regs.items():
                    if k + '_Loss' not in self.training_context['losses']:
                        self.training_context['losses'][k + '_Loss'] = []
                    this_loss = v(output)
                    self.training_context['current_loss'] = self.training_context[
                                                                'current_loss'] + this_loss  # self.training_context[
                    # 'current_loss'] + this_loss
                    if is_collect_data:
                        self.training_context['losses'][k + '_Loss'].append(float(to_numpy(this_loss)))

                for k, v in self._model_regs.items():
                    if k + '_Loss' not in self.training_context['losses']:
                        self.training_context['losses'][k + '_Loss'] = []
                    this_loss = v(self.model)
                    self.training_context['current_loss'] = self.training_context['current_loss'] + this_loss
                    if is_collect_data:
                        self.training_context['losses'][k + '_Loss'].append(float(to_numpy(this_loss)))

                self.training_context['optimizer'] = self.optimizer
                # self.do_post_loss_calculation()
                #
                # for callback in self.callbacks:
                #     callback.post_loss_calculation(self.training_context)

                self.do_pre_optimization_step()
                self.do_gradient_update(log_gradients and is_collect_data)
                self.training_context['optimizer'] = self.optimizer
                self.training_context['current_lr'] = self.optimizer.lr

                # ON_POSTBACKWARD_CALCULATION
                self.do_post_gradient_update()

                self.training_context['tmp_losses'].append(float(to_numpy(self.training_context['current_loss'])))
                if is_collect_data:
                    self.training_context['losses']['total_losses'].append(
                        float(to_numpy(self.training_context['tmp_losses']).mean()))
                    self.training_context['tmp_losses'] = []

                # model comfirm
                for k, v in self._constraints.items():
                    v(self.model)

                if log_weights and is_collect_data:
                    self.log_weight()

                output = self.model(test_input)
                self.training_context['current_model'] = self.model
                self.training_context['current_output'] = output

                # ON_EVALUATION_START
                self.do_on_metrics_evaluation_start()
                for callback in self.training_context['callbacks']:
                    callback.on_metrics_evaluation_start(self.training_context)

                for k, v in self._metrics.items():
                    if k not in self.training_context['metrics']:
                        self.training_context['tmp_metrics'][k] = []
                        self.training_context['metrics'][k] = []

                    self.training_context['tmp_metrics'][k].append(
                        float(to_numpy(v.forward(output, test_target))) if hasattr(v, 'forward') else float(
                            to_numpy(v(output, test_target))))

                for k, v in self.training_context['tmp_metrics'].items():
                    if k not in self.epoch_metric_history:
                        self.epoch_metric_history[k] = []

                if is_collect_data:
                    for k, v in self.training_context['tmp_metrics'].items():
                        self.training_context['metrics'][k].append(float(to_numpy(v).mean()))
                        self.training_context['tmp_metrics'][k] = []

                # ON_EVALUATION_END
                self.do_on_metrics_evaluation_end()
                for callback in self.training_context['callbacks']:
                    callback.on_metrics_evaluation_end(self.training_context)

                # print batch progresss
                if is_print_batch_progress:
                    self.do_on_progress_start()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_start(self.training_context)

                    self.print_batch_progress(self.training_context['print_batch_progress_frequency'])
                    self.training_context['print_batch_progress_frequency'] = 1
                    self.do_on_progress_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_end(self.training_context)
                else:
                    self.training_context['print_batch_progress_frequency'] += 1

                    # ON_BATCH_END
                    self.do_on_batch_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_batch_end(self.training_context)

            if self.training_context['current_batch'] == self.training_context['total_batch'] - 1:
                self.do_on_epoch_end()

                slice_cnt = sum(self.sample_collect_history[-1 * total_batch:])
                self.epoch_loss_history['total_losses'].append(
                    np.array(self.training_context['losses']['total_losses'][-1 * slice_cnt:]).mean())
                for k, v in self.training_context['metrics'].items():
                    self.epoch_metric_history[k].append(np.array(v[-1 * slice_cnt:]).mean())

                if is_print_epoch_progress:
                    self.do_on_progress_start()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_start(self.training_context)
                    self.print_epoch_progress(self.training_context['print_epoch_progress_frequency'])
                    self.training_context['print_epoch_progress_frequency'] = 1
                    self.do_on_progress_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_progress_end(self.training_context)
                else:
                    self.training_context['print_epoch_progress_frequency'] += 1

                for callback in self.training_context['callbacks']:
                    callback.on_epoch_end(self.training_context)

                if self.training_context['current_epoch'] == self.training_context['total_epoch'] - 1:
                    self.do_on_training_end()
                    for callback in self.training_context['callbacks']:
                        callback.on_training_end(self.training_context)
        except Exception:
            PrintException()

    def summary(self):
        raise NotImplementedError


class TrainingPlan(object):
    def __init__(self):
        self.training_items = OrderedDict()
        self.training_names = OrderedDict()
        self._dataloaders = OrderedDict()
        self.num_epochs = 1
        self._minibatch_size = 1
        self.warmup = 0
        self.default_collect_data_inteval = 1
        self.print_progress_frequency = 10
        self.print_progress_unit = 'batch'
        self.print_progress_on_epoch_end = False
        self.save_model_frequency = -1
        self.save_model_unit = 'batch'

        self._is_optimizer_warmup = False
        self.plot_loss_metric_curve_frequency = 10
        self.plot_loss_metric_curve_unit = 'batch'
        self.need_tile_image = False
        self.tile_image_save_path = 'Results'
        self.tile_image_name_prefix = None
        self.tile_image_frequency = None
        self.tile_image_unit = 'batch'
        self.tile_image_include_input = False
        self.tile_image_include_output = False
        self.tile_image_include_target = False
        self.tile_image_include_mask = False
        self.tile_image_imshow = False
        self.callbacks = []  # if self.callbacks is None:  #     self.callbacks = [NumberOfEpochsStoppingCriterionCallback(1)]  # elif not any([issubclass(type(cb), StoppingCriterionCallback) for cb in self.callbacks]):  #  #     self.callbacks.append(NumberOfEpochsStoppingCriterionCallback(1))

    @property
    def minibatch_size(self):
        return self._minibatch_size

    @minibatch_size.setter
    def minibatch_size(self, value):
        self._minibatch_size = value
        for i, (k, v) in enumerate(self._dataloaders.items()):
            v.minibatch_size = value
            self._dataloaders[k] = v

    def with_callbacks(self, *callbacks):
        if len(self.callbacks) == 0:
            self.callbacks = to_list(callbacks)
        else:
            self.callbacks.extend(callbacks)
        return self

    def __getattr__(self, name):
        if name == 'self':
            return self
        if '_training_items' in self.__dict__:
            _training_items = self.__dict__['_training_items']
            if name in _training_items:
                return _training_items[name]

        if '_dataloaders' in self.__dict__:
            _dataloaders = self.__dict__['_dataloaders']
            if name in _dataloaders:
                return _dataloaders[name]

        raise AttributeError("'{}' object has no attribute '{}'".format(type(self).__name__, name))

    def extra_repr(self):
        r"""Set the extra representation of the module

        To print customized extra information, you should reimplement
        this method in your own modules. Both single-line and multi-line
        strings are acceptable.
        """
        return ''

    def __str__(self):
        self.__repr__()

    def _get_name(self):
        return self.__class__.__name__

    def __repr__(self):
        # We treat the extra repr like the sub-module, one item per line
        extra_lines = []
        extra_repr = self.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
        child_lines = []
        for key, value in self.__dict__.items():
            if isinstance(value, OrderedDict):
                for subkey, subvalue in value.items():
                    mod_str = repr(subvalue)
                    mod_str = addindent(mod_str, 2)
                    child_lines.append('(' + key + '): ' + mod_str)
            else:
                mod_str = repr(value)
                mod_str = addindent(mod_str, 2)
                child_lines.append('(' + key + '): ' + mod_str)
        lines = extra_lines + child_lines

        main_str = self._get_name() + '('
        if lines:
            # simple one-liner info, which most builtin Modules will use
            if len(extra_lines) == 1 and not child_lines:
                main_str += extra_lines[0]
            else:
                main_str += '\n  ' + '\n  '.join(lines) + '\n'

        main_str += ')'
        return main_str

    def __dir__(self):
        module_attrs = dir(self.__class__)

        # training_items = list(self.training_items.keys())
        keys = module_attrs

        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)

    @classmethod
    def create(cls):
        plan = cls()
        return plan

    def add_training_item(self, training_item, name=''):
        n = len(self.training_items)

        if len(training_item.name) > 0:
            self.training_names[n] = training_item.name
        else:
            if len(name) > 0:
                training_item.name = name
                self.training_names[n] = name
            else:
                training_item.name = 'model {0}'.format(n)
                self.training_names[n] = 'model {0}'.format(n)
        self.training_items[n] = training_item
        return self

    def with_data_loader(self, data_loader, **kwargs):
        self._dataloaders[data_loader.__class__.__name__] = data_loader
        return self

    def repeat_epochs(self, num_epochs: int):
        self.num_epochs = num_epochs
        return self

    def within_minibatch_size(self, minibatch_size: int):
        self.minibatch_size = minibatch_size
        return self

    def print_progress_scheduling(self, frequency: int, unit='batch', on_epoch_end=True, show_loss_metric_curve=True):
        self.print_progress_on_epoch_end = on_epoch_end
        self.print_progress_frequency = frequency
        self.default_collect_data_inteval = frequency
        if unit not in ['batch', 'epoch']:
            raise ValueError('unit should be batch or epoch')
        else:
            self.print_progress_unit = unit
        if self.tile_image_frequency is None or self.print_progress_frequency > self.tile_image_frequency:
            self.tile_image_frequency = self.print_progress_frequency * 5
        return self

    def print_gradients_scheduling(self, frequency: int, unit='batch'):

        pg = PrintGradientsCallback(batch_inteval=frequency)
        pg.is_shared = False
        self.callbacks.append(pg)
        return self

    def save_model_scheduling(self, frequency: int, unit='batch'):
        self.save_model_frequency = frequency
        if unit not in ['batch', 'epoch']:
            raise ValueError('unit should be batch or epoch')
        else:
            self.save_model_unit = unit
        return self

    def display_tile_image_scheduling(self, frequency: int, unit='batch', save_path: str = None,
                                      name_prefix: str = 'tile_image_{0}.png', include_input=True, include_output=True,
                                      include_target=True, include_mask=None, imshow=False):
        if unit not in ['batch', 'epoch']:
            raise ValueError('unit should be batch or epoch')

        tile = TileImageCallback(frequency if unit == 'epoch' else -1, frequency if unit == 'batch' else -1,
                                 save_path=save_path, name_prefix=name_prefix, include_input=include_input,
                                 include_output=include_output, include_target=include_target,
                                 include_mask=include_mask, imshow=imshow)
        self.callbacks.append(tile)

        return self

    def display_loss_metric_curve_scheduling(self, frequency: int, unit='batch', save_path: str = None, imshow=False):
        if save_path is not None:
            folder, file = os.path.split(save_path)
            if not os.path.exists(folder):
                try:
                    os.makedirs(folder)
                except Exception as e:
                    PrintException()
                    raise ValueError('save_path:{0} is not valid path'.format(folder))

        self.tile_image_save_path = save_path
        self.tile_image_unit = unit
        self.tile_image_frequency = frequency

        self.tile_image_imshow = imshow

        if unit not in ['batch', 'epoch']:
            raise ValueError('unit should be batch or epoch')
        else:
            self.tile_image_unit = unit
        return self

    def plot_loss_metric_curve(self, unit='batch'):

        if unit == 'batch':
            loss_metric_curve(self.training_items[0].batch_loss_history, self.training_items[0].batch_metric_history,
                              self.training_items[0].sample_collect_history, max_iteration=None, calculate_base=unit,
                              save_path=None, imshow=True)
        elif unit == 'epoch':
            loss_metric_curve(self.training_items[0].epoch_loss_history, self.training_items[0].epoch_metric_history,
                              self.training_items[0].sample_collect_history, max_iteration=self.num_epochs,
                              calculate_base=unit, save_path=None, imshow=True)
        else:
            raise ValueError('unit should be batch or epoch.')

    def start_now(self, collect_data_inteval=1):
        try:
            self.execution_id = str(uuid.uuid4())[:8].__str__().replace('-', '')
            if self.tile_image_save_path is None:
                self.tile_image_save_path = 'Results'
            make_dir_if_need(self.tile_image_save_path)
            # update callback
            for item in self.training_items.values():
                for callback in self.callbacks:
                    if callback not in item.callbacks:
                        if callback.is_shared == False:
                            item.with_callbacks(copy.deepcopy(callback))
                        else:
                            item.with_callbacks(callback)
            for callback in self.callbacks:
                if callback.is_shared == True:
                    callback.on_training_start(self.__dict__)

            data_loader = self._dataloaders.value_list[0]
            data_loader.minibatch_size = self.minibatch_size
            tile_images_list = []
            print(self.__repr__)
            if collect_data_inteval == 1 and len(data_loader.batch_sampler) * self.num_epochs > 1000:
                collect_data_inteval = self.default_collect_data_inteval

            for epoch in range(self.num_epochs):
                try:
                    input = None
                    target = None
                    test_input = None
                    test_target = None
                    for mbs, iter_data in enumerate(data_loader):
                        iter_testdata = None
                        if isinstance(data_loader, DataProviderV2):
                            iter_testdata = data_loader.next_test()

                        # input, target = Variable(input).to(self.device), Variable(target).to(self.device)

                        for k, trainitem in self.training_items.items():
                            trainitem.train_model(iter_data, iter_testdata, epoch, mbs, self.num_epochs,
                                                  len(data_loader.batch_sampler),
                                                  is_collect_data=mbs % collect_data_inteval == 0,
                                                  is_print_batch_progress=self.print_progress_unit == 'batch' and mbs % self.print_progress_frequency == 0,
                                                  is_print_epoch_progress=self.print_progress_unit == 'epoch' and (
                                                          epoch + 1) % self.print_progress_frequency == 0,
                                                  log_gradients=False, log_weights=False, accumulate_grads=False)

                        #
                        if is_in_ipython() and self.tile_image_unit == 'batch' and mbs > 0 and epoch < self.num_epochs - 1 and (
                                epoch * len(data_loader.batch_sampler) + mbs) % (self.tile_image_frequency * 2) == 0:
                            display.clear_output(wait=True)

                        if (
                                mbs > 0 and mbs % self.tile_image_frequency == 0 and self.tile_image_unit == 'batch'):  # or ( mbs == len(data_loader.batch_sampler) - 1):
                            loss_history = []
                            metric_history = []

                            for trainitem in self.training_items.value_list:
                                loss_history.append(trainitem.batch_loss_history)
                                metric_history.append(trainitem.batch_metric_history)

                            loss_metric_curve(loss_history, metric_history,
                                              sample_collected=self.training_items.value_list[0].sample_collect_history,
                                              legend=self.training_names.value_list, calculate_base='batch',
                                              max_iteration=None, save_path=os.path.join(self.tile_image_save_path,
                                                                                         'loss_metric_curve.png'),
                                              imshow=True)

                            tile_images_list = []

                        if self.save_model_frequency > 0 and self.save_model_unit == 'batch' and mbs % self.save_model_frequency == 0:
                            for k, trainitem in self.training_items.items():
                                trainitem.save_model()

                        if (mbs + 1) % len(data_loader.batch_sampler) == 0:
                            break

                    if self.tile_image_unit == 'epoch' and (epoch + 1) % self.tile_image_frequency == 0:
                        epoch_loss_history = [trainitem.epoch_loss_history for k, trainitem in
                                              self.training_items.items()]
                        epoch_metric_history = [trainitem.epoch_metric_history for k, trainitem in
                                                self.training_items.items()]

                        loss_metric_curve(epoch_loss_history, epoch_metric_history,
                                          legend=self.training_names.value_list, calculate_base='epoch',
                                          max_iteration=self.num_epochs,
                                          save_path=os.path.join(self.tile_image_save_path, 'loss_metric_curve.png'),
                                          imshow=True)

                    if self.save_model_frequency > 0 and self.save_model_unit == 'epoch' and (
                            epoch + 1) % self.save_model_frequency == 0:
                        for k, trainitem in self.training_items.items():
                            trainitem.save_model()



                except StopIteration:
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_epoch_end()
                    pass
                except ValueError as ve:
                    print(ve)
                    PrintException()
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_training_end()

                except Exception as e:
                    print(e)
                    PrintException()
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_training_end()
        except KeyboardInterrupt:
            for k, trainitem in self.training_items.items():
                trainitem.save_model()

    def resume(self):
        if self.execution_id is None:
            raise ValueError('There is no history execution to resume')
        else:
            data_loader = self._dataloaders.value_list[0]

            print(self.__repr__)
            trainingcontext = self.training_items.value_list[0].training_context
            current_epoch = trainingcontext['current_epoch']
            print('current_epoch: ', current_epoch)
            current_batch = trainingcontext['current_batch']
            print('current_batch : ', current_batch)
            sample_collect_history = self.training_items.value_list[0].sample_collect_history
            tile_images_list = []
            collect_data_inteval = self.default_collect_data_inteval
            if len(sample_collect_history) > 0 and sum(sample_collect_history) > 1:
                pos = 0
                pos_list = []
                for i in range(len(sample_collect_history)):
                    if sample_collect_history[i] == 1 and i == 0:
                        pass
                    elif sample_collect_history[i] == 1:
                        pos_list.append(i - pos)
                        pos = i
                    else:
                        pass
                collect_data_inteval = np.median(np.array(pos_list))
            print('collect_data_inteval : ', collect_data_inteval)
            print('resume start')

            for epoch in range(current_epoch, self.num_epochs):
                try:
                    print('epoch:{0}'.format(epoch))
                    input = None
                    target = None
                    test_input = None
                    test_target = None
                    for mbs, iter_data in enumerate(data_loader):
                        iter_testdata = None
                        if isinstance(data_loader, DataProviderV2):
                            iter_testdata = data_loader.next_test()
                        # input, target = Variable(input).to(self.device), Variable(target).to(self.device)

                        for k, trainitem in self.training_items.items():
                            trainitem.train_model(iter_data, iter_testdata, epoch, mbs, self.num_epochs,
                                                  len(data_loader.batch_sampler),
                                                  is_collect_data=mbs % collect_data_inteval == 0,
                                                  is_print_batch_progress=self.print_progress_unit == 'batch' and mbs % self.print_progress_frequency == 0,
                                                  is_print_epoch_progress=self.print_progress_unit == 'epoch' and (
                                                          epoch + 1) % self.print_progress_frequency == 0,
                                                  log_gradients=False, log_weights=False, accumulate_grads=False)

                        if is_in_ipython() and mbs > 0 and mbs % (self.tile_image_frequency * 2) == 0:
                            display.clear_output(wait=True)

                        if (mbs > 0 and mbs % self.tile_image_frequency == 0) or (
                                mbs == len(data_loader.batch_sampler) - 1):
                            loss_history = [trainitem.batch_loss_history for trainitem in
                                            self.training_items.value_list]
                            metric_history = [trainitem.batch_metric_history for trainitem in
                                              self.training_items.value_list]
                            if epoch == 0:
                                loss_history = [trainitem.training_context['losses'] for trainitem in
                                                self.training_items.value_list]
                                metric_history = [trainitem.training_context['metrics'] for trainitem in
                                                  self.training_items.value_list]
                            loss_metric_curve(loss_history, metric_history,
                                              sample_collected=self.training_items.value_list[0].sample_collect_history,
                                              legend=self.training_names.value_list, calculate_base='batch',
                                              max_iteration=None, save_path=os.path.join(self.tile_image_save_path,
                                                                                         'loss_metric_curve.png'),
                                              imshow=True)

                            tile_images_list = []

                        if self.save_model_frequency > 0 and self.save_model_unit == 'batch' and mbs % self.save_model_frequency == 0:
                            for k, trainitem in self.training_items.items():
                                trainitem.save_model()

                        if (mbs + 1) % len(data_loader.batch_sampler) == 0:
                            break

                    if self.need_tile_image == True and self.tile_image_unit == 'epoch' and (
                            epoch + 1) % self.tile_image_frequency == 0:

                        epoch_loss_history = [trainitem.epoch_loss_history for k, trainitem in
                                              self.training_items.items()]
                        epoch_metric_history = [trainitem.epoch_metric_history for k, trainitem in
                                                self.training_items.items()]
                        if epoch >= 10:
                            loss_metric_curve(epoch_loss_history, epoch_metric_history,
                                              legend=self.training_names.value_list, calculate_base='epoch',
                                              max_iteration=self.num_epochs,
                                              save_path=os.path.join(self.tile_image_save_path,
                                                                     'loss_metric_curve.png'), imshow=True)
                        tile_images_list = []

                    if self.save_model_frequency > 0 and self.save_model_unit == 'epoch' and (
                            epoch + 1) % self.save_model_frequency == 0:
                        for k, trainitem in self.training_items.items():
                            trainitem.save_model()



                except StopIteration:
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_epoch_end()
                    pass
                except ValueError as ve:
                    print(ve)
                    PrintException()
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_training_end()

                except Exception as e:
                    print(e)
                    PrintException()
                    for k, trainitem in self.training_items.items():
                        trainitem.do_on_training_end()

    def only_steps(self, num_steps, collect_data_inteval=1, keep_weights_history=False, keep_gradient_history=False):
        self.execution_id = str(uuid.uuid4())[:8].__str__().replace('-', '')
        # update callback
        for item in self.training_items.values():
            for callback in self.callbacks:
                if callback not in item.callbacks:
                    item.with_callbacks(callback)

        data_loader = list(self._dataloaders.items())[0][1]
        data_loader.minibatch_size = self.minibatch_size

        tile_images_list = []

        try:
            # if self.lr_schedule is not None and trainingitem.is_optimizer_initialized()==True:
            # don't print learning rate if print_progress_every unit is epoch
            input = None
            target = None
            test_input = None
            test_target = None
            for mbs, iter_data in enumerate(data_loader):
                if mbs < num_steps:
                    iter_testdata = None
                    if isinstance(data_loader, DataProviderV2):
                        iter_testdata = data_loader.next_test()
                    # input, target = Variable(input).to(self.device), Variable(target).to(self.device)

                    for k, trainitem in self.training_items.items():
                        trainitem.train_model(iter_data, iter_testdata, 0, mbs, 1, num_steps,
                                              is_collect_data=mbs % collect_data_inteval == 0,
                                              is_print_batch_progress=self.print_progress_unit == 'batch' and mbs % self.print_progress_frequency == 0,
                                              is_print_epoch_progress=False,
                                              log_gradients=keep_gradient_history and mbs % collect_data_inteval == 0,
                                              log_weights=keep_weights_history and mbs % collect_data_inteval == 0,
                                              accumulate_grads=False)
                    if len(
                            self.training_items.items()) > 2 and self.print_progress_unit == 'batch' and mbs % self.print_progress_frequency == 0:
                        print('')

                else:
                    break
            # if self.print_progress_on_epoch_end:
            #     progress_bar(num_steps, num_steps, 'Loss: {0:<8.3f}| {1} | learning rate: {2:<10.4e}'.format(
            #         np.array(self.training_items[0].batch_loss_history['total_losses']).mean(),
            #         ','.join(['{0}: {1:<8.3%}'.format(snake2camel(k), np.array(v).mean()) for k, v in self.training_items[0].batch_metric_history.items()]),
            #         optimizer.param_groups[0]['lr']))

            batch_loss_history = [trainitem.batch_loss_history for k, trainitem in self.training_items.items()]
            batch_metric_history = [trainitem.batch_metric_history for k, trainitem in self.training_items.items()]
            loss_metric_curve(batch_loss_history, batch_metric_history, legend=self.training_names.value_list,
                              sample_collected=self.training_items[0].sample_collect_history, max_iteration=num_steps,
                              calculate_base='batch', save_path=None, imshow=True)


        except StopIteration:
            for k, trainitem in self.training_items.items():
                trainitem.do_on_training_end()
        except ValueError as ve:
            for k, trainitem in self.training_items.items():
                trainitem.do_on_training_end()
            print(ve)
            PrintException()
        except Exception as e:
            for k, trainitem in self.training_items.items():
                trainitem.do_on_training_end()
            print(e)
            PrintException()


last_time = time.time()
begin_time = last_time


def progress_bar(current, total, msg=None, name=''):
    global last_time, begin_time
    if current == 0:
        begin_time = time.time()  # Reset for new bar.
    cur_len = max(int(TOTAL_BAR_LENGTH * float(current) / total), 1)
    rest_len = int(TOTAL_BAR_LENGTH - cur_len) - 1 + cur_len
    # sys.stdout.write(' [')
    # for i in range(cur_len):
    #     sys.stdout.write('=')
    # sys.stdout.write('>')
    # for i in range(rest_len):
    #     sys.stdout.write('.')
    # sys.stdout.write(']')
    cur_time = time.time()
    step_time = cur_time - last_time
    last_time = cur_time
    tot_time = cur_time - begin_time
    L = []
    L.append('{0:<16s}'.format(name))
    L.append(' Step: {0:<8s}'.format(format_time(step_time)))
    # L.append(' | Tot: {0:<12s}'.format(format_time(tot_time)))
    if msg:
        L.append(' | ' + msg)
    msg = ''.join(L)
    sys.stdout.write(msg)
    for i in range(term_width - int(TOTAL_BAR_LENGTH) - len(msg) - 3):
        sys.stdout.write(' ')
    sys.stdout.write(' ( %d/%d )' % (current, total))
    sys.stdout.write('\n')
    sys.stdout.flush()  # # Go back to the center of the bar.  # for i in range(term_width-int(TOTAL_BAR_LENGTH/2)+2):  #     sys.stdout.write('\b')  # sys.stdout.write(' %d/%d ' % (current+1, total))  # if current < total-1:  #     sys.stdout.write('\r')  # else:  #     sys.stdout.write('\n')  # sys.stdout.flush()

