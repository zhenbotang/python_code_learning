"""
自定义数据集要看01的dataset用法
用pytorch.org的数据集用10的dataset用法
"""
from torch.utils.data import Dataset  # 导入Dataset类
from PIL import Image                 # 读取图片的库，可以对图片进行可视化
import os                             # 关于系统操作的库，主要用来对文件路径操作，对数据所在文件路径进行字符串操作


class MyData(Dataset):

    def __init__(self, root_dir, label_dir):  # 传入根目录与子目录
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path_list = os.listdir(self.path)

    def __getitem__(self, idx):  # idx(index)可以用缩写
        img_name = self.img_path_list[idx]  # 从文件名列表中获取了文件名
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)  # 组装路径，获得了图片具体的路径(self,path?)
        img = Image.open(img_item_path)  # 使用PIL读取这个图像 img.show()才是打开
        label = self.label_dir
        return img, label  # 此处img是一个JpegImageFile对象，label是一个字符串。

    def __len__(self):  # __len__方法，返回数据集的size大小
        return len(self.img_path_list)


root_dir = "dataset/train"  # 根目录
ants_label_dir = "ants"     # 子目录：指向存放train数据集里的ants数据的文件夹
bees_label_dir = "bees"

ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)
img, label = bees_dataset[1]
# img.show()
print(bees_dataset[1])

train_dataset = ants_dataset + bees_dataset  # 内部代码支持直接相加
print(len(train_dataset))
print(len(ants_dataset))
print(len(bees_dataset))

img, label = train_dataset[123]
print(img)
print(label)
# img.show()
