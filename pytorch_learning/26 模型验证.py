# 从本文件位置找到dog图片位置：用相对路径
# img_path = "../dataset/dog.png"  ???
import torch
import torchvision
from PIL import Image


img_path = "dataset/dog.png"
img = Image.open(img_path)
print(img)

# png为四通道格式，比RGB多个透明度通道
img = img.convert("RGB")  # 保留颜色通道
print(img)  # 好像不改也是RGB？

transforms = torchvision.transforms.Compose([
    torchvision.transforms.Resize((32, 32)),  # Resize输入 h w
    torchvision.transforms.ToTensor()
])

img = transforms(img)
print(img.shape)
img = torch.reshape(img, (1, 3, 32, 32))  # 改图片维度语法
print(img.shape)

vgg16 = torch.load("vgg16_18.pth", map_location=torch.device("cpu"))  # 将cuda训练的模型 映射到cpu上
print(vgg16)

output = vgg16(img)
print(output)
print(output.argmax(1))

# 因为是用CIFAI10的数据与标签训练的，所以0-9表示的类别与CIFAI10的一致
# debug在CIFAI10的数据集dataset找类别
