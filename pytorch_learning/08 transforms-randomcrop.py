# randomcrop随机裁剪
from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path = "dataset/train/ants/0013035.jpg"
img = Image.open(img_path)

# 随机裁剪+totensor
object5 = transforms.Compose([
    transforms.RandomCrop((512, 700)),
    transforms.ToTensor(),
])

writer = SummaryWriter("logs")

for i in range(10):
    img_last = object5(img)
    writer.add_image("img_last", img_last, i)

writer.close()
