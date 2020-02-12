import warnings
import math
import numpy as np
import os
import sys
from  ..callbacks import CallbackBase
from ..backend.common import *
from ..backend.load_backend import get_backend
from ..misc.ipython_utils import is_in_ipython,is_in_colab
from ..misc.visualization_utils import *
_session=get_session()
_backend=get_backend()

if get_backend()=='pytorch':
    from ..backend.pytorch_backend import to_numpy,to_tensor
elif get_backend()=='tensorflow':
    from ..backend.tensorflow_backend import  to_numpy,to_tensor
elif get_backend()=='cntk':
    from ..backend.cntk_backend import  to_numpy,to_tensor


__all__ = ['VisualizationCallbackBase','TileImageCallback','PrintGradientsCallback']

class VisualizationCallbackBase(CallbackBase):
    def __init__(self,epoch_inteval,batch_inteval,save_path: str = None, imshow=False):
        super(VisualizationCallbackBase, self).__init__()
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.epoch_inteval=epoch_inteval
        self.batch_inteval=batch_inteval
        if save_path is not None:
            self.save_path=make_dir_if_need(save_path)
        else:
            self.save_path=None
        self.imshow = imshow
    pass


class TileImageCallback(VisualizationCallbackBase):
    def __init__(self,epoch_inteval=-1,batch_inteval=-1,save_path: str = 'results',
                                      name_prefix: str = 'tile_image_{0}.png', include_input=True, include_output=True,
                                      include_target=True, include_mask=None, imshow=False):
        super(TileImageCallback,self).__init__(epoch_inteval,batch_inteval,save_path,imshow)
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.tile_image_name_prefix = name_prefix

        self.include_input = include_input
        self.include_output = include_output
        self.include_target = include_target
        self.include_mask = include_mask

    def plot_tile_image(self,training_context):
        tile_images_list=[]
        input=training_context['current_input']
        target=training_context['current_target']
        output = training_context['current_output']

        if self.include_input:
            input_arr = to_numpy(input).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(input)
            tile_images_list.append(input_arr * 127.5 + 127.5)
        if self.include_target:
            target_arr = to_numpy(target).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(target)
            tile_images_list.append(target_arr * 127.5 + 127.5)
        if self.include_output:
            output_arr = to_numpy(output).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(output)
            tile_images_list.append(output_arr * 127.5 + 127.5)

        # if self.tile_image_include_mask:
        #     tile_images_list.append(input*127.5+127.5)
        tile_rgb_images(*tile_images_list,save_path=os.path.join(self.save_path, self.tile_image_name_prefix ), imshow=True)

    def on_batch_end(self, training_context):
        if self.batch_inteval > 0 and (training_context['current_batch'] + 1) % self.batch_inteval == 0:
            self.plot_tile_image(training_context)

    def on_epoch_end(self, training_context):
        if self.epoch_inteval>0 and (training_context['current_epoch']+1)%self.epoch_inteval==0:
            self.plot_tile_image(training_context)

class PrintGradientsCallback(VisualizationCallbackBase):
    def __init__(self,batch_inteval=-1):
        super(PrintGradientsCallback,self).__init__(epoch_inteval=-1,batch_inteval=batch_inteval)
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.batch_inteval=batch_inteval
        self.first_layer=''
        self.last_layer=''

    def on_optimization_step_start(self, training_context):
        if self.batch_inteval > 0 and (training_context['current_epoch']*training_context['total_batch']+training_context['current_batch'] +1)%self.batch_inteval==0:
            grad_dict = {}
            if self.first_layer!='' and self.last_layer!='':
                for i, (k, v) in enumerate(training_context['current_model'].named_parameters()):
                    if k==self.first_layer:
                        training_context['grads_state']['first_layer'].append(to_numpy(v.grad).mean())
                    elif k==self.last_layer:
                        training_context['grads_state']['last_layer'].append(to_numpy(v.grad).mean())
            else:
                for i, (k, v) in enumerate(training_context['current_model'].named_parameters()):
                    grad_dict[k] = to_numpy(v.grad)
                    if grad_dict[k].ndim > 1:
                        if self.first_layer == '':
                            self.first_layer = k
                        else:
                            self.last_layer = k

                training_context['grads_state']['first_layer'].append(grad_dict[self.first_layer].mean())
                training_context['grads_state']['last_layer'].append(grad_dict[self.last_layer].mean())
            L = []
            L.append('{0:<16s}'.format(training_context['current_model'].name))
            L.append('first_layer gradients: {0:<8.3e}| last_layer gradients: {1:<8.3e}'.format(training_context['grads_state']['first_layer'][-1],training_context['grads_state']['last_layer'][-1]))
            sys.stdout.write( ''.join(L))
            sys.stdout.write('\n')
            sys.stdout.flush()