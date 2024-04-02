import torch
from torch import nn


class FullyConnected(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            # nn.Flatten(),
            nn.Linear(in_features=1*28*28, out_features=30),  # 隐藏层有30个权重 # 一张黑白图片（1*28*28）
            nn.ReLU(),
            nn.Linear(in_features=30, out_features=10),  # 最后分为10个类别
            # nn.ReLU()
            nn.Softmax(dim=1)  # 按行归一化
        )

    def forward(self, x):
        x = x.view(-1, 1*28*28)  # 改变输入x的形状
        # print(x.shape)
        x = self.model(x)  # 少了（x）  # 输出层的激活函数softmax？？？  # 根据归一化的值计算损失
        return x


if __name__ == '__main__':
    fully = FullyConnected()
    input = torch.ones((64, 1, 28, 28))
    output = fully(input)
    print(input)
    print(output)
    print(output.shape)
