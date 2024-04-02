# ReLU:在网络中引入一些非线性特征，非线性特征多才能训练出符合各种曲线或特征的模型，增强泛化能力
import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

input = torch.tensor([[1, -0.5],
                      [-1, 3]])
print(input.shape)
input = torch.reshape(input, (-1, 1, 2, 2))  # 由于ReLU函数输入要N(batch_size)所以要reshape但不知道为什么都要reshape成4维的，但好像一个数据不需要？？？
print(input.shape)  # 好像是输入的2维张量都要reshape成4维的（加上N/batch_size 和 channel）


class M(nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU()  # inplace=True激活后在input上直接变，inplace=False激活后input不变，输出新的output(一般inplace使用False防止原始数据丢失)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        # output = self.relu(input)
        output = self.sigmoid(input)
        return output


m = M()
output = m(input)  # 使用的是实例化的神经网络，而不是class的模板（面对对象编程）
print(output)

dataset = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    download=True
)
dataloader = DataLoader(
    dataset=dataset,
    batch_size=64
)

writer = SummaryWriter("logs_ReLU")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, global_step=step)
    output = m(imgs)
    writer.add_images("output_sigmoid", output, global_step=step)
    step += 1
writer.close()

# 所以增加非线性的激活函数实际上是给模型增加非线性的表达能力或者因素，
# 有了非线性函数模型的表达能力就会更强。整个模型就像活了一样，而不是想机器只会做单一的线性操作。
