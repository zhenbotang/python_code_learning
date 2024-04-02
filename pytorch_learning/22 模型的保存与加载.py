import torch
import torchvision.models

vgg16 = torchvision.models.vgg16(weights=None)

# 保存方式一(保存了模型+参数)
torch.save(vgg16, "vgg16_save1.pth")

# 方式一加载
vgg16_load = torch.load("vgg16_save1.pth")
print(vgg16_load)

# 保存方式二(保存模型的参数-官方推荐，因为占空间小)
torch.save(vgg16.state_dict(), "vgg16_save2.pth")  # 将参数保存为字典

vgg16_load2_1 = torch.load("vgg16_save2.pth")  # 字典
print(vgg16_load2_1)

# 方式二加载
vgg16_load2_2 = torchvision.models.vgg16(weights=None)  # 加入模型结构（包括初始化参数）
vgg16_load2_2.load_state_dict(torch.load("vgg16_save2.pth"))  # 将参数字典加入到模型中
print(vgg16_load2_2)
