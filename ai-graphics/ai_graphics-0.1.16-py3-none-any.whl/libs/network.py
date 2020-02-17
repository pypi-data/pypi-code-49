from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms
from .logger import Logger

__all__ = ['Network']


class Network(nn.Module):
    def __init__(self, model_name, ctx_id=-1):
        super(Network, self).__init__()
        self.model_name = model_name
        self.device = torch.device("cuda:" + str(ctx_id)) if ctx_id > -1 else torch.device("cpu")

    @staticmethod
    def transform_data():
        """
        数据增强函数，可改写
        :return:
        """
        data_transforms = {
            'train': transforms.Compose([
                transforms.Resize((224, 224)),
                # transforms.RandomCrop(224),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor()
            ]),
            'val': transforms.Compose([
                transforms.Resize((224, 224)),
                # transforms.CenterCrop(224),
                transforms.ToTensor()
            ])
        }

        return data_transforms

    def _load_data(self, data_dir, batch_size):
        import os
        data_transforms = self.transform_data()
        image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x])
                          for x in ['train', 'val']}
        dataset_loaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True)
                           for x in ['train', 'val']}
        dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}

        return dataset_loaders, dataset_sizes

    def  create_model(self, num_classes):
        """
        创建模型，可改写
        :return:
        """
        model = models.resnet18(pretrained=True)
        num_feature = model.fc.in_features
        model.fc = nn.Linear(num_feature, num_classes)
        model = torch.load(self.model_name)
        if torch.cuda.is_available():
            model = model.to(self.device)

        return model

    @staticmethod
    def _get_loss_function():
        criterion = nn.CrossEntropyLoss()
        return criterion

    @staticmethod
    def _get_optimizer(model):
        optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
        return optimizer

    @staticmethod
    def _get_lr_function(optimizer):
        # Decay LR by a factor of 0.1 every 7 epochs
        lr = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)
        return lr

    def train(self, data_dir, num_classes, batch_size=32, num_epochs=15):
        import time
        # 1、加载数据集
        dataset_loaders, dataset_sizes = self._load_data(data_dir, batch_size)
        # 2、创建模型
        model = self.create_model(num_classes)
        # 3、定义损失函数
        criterion = self._get_loss_function()
        # 4、定义优化器
        optimizer = self._get_optimizer(model)
        # 5、定义学习率衰减函数
        scheduler = self._get_lr_function(optimizer)

        best_model = model.state_dict()
        best_acc = 0.0

        # 6、训练模型
        for epoch in range(num_epochs):
            print('Epoch {}/{}'.format(epoch, num_epochs - 1))
            begin_time = time.time()
            for phase in ['train', 'val']:
                count_batch = 0
                if phase == 'train':
                    scheduler.step()
                    model.train(True)  # Set model to training mode
                else:
                    model.train(False)  # Set model to evaluate mode
                running_loss = 0.0
                running_corrects = 0.0

                for data in dataset_loaders[phase]:
                    count_batch += 1
                    inputs, labels = data
                    if torch.cuda.is_available():
                        inputs, labels = inputs.to(self.device), labels.to(self.device)

                    optimizer.zero_grad()
                    outputs = model(inputs)
                    _, preds = torch.max(outputs.data, 1)
                    loss = criterion(outputs, labels)
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                    running_loss += loss.item()
                    running_corrects += torch.sum(preds == labels.data).to(torch.float32)

                    if count_batch % 10 == 0:
                        batch_loss = running_loss / (batch_size * count_batch)
                        batch_acc = running_corrects / (batch_size * count_batch)
                        print('{} Epoch [{}] Batch [{}] Loss: {:.4f} Acc: {:.4f} Time: {:.4f}s'. \
                              format(phase, epoch, count_batch, batch_loss, batch_acc, time.time() - begin_time))
                        begin_time = time.time()

                epoch_loss = running_loss / dataset_sizes[phase]
                epoch_acc = running_corrects / dataset_sizes[phase]
                print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

                # (1) Log the scalar values
                info = {'loss': epoch_loss, 'accuracy': epoch_acc}
                if phase == 'train':
                    logger = Logger('./logs/train')
                else:
                    logger = Logger('./logs/val')

                for tag, value in info.items():
                    logger.scalar_summary(tag, value, epoch)

                # (2) Log values and gradients of the parameters (histogram)
                for tag, value in model.named_parameters():
                    tag = tag.replace('.', '/')
                    logger.histo_summary(tag, value.data.cpu().numpy(), epoch)
                    logger.histo_summary(tag + '/grad', value.grad.data.cpu().numpy(), epoch)

                # (3) Log the images
                info = {'images': inputs.view(-1, 3, 224, 224)[:5].cpu().data.numpy()}

                for tag, images in info.items():
                    logger.image_summary(tag, images, epoch)

                if phase == 'val' and epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model = model.state_dict()

        print('Best val Acc: {:4f}'.format(best_acc))
        model.load_state_dict(best_model)

        # 7、保存模型
        torch.save(model, self.model_name)
        return model
