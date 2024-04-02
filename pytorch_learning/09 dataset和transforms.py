"""
dataset（下载数据）和transforms（转化数据）联合运用
"""
import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transforms = torchvision.transforms.Compose([  # 中括号别忘了
    torchvision.transforms.ToTensor()
])
# 从pytorch官网下载数据集（训练集 测试集），大数据集用迅雷下载粘贴到目录中，ctrl+点击数据集名字（CIFAR10），中的url就是下载地址
train_set = torchvision.datasets.CIFAR10(
    root="./train_set",  # ./ 表示当前目录
    train=True,
    transform=dataset_transforms,  # 学习了transforms主要就用在第4、11行中
    download=True
)
test_set = torchvision.datasets.CIFAR10(
    root="./train_set",
    train=False,
    transform=dataset_transforms,
    download=True
)
"""
没有数据集中加入transform=dataset_transforms时图片为PIL格式可以用以下操作测试：
print(test_set[0])
print(test_set.classes)
img, target = test_set[0]
print(img)
print(target)
print(test_set.classes[target])
img.show()
"""

print(test_set[0])  # 为tensor类型后可以用tensorboard显示,但test_set[0]还是包括target：从(PIL,target)->(tensor,target)

# 在tensorboard显示
writer = SummaryWriter("logs")
for i in range(10):
    # writer.add_image("test_set(1-10)", test_set[i], i)  :test_set[i]包括tensor和target，要拆开
    img, target = test_set[i]  # 拆分
    writer.add_image("test_set(1-10)", img, i)
writer.close()
