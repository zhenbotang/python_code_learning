"""
shift + 回车跳转到下一行
python console 可以按行和按块执行，shift+回车换行
python console 点方向上键是上一条代码，按几次就是上几条代码

python console下面的Terminal可以直接进入Anaconda prompt的pytorch环境--很方便
Terminal中按ctrl+c是取消
未导入的模块提示红色下划线
设置取消大小写对应匹配：设置--code completion--取消勾选match case
可以多行一起缩进：全选+tab
更新pip：pip install --upgrade pip
ctrl+回车直接把代码复制到terminal运行了！！！离谱
大写可以按住shift+大写字母，不需要按下去！！！
"""
"""
img_path = "tensorboard-data/train/bees_image/17209602_fe5a5a746f.jpg"
img = Image.open(img_path)
# 停在Image上或者移到img——上可以快速导入模块
"""
import torch

# 小tips
a = torch.tensor(5)
print(a)
print(a.item())  # 直接显示具体数据，不显示数据类型
b = 1
c = 1.1
print(a, b, c, "type:", type(a), type(b), type(c))
print(a + b, type(a + b))
print(a + c, type(a + c))
print(b + c, type(b + c))

print(type(a.item()))  # a为整数张量.item()就返回整数，a为浮点数张量.item()就返回浮点数
# int和float一起 -> float
# int/float和tensor一起 -> tensor

# 三目运算：if语句的简化写法
a = 3
b = 6
maxNum = a if a > b else b
print(maxNum)
