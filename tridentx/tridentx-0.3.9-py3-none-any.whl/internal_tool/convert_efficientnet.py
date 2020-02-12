
import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import torch

effb0=EfficientNet(1.0, 1.0, 224, 0.2, model_name='efficientnet-b0',include_top=True,num_classes=1000)
pretrain_weights1 =list(effb0.model.named_parameters())
buf=list(effb0.model.named_buffers())
buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
pretrain_weights1.extend(buf)



effnetb0=torch.load('efficientnet-b0-355c32eb.pth')
pretrain_weights=OrderedDict()

for k,v in effnetb0.items():
    if 'weight' in k or 'bias' in k or  'running_mean' in k or  'running_var' in k:
        pretrain_weights[k]=v




mapping=OrderedDict()
pretrain_weights_dict=OrderedDict()
for  item in pretrain_weights.item_list:
    mapping[item[0]]=''
    pretrain_weights_dict[item[0]]=item[1]

keyword_map1={"_blocks.0.":"block1a",
"_blocks.1.":"block2a",
"_blocks.2.":"block2b",
"_blocks.3.":"block3a",
"_blocks.4.":"block3b",
"_blocks.5.":"block4a",
"_blocks.6.":"block4b",
"_blocks.7.":"block4c",
"_blocks.8.":"block5a",
"_blocks.9.":"block5b",
"_blocks.10.":"block5c",
"_blocks.11.":"block6a",
"_blocks.12.":"block6b",
"_blocks.13.":"block6c",
"_blocks.14.":"block6d",
"_blocks.15.":"block7a",
"fc":"fc"}
keyword_map={}
for k,v in keyword_map1.items():
    keyword_map[v]=k



no_match=[]

for  i in range(len(pretrain_weights1)):
    item=pretrain_weights1[i]
    k1 = None
    for k in keyword_map.keys():
        if k in item[0]:
            k1 = keyword_map[k]

    if ('norm' in item[0] or 'bn' in  item[0] ) and 'weight'in item[0] :
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]=='' and  ('bn' in k or 'norm' in k) and 'weight'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif ('norm' in item[0] or 'bn' in  item[0] ) and 'bias' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]==''and  ('bn' in k or 'norm' in k) and 'bias'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif  'running_mean'in item[0] :
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]==''and   'running_mean'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif 'running_var' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]==''  and 'running_var'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break


    elif  'squeeze.weight' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]==''and   '_se_reduce.weight'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif 'squeeze.bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (
                    k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and '_se_reduce.bias' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    elif 'excite.weight' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (
                    k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and '_se_expand.weight'in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break 
    elif 'excite.bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (
                    k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and '_se_expand.bias' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    elif ('conv' in item[0]  or 'depthwise'in item[0]  ) and 'weight' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k]==''and ( 'conv' in k or 'feature' in k) and 'weight'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif ('conv' in item[0]  or 'depthwise'in item[0] )  and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and ( 'conv' in k or 'feature' in k)  and 'bias' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    elif 'fc' in item[0] and 'weight' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and 'fc' in k and 'weight' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    elif 'fc' in item[0] and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len([vv for vv in keyword_map.values() if (vv in k)]) == 0):
                if mapping[k] == '' and 'fc' in k and 'bias' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    else:
        no_match.append(item)


print(len(set(list(mapping.key_list))))
print(len(set(list(mapping.value_list))))
mapping1=OrderedDict()
for k,v in mapping.items():
    mapping1[v]=k



for name,para in effb0.model.named_parameters():
    if name in mapping1:
        para.data=pretrain_weights_dict[mapping1[name]].data

for name, buf in effb0.model.named_buffers():
    if name in mapping1:
        buf.data = pretrain_weights_dict[mapping1[name]].data


print(effb0.infer_single_image('cat.jpg',5))

effb0.model.cpu()
#vgg19.save_model('vgg19.pth')
torch.save(effb0.model,'efficientnet-b0.pth')


