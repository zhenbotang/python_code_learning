# 池化作用：保留输入数据的特征，并且减小数据量（1080p->720p)
# dilation 空洞卷积
# 池化层的stride默认是kernel_size
# ceil_model=True:保留 False:不保留  （默认为False）
# 画图软件：powerpoint 截图软件：snipaste


import torch
import torchvision.datasets
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

input_1 = torch.tensor([[1, 2, 0, 3, 1],
                        [0, 1, 2, 3, 1],
                        [1, 2, 1, 0, 0],
                        [5, 2, 3, 1, 1],
                        [3, 2, 1, 1, 1]], dtype=torch.float32)  # dtype=torch.float32（可以不写）将数据设置为浮点数，1->1.(1.就是1.0)
input_1 = torch.reshape(input_1, (-1, 1, 5, 5))  # (数量-batch_size, channel, H, W)
print(input_1, input_1.shape)


class MyNetwork(nn.Module):  # module模块
    def __init__(self):
        super().__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=True)  # 初始化，定义一个池化函数

    def forward(self, x_input):
        y_output = self.maxpool1(x_input)
        return y_output


mynetwork = MyNetwork()
print(mynetwork)
output_1 = mynetwork(input_1)
print(output_1)


#
dataset = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    download=True
)
dataloader = DataLoader(  # 不用知道DataLoader在哪个package下面，知道写DataLoader就行
    dataset=dataset,
    batch_size=64
)
step = 0
writer = SummaryWriter("logs_pool")
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, global_step=step)
    output = mynetwork(imgs)
    writer.add_images("output", output, global_step=step)
    step += 1
writer.close()
