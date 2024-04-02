"""
装tensorboard装半天，最后用conda install tensorboard成功
"""
# form torch.utils.tensorboard import SummaryWriter  # 注意from不是form
# from torch.utils.tensorboard import SummaryWriter  导入SummaryWriter类

from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("logs")  # 建立变量（对象）writer，存储空间为logs
# writer.add_scalar()           # (标题，y轴scalar_value,x轴global_step)
# writer.add_image()

x = range(100)
for i in x:
    writer.add_scalar('y=x', i, i)
writer.close()

# 打开事件文件（logs）
# Terminal中输入tensorboard --logdir=logs (--port=6007) 打开tensorboard网页窗口
# Image.open(img_path) 填入读取的地址

# tips
# tensorboard --logdir=logs  log若为log 123（有空格的情况要加“”）   即tensorboard --logdir="logs 123"
