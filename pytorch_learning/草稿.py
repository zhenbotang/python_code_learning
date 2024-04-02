import torch
from torch import nn
import torchvision
from torch.utils.data import DataLoader

transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.1307], std=[0.3081])  # (0.1307,), (0.3081,)?
])
train_dataset = torchvision.datasets.MNIST(
    root="./train_dataset",
    train=True, transform=transforms,
    download=True
)
dataloader = DataLoader(
    dataset=train_dataset,
    batch_size=64,
    shuffle=True  # 一般true随机打乱
)
print(train_dataset.data.shape)
