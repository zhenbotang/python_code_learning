"""
模型一般另放一个文件，用main测试模型正确性
模型文件和训练文件需要在同一个文件夹里面
"""
import torch
from torch import nn


class VGG16(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding=2),
            nn.MaxPool2d(kernel_size=2),  # ceil_mode为True就是池化保留不足部分
            nn.Conv2d(32, 32, 5, padding=2),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(32, 64, 5, padding=2),
            nn.MaxPool2d(kernel_size=2, ceil_mode=True),
            nn.Flatten(),
            nn.Linear(64*4*4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):  # forward灰的说明没对其
        x = self.model(x)
        return x


# 测试模型是否正确
if __name__ == '__main__':
    vgg16 = VGG16()
    input = torch.ones((64, 3, 32, 32))
    output = vgg16(input)
    print(input)
    print(output)
    print(output.shape)
