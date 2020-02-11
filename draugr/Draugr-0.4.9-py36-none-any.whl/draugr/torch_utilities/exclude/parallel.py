#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from draugr.torch_utilities.datasets.random_dataset import RandomDataset

__author__ = 'Christian Heider Nielsen'
__doc__ = ''

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

# Parameters and DataLoaders
input_size = 5
output_size = 2

batch_size = 30
data_size = 200

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

rand_loader = DataLoader(dataset=RandomDataset(input_size, data_size),
                         batch_size=batch_size, shuffle=True)


class Model(nn.Module):
  # Our model

  def __init__(self, input_size, output_size):
    super(Model, self).__init__()
    self.fc = nn.Linear(input_size, output_size)

  def forward(self, input):
    output = self.fc(input)
    print("\tIn Model: input size", input.size(),
          "output size", output.size())

    return output


model = Model(input_size, output_size)
if torch.cuda.device_count() > 1:
  print("Let's use", torch.cuda.device_count(), "GPUs!")
  # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
  model = nn.DataParallel(model)

model.to(get_torch_device())

for data in rand_loader:
  input = data.to(get_torch_device())
  output = model(input)
  print("Outside: input size", input.size(),
        "output_size", output.size())
