import torch
from PIL import Image
from torch import nn
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from FullyConnected import *

device = torch.device("cuda")

transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.1307], std=[0.3081])  # (0.1307,), (0.3081,)? 黑白图片单通道
])
train_dataset = torchvision.datasets.MNIST(root="./Handwritten_data/train_dataset", train=True, transform=transforms, download=True)
test_dataset = torchvision.datasets.MNIST(root="./Handwritten_data/test_dataset", train=False, transform=transforms, download=True)

train_dataloader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)  # 一般True随机打乱
test_dataloader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=True)

print(train_dataset.data.shape, len(train_dataset))
print(test_dataset.data.shape, len(test_dataset))

# 验证
fully = torch.load("fully100.pth", map_location=torch.device("cpu"))  # 将cuda训练的模型 映射到cpu上

img, target = train_dataset[123]
print(target)  # 7
print(img.shape)  # (1, 28, 28)
transform_PIL = torchvision.transforms.ToPILImage()
img_PIL = transform_PIL(img)
img_PIL.show()
output = fully(img)
print(output)
print(output.argmax(1))


