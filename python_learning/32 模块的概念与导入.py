# 模块就是一个工具包
# 模块就是一个python文件，里面有类，函数，变量，可以拿过来用(导入模块)
# 导入模块语法：[from 模块名] import [模块|类|变量|函数|*] [as 别名]
# [] 中括号表示可以不写，*表示导入模块所有内容
import time  # ctrl+点击模块名可以进入模块文件
# built-in(内置的) time values(时间值)

# 语法一：全部导入（import 模块名）
print("开始睡觉")
time.sleep(1)  # 通过.使用模块内所有功能（类，函数，变量）
print("睡醒了")
# 语法二：部分导入（from 模块名 import 功能名）
from time import sleep
print("开始")
sleep(1)
print("结束")
# import time 约等于 from time import *
# time.sleep(3) | sleep(3)

# 别名
import random as r  # 导入模块写在开头
num = r.randint(1, 10)
print(num)

# 导入自定义模块
import my_module1
a = my_module1.text(1, 2)
print(a)
# from my_module1 import text
# from my_module2 import text  (后面的text会把前面的覆盖掉)

# 模块内部main回车后下面的if可以用于测试，外部调用时不会执行
# 模块内部name == main，外部不等于

# # 内置变量 * = __all__,所以使用from 模块名 import * 时，__all__设置了只能用__all__里面的功能
