# forward前向传播 backward反向传播
"""
pytorch.org的神经网络模板:

import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))
"""
import torch
from torch import nn  # ==import torch.nn as nn


class Module(nn.Module):  # 创建了一个神经网络模板（Module），后面要用具体变量（对象）接收模板
    def __init__(self):
        super().__init__()

    def forward(self, input):  # 因为集成的nn.Module中forward方法是__call__()方法的实现，可调用对象会调用__call__()方法?
        output = input + 1
        return output


module = Module()
x_input = torch.tensor(1.0)  # torch.tensor：复制data的值生成张量
y_output = module(x_input)
print(y_output)

