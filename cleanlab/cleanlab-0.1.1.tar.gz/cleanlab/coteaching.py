#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import torch 
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torchvision.transforms as transforms
from models.coteaching_pytorch import CNN
import argparse, sys
import numpy as np
import datetime
import shutil


# In[4]:


# Loss functions
def loss_coteaching(
    y_1, 
    y_2, 
    t, 
    forget_rate, 
    ind, 
    noise_or_not,
    class_weights=None,
):
    '''Co-Teaching Loss function.
    Source: https://github.com/bhanML/Co-teaching/blob/master/loss.py

    Parameters
    ----------
    y_1 : Tensor array
      Output logits from model 1

    y_2 : Tensor array
      Output logits from model 2

    t : np.array
      List of Noisy Labels (t standards for targets)

    forget_rate : float
      Decimal between 0 and 1 for how quickly the models forget what they learn.
      Just use rate_schedule[epoch] for this value

    ind : iterable / list / np.array
      Indices from train_loader created like this:
      for i, (images, labels, indexes) in enumerate(train_loader):
        ind=indexes.cpu().numpy().transpose()

    noise_or_not : np.array
      Np.array of length number of total training examples in dataset that says
      for every training example if its prediction is equal to its given label.
      For each example in the training dataset, true if equal, else false.

    class_weights : Tensor array, shape (Number of classes x 1), Default: None
      A np.torch.tensor list of length number of classes with weights
    '''
    loss_1 = F.cross_entropy(y_1, t, reduce=False, weight=class_weights)
    ind_1_sorted = np.argsort(loss_1.data.cpu())
    loss_1_sorted = loss_1[ind_1_sorted]

    loss_2 = F.cross_entropy(y_2, t, reduce=False, weight=class_weights)
    ind_2_sorted = np.argsort(loss_2.data.cpu())
    loss_2_sorted = loss_2[ind_2_sorted]

    remember_rate = 1 - forget_rate
    num_remember = int(remember_rate * len(loss_1_sorted))

    pure_ratio_1 = np.sum(
        noise_or_not[ind[ind_1_sorted[:num_remember]]]) / float(num_remember)
    pure_ratio_2 = np.sum(
        noise_or_not[ind[ind_2_sorted[:num_remember]]]) / float(num_remember)

    ind_1_update=ind_1_sorted[:num_remember]
    ind_2_update=ind_2_sorted[:num_remember]
    # Share updates between the two models.
    loss_1_update = F.cross_entropy(
        y_1[ind_2_update], t[ind_2_update], weight=class_weights)
    loss_2_update = F.cross_entropy(
        y_2[ind_1_update], t[ind_1_update], weight=class_weights)

    return (
        torch.sum(loss_1_update) / num_remember,
        torch.sum(loss_2_update) / num_remember,
        pure_ratio_1,
        pure_ratio_2,
    )


def adjust_learning_rate(optimizer, epoch):
    for param_group in optimizer.param_groups:
        param_group['lr']=alpha_plan[epoch]
        param_group['betas']=(beta1_plan[epoch], 0.999) # Only change beta1


def accuracy(logit, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    output = F.softmax(logit, dim=1)
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


# Train the Model
def train(train_loader,epoch, model1, optimizer1, model2, optimizer2):
    print('Training', model_str)
    pure_ratio_list=[]
    pure_ratio_1_list=[]
    pure_ratio_2_list=[]
    
    train_total=0
    train_correct=0 
    train_total2=0
    train_correct2=0 

    for i, (images, labels, indexes) in enumerate(train_loader):
        ind=indexes.cpu().numpy().transpose()
        if i>args.num_iter_per_epoch:
            break
      
        images = Variable(images).cuda()
        labels = Variable(labels).cuda()
        
        # Forward + Backward + Optimize
        logits1=model1(images)
        prec1, _ = accuracy(logits1, labels, topk=(1, 5))
        train_total+=1
        train_correct+=prec1

        logits2 = model2(images)
        prec2, _ = accuracy(logits2, labels, topk=(1, 5))
        train_total2+=1
        train_correct2+=prec2
        loss_1, loss_2, pure_ratio_1, pure_ratio_2 = loss_coteaching(
            logits1,
            logits2,
            labels,
            rate_schedule[epoch],
            ind,
            noise_or_not,
            class_weights=train_dataset.class_weights,
        )
        pure_ratio_1_list.append(100*pure_ratio_1)
        pure_ratio_2_list.append(100*pure_ratio_2)

        optimizer1.zero_grad()
        loss_1.backward()
        optimizer1.step()
        optimizer2.zero_grad()
        loss_2.backward()
        optimizer2.step()
        if (i+1) % args.print_freq == 0:
            print ('Epoch [%d/%d], Iter [%d/%d] Training Accuracy1: %.4F, Training Accuracy2: %.4f, Loss1: %.4f, Loss2: %.4f, Pure Ratio1: %.4f, Pure Ratio2 %.4f' 
                  %(epoch+1, args.n_epoch, i+1, len(train_dataset)//batch_size, prec1, prec2, loss_1.data.item(), loss_2.data.item(), np.sum(pure_ratio_1_list)/len(pure_ratio_1_list), np.sum(pure_ratio_2_list)/len(pure_ratio_2_list)))

    train_acc1=float(train_correct)/float(train_total)
    train_acc2=float(train_correct2)/float(train_total2)
    return train_acc1, train_acc2, pure_ratio_1_list, pure_ratio_2_list


# Evaluate the Model
def evaluate(test_loader, model1, model2):
    print 'Evaluating %s...' % model_str
    model1.eval()    # Change model to 'eval' mode.
    correct1 = 0
    total1 = 0
    for images, labels, _ in test_loader:
        images = Variable(images).cuda()
        logits1 = model1(images)
        outputs1 = F.softmax(logits1, dim=1)
        _, pred1 = torch.max(outputs1.data, 1)
        total1 += labels.size(0)
        correct1 += (pred1.cpu() == labels).sum()

    model2.eval()    # Change model to 'eval' mode 
    correct2 = 0
    total2 = 0
    for images, labels, _ in test_loader:
        images = Variable(images).cuda()
        logits2 = model2(images)
        outputs2 = F.softmax(logits2, dim=1)
        _, pred2 = torch.max(outputs2.data, 1)
        total2 += labels.size(0)
        correct2 += (pred2.cpu() == labels).sum()
 
    acc1 = 100*float(correct1)/float(total1)
    acc2 = 100*float(correct2)/float(total2)
    return acc1, acc2


# In[5]:


parser = argparse.ArgumentParser()
parser.add_argument('--lr', type = float, default = 0.001)
parser.add_argument('--result_dir', type = str,
    help = 'dir to save result txt files', default = 'results/')
parser.add_argument('--batch_size', type = float, default = 128)
parser.add_argument('--noise_rate', type = float,
    help = 'corruption rate, should be less than 1', default = 0.2)
parser.add_argument('--forget_rate', type = float,
    help = 'forget rate', default = None)
parser.add_argument('--num_gradual', type = int, default = 10,
    help='how many epochs for linear drop rate, can be 5, 10, 15. \
    This parameter is equal to Tk for R(T) in Co-teaching paper.')
parser.add_argument('--exponent', type = float, default = 1,
    help='exponent of the forget rate, can be 0.5, 1, 2. \
    This parameter is equal to c in Tc for R(T) in Co-teaching paper.')
parser.add_argument('--top_bn', action='store_true', default=False)
parser.add_argument('--n_epoch', type=int, default=250)
parser.add_argument('--seed', type=int, default=1)
parser.add_argument('--print_freq', type=int, default=50)
parser.add_argument('--num_workers', type=int, default=4,
    help='how many subprocesses to use for data loading')
parser.add_argument('--num_iter_per_epoch', type=int, default=400)
parser.add_argument('--epoch_decay_start', type=int, default=80)
parser.add_argument('--fn', type=str, default='~')
parser.add_argument('--train_mask_dir', type=str, default=None)
parser.add_argument('--num_classes', type=int, default=10)

args = parser.parse_args()

# Seed
torch.manual_seed(args.seed)
torch.cuda.manual_seed(args.seed)

# Hyper Parameters
batch_size = args.batch_size
learning_rate = args.lr 
input_channel=3


# In[ ]:




train_dataset = CIFAR10(
    root='/home/cgn/data/',
    download=True,  
    train=True,
#         transform=transforms.ToTensor(),
    transform=transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
#             transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
    ]),
    noise_type=args.noise_type,
    noise_rate=args.noise_rate,
    fn=args.fn,  # path to noisy labels
    train_mask_dir=args.train_mask_dir,  # path to train mask
)

test_dataset = CIFAR10(
    root='/home/cgn/data/',
    download=True,  
    train=False, 
    transform=transforms.ToTensor(),
    noise_type=args.noise_type,
    noise_rate=args.noise_rate,
)


if args.forget_rate is None:
    forget_rate=args.noise_rate
else:
    forget_rate=args.forget_rate

noise_or_not = train_dataset.noise_or_not

# Adjust learning rate and betas for Adam Optimizer
mom1 = 0.9
mom2 = 0.1
alpha_plan = [learning_rate] * args.n_epoch
beta1_plan = [mom1] * args.n_epoch
for i in range(args.epoch_decay_start, args.n_epoch):
    alpha_plan[i] = float(args.n_epoch - i) / (
        args.n_epoch - args.epoch_decay_start) * learning_rate
    beta1_plan[i] = mom2


        
# define drop rate schedule
rate_schedule = np.ones(args.n_epoch)*forget_rate
rate_schedule[:args.num_gradual] = np.linspace(
    0, forget_rate**args.exponent, args.num_gradual)

model_str=args.dataset + '_coteaching_' + args.noise_type + '_' + str(args.noise_rate)


def main():
    # Data Loader (Input Pipeline)
    print('loading dataset...')
    train_loader = torch.utils.data.DataLoader(
        dataset=train_dataset,
        batch_size=batch_size, 
        num_workers=args.num_workers,
        drop_last=True,
        shuffle=True,
    )
    
    test_loader = torch.utils.data.DataLoader(
        dataset=test_dataset,
        batch_size=batch_size, 
        num_workers=args.num_workers,
        drop_last=True,
        shuffle=False,
    )
    # Define models
    print('building model...')
    cnn1 = CNN(input_channel=input_channel, n_outputs=num_classes)
    cnn1.cuda()
    print cnn1.parameters
    optimizer1 = torch.optim.Adam(cnn1.parameters(), lr=learning_rate)
    
    cnn2 = CNN(input_channel=input_channel, n_outputs=num_classes)
    cnn2.cuda()
    print cnn2.parameters
    optimizer2 = torch.optim.Adam(cnn2.parameters(), lr=learning_rate)

    mean_pure_ratio1=0
    mean_pure_ratio2=0

    epoch=0
    train_acc1=0
    train_acc2=0
    # evaluate models with random weights
    test_acc1, test_acc2=evaluate(test_loader, cnn1, cnn2)
    print('Epoch [%d/%d] Test Accuracy on the %s test images: Model1 %.4f %% ' +
          'Model2 %.4f %% Pure Ratio1 %.4f %% Pure Ratio2 %.4f %%' % \
          (epoch+1, args.n_epoch, len(test_dataset), test_acc1, test_acc2,
           mean_pure_ratio1, mean_pure_ratio2))

    # training
    for epoch in range(1, args.n_epoch):
        # train models
        cnn1.train()
        adjust_learning_rate(optimizer1, epoch)
        cnn2.train()
        adjust_learning_rate(optimizer2, epoch)
        train_acc1, train_acc2, pure_ratio_1_list, pure_ratio_2_list=train(
            train_loader, epoch, cnn1, optimizer1, cnn2, optimizer2)
        # evaluate models
        test_acc1, test_acc2=evaluate(test_loader, cnn1, cnn2)
        # save results
        mean_pure_ratio1 = sum(pure_ratio_1_list)/len(pure_ratio_1_list)
        mean_pure_ratio2 = sum(pure_ratio_2_list)/len(pure_ratio_2_list)
        print('Epoch [%d/%d] Test Accuracy on the %s test images: Model1 %.4f '+
              '%% Model2 %.4f %%, Pure Ratio 1 %.4f %%, Pure Ratio 2 %.4f %%' %\
              (epoch+1, args.n_epoch, len(test_dataset), test_acc1, test_acc2,
               mean_pure_ratio1, mean_pure_ratio2))

if __name__=='__main__':
    main()

