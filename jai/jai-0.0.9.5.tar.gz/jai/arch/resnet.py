import torch.nn as nn
import torch
import torchvision.models as models


class ResNext50SingleCh(nn.Module):

    def __init__(self, n_classes=(168, 11, 7), pre=True):
        super().__init__()
        arch = models.resnext50_32x4d(pretrained=pre)

        # construct the inlet
        conv0 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
        # Gray: Y = 0.299⋅R + 0.587⋅G + 0.114⋅B
        # conv weights dim order: n_out, n_in, ksize, k_size
        gray_scale_coef = torch.Tensor([0.299, 0.585, 0.144])[None, :, None, None]
        gray_scale_coef.requires_grad = False
        w = (arch.conv1.weight * gray_scale_coef).sum(1).unsqueeze(1) # sum over the 3 channel weights
        conv0.weight = nn.Parameter(w, requires_grad=True)
        self.layer0 = nn.Sequential(conv0, arch.bn1, nn.ReLU(inplace=True))
        self.layer1 = arch.layer1
        self.layer2 = arch.layer2
        self.layer3 = arch.layer3
        self.layer4 = arch.layer4
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        in_features = arch.fc.in_features
        self.head1 = nn.Linear(in_features, n_classes[0])
        self.head2 = nn.Linear(in_features, n_classes[1])
        self.head3 = nn.Linear(in_features, n_classes[2])

    def forward(self, x):
        x = self.layer0(x)
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)  # BxCxWxH -> BxX
        x1 = self.head1(x)
        x2 = self.head2(x)
        x3 = self.head3(x)

        return [x1, x2, x3]

