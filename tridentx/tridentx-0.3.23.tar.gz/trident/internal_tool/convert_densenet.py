
import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import torch
import torchvision
from torchvision.models import  vgg,resnet,densenet121

dense121_1=densenet121(True).cpu()

_session = get_session()
dense121=DenseNet121(pretrained=False)
#print(dense121.infer_single_image(read_image('cat.jpg'),5))
dense121.model.cpu()

pretrain_weights =list(dense121_1.named_parameters())
buf=list(dense121_1.named_buffers())
buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
pretrain_weights.extend(buf)


mapping=OrderedDict()
pretrain_weights_dict=OrderedDict()
for  item in pretrain_weights:
    mapping[item[0]]=''
    pretrain_weights_dict[item[0]]=item[1]



pretrain_weights1=list(dense121.model.named_parameters())
buf=list(dense121.model.named_buffers())
buf=[ item for item in buf if  'running_mean' in  item[0] or  'running_var' in  item[0]]
pretrain_weights1.extend(buf)

keyword_map={"denseblock1":"denseblock1",
"denseblock2":"denseblock2",
"denseblock3":"denseblock3",
"denseblock4":"denseblock4",
"transitiondown1":"transition1",
"transitiondown2":"transition2",
"transitiondown3":"transition3"}

no_match=[]

for  i in range(len(pretrain_weights1)):
    item=pretrain_weights1[i]
    k1=None
    for k in keyword_map.keys():
        if k in  item[0]:
            k1=keyword_map[k]


    if ('norm' in item[0] or 'bn' in  item[0] ) and 'weight'in item[0] :
        for k,v in pretrain_weights_dict.items():
            test_cnt=len( [ vv for vv in keyword_map.values() if (vv in k)])
            if (k1 is not None  and k1 in k ) or (k1 is None and test_cnt==0):
                if mapping[k]=='' and  ('bn' in k or 'norm' in k) and 'weight'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif ('norm' in item[0] or 'bn' in  item[0] ) and 'bias' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (k1 is None and len( [ vv for vv in keyword_map.values() if (vv in k)])==0):
                if mapping[k]==''and  ('bn' in k or 'norm' in k) and 'bias'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif  'running_mean'in item[0] :
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (k1 is None and len( [ vv for vv in keyword_map.values() if (vv in k)])==0):
                if mapping[k]==''and   'running_mean'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif 'running_var' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len( [ vv for vv in keyword_map.values() if (vv in k)])==0):
                if mapping[k]==''  and 'running_var'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif ('conv' in item[0] or 'denseblock' in item[0]) and 'weight' in item[0]:
        for k,v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or (k1 is None and len( [ vv for vv in keyword_map.values() if (vv in k)])==0):
                if mapping[k]==''and ( 'conv' in k or 'feature' in k) and 'weight'in k and item[1].shape==v.shape:
                    mapping[k]=item[0]
                    break

    elif ('conv' in item[0]or 'denseblock' in item[0])  and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if (k1 is not None and k1 in k) or ( k1 is None and len( [ vv for vv in keyword_map.values() if (vv in k)])==0):
                if mapping[k] == '' and ( 'conv' in k or 'feature' in k)  and 'bias' in k and item[1].shape == v.shape:
                    mapping[k] = item[0]
                    break

    elif 'classifier' in item[0] and 'weight' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if mapping[k] == '' and 'classifier' in k and 'weight' in k and item[1].shape == v.shape:
                mapping[k] = item[0]
                break

    elif 'classifier' in item[0] and 'bias' in item[0]:
        for k, v in pretrain_weights_dict.items():
            if mapping[k] == '' and 'classifier' in k and 'bias' in k and item[1].shape == v.shape:
                mapping[k] = item[0]
                break

    else:
        no_match.append(item)


print(len(set(list(mapping.key_list))))
print(len(set(list(mapping.value_list))))
mapping1=OrderedDict()
for k,v in mapping.items():
    mapping1[v]=k


for name,para in dense121.model.named_parameters():
    if name in mapping1:
        para.data=pretrain_weights_dict[mapping1[name]].data

for name, buf in dense121.model.named_buffers():
    if name in mapping1:
        buf.data = pretrain_weights_dict[mapping1[name]].data

dense121.model.eval()
print(dense121.infer_single_image(read_image('cat.jpg'),5))
dense121.model.cpu()
#vgg19.save_model('vgg19.pth')
torch.save(dense121.model,'densenet121.pth')
# w=np.array(list(vgg19.model.named_parameters()))
# np.save('vgg19_weights.npy',w)



