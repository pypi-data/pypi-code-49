
import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'tensorflow'
#!pip install tridentx --upgrade
import trident as T
from trident import *

import tensorflow as tf



resnet50_1=tf.keras.applications.ResNet50(
             include_top=True,
             weights='imagenet',
             input_shape=(224,224,3),
             pooling = 'avg',
             classes=1000)




pretrain_weights =OrderedDict()
pretrain_weights_dict =OrderedDict()
for w in resnet50_1.weights:
    pretrain_weights[w.name]=to_numpy(w.shape)
    pretrain_weights_dict[w.name]=to_numpy(w)

resnet50=ResNet50(pretrained=False)
resnet50_m=resnet50.model

pretrain_weights1 =OrderedDict()
for w in resnet50_m.weights:
    pretrain_weights1[w.name]=to_numpy(w.shape)




mapping=OrderedDict()
#pretrain_weights_dict=OrderedDict()
for  k,v in pretrain_weights.items():
    mapping[k]=''






no_match=[]

for  i in range(len(pretrain_weights1)):
    item=pretrain_weights1.item_list[i]
    if ('norm' in item[0] or 'bn' in  item[0] ) and 'gamma'in item[0] and  item[0] not in mapping.value_list :
        for k,v in pretrain_weights.items():
            if mapping[k]==''   and  ('bn' in k or 'norm' in k) and 'gamma'in k and np.array_equal(item[1],v):
                mapping[k]=item[0]
                break

    elif ('norm' in item[0] or 'bn' in  item[0] ) and 'beta' in item[0] and  item[0] not in mapping.value_list:
        for k,v in pretrain_weights.items():
            if mapping[k]=='' and  ('bn' in k or 'norm' in k) and 'beta'in k and np.array_equal(item[1],v):
                mapping[k]=item[0]
                break

    elif  'moving_mean'in item[0] and  item[0] not in mapping.value_list:
        for k,v in pretrain_weights.items():
            if mapping[k]==''  and   'moving_mean'in k and np.array_equal(item[1],v):
                mapping[k]=item[0]
                break

    elif 'moving_variance' in item[0] and  item[0] not in mapping.value_list:
        for k,v in pretrain_weights.items():
            if mapping[k]=='' and 'moving_variance'in k and np.array_equal(item[1],v):
                mapping[k]=item[0]
                break



    elif ('conv' in item[0] or 'block' in item[0]or 'sequential' in item[0])  and 'fc' not in item[0] and 'kernel' in item[0] and  item[0] not in mapping.value_list:
        for k,v in pretrain_weights.items():
            if mapping[k]==''and ( 'conv' in k or 'block' in k) and 'kernel'in k and np.array_equal(item[1],v):
                mapping[k]=item[0]
                break

    elif ('conv' in item[0]or 'block' in item[0] or 'sequential' in item[0])  and 'fc' not in item[0]  and 'bias' in item[0] and  item[0] not in mapping.value_list:
        for k, v in pretrain_weights.items():
            if mapping[k] == ''and ( 'conv' in k or 'block' in k)  and 'bias' in k and np.array_equal(item[1],v):
                mapping[k] = item[0]
                break



    else:
        no_match.append(item)

if 'probs/kernel:0' in mapping:
    mapping['probs/kernel:0'] = 'sequential/fc1000/kernel:0'
if 'probs/bias:0' in mapping:
    mapping['probs/bias:0'] = 'sequential/fc1000/bias:0'

print(len(set(list(mapping.key_list))))
print(len(set(list(mapping.value_list))))
mapping1=OrderedDict()
for k,v in mapping.items():
    mapping1[v]=k

for layer in resnet50_m.layers:
    if layer is BatchNorm:
        layer._USE_V2_BEHAVIOR=False
    w_new=[]
    for i in range(len(layer.weights)):
        w_var=layer.weights[i]
        w_new.append(pretrain_weights_dict[mapping1[w_var.name]])
    w=layer.get_weights()
    layer.set_weights(w_new)



resnet50.model=resnet50_m
resnet50_m.save('resnet50.h5')
print(resnet50.infer_single_image(read_image('cat.jpg'),5))

print('')

# w=np.array(list(vgg19.model.named_parameters()))
# np.save('vgg19_weights.npy',w)



