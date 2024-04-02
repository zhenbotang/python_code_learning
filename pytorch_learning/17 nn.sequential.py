import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


class VGG16(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),  # ceil_mode为True就是池化保留不足部分

            nn.Conv2d(32, 32, 5, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),

            nn.Conv2d(32, 64, 5, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, ceil_mode=True),

            nn.Flatten(),
            nn.Linear(1024, 64),  # 不知道展开后是多少（1024）可以把linear层先不写，输出output.shape看是多少
            nn.Linear(64, 10)
        )

    def forward(self, x):  # forward灰的说明没对其
        y = self.model(x)
        return y


vgg16 = VGG16()
# print(VGG16) print的是实例化的自己的网络
print(vgg16)

# 检查网络是非正确
input_1 = torch.ones((64, 3, 32, 32))  # ones:创建一个都是1的数据，输入带括号的size
output_1 = vgg16(input_1)
print(input_1.shape)
print(output_1.shape)

# graph可视化
writer = SummaryWriter("logs_VGG16")
writer.add_graph(vgg16, input_1)
writer.close()




