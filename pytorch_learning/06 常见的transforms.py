from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)
print(img)


# ①transforms的ToTensor
object1 = transforms.ToTensor()  # object:Shadows built-in name 'object'
img_tensor = object1(img)
print(img_tensor)

writer = SummaryWriter("logs")
writer.add_image("tensor_test", img_tensor)


# ②transforms的Normalize(标准化)
print(img_tensor[2][2][2])
object2 = transforms.Normalize([0.7, 0.7, 0.7], [0.7, 0.7, 0.7])  # mean:均值、std:标准差,三通道写三个，0.7人为定义
img_norm = object2(img_tensor)
print(img_norm[2][2][2])  # 标准化后忘记改出的的对象了
writer.add_image("normalize_test", img_norm, 3)  # global_step第几步

writer.close()  # 记得关闭


# ③Resize
print(img.size)
object3 = transforms.Resize((512, 512))  # (512, 512)是图像大小高和宽
img_resize = object3(img)  # 输入PIL类型
print(img_resize)


# ④Compose（组合）
# 创建一个包含多个数据预处理操作的序列
object4 = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
])
# 应用转换到输入数据
input_data = object4(img)



# __call__的使用，01的__getitem__也是这样
class Person:

    def __call__(self, name):
        print(f"__call__,{name}")

    def name1(self, name):
        print(f"{name}")


person = Person()
person("1")
person.name1("2")
