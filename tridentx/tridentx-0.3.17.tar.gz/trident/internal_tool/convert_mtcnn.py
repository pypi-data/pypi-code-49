import os
import cv2
os.environ['TRIDENT_BACKEND'] = 'pytorch'
#!pip install tridentx --upgrade
import trident as T
from trident import *
import torch
import torchvision
import inspect

onet_old=Onet(True)
onet=Onet(False)
onet_old.model.cpu()
onet.model.cpu()
onet.model.trainable=True

paras_old=list(onet_old.model.named_parameters())
paras=list(onet.model.named_parameters())

print('paras_old',len(paras_old))
print('paras',len(paras))

buffer_old=list(onet_old.model.named_buffers())
buffer=list(onet.model.named_buffers())


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




onet.model.eval()
onet.model.cpu()

#vgg19.save_model('vgg19.pth')
torch.save(onet.model,'onet.pth')


