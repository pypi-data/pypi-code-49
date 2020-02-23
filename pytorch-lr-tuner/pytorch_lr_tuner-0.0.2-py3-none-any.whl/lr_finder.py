import torch
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class LearningRateFinder():
    """
    Class for finding optimum learning rate for given neural network.

    Parameters:
    -----------
    estimator: nn.Module
        Class extended from nn.Module defining the desired architecture

    config: dict
        Dictionary containing the configuaration of the instance of estimator class

    optimizer: str
        String defining the type of optimizer to be instantiated. Must be either 'adam' or 'sgd'

    criterion: torch.nn.criterion
        Instance of the criterion class which will be used as the loss function for the instance of estimator

    train_set: torch.utils.data.TensorDataset
        Subset of data used for training

    val_set: torch.utils.data.TensorDataset
        Subset of data used for validation

    batch: int, optional (default = 32)
        Mini batch size


    Attributes:
    -----------
    model: nn.Module
        Instance of estimator class with the architecture provided in config

    train_loader: torch.utils.data.DataLoader
        Dataset loader of train set

    val_loader: torch.utils.data.DataLoader
        Dataset loader of validation set

    lr_history: dict
        Dictionary containing losses against learning rates

    """

    def __init__(self, estimator, config: dict, optimizer: str, criterion, train_set, val_set, batch=32):

        # Model Instantiation
        self.model = estimator(**config)

        # Optimizer Instantiation
        if optimizer == 'adam':
            self.optimizer = torch.optim.Adam(self.model.parameters())

        elif optimizer == 'sgd':
            self.optimizer = torch.optim.SGD(self.model.parameters(), lr=0.1)

        self.criterion = criterion

        # Load Data from Tensor Dataset
        self.train_loader = torch.utils.data.DataLoader(
            train_set, batch_size=batch, shuffle=True)
        self.val_loader = torch.utils.data.DataLoader(
            val_set, batch_size=batch, shuffle=True)

        # LR History Tracker
        self.lr_history = dict()
        self.smooth_loss = None

    def fit(self, s_lr: float = 1e-7, e_lr: float = 10.0, num_iter=100, verbose=False):
        """
        Function for finding optimal learning rate.

        Args:
        -----
        s_lr: float, optional (default=1e-7)
            Start or minimum learning rate to be searched

        e_lr: float, optional (default=10)
            End or maximum learning rate to be searched

        num_iter: int, optional (default=100)
            Number of training steps on mini batch required for finding optimal learning rate

        verbose: bool, optional (default=False)
            If set to True, prints the track of losses against varied learning rate
        """

        # increment = (e_lr - s_lr) / num_iter
        factor = (e_lr / s_lr) ** (1 / num_iter)

        step_cnt = 0
        terminate = False

        self.model.train()

        while terminate == False:

            for features, labels in self.train_loader:

                step_cnt += 1

                if (step_cnt > num_iter) or (s_lr > e_lr):
                    terminate = True
                    break

                for g in self.optimizer.param_groups:
                    g['lr'] = s_lr

                self.optimizer.zero_grad()

                predictions = self.model(features)
                loss = self.criterion(predictions, labels)

                self.lr_history[s_lr] = loss.item()

                loss.backward()
                self.optimizer.step()

                # s_lr += increment
                s_lr *= factor

        if verbose == True:
            print(self.lr_history)

        print('LR Finder Complete: Call plot() function for visualizing loss VS. log learning rate')

    def plot(self, smoothing=True):
        """
        Function for visualizing loss VS. log learning rate

        Args:
        -----
        smoothing: bool, optional (default=True)
            If set to True, calculates the exponential moving average of the loss and apply bias correction on it. The smoothed loss is plotted against log LR.
        """

        if smoothing == False:
            plt.plot(list(self.lr_history.keys()),
                     list(self.lr_history.values()))
        else:
            self.smooth_loss = pd.Series(list(self.lr_history.values()))

            # Exponential Moving Average
            self.smooth_loss = self.smooth_loss.ewm(alpha=0.05).mean()

            # Bias Correction
            self.smooth_loss = self.smooth_loss.divide(
                pd.Series([1 - (0.95)**i for i in range(1, len(self.smooth_loss))]))

            # gradient = np.gradient(self.smooth_loss, np.log(np.array(list(self.lr_history.keys()))))
            # print(gradient)

            # print(self.lr_history.keys())

            self.smooth_loss = self.smooth_loss.values[5:]
            lr_list = list(self.lr_history.keys())[5:]

            plt.plot(lr_list, self.smooth_loss)

            # self.smooth_loss = self.smooth_loss[~np.isnan(self.smooth_loss)]

            # print(self.smooth_loss[:-1] - self.smooth_loss[1:])
            # print(len(self.smooth_loss[:-1] - self.smooth_loss[1:]))
            # print(np.argmax(self.smooth_loss[:-1] - self.smooth_loss[1:]))

        plt.xscale('log')
        plt.xlabel('Log Learning Rate')

        # plt.yscale('log')
        plt.ylabel('Loss')

        plt.title('Learning Rate Finder')

        plt.grid()

        plt.savefig('loss_vs_lr.png')
        plt.show()

