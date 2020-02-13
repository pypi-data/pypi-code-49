
import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import torch
import torchvision
from torchvision.models import  vgg,resnet
vgg19_1=vgg.vgg19(True)

_session = get_session()
vgg19=VGG19(pretrained=False)


pretrain_weights =list(vgg19_1.named_parameters())
buf=list(vgg19_1.named_buffers())
buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
pretrain_weights.extend(buf)


mapping=OrderedDict()
pretrain_weights_dict=OrderedDict()
for  item in pretrain_weights:
    mapping[item[0]]=''
    pretrain_weights_dict[item[0]]=item[1]



pretrain_weights1=list(vgg19.model.named_parameters())
buf=list(vgg19.model.named_buffers())
buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
pretrain_weights1.extend(buf)

for  i in range(len(pretrain_weights1)):
    item=pretrain_weights1[i]
    if 'norm' in item[0] and 'weight'in item[0] :
        for k,v in pretrain_weights_dict.items():
            if mapping[k]=='' and  ('bn' in k or 'downsample' in k) and 'weight'in k and item[1].shape==v.shape:
                mapping[k]=item[0]
                break
    elif 'norm' in item[0] and 'bias' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if mapping[k]=='' and  ('bn' in k or 'feature' in k) and 'bias'in k and item[1].shape==v.shape:
                mapping[k]=item[0]
                break
    if 'norm' in item[0] and 'running_mean'in item[0] :
        for k,v in pretrain_weights_dict.items():
            if mapping[k]=='' and  ('bn' in k or 'feature' in k) and 'running_mean'in k and item[1].shape==v.shape:
                mapping[k]=item[0]
                break
    elif 'norm' in item[0] and 'running_var' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if mapping[k]=='' and  ('bn' in k or 'feature' in k) and 'running_var'in k and item[1].shape==v.shape:
                mapping[k]=item[0]
                break
    elif 'conv' in item[0] and 'weight' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if mapping[k]=='' and ( 'conv' in k or 'feature' in k) and 'weight'in k and item[1].shape==v.shape:
                mapping[k]=item[0]
                break
    elif 'conv' in item[0] and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if mapping[k] == '' and ( 'conv' in k or 'feature' in k)  and 'bias' in k and item[1].shape == v.shape:
                mapping[k] = item[0]
                break
    elif 'fc' in item[0] and 'weight' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if mapping[k] == '' and 'classifier' in k and 'weight' in k and item[1].shape == v.shape:
                mapping[k] = item[0]
                break
    elif 'fc' in item[0] and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if mapping[k] == '' and 'classifier' in k and 'bias' in k and item[1].shape == v.shape:
                mapping[k] = item[0]
                break
mapping1=OrderedDict()
for k,v in mapping.items():
    mapping1[v]=k


for name,para in vgg19.model.named_parameters():
    if name in mapping1:
        para.data=pretrain_weights_dict[mapping1[name]].data

for name, buf in vgg19.model.named_buffers():
    if name in mapping1:
        buf.data = pretrain_weights_dict[mapping1[name]].data


vgg19.model.cpu()
#vgg19.save_model('vgg19.pth')
torch.save(vgg19.model,'vgg19.pth')
# w=np.array(list(vgg19.model.named_parameters()))
# np.save('vgg19_weights.npy',w)


print(vgg19.infer_single_image(read_image('cat.jpg'),5))
