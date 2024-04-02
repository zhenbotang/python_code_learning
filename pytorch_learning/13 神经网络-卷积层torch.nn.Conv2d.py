# nn.Conv1d 一维卷积、nn.Conv2d 二维卷积、nn.Conv3d 三维卷积
# convolution 卷积
# 卷积核与被卷积对象的通道数相等，有几个卷积核结果就是几通道
# 很多算法都是增加channel数（卷积核个数）
# tip(torchvision.transforms)

import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor()]),  # 这里Compose可以不用写
    download=True
)
dataloader = DataLoader(
    dataset=dataset,
    batch_size=64,
    # shuffle=True,
    # drop_last=False
)


class MyNetwork(nn.Module):
    def __init__(self):  # Call to __init__ of super class is missed:子类未调用父类的__init__()方法
        super().__init__()
        self.conv1 = Conv2d(3, 6, 3, stride=1, padding=0)  # 定义成员方法中的函数？

    def forward(self, x_input):  # forward是由内置的call方法调用的(自动)！！！！！！
        x_output = self.conv1(x_input)
        return x_output


mynetwork1 = MyNetwork()  # 实例化网络
print(mynetwork1)

writer = SummaryWriter("logs")
count = 0
# 通过for循环传入数据，每次循环先卷积，后可视化
for data in dataloader:
    imgs, targets = data
    output = mynetwork1(imgs)  # missing whitespace around operator:运算符周围缺少空白
    # print(imgs.shape)
    # print(output.shape)
    # size为[64, 3, 32, 32]
    writer.add_images("cnn_input", imgs, global_step=count)
    # size为[64, 6, 30, 30]  输出通道为6，但图片最多3通道所以会报错,所以用个不合适的方法改大小
    output = torch.reshape(output, (-1, 3, 30, 30))  # -1是一个占位符，表示让PyTorch自动计算该维度的大小。
    writer.add_images("cnn_output3", output, global_step=count)
    count += 1
# 图像出来的效果是随机的好像是因为卷积核随机？

"""
报错时看路径，不是源代码的路径不用看（什么line704这些根本没有的）
torch.reshape用来改变tensor的shape
torch.reshape(tensor,shape)
别人的论文strid和padding没给也可以推导
"""







