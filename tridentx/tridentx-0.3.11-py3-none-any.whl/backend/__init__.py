from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six


from .load_backend import get_backend,get_image_backend,PrintException,if_else
from .load_backend import  get_session , get_trident_dir , epsilon , set_epsilon , floatx , set_floatx , camel2snake , snake2camel , addindent , format_time , get_time_suffix , get_function , get_class , get_terminal_size , gcd , get_divisors , isprime , next_prime , prev_prime , nearest_prime




from .load_backend import tile_rgb_images,loss_metric_curve,steps_histogram
from .load_backend import read_image , read_mask , save_image , save_mask , image2array , array2image , mask2array , array2mask , list_pictures , normalize , unnormalize , random_crop , resize , add_noise , image_backend_adaptive , random_channel_shift , random_cutout
from ..optims.trainers import ModelBase,OptimizerMixin,TrainingPlan


from  ..optims.trainers import *
from ..data import *
from ..data import ImageReader,ImageThread
from ..optims.trainers import *

if get_backend()=='pytorch':
    from .pytorch_backend import *
    from .pytorch_ops import *
    from ..layers.pytorch_activations import *
    from ..layers.pytorch_layers import *
    from ..layers.pytorch_pooling import *
    from ..layers.pytorch_blocks import *
    from ..layers.pytorch_normalizations import *
    from ..optims.pytorch_regularizers import *

    from ..optims.pytorch_constraints import *
    from ..optims.pytorch_losses import *
    from ..optims.pytorch_metrics import *
    from ..optims.pytorch_optimizers import *
    from ..optims.pytorch_trainer import *
    from ..data.pytorch_datasets import *
    from ..models.pytorch_resnet import *
    from ..models.pytorch_mtcnn import *
    from ..models.pytorch_vgg import *
    from ..models.pytorch_densenet import *
    from ..models.pytorch_efficientnet import *
    from ..models.pytorch_mobilenet import *

elif get_backend()=='cntk':
    from .cntk_backend import to_numpy, to_tensor, get_device,Layer, Sequential, ConcatContainer, ShortcutContainer,Input,update_add
    from ..layers.cntk_activations import Identity, Sigmoid, Tanh, Relu, Relu6, LeakyRelu, LeakyRelu6, SmoothRelu, \
        PRelu, Swish, Elu, HardSigmoid, HardSwish, Selu, LecunTanh, SoftSign, SoftPlus, HardTanh, Logit, LogLog, Mish, \
        Softmax, identity, sigmoid, tanh, relu, relu6, leaky_relu, leaky_relu6, smooth_relu, p_relu, swish, elu, \
        hard_sigmoid, hard_swish, selu, lecun_tanh, soft_sign, soft_plus, hard_tanh, logit, log_log, mish, softmax, \
        get_activation
    from ..layers.cntk_normalizations import *
    from ..layers.cntk_layers import *
    from ..layers.cntk_blocks import *
    from ..optims.cntk_optimizers import  *
    from ..optims.cntk_trainer import *
    from ..optims.cntk_losses import *
    from ..optims.cntk_metrics import *
    from ..optims.cntk_constraints import *
    from ..optims.cntk_regularizers import *

elif get_backend()=='tensorflow':
    from .tensorflow_backend import Input,Sequential,ConcatContainer,to_tensor,to_numpy
    from .tensorflow_ops import *
    from ..optims.tensorflow_regularizers import*
    from ..optims.tensorflow_optimizers import *
    from ..optims.tensorflow_losses import *
    from ..optims.tensorflow_metrics import *
    from ..optims.tensorflow_constraints import *

    from ..optims.tensorflow_trainer import *
    from ..layers.tensorflow_activations import Identity ,  Sigmoid ,  Tanh ,  Relu ,  Relu6 ,  LeakyRelu ,  LeakyRelu6 ,  SmoothRelu ,  PRelu ,  Swish ,  Elu ,HardSigmoid ,  HardSwish ,  Selu ,  LecunTanh ,  SoftSign ,  SoftPlus ,  HardTanh ,  Logit ,  LogLog ,  Mish , Softmax ,  identity ,  sigmoid ,  tanh ,  relu ,  relu6 ,  leaky_relu ,  leaky_relu6 ,  smooth_relu ,  p_relu , swish ,  elu ,  hard_sigmoid ,  hard_swish ,  selu ,  lecun_tanh ,  soft_sign ,  soft_plus ,  hard_tanh , logit ,  log_log ,  mish ,  softmax ,  get_activation
    from ..layers.tensorflow_layers import *
    from ..layers.tensorflow_blocks import *
    from ..layers.tensorflow_normalizations import *
    from ..models.tensorflow_resnet import *



from ..misc.ipython_utils import *
from ..misc.visualization_utils import *
from .iteration_tools import *
from ..callbacks  import *


