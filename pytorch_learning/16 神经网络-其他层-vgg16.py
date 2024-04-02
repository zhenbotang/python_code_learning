# dropout层 随机将一些元素变为0，变0的概率为p---防止过拟合
# Linear 线性层
# 在vgg16模型中， 将224*224*3的图片转变为了1*1*4096的大小，经过训练，得到最终的1*1*1000的结果。
# (1,1,4096)的4096就是in_features,(1,1,1000)的1000就是out_features(层数？)

import torch
import torchvision.datasets
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
    batch_size=64,
    drop_last=True
)


class M(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(196608, 10)

    def forward(self, input):
        output = self.linear(input)
        return output


m = M()
writer = SummaryWriter("logs_linear")
step = 0
for data in dataloader:
    imgs, targets = data
    print(imgs.shape)  # [64, 3, 32, 32]
    writer.add_images("input", imgs, global_step=step)
    # flatten：摊平
    imgs = torch.reshape(imgs, (1, 1, 1, -1))
    # imgs = torch.flatten(imgs)  # imgs = torch.reshape(imgs, (1, 1, 1, -1))  # 最后一维填feature--># [1, 1, 1, 196608]
    print(imgs.shape)
    output = m(imgs)
    writer.add_images("output", output, global_step=step)
    step += 1
writer.close()
