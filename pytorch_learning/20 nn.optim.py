"""
lr learning rate学习速率
随机梯度下降算法SGD（Stochastic gradient descent）
"""
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
"""
加入损失函数
加入优化器
1运行
2计算损失
3优化器归零梯度
4反向传播计算梯度
5优化器调节梯度
"""
optim = torch.optim.SGD(vgg16.parameters(), lr=0.01)  # lr先大后小
# 一轮不够，设置20轮
for epoch in range(20):  # epoch就是一轮一轮的意思
    # 查看每轮循环loss之和
    running_loss = 0
    for data in dataloader:
        imgs, targets = data
        output = vgg16(imgs)
        loss1 = loss(output, targets)
        optim.zero_grad()  # 设置参数为零
        loss1.backward()  # backward()后才有梯度，所以zero_grad()在backward()后面就行
        optim.step()  # 开始优化
        running_loss += loss1
    print(running_loss)
