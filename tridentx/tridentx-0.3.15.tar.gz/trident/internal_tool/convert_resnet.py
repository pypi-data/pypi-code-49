
import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import torch
import torchvision
from torchvision.models import  vgg,resnet




import torchvision
import torch

mobilenet_old=MobileNetV2(pretrained=True)
mobilenet=MobileNetV2(pretrained=False)
mobilenet.model.trainable=True

paras_old=list(mobilenet_old.model.named_parameters())
paras=list(mobilenet.model.named_parameters())

print('paras_old',len(paras_old))
print('paras',len(paras))

buffer_old=list(mobilenet_old.model.named_buffers())
buffer=list(mobilenet.model.named_buffers())


buffer_old=[b for b in buffer_old  if 'running_mean' in b[0] or 'running_var' in b[0]]
buffer=[b for b in buffer  if 'running_mean' in b[0] or 'running_var' in b[0]]

print('buffer_old',len(buffer_old))
print('buffer',len(buffer))

for i in range(len(paras)):
    p_old=paras_old[i]
    p = paras[i]
    if  p[1].shape==p_old[1].shape: #p[0]==p_old[0] and
        p[1].data=p_old[1].data
    else:
        print(p[0], p_old[0])

for i in range(len(buffer)):
    b_old = buffer_old[i]
    b = buffer[i]
    if 'running_mean' in b[0] or 'running_var' in b[0]:
        if  b[1].shape == b_old[1].shape: #b[0] == b_old[0] and
            b[1].data = b_old[1].data
    else:
        pass




mobilenet.model.eval()
print(mobilenet.infer_single_image('cat.jpg',5))
mobilenet.model.cpu()

torch.save(mobilenet.model,'mobilenet_v2.pth')




#
#
#
#
# torch_resnet18=torchvision.models.resnet18(pretrained=True)
# pretrain_weights_dict=torch.load('resnet18-5c106cde.pth')
# mapping=OrderedDict()
# for k,v in pretrain_weights_dict.items():
#     mapping[k]=''
#
#
#
# #model=torch.load(torch.load(os.path.join(_session.trident_dir, 'models','resnet18.pth')))
# resnet18=ResNet(bottleneck,[3, 8, 36, 3],(3,224,224),model_name='resnet18')
# pretrain_weights1=list(resnet18.model.named_parameters())
# buf=list(resnet18.model.named_buffers())
# buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
# pretrain_weights1.extend(buf)
#
# no_match=[]
#
# for  i in range(len(pretrain_weights1)):
#     item=pretrain_weights1[i]
#     if 'norm' in item[0] and 'weight'in item[0]  and item[0] not in mapping.value_list:
#         for k,v in pretrain_weights_dict.items():
#             if mapping[k]=='' and  ('bn' in k or 'downsample' in k) and 'weight'in k and item[1].shape==v.shape:
#                 mapping[k]=item[0]
#                 break
#         no_match.append(item)
#     elif 'norm' in item[0] and 'bias' in item[0]   and item[0] not in mapping.value_list:
#         for k,v in pretrain_weights_dict.items():
#             if mapping[k]=='' and  ('bn' in k ) and 'bias'in k and item[1].shape==v.shape:
#                 mapping[k]=item[0]
#                 break
#
#     elif 'norm' in item[0] and 'running_mean'in item[0]   and item[0] not in mapping.value_list :
#         for k,v in pretrain_weights_dict.items():
#             if mapping[k]=='' and  'running_mean'in k and item[1].shape==v.shape:
#                 mapping[k]=item[0]
#                 break
#     elif 'norm' in item[0] and 'running_var' in item[0]   and item[0] not in mapping.value_list:
#         for k,v in pretrain_weights_dict.items():
#             if mapping[k]=='' and 'running_var'in k and item[1].shape==v.shape:
#                 mapping[k]=item[0]
#                 break
#     elif  'weight' in item[0] and ('conv' in item[0]  or 'first_layer' in item[0]) and item[0] not in mapping.value_list:
#         for k,v in pretrain_weights_dict.items():
#             if mapping[k]=='' and ( 'conv' in k or 'downsample' in k) and 'weight'in k and item[1].shape==v.shape:
#                 mapping[k]=item[0]
#                 break
#     elif 'fc.' in item[0] and 'weight' in item[0]   and item[0] not in mapping.value_list:
#         for k, v in pretrain_weights_dict.items():
#             if mapping[k] == '' and 'fc' in k and 'weight' in k and item[1].shape == v.shape:
#                 mapping[k] = item[0]
#                 break
#     elif 'fc.' in item[0] and 'bias' in item[0]   and item[0] not in mapping.value_list:
#         for k, v in pretrain_weights_dict.items():
#             if mapping[k] == '' and 'fc' in k and 'bias' in k and item[1].shape == v.shape:
#                 mapping[k] = item[0]
#                 break
#     else:
#         no_match.append(item)
#
# print(len(set(list(mapping.key_list))))
# print(len(set(list(mapping.value_list))))
#
# mapping1=OrderedDict()
# for k,v in mapping.items():
#     mapping1[v]=k
#
#
# for name,para in resnet18.model.named_parameters():
#     if name in mapping1:
#         para.data=pretrain_weights_dict[mapping1[name]].data
#
# for name, buf in resnet18.model.named_buffers():
#    if name in mapping1:
#         buf.data = pretrain_weights_dict[mapping1[name]].data
