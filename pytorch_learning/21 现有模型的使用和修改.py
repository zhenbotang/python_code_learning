# pip install scipy 下载龟速，用conda就行

import torch
import torchvision
from torch import nn
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# dataset = torchvision.datasets.ImageNet(  # ImageNet的训练集147个g，且官方不能下载了
#     root="./train_set_ImageNet",
#     split="train",
#     transform=torchvision.transforms.ToTensor(),
# )

vgg16_False = torchvision.models.vgg16(weights=None)  # None表示不下载，参数都是初始化的
vgg16_True = torchvision.models.vgg16(weights="DEFAULT")  # "DEFAULT"表示下载，参数都是已经训练好的
# print(vgg16_False)
print("---")
print(vgg16_True)

"""
可以用现有的网络(如vgg16训练CIFAIR10的数据)
vgg16的分类是1000分类，CIFAIR10是10分类，1、可以将vgg16最后线性层的1000改为10。2、也可以最后加一层1000->10的线性层
以vgg16——True为例
迁移学习？
"""

dataset = torchvision.datasets.CIFAR10(root="./train_set", train=True, transform=torchvision
                                       .transforms.ToTensor, download=True)
# 在vgg16_True基础上添加层
# vgg16_True.add_module("add_Linear", nn.Linear(1000, 10))
vgg16_True.classifier.add_module("7", nn.Linear(1000, 10))
print("--")
print(vgg16_True)

# 修改vgg16_False层结构
print("---")
print(vgg16_False)
vgg16_False.classifier[6] = nn.Linear(4096, 10)
print(vgg16_False)
