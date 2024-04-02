# Image读取的图片数据类型是PIL.JpeglmagePlugin不满足要求.add_image()要求的torch.Tensor, numpy.ndarray, or string类型
# 所以使用Opencv读取数据为numpy.ndarray------安装opencv：pip install opencv-python


from PIL import Image
import numpy
img_path = "tensorboard-data/train/bees_image/17209602_fe5a5a746f.jpg"
img = Image.open(img_path)
# img.show()
print(type(img))

# 或利用numpy将PIL类型转化为array
import numpy
img_array = numpy.array(img)
print(type(img_array))
print(img_array.shape)  # 默认第一位为通道数（3）才行，不是需要改

from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("logs")
writer.add_image("tag2", img_array, 2, dataformats='HWC')
writer.close()
