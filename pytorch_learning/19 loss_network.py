import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    download=True
)
dataloader = DataLoader(
    dataset=dataset,
    batch_size=1
)


class VGG16(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding=2),
            # nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),  # ceil_mode为True就是池化保留不足部分

            nn.Conv2d(32, 32, 5, padding=2),
            # nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),

            nn.Conv2d(32, 64, 5, padding=2),
            # nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, ceil_mode=True),

            nn.Flatten(),
            nn.Linear(1024, 64),  # 不知道展开后是多少（1024）可以把linear层先不写，输出output.shape看是多少
            nn.Linear(64, 10)
        )

    def forward(self, x):  # forward灰的说明没对其
        y = self.model(x)
        return y


vgg16 = VGG16()
loss = nn.CrossEntropyLoss()
for data in dataloader:
    imgs, targets = data
    output = vgg16(imgs)
    # 输出和真实的target
    print(output)   # 每次结果不同，好像是因为卷积核是随机初始化的，卷积核不同
    print(targets)  # targets是数据集自带的，好像是不变的  # 想要分类还少个softmax分类的层  # 还要用loss反向传播更新卷积核参数（权重）
    loss1 = loss(output, targets)
    # print(output.shape)
    print(loss1)
# 梯度（grad）,gradient descent梯度下降
    loss1.backward()  # backward()是对loss使用的计算grad梯度  反向传播
