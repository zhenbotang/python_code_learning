import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import time

"""
第二种GPU训练写法
先定义device
相比于第一种，若要换训练device，改device("cup")的cup就行，修改方便（改为gpu写法  "cup"  ->  "cuda:0"("cuda")  /"cuda:1"）
tips:第一种和第二种方法都是要对imgs和targets重新赋值，模型和损失函数可以不用赋值，直接vgg16.cuda()/vgg16.to(device)
"""
device = torch.device("cuda")
# decice = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 准备数据集
train_dataset = torchvision.datasets.CIFAR10(root="./train_set", train=True,
                                             transform=torchvision.transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.CIFAR10(root="./test_set", train=False,
                                            transform=torchvision.transforms.ToTensor(), download=True)

# 查看数据集长度
train_dataset_size = len(train_dataset)
text_dataset_size = len(test_dataset)
print(f"训练集的长度为{train_dataset_size},测试集的长度为{text_dataset_size}")

# 加载数据集
train_dataloader = DataLoader(dataset=train_dataset, batch_size=64)
test_dataloader = DataLoader(dataset=test_dataset, batch_size=64)


# 创建（加载）神经网络
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
            nn.Linear(1024, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):  # forward灰的说明没对其
        x = self.model(x)
        return x


vgg16 = VGG16()
"""
模型调用cuda:将模型转移到到大上
"""
# vgg16 = vgg16.cuda()
vgg16 = vgg16.to(device)  # 将网络模型转移到设备上去
# 损失函数
loss_function = nn.CrossEntropyLoss()  # 参数全默认
# loss_function = loss_function.cuda()
loss_function = loss_function.to(device)

# 优化器
learning_rate = 0.01  # 提出来方便修改，1e-2 == 1 * (10)^(-2) == 0.01，0非常多可以用e-的写法
optim = torch.optim.SGD(vgg16.parameters(), lr=learning_rate)  # 优化器使用：随机梯度下降

# 设置一些参数
total_train_step = 0  # 记录训练的次数
total_test_step = 0   # 记录测试的次数
epoch = 10            # 训练的轮次

# 添加tensorboard可视化
# writer = SummaryWriter("logs_train and test")

# 训练模型
# 有dropout层是训练和测试前要调用如下代码:vgg16.train(), vgg16.eval()
vgg16.train()  # 表示网络进入训练状态
start_time = time.time()  # 用time模块的time()方法记录时间
for i in range(epoch):
    print(f"---正在训练第{i+1}轮---")

    for data in train_dataloader:
        imgs, targets = data
        # imgs =imgs.cuda()
        # targets = targets.cuda()
        imgs = imgs.to(device)
        targets = targets.to(device)
        outputs = vgg16(imgs)
        loss_result = loss_function(outputs, targets)
        optim.zero_grad()
        loss_result.backward()
        optim.step()
        total_train_step += 1
        if total_train_step % 100 == 0:
            end_time = time.time()  # 记录每一百次训练的时间
            print(f"{total_train_step}次训练时间为{end_time-start_time}")
            print(f"第{i + 1}轮上第{total_train_step}次训练的损失loss:{loss_result}")
            # writer.add_scalar("train_loss(every 100 times)", loss_result, global_step=total_train_step-1)  # 每一百次记录一次

    # 每轮训练后都要进行验证，看看训练是否正常，测试时不需要调优，所以梯度在测试时不能变动
    # 测试模型
    vgg16.eval()
    with torch.no_grad():
        running_loss = 0
        running_accuracy = 0

        for data in test_dataloader:
            imgs, targets = data
            imgs = imgs.to(device)
            targets = targets.to(device)
            outputs = vgg16(imgs)
            loss_result = loss_function(outputs, targets)
            running_loss += loss_result  # loss_result损失是tensor类型，定义的running_loss是int，所以可以用.item()化tensor为整数？好像又不需要
            preds = outputs.argmax(1)
            accuracy_result = (preds == targets).sum()  # accuracy_result为一组64个中分类正确的个数，running_accuracy为一轮1000个数据分类正确的个数
            running_accuracy += accuracy_result

    print(f"第{i + 1}轮测试集上的总损失为{running_loss}")
    print(f"第{i + 1}轮测试集上的准确率为{running_accuracy/text_dataset_size}")
    # writer.add_scalar("test_loss(every one epoch)", running_loss, global_step=i)
    # writer.add_scalar("text_accuracy(every one epoch)", running_accuracy/text_dataset_size, global_step=i)

# 保存（每轮）训练好的模型
#     torch.save(vgg16, f"vgg16_{i+1}.pth")
#     print(f"第{i+1}轮模型已保存")
# writer.close()

# 分类问题除了用loss还会用准确率显示训练效果
