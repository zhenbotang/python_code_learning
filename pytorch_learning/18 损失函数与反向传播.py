# loss的作用：1.计算实际输出和目标函数的差距2.为我们更新输出提供一定依据（反向传播）

import torch
from torch import nn  # 把这个写了方便一点
from torch.nn import L1Loss, MSELoss

input1 = torch.tensor([1, 2, 3], dtype=torch.float32)  # 需要浮点数,实际中数据中一般都有浮点数，所以不需要dtype（这里需要）
target = torch.tensor([1, 2, 5], dtype=torch.float32)
input1 = torch.reshape(input1, (1, 1, 1, 3))  # h w(一行三列)
target = torch.reshape(target, (1, 1, 1, 3))

loss1 = L1Loss(reduction='mean')
loss2 = L1Loss(reduction="sum")
result1 = loss1(input1, target)  # (|1-1|+|2-2|+|5-2|)/3 = 0.6667
result2 = loss2(input1, target)
print(result1)
print(result2)

# MSELoss平方差
loss3 = MSELoss()
result3 = loss3(input1, target)  # [(5-3)*(5-3)]/3 = 0.6667
print(result3)

print("---")
# exp(x)表示的是e的x次方
# 分类问题的交叉损失
x = torch.tensor([0.1, 0.2, 0.3])  # class0:0.1, class1:0.2, class2:0.3  # 相加不等于1？应该是没有进行归一化softmax
print(x.shape)
y = torch.tensor([1])  # 这里表示真实值是1，即真实分类为第二类，与预测的结果无关
x = torch.reshape(x, (1, 3))  # 因为x是一维向量有3个类别所以是3，不是1,3
print(x.shape)
loss4 = nn.CrossEntropyLoss()
result4 = loss4(x, y)  # (-0.2) + ln(exp(0.1) + exp(0.2) + exp(0.3)) = 1.1019
print(result4)
