# torchvision.transforms.ToTensor：ToTensor功能是将 PIL Image类型或者numpy.ndarray类型的图片对象转换为tensor类型
# tensor 数据类型可以理解为包装了反向神经网络一些理论基础参数。在神经网络中，要将数据先转换为Tensor类型，再进行训练
# transforms.py(是一个模块)

from PIL import Image
from torchvision import transforms
img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)
# img.show()
print(type(img))
print(img)

# 转为tensor
img_Tensor = transforms.ToTensor()  # ToTensor是一个类不是方法,
img_tensor = img_Tensor(img)        # 使用transforms的方法就是 先实例化选中的类，然后用实例化的对象去处理图片就行
print(img_tensor)                   # img_Tensor是类ToTensor的一个实例化对象，在具体对象传入pic可以返回tensor类型
# __call__魔术方法，把实例好的对象当作方法（函数），直接加括号就可以调用
# call()的本质是将一个类变成一个函数（使这个类的实例可以像函数一样调用）。
# transforms.py类似工具箱，img_Tensor(img)类似创建了具体的一个工具去转化img

# 转为numpy.ndarray
import cv2  # 用pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python下载
img_cv = cv2.imread(img_path)  # 图片地址转为numpy.ndarray类型
# print(img_cv)

# 创建SummaryWriter文件
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("logs")
writer.add_image("tensor_img", img_tensor)
writer.close()

# Terminal中输入tensorboard --logdir=logs (--port=6007) 打开tensorboard网页窗口
