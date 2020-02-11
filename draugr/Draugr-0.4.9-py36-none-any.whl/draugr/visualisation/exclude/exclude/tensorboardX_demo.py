#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from torch.utils.tensorboard import SummaryWriter
from torchvision.utils import make_grid

__author__ = 'Christian Heider Nielsen'

# demo.py

import torch
import numpy
import torchvision.models as models
from torchvision import datasets

resnet18 = models.resnet18(False)
writer = SummaryWriter()
sample_rate = 44100
freqs = [262, 294, 330, 349, 392, 440, 440, 440, 440, 440, 440]

for n_iter in range(100):

  dummy_s1 = torch.rand(1)
  dummy_s2 = torch.rand(1)
  # data grouping by `slash`
  writer.add_scalar('data/scalar1', dummy_s1[0], n_iter)
  writer.add_scalar('data/scalar2', dummy_s2[0], n_iter)

  writer.add_scalars('data/scalar_group', {'xsinx':  n_iter * numpy.sin(n_iter),
                                           'xcosx':  n_iter * numpy.cos(n_iter),
                                           'arctanx':numpy.arctan(n_iter)
                                           }, n_iter)

  dummy_img = torch.rand(32, 3, 64, 64)  # output from network
  if n_iter % 10 == 0:
    x = make_grid(dummy_img, normalize=True, scale_each=True)
    writer.add_image('Image', x, n_iter)

    dummy_audio = torch.zeros(sample_rate * 2)
    for i in range(x.size(0)):
      # amplitude of sound should in [-1, 1]
      dummy_audio[i] = numpy.cos(freqs[n_iter // 10] * numpy.pi * float(i) / float(sample_rate))
    writer.add_audio('myAudio', dummy_audio, n_iter, sample_rate=sample_rate)

    writer.add_text('Text', 'text logged at step:' + str(n_iter), n_iter)

    for name, param in resnet18.named_parameters():
      writer.add_histogram(name, param.clone().cpu().data.numpy(), n_iter)

    # needs tensorboard 0.4RC or later
    writer.add_pr_curve('xoxo', numpy.random.randint(2, size=100), numpy.random.rand(100), n_iter)

dataset = datasets.MNIST(os.environ.get('DATASETS_HOME',
                                        '~/Data/Datasets') + '/Text/mnist',
                         train=False,
                         download=True)
images = dataset.test_data[:100].float()
label = dataset.test_labels[:100]

features = images.view(100, 784)
writer.add_embedding(features, metadata=label, label_img=images.unsqueeze(1))

# export scalar data to JSON for external processing
writer.export_scalars_to_json("./all_scalars.json")
writer.close()
