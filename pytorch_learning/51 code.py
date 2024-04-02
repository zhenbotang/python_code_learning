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
# print(train_dataset.data[0])
"""tensor->PIL"""
# transform_pil = torchvision.transforms.ToPILImage()
# img0 = train_dataset.data[0]
# img0 = transform_pil(img0)
# print(img0)
# img0.show()
"""tensor->array->PIL"""
# img1 = train_dataset.data[0].numpy()
# img1 = Image.fromarray(img1)
# print(img1)
# img1.show()

fully = FullyConnected()
fully = fully.to(device)

loss_function = nn.CrossEntropyLoss()
loss_function = loss_function.to(device)

learning_rate = 0.001
optimizer = torch.optim.SGD(fully.parameters(), lr=learning_rate)

total_train_step = 0
total_test_step = 0
epoch = 100

writer = SummaryWriter("logs_handwritten")

# 训练模型
for i in range(epoch):
    print(f"----正在训练第{i+1}轮----")
    fully.train()
    for data in train_dataloader:
        imgs, targets = data
        imgs =imgs.to(device)
        targets = targets.to(device)
        output = fully(imgs)
        loss_result = loss_function(output, targets)
        optimizer.zero_grad()
        loss_result.backward()
        optimizer.step()
        total_train_step += 1
        if total_train_step % 200 == 0:
            print(f"第{total_train_step}次训练的损失为{loss_result}")
            writer.add_scalar(tag="train_loss", scalar_value=loss_result, global_step=total_train_step-1)
    fully.eval()
    with torch.no_grad():
        running_accuracy = 0
        loss_epoch = 0
        for data in test_dataloader:
            imgs, targets = data
            imgs = imgs.to(device)
            targets = targets.to(device)
            output = fully(imgs)
            loss_result = loss_function(output, targets)
            preds = output.argmax(1)
            accuracy_result = (preds == targets).sum()
            running_accuracy += accuracy_result  # # accuracy_result为一组64个中分类正确的个数，running_accuracy为一轮1000个数据分类正确的个数
            total_test_step += 1
            loss_epoch += loss_result

    print(f"第{i+1}轮测试的准确率为{running_accuracy/len(test_dataset)}")
    writer.add_scalar(tag="test_loss", scalar_value=loss_epoch, global_step=total_test_step-1)
    writer.add_scalar(tag="accuracy", scalar_value=running_accuracy, global_step=total_test_step-1)

    if i == 49 or i == 99:
        torch.save(fully, f"fully{i+1}.pth")
        print(f"训练{i+1}轮的模型已保存")
writer.close()


# 30轮到90.0%
# 40轮到90.7%
# 50轮到91.1%
# 99轮到92.22%
# 100轮到92.20%
