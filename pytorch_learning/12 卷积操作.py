"""
几个中括号就是几维
一维
[1,1]
二维
[[1,2],
 [1,2]]
三维
[[[1,2],[1,2]],
 [[1,2],[1,2]]]
"""
# 一通道的图片是二维的
# stride步长：1、单数字1就是横向纵向都是步长都是1  2、输入元组（1，2）（sH,sW）就是High高和Wide宽
# 权重：卷积核
import torch
import torch.nn.functional as F  # 导入functional利用里面的conv进行卷积  # 以非小写形式导入的小写变量

x_input = torch.tensor([[1, 2, 0, 3, 1],
                        [0, 1, 2, 3, 1],
                        [1, 2, 1, 0, 0],
                        [5, 2, 3, 1, 1],
                        [2, 1, 0, 1, 1]])

kernel = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])
print(x_input, type(x_input), x_input.shape)  # print(x_input.size())
x_input = torch.reshape(x_input, (1, 1, 5, 5))  # input – input tensor of shape(minibatch,in_channels,iH,iW)

kernel = torch.reshape(kernel, (1, 1, 3, 3))
print(x_input, type(x_input), x_input.shape, kernel.shape)

output = F.conv2d(x_input, kernel, stride=1)
print(output)  # 输入和卷积核都被reshape成四维的了所以输出也是四维
output2 = F.conv2d(x_input, kernel, stride=2)
print(output2)
output3 = F.conv2d(x_input, kernel, stride=1, padding=1)  # padding卷积中的填充
print(output3)
