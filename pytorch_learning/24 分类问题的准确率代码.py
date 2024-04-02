"""
1将output的得分转化为分类标签下表
2与真实值标签比较，相等为True，不等为False，最后[True, False].sum() = ···
"""
import torch

output = torch.tensor([[0.1, 0.2],
                       [0.3, 0.4]])
# argmax可以求出output横向或纵向最大值的位置下标
# 0轴代表一个矩阵里竖着的那一个方向，1轴代表一个矩阵里横着的那一个方向。
print(output.argmax(1))  # 0为纵向，1为横向
preds = output.argmax(1)
targets = torch.tensor([0, 1])

print((preds == targets).sum())
