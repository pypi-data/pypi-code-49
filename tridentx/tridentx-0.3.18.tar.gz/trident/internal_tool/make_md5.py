
import sys
import os
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import json
_trident_dir=get_trident_dir()

_md5_path = os.path.expanduser(os.path.join(_trident_dir, 'models/models_md5.json'))


models_md5=OrderedDict()
if os.path.exists(_md5_path):
    with open(_md5_path) as f:
        models_md5 = json.load(f)

def calculate_md5(fpath, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def add_model(model_path):
    global models_md5
    file=os.path.join(_trident_dir,'models',model_path)
    md5=calculate_md5(file)
    if os.path.exists(file):
        models_md5[model_path]=md5
        with open(_md5_path, 'w') as f:
            f.write(json.dumps(models_md5, indent=4))


add_model('resnet152.pth')
add_model('resnet101.pth')
add_model('resnet50.pth')
add_model('densenet121.pth')
add_model('densenet161.pth')
add_model('densenet169.pth')
add_model('densenet201.pth')
add_model('efficientnet-b0.pth')
add_model('efficientnet-b1.pth')
add_model('efficientnet-b2.pth')
add_model('efficientnet-b3.pth')
add_model('efficientnet-b4.pth')
add_model('efficientnet-b5.pth')
add_model('efficientnet-b6.pth')
add_model('efficientnet-b7.pth')
add_model('vgg11.pth')
add_model('vgg13.pth')
add_model('vgg16.pth')
add_model('vgg19.pth')
add_model('mobilenet_v2.pth')
add_model('pnet.pth')
add_model('rnet.pth')
add_model('onet.pth')








