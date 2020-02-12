# Imports models
from .mobilenet.cifar10.model import mobilenet_cifar10
from .mobilenet.imagenet.model import mobilenet_imagenet
from .mobilenet.kws.model import mobilenet_kws
from .vgg.cifar10.model import vgg_cifar10

from . import quantization_blocks