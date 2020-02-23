import numpy as np
import pandas as pd
import torch
from torch import nn
from matplotlib import pyplot as plt



class LearningRateFinder():
    """Train model using different learning rates within a range to find optimal  

    Important methods are fit, find_optimal_lr.

    LearningRateFinder() implements a fit method that trains a given model using varied learning rate within a range 
    for number of steps stores the corresponding losses.

    Args:
    -----
    model: torch.nn.module
        instantiated model of type nn.module

    criterion : torch.nn.criterion 
        loss to be used function, e.g nn.CrossEntropyLoss

    optimizer : torch.optim
        optimizer for training e.g torch.optim.SGD, torch.optim.Adam


    Attributes:
    ----------
    loss_history: dict
        dict containing loss value for corresponding learning rate

    """

    def __init__(self, model:nn.Module, criterion, optimizer):
        self.model= model
        self.criterion = criterion
        self.optimizer = optimizer
        self.loss_history = {}

    def fit(self, data_loader:torch.utils.data.DataLoader, steps=100, min_lr=1e-8, max_lr=1):
        """Trains the model for number of steps using varied learning rate and store the statistics

        Args:
        ------
        data_loader: torch.utils.data.DataLoader
            dataloader for training data

        steps: int (optional, default 100)
            number of training steps in terms of batches

        min_lr: float (optional, default 1e-8)
            start of the range for learning rate search

        max_lr: float (optional, default 1.0)
            end of the range for learning rate search
        """
        self.loss_history = {}
        self.model.train()
        completed_steps = 0
        current_lr = min_lr

        while completed_steps < steps:
            for X, y in data_loader:
                for param_group in self.optimizer.param_groups:
                    param_group['lr'] = current_lr
                self.optimizer.zero_grad()
                y_pred = self.model(X)
                loss = self.criterion(y_pred, y)
                loss.backward()
                self.optimizer.step()
                self.loss_history[current_lr] = loss.item()

                current_lr += (max_lr - min_lr)/steps

                completed_steps+=1
                if completed_steps > steps:
                    break


    def plot(self, smoothing=True):
        """Shows loss vs learning rate(log scale) in a matplotlib plot

        Args:
        -------
        smoothing: bool (optional, default True)
            controls whether exponential moving average smoothing is applied
        """
        loss_data = pd.Series(list(self.loss_history.values()))
        if smoothing:
            loss_data = loss_data.ewm(alpha=.02).mean()
            loss_data = loss_data.divide(pd.Series([1-.98**i for i in range(1,loss_data.shape[0]+1)])) # bias correction
        plt.plot(list(self.loss_history.keys()), loss_data)
        plt.xscale('log')
        plt.title('Loss vs Learning rate')
        plt.xlabel('Learning rate (log scale)')
        plt.ylabel('Loss (exponential moving average)')
        plt.show()

    def find_optimal_lr(self):
        """Not implemented"""
        loss_data = pd.Series(list(self.loss_history.values()))
        loss_data = loss_data.ewm(alpha=.02).mean().divide(pd.Series([1-.98**i for i in range(1,loss_data.shape[0]+1)]))
        plt.show()