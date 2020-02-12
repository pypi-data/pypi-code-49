
from ..backend.load_backend import get_backend
if get_backend()=='pytorch':
    from trident.models import pytorch_vgg
    from trident.models import pytorch_mtcnn
    from trident.models import pytorch_resnet
    from trident.models import pytorch_densenet
    from trident.models import pytorch_efficientnet
    from trident.models import pytorch_mobilenet
    from trident.models import pytorch_gan
    # from .pytorch_resnet import *
    # from .pytorch_mtcnn import *
    # from .pytorch_vgg import *
elif get_backend()=='tensorflow':
    from trident.models import tensorflow_resnet

    from ..backend.tensorflow_backend import  to_numpy,to_tensor
elif get_backend()=='cntk':
    from ..backend.cntk_backend import  to_numpy,to_tensor

