from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)

"""transforms--compose（组合）"""
# 创建一个包含多个数据预处理操作的序列
object4 = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小,如果只输一个数，给到长宽小的那一个等比缩放
    transforms.ToTensor(),  # 转换为张量
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 标准化
])
# 应用转换到输入数据
img_last = object4(img)


writer = SummaryWriter("logs")
writer.add_image("img_last", img_last)
writer.close()
