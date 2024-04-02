# dataset：告诉程序数据集在什么地方 以及 第一个第二个···数据是什么
# dataloader数据加载器：将数据加载到神经网络中去
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

data_transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])
test_dataset = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=data_transforms,
    download=True
)

test_dataloader = DataLoader(
    dataset=test_dataset,
    batch_size=64,    # 每次取几个数据
    shuffle=True,     # shuffle：是否打乱，默认是False（不打乱），但一般设置为True，True就是每次训练打乱序列
    num_workers=0,    # 0为主（单）线程，123为234线程
    drop_last=True    # 取数据除不尽时，舍不舍去最后的数据，True为舍去，False为不舍去
)


# 测试集第一个图片的信息
print(test_dataset[0])
img, target = test_dataset[0]
print(img)
print(target)     # target不是标签，是标签存放的位置，标签列表是classes，真正的标签是classes[target]？
print(img.shape)  # [3, 32, 32]：3通道、32*32
print(test_dataset.classes)
print(test_dataset.classes[3])


# 数据类型为tensor可以用tensorboard显示
writer = SummaryWriter("logs")
step = 0
for data in test_dataloader:
    imgs, targets = data  # imgs作为神经网络的输入
    # print(img.shape)
    # print(targets)
    writer.add_images("64一组数据-drop-list", imgs, step)  # 这里一次不止一张图片用add.images  # 重新运行要修改tag
    step += 1
writer.close()  # 又忘了
